"""Module for specific analysis objects for CIN layer 2 network testing."""
import logging
from typing import Optional  # for type hinting

# ! FIXME: We are using "protected" modules/classes
#          * These might be subject to change in later versions
#          * of the ByteBlower Test Framework!
from byteblower_test_framework._analysis.data_analysis.frameblasting import (
    FrameCountAnalyser,
)
from byteblower_test_framework._analysis.data_gathering.trigger import (
    BaseFrameCountDataGatherer,
    FrameFilterBuilder,
)
from byteblower_test_framework._analysis.framelossanalyser import (
    BaseFrameLossAnalyser,
)
from byteblower_test_framework._analysis.render.frameblasting import (
    FrameCountRenderer,
)
from byteblower_test_framework._analysis.storage.frame_count import (
    FrameCountData,
)
from byteblower_test_framework.endpoint import Endpoint, IPv4Port, IPv6Port
from byteblower_test_framework.report import Layer2Speed
from byteblower_test_framework.traffic import FrameBlastingFlow
from byteblowerll.byteblower import TriggerBasicResultData

from .exceptions import FeatureNotSupported, InvalidInput, LowLatencyException

_LOGGER = logging.getLogger(__name__)

# TODO: Re-defined here because the location will change
#       * in the upcoming (beta) release of the ByteBlower Test Framework

#: Default maximum frame loss percentage (range ``[0.0, 100.0]``)
#: used in the latency and frame loss related analysers.
DEFAULT_LOSS_PERCENTAGE: float = 1.0
#: Default maximum average latency in milliseconds
#: used in the latency and frame loss related analysers.
DEFAULT_MAX_LATENCY_THRESHOLD: float = 5  # [ms]


class L4SMarkingFilterBuilder(FrameFilterBuilder):  # pylint: disable=too-few-public-methods
    """Filter builder for L4S markings data gathering."""

    __slots__ = (
        '_ecn',
        '_dscp',
    )

    def __init__(
        self,
        ecn: Optional[int] = None,
        dscp: Optional[int] = None,
    ) -> None:
        """Create a L4S markings filter builder.

        :param ecn:  When defined, this analyser will check the IP ECN bits,
           defaults to None
        :type ecn: Optional[int], optional
        :param dscp: When defined, this analyser will check the IP DSCP bits,
           defaults to None
        :type dscp: Optional[int], optional
        """
        super().__init__()

        # Sanity check
        _check_input(ecn, dscp)
        self._ecn = ecn
        self._dscp = dscp

    def build_bpf_filter(self, flow: FrameBlastingFlow) -> str:  # pylint: disable=arguments-differ
        """Create the BPF filter string.

        :param flow: Flow to create the BPF filter string for
        :type flow: FrameBlastingFlow
        :return: BPF filter string
        :rtype: str
        """
        bpf_filter = super().build_bpf_filter(flow)
        if self._ecn:
            ecn_filter = self._create_ecn_bpf_filter(flow, self._ecn)
            if ecn_filter:
                # MUST *append* it here:
                bpf_filter = f"({bpf_filter}) and ({ecn_filter})"

        if self._dscp is not None:
            dscp_filter = self._create_dscp_bpf_filter(flow, self._dscp)
            # MUST *append* it here:
            bpf_filter = f"({bpf_filter}) and ({dscp_filter})"

        _LOGGER.debug("L4S markings BPF Filter: %r", bpf_filter)
        return bpf_filter

    @staticmethod
    def _create_ecn_bpf_filter(flow: FrameBlastingFlow,
                               ecn: int) -> Optional[str]:
        source_port = flow.source
        destination_port = flow.destination
        if isinstance(source_port, IPv6Port) and isinstance(destination_port,
                                                            IPv6Port):
            return f"((ip6[1] & 0x30) >> 4) = {ecn}"
        if isinstance(source_port, IPv4Port) and isinstance(destination_port,
                                                            IPv4Port):
            return f"ip[1] & 0x3 = {ecn}"
        raise LowLatencyException(
            'L4SMarkingFilterBuilder: Cannot create BPF filter for Flow'
            f' {flow.name}: Unsupported Port type: Source:'
            f' {source_port.name} > {type(source_port)}'
            ' or destination:'
            f' {destination_port.name} > {type(destination_port)}'
        )

    @staticmethod
    def _create_dscp_bpf_filter(flow: FrameBlastingFlow, dscp: int) -> str:
        source_port = flow.source
        destination_port = flow.destination
        if isinstance(source_port, IPv6Port) and isinstance(destination_port,
                                                            IPv6Port):
            return f"((ip6[0:2] & 0xfc0) >> 6) = {dscp}"
        if isinstance(source_port, IPv4Port) and isinstance(destination_port,
                                                            IPv4Port):
            return f"((ip[1] & 0xfc) >> 2) = {dscp}"
        raise LowLatencyException(
            'L4SMarkingFilterBuilder: Cannot create BPF filter for Flow'
            f' {flow.name}: Unsupported Port type: Source:'
            f' {source_port.name} > {type(source_port)}'
            ' or destination:'
            f' {destination_port.name} > {type(destination_port)}'
        )


class L4SMarkingDataGatherer(BaseFrameCountDataGatherer):
    """Data gatherer for L4S marking analysis."""

    __slots__ = ()

    def __init__(
        self,
        framecount_data: FrameCountData,
        flow: FrameBlastingFlow,
        ecn: Optional[int] = None,
        dscp: Optional[int] = None
    ) -> None:
        """Create the L4S marking data gatherer.

        :param framecount_data: Storage for the frame count data
        :type framecount_data: FrameCountData
        :param flow: Flow to analyse
        :type flow: FrameBlastingFlow
         When defined, this analyser will check the IP ECN bits,
           defaults to None
        :param ecn:  When defined, this analyser will check the IP ECN bits,
           defaults to None
        :type ecn: Optional[int], optional
        :param dscp: When defined, this analyser will check the IP DSCP bits,
           defaults to None
        :type dscp: Optional[int], optional
           speed reporting, defaults to :attr:`~.options.Layer2Speed.frame`
        """
        if isinstance(flow.destination, Endpoint):
            raise FeatureNotSupported(
                "L4SMarkingAnalyzer does not support ByteBlower Endpoint"
            )
        super().__init__(
            framecount_data,
            flow,
            frame_filter_builder=L4SMarkingFilterBuilder(ecn=ecn, dscp=dscp)
        )

    def realtime_packet_count(self) -> int:
        self._rx_result.Refresh()
        result_cumul: TriggerBasicResultData = (
            self._rx_result.CumulativeLatestGet()
        )
        total_rx_packets = result_cumul.PacketCountGet()
        return total_rx_packets


class L4SMarkingAnalyser(BaseFrameLossAnalyser):
    """Analyse frame count over time.

    The data gathering counts the number of frames which match
    the expected IP ECN and/or IP DSCP bits.

    The analyser also provides the RX and TX frame count and frame loss
    over the duration of the test.

    This analyser is intended for use with a
    :class:`~byteblower_test_framework.traffic.Flow` based on a
    :class:`~byteblower_test_framework.traffic.FrameBlastingFlow`.

    Supports:

    * Analysis of a single flow
    * Usage in :class:`~byteblower_test_framework.analysis.AnalyserAggregator`.
    """

    _DATA_GATHERER_CLASS = L4SMarkingDataGatherer

    __slots__ = (
        '_ecn',
        '_dscp',
    )

    def __init__(
        self,
        ecn: Optional[int] = None,
        dscp: Optional[int] = None,
        layer2_speed: Layer2Speed = Layer2Speed.frame,
        max_loss_percentage: float = DEFAULT_LOSS_PERCENTAGE
    ):
        """Create frame count over time analyser for L4S marking.

        :param layer2_speed: Configuration setting to select the layer 2
        :param ecn:  When defined, this analyser will check the IP ECN bits,
           defaults to None
        :type ecn: Optional[int], optional
        :param dscp: When defined, this analyser will check the IP DSCP bits,
           defaults to None
        :type dscp: Optional[int], optional
           speed reporting, defaults to :attr:`~.options.Layer2Speed.frame`
        :type layer2_speed: ~options.Layer2Speed, optional
        :param max_loss_percentage: Maximum allowed packet loss in %,
           defaults to :const:`DEFAULT_LOSS_PERCENTAGE`
        :type max_loss_percentage: float, optional
        """
        # Sanity check
        _check_input(ecn, dscp)

        super().__init__(
            'L4S marking analyser',
            layer2_speed=layer2_speed,
            max_loss_percentage=max_loss_percentage
        )

        self._ecn = ecn
        self._dscp = dscp

    def _initialize(self) -> None:
        flow = self.flow
        flow.require_stream_data_gatherer()
        self._data_gatherer: L4SMarkingDataGatherer = (
            self._DATA_GATHERER_CLASS(
                self._data, flow, ecn=self._ecn, dscp=self._dscp
            )
        )
        self._data_analyser = FrameCountAnalyser(
            flow.stream_frame_count_data, self._data, self._layer2_speed,
            self._max_loss_percentage
        )
        self._renderer = FrameCountRenderer(self._data_analyser)

    def realtime_packet_count(self) -> int:
        total_rx_packets = self._data_gatherer.realtime_packet_count()
        return total_rx_packets


def _check_input(ecn: Optional[int], dscp: Optional[int]) -> None:
    if ecn is None and dscp is None:
        raise InvalidInput("Missing parameters: Either ECN or DSCP, or both")
