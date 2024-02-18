import logging
from datetime import timedelta
from enum import Enum
from typing import TYPE_CHECKING, Iterable, Optional, Union

from byteblower_test_framework.factory import create_frame

from .dynamic_frameblastingflow import (
    BaseDynamicRateFrameBlastingFlow,
    DynamicStreamScaler,
)
from .exceptions import InvalidInput
from .l4s_analysers import L4SMarkingAnalyser

if TYPE_CHECKING:
    # For type hinting
    # ! FIXME: We are using "protected" modules/classes
    #          * These might be subject to change in later versions
    #          * of the ByteBlower Test Framework!
    from byteblower_test_framework._helpers.syncexec import (
        SynchronizedExecutable,
    )
    from byteblower_test_framework.endpoint import Port

_LOGGER = logging.getLogger(__name__)


class ECN_codepoint(Enum):
    #: Not-ECT - Not ECN-Capable Transport
    not_ect: int = 0b00
    #: ECT(0) - ECN-Capable Transport(0)
    classic: int = 0b10
    #: ECT(1) - ECN-Capable Transport(1)
    l4s: int = 0b01
    #: CE - Congestion Experienced
    ce: int = 0b11


class L4SFrameBlastingFlow(BaseDynamicRateFrameBlastingFlow):
    """Flow for simulating L4S frame blasting flow."""

    __slots__ = (
        '_l4s_ecn',
        '_l4s_stream_scaler',
        '_ce_stream_scaler',
        '_l4s_analyser',
        '_ce_analyser',
    )

    def __init__(
        self,
        source: 'Port',
        destination: 'Port',
        name: Optional[str] = None,
        bitrate: Optional[float] = None,  # [bps]
        frame_rate: Optional[float] = None,  # [fps]
        frame_size: Optional[float] = None,  # [Bytes]
        udp_src: int = None,
        udp_dest: int = None,
        number_of_frames: Optional[int] = None,
        l4s_ecn: Optional[ECN_codepoint] = None,
        ip_dscp: Optional[int] = None,
        duration: Optional[Union[timedelta, float, int]] = None,  # [seconds]
        enable_latency: Optional[bool] = True,
        initial_time_to_wait: Optional[Union[timedelta, float,
                                             int]] = None,  # [seconds]
        max_bitrate: Optional[Union[int, float]] = None,
        min_bitrate: Optional[Union[int, float]] = None,
        **kwargs
    ) -> None:
        if l4s_ecn is None:
            # Default is L4S flow:
            l4s_ecn = ECN_codepoint.l4s
        else:
            # NOTE:
            #     Allow 'ce' to be able to "force" congestion-notified traffic
            # if l4s_ecn not in (ECN_codepoint.classic, ECN_codepoint.l4s,
            #                    ECN_codepoint.not_ect):
            if l4s_ecn not in ECN_codepoint:
                raise InvalidInput("Unsupported ECN codepoint")
            if l4s_ecn == ECN_codepoint.ce:
                _LOGGER.warning(
                    "Flow %r: Creating L4S traffic stream with"
                    " ECN bits set to CE.", name
                )
        self._l4s_ecn = l4s_ecn

        # Determine flow version and create frame
        ip_ecn = l4s_ecn.value
        frame = create_frame(
            source,
            length=frame_size,
            udp_src=udp_src,
            udp_dest=udp_dest,
            ip_ecn=ip_ecn,
            ip_dscp=ip_dscp,
            latency_tag=enable_latency
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
            frame_list=[frame],
            max_bitrate=max_bitrate,
            min_bitrate=min_bitrate,
            **kwargs,
        )

        # l4s flow specific scaler
        self._l4s_stream_scaler = DynamicStreamScaler(timedelta(seconds=2), 3)
        # ce flow specific scaler
        self._ce_stream_scaler = DynamicStreamScaler(timedelta(seconds=2), -3)

        # # OPTIONAL: Add Check DSCP traffic
        # if dscp is not None:
        #     self._dscp_analyser = L4SMarkingAnalyser(dscp=64)
        #     self.add_analyser(self._dscp_analyser)

        # Check L4S traffic (ECT 1)
        # NOTE: Allow 'ce' to "force" congestion-notified traffic ...
        if self._l4s_ecn == ECN_codepoint.ce:
            # ... but then don't add the analyser for "not notified" traffic
            self._l4s_analyser = None
        else:
            self._l4s_analyser = L4SMarkingAnalyser(ecn=self._l4s_ecn.value)
            # NOTE: Don't add it for reporting, but properly initialize it:
            # self.add_analyser(self._l4s_analyser)
            self._l4s_analyser._add_to_flow(self)

        # Check Congestion Experienced (CE):
        # Set max_loss_percentage=99.9 to try avoid Fail status in report
        self._ce_analyser = L4SMarkingAnalyser(
            ecn=ECN_codepoint.ce.value, max_loss_percentage=99.9
        )
        # NOTE: Don't add it for reporting, but properly initialize it:
        # self.add_analyser(self._ce_analyser)
        self._ce_analyser._add_to_flow(self)

    def prepare_configure(self) -> None:
        "Prepare L4S and CE analysers."
        super().prepare_configure()
        if self._l4s_analyser is not None:
            self._l4s_analyser.prepare_configure()
        self._ce_analyser.prepare_configure()

    def initialize(self) -> None:
        "Initialize L4S and CE analysers."
        super().initialize()
        if self._l4s_analyser is not None:
            self._l4s_analyser.initialize()
        self._ce_analyser.initialize()

    def prepare_start(
        self,
        maximum_run_time: Optional[timedelta] = None
    ) -> Iterable['SynchronizedExecutable']:
        "Prepare L4S and CE stream scalers."
        yield from super().prepare_start(maximum_run_time=maximum_run_time)

        if self._l4s_analyser is not None:
            self._l4s_analyser.prepare_start()
        self._ce_analyser.prepare_start()

        self._l4s_stream_scaler.prepare(self.duration)
        self._ce_stream_scaler.prepare(self.duration)

    def process(self) -> None:
        # Don't process Not-ECN-Capable Transport flows
        # NOTE: Allowing 'Congestion Experienced' flows
        #       to process "forced" congestion-notified traffic
        if self._l4s_ecn not in {ECN_codepoint.classic, ECN_codepoint.l4s,
                                 ECN_codepoint.ce}:
            return

        # Scale up only if no congestion experienced
        # (CE packets received) during last interval
        packet_count = self._ce_analyser.realtime_packet_count()
        if packet_count > self._ce_stream_scaler.last_packet_count:
            # Scale down framerate in case of Congestion Experienced CE
            self._ce_stream_scaler.scale(
                self._name,
                self._stream,
                self.stream_data_gatherer,
                packet_count,
            )
        else:
            # Scale up framerate if no congestion experienced
            if self._l4s_analyser is not None:
                self._l4s_stream_scaler.scale(
                    self._name,
                    self._stream,
                    self.stream_data_gatherer,
                    self._l4s_analyser.realtime_packet_count(),
                )
        super().process()

        if self._l4s_analyser is not None:
            self._l4s_analyser.process()
        self._ce_analyser.process()

    def updatestats(self) -> None:
        super().updatestats()
        if self._l4s_analyser is not None:
            self._l4s_analyser.updatestats()
        self._ce_analyser.updatestats()

    def analyse(self) -> None:
        super().analyse()
        if self._l4s_analyser is not None:
            self._l4s_analyser.analyse()
        self._ce_analyser.analyse()
