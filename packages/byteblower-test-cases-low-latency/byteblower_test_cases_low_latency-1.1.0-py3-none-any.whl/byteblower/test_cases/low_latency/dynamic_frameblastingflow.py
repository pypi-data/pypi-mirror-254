import logging
from datetime import datetime, timedelta
from statistics import mean
from typing import Iterable, Optional, Sequence, Union  # for type hinting

# ! FIXME: We are using "protected" modules/classes
#          * These might be subject to change in later versions
#          * of the ByteBlower Test Framework!
from byteblower_test_framework._helpers.syncexec import \
    SynchronizedExecutable  # for type hinting
from byteblower_test_framework.endpoint import Port  # for type hinting
from byteblower_test_framework.endpoint import Endpoint
from byteblower_test_framework.traffic import Frame  # for type hinting
from byteblower_test_framework.traffic import Imix  # for type hinting
from byteblower_test_framework.traffic import FrameBlastingFlow
from byteblowerll.byteblower import Stream as TxStream  # for type hinting

from ._definitions import (
    DEFAULT_SCALING_INTERVAL,
    DEFAULT_SCALING_RATE,
    MAX_BITRATE_THRESHOLD,
    MIN_BITRATE_THRESHOLD,
)
from ._stream_data_gatherer import DynamicStreamFrameCountDataGatherer
from .exceptions import FeatureNotSupported

_LOGGER = logging.getLogger(__name__)


class DynamicStreamScaler(object):

    __slots__ = (
        '_scaling_interval',
        '_scaling_rate',
        '_init_duration',
        '_last_packet_count',
        '_last_ts',
    )

    def __init__(
        self,
        scaling_interval: timedelta,  # [seconds]
        scaling_rate: float,
    ) -> None:
        self._scaling_interval = scaling_interval
        self._scaling_rate = scaling_rate

        self._init_duration = None

        self._last_packet_count = 0
        self._last_ts = None

    def prepare(self, flow_duration: timedelta) -> None:
        self._init_duration = flow_duration

        # Reset the counters
        # NOTE: Relevant when re-using this Flow in a new Scenario run

        self._last_packet_count = 0
        self._last_ts = None

    @property
    def last_packet_count(self) -> int:
        return self._last_packet_count

    def flip_scaling(self) -> None:
        self._scaling_rate *= -1

    def scale(
        self, _flow_name: str, stream: TxStream,
        stream_data_gatherer: DynamicStreamFrameCountDataGatherer,
        current_packet_count: int
    ) -> Optional[float]:
        # When there is an initial_time_to_wait, packet count will stay at 0
        # for some time. So don't start counting when there are no packets.
        if current_packet_count == 0:
            return None

        if self._last_ts is None:
            self._last_ts = datetime.utcnow()
            time_since_last_ts = timedelta(seconds=0)
        else:
            time_since_last_ts = datetime.utcnow() - self._last_ts

        if (current_packet_count > self._last_packet_count
                and time_since_last_ts >= self._scaling_interval):
            # Get remaining flow duration
            elapsed = stream_data_gatherer.elapsed_duration()

            if not elapsed:
                logging.warning(
                    'Flow %r: Transferred packets, but none sent yet?'
                    ' current_packet_count (%r) > previous_packet_count (%r)',
                    _flow_name,
                    current_packet_count,
                    self._last_packet_count,
                )
                return None
            # DEBUG
            _LOGGER.debug(
                "Flow %r: elapsed time %.02f s.", _flow_name,
                elapsed.total_seconds()
            )

            # Update frame count & last timestamp
            self._last_ts = datetime.utcnow()
            self._last_packet_count = current_packet_count

            # NOTE: initial_time_to_wait is not included
            #       in `_init_duration` nor `elapsed`.
            #       So no need to account for it.
            if self._init_duration >= elapsed:
                remaining_duration: timedelta = self._init_duration - elapsed

                # Update frame rate & number of frames
                inter_frame_gap: int = stream.InterFrameGapGet()
                inter_frame_gap /= (1 + self._scaling_rate / 100)
                # DEBUG
                frame_rate = 1e9 / inter_frame_gap
                _LOGGER.debug("Flow %r: new rate %d.", _flow_name, frame_rate)
                number_of_frames = int(
                    remaining_duration.total_seconds() *
                    (1e9 / inter_frame_gap)
                )

                # Update stream rate & number of frames
                stream.Stop()

                # Make sure that we don't loose any TX results
                stream_data_gatherer.persist_current_stream_results()

                # Don't wait after *continuing* transmission
                stream.InitialTimeToWaitSet(0)

                stream.InterFrameGapSet(int(inter_frame_gap))
                stream.NumberOfFramesSet(number_of_frames)
                stream.Start()

                _LOGGER.info("Flow %r: Flow restarted", _flow_name)
                return frame_rate


class BaseDynamicRateFrameBlastingFlow(FrameBlastingFlow):

    __slots__ = (
        '_max_frame_rate',
        '_min_frame_rate',
    )

    _stream_data_gatherer_class = DynamicStreamFrameCountDataGatherer

    def __init__(
        self,
        source: Port,
        destination: Port,
        name: Optional[str] = None,
        bitrate: Optional[float] = None,  # [bps]
        frame_rate: Optional[float] = None,  # [fps]
        number_of_frames: Optional[int] = None,
        duration: Optional[Union[timedelta, float, int]] = None,  # [seconds]
        initial_time_to_wait: Optional[Union[timedelta, float,
                                             int]] = None,  # [seconds]
        frame_list: Optional[Sequence[Frame]] = None,
        imix: Optional[Imix] = None,
        max_bitrate: Optional[Union[int, float]] = None,
        min_bitrate: Optional[Union[int, float]] = MIN_BITRATE_THRESHOLD,
        **kwargs
    ) -> None:
        if isinstance(source, Endpoint) or isinstance(destination, Endpoint):
            raise FeatureNotSupported(
                "Dynamic-rate FrameBlastingFlow does not support"
                " ByteBlower Endpoint"
            )
        super().__init__(
            source,
            destination,
            name=name,
            bitrate=bitrate,
            frame_rate=frame_rate,
            number_of_frames=number_of_frames,
            duration=duration,
            initial_time_to_wait=initial_time_to_wait,
            frame_list=frame_list,
            imix=imix,
            **kwargs,
        )

        # Calculate average frame size
        frame_sizes = (frame.length for frame in self._frame_list)
        avg_frame_size = mean(frame_sizes)  # [Bytes]

        # Convert bitrate to frame rate
        if max_bitrate is not None:
            self._max_frame_rate = (max_bitrate / 8) / avg_frame_size
        else:
            self._max_frame_rate = None
        if min_bitrate is not None:
            self._min_frame_rate = (min_bitrate / 8) / avg_frame_size
        else:
            self._min_frame_rate = None

    @property
    def stream_data_gatherer(self) -> DynamicStreamFrameCountDataGatherer:
        # NOTE: Defined for proper type hinting
        return self._stream_data_gatherer


class DynamicRateFrameBlastingFlow(BaseDynamicRateFrameBlastingFlow):

    __slots__ = ('_stream_scaler', )

    def __init__(
        self,
        source: Port,
        destination: Port,
        name: Optional[str] = None,
        bitrate: Optional[float] = None,  # [bps]
        frame_rate: Optional[float] = None,  # [fps]
        number_of_frames: Optional[int] = None,
        duration: Optional[Union[timedelta, float, int]] = None,  # [seconds]
        initial_time_to_wait: Optional[Union[timedelta, float,
                                             int]] = None,  # [seconds]
        frame_list: Optional[Sequence[Frame]] = None,
        imix: Optional[Imix] = None,
        scaling_interval: timedelta = DEFAULT_SCALING_INTERVAL,  # [seconds]
        scaling_rate: float = DEFAULT_SCALING_RATE,  #[percentage]
        max_bitrate: Optional[Union[int, float]] = MAX_BITRATE_THRESHOLD,
        min_bitrate: Optional[Union[int, float]] = MIN_BITRATE_THRESHOLD,
        **kwargs
    ) -> None:
        super().__init__(
            source,
            destination,
            name=name,
            bitrate=bitrate,
            frame_rate=frame_rate,
            number_of_frames=number_of_frames,
            duration=duration,
            initial_time_to_wait=initial_time_to_wait,
            frame_list=frame_list,
            imix=imix,
            max_bitrate=max_bitrate,
            min_bitrate=min_bitrate,
            **kwargs,
        )

        self._stream_scaler = DynamicStreamScaler(
            timedelta(seconds=scaling_interval), scaling_rate
        )

    def prepare_start(
        self,
        maximum_run_time: Optional[timedelta] = None
    ) -> Iterable[SynchronizedExecutable]:
        """Prepare Stream Scaler."""
        yield from super().prepare_start(maximum_run_time)

        self._stream_scaler.prepare(self.duration)

    def process(self) -> None:
        frame_rate = self._stream_scaler.scale(
            self._name,
            self._stream,
            self.stream_data_gatherer,
            self.stream_data_gatherer.realtime_packet_count(),
        )

        # Revert the updating direction if any threshold is reached
        if frame_rate is not None and (
            (self._max_frame_rate is not None
             and frame_rate > self._max_frame_rate) or
            (self._min_frame_rate is not None
             and frame_rate < self._min_frame_rate)):
            _LOGGER.info("Flow %r: Inverting scaling rate", self._name)
            self._stream_scaler.flip_scaling()

        super().process()
