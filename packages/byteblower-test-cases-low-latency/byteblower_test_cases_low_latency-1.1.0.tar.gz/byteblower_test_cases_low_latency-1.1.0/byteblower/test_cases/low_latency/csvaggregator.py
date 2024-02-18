"""Aggregation of flow analysers into CSV."""
from typing import List, Union  # for type hinting

from byteblower_test_framework._analysis.framelossanalyser import (
    BaseFrameLossAnalyser,
    FrameLossAnalyser,
)
from byteblower_test_framework._analysis.latencyanalyser import (
    BaseLatencyFrameLossAnalyser,
)
from byteblower_test_framework.analysis import FlowAnalyser  # for type hinting
from pandas import DataFrame

# Type aliases
# XXX - Explicit classes to avoid user-specific classes
#       (like L4SMarkingAnalyser)
# _OverTimeLatencyAnalysers = (BaseLatencyFrameLossAnalyser, )
_FrameCountAnalysers = (FrameLossAnalyser, )
_OverTimeLatencyAnalysers = (BaseLatencyFrameLossAnalyser, )
# NOTE: CDF analyser does not support "over time" results (yet):
_OverTimeSupportedAnalysersList = (
    _FrameCountAnalysers + _OverTimeLatencyAnalysers
)
# NOTE: CDF analyser does not support "over time" results (yet):
# PossiblySupportedAnalysers = Union[BaseFrameLossAnalyser,
#                                    BaseLatencyFrameLossAnalyser,
#                                    BaseLatencyCDFFrameLossAnalyser]
PossiblySupportedAnalysers = Union[BaseFrameLossAnalyser,
                                   BaseLatencyFrameLossAnalyser]
# CsvAggregator only support over-time analysers (for now)
_OverTimeSupportedAnalysers = PossiblySupportedAnalysers


class CsvAggregator(object):
    __slots__ = ('_analysers', )

    def __init__(self) -> None:
        self._analysers: List[FlowAnalyser] = []

    def add_analyser(self, analyser: FlowAnalyser) -> None:
        self._analysers.append(analyser)

    def can_render(self) -> bool:
        return len(self._analysers) > 0

    def store(self, csv_file: str) -> None:
        result = DataFrame()
        for analyser in self._analysers:
            flow = analyser._flow
            # Unicode characters don't work properly in CSV:
            # series_title = (
            #     f'{flow.name}\n{flow.source.name}'
            #     f' \u2794 {flow.destination.name}'
            # )
            series_title = (
                f'{flow.name}\n{flow.source.name}'
                f' -> {flow.destination.name}'
            )
            if _analyser_has_frame_count_over_time(analyser):
                df_tx_bytes = analyser.df_tx_bytes
                result = result.join(
                    df_tx_bytes.rename(
                        columns={'Bytes interval': f'TX ({series_title})'}
                    ),
                    how='outer',
                )
                df_rx_bytes = analyser.df_rx_bytes
                result = result.join(
                    df_rx_bytes.rename(
                        columns={'Bytes interval': f'RX ({series_title})'}
                    ),
                    how='outer',
                )
            if _analyser_has_latency_over_time(analyser):
                df_latency = analyser._latency_analyser.df_latency
                result = result.join(
                    df_latency.rename(
                        columns={
                            'Minimum': f'Minimum latency ({series_title})',
                            'Maximum': f'Maximum latency ({series_title})',
                            'Average': f'Average latency ({series_title})',
                            'Jitter': f'Jitter latency ({series_title})',
                        }
                    ),
                    how='outer',
                    rsuffix=f' | Latency | {flow.name}'
                )

        result.to_csv(csv_file, encoding='utf-8')


def _analyser_has_frame_count_over_time(
    analyser: _OverTimeSupportedAnalysers
) -> bool:
    return isinstance(analyser, _OverTimeSupportedAnalysersList)


def _analyser_has_latency_over_time(
    analyser: _OverTimeSupportedAnalysers
) -> bool:
    return isinstance(analyser, _OverTimeLatencyAnalysers)
