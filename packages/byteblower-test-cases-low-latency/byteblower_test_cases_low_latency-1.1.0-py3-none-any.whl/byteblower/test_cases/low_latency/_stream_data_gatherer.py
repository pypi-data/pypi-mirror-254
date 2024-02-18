from datetime import timedelta
from typing import TYPE_CHECKING  # for type hinting

from byteblower_test_framework._analysis.data_gathering.stream import (
    StreamFrameCountDataGatherer,
)
from pandas import DataFrame, to_datetime

if TYPE_CHECKING:
    # For type hinting
    from byteblower_test_framework._analysis.storage.frame_count import (
        FrameCountData,
    )
    from byteblower_test_framework._analysis.storage.stream import (
        StreamStatusData,
    )
    from byteblower_test_framework._traffic.frameblastingflow import (
        FrameBlastingFlow,
    )
    from byteblowerll.byteblower import StreamResultData
    from pandas import Timestamp


class DynamicStreamFrameCountDataGatherer(StreamFrameCountDataGatherer):

    __slots__ = (
        '_latest_cumulative_packets',
        '_latest_cumulative_bytes',
        '_ts_first',
        '_cumulative_df_tx',
        '_interval_df_tx',
    )

    def __init__(
        self, stream_status_data: 'StreamStatusData',
        frame_count_data: 'FrameCountData', flow: 'FrameBlastingFlow'
    ) -> None:
        super().__init__(stream_status_data, frame_count_data, flow)
        self._latest_cumulative_packets = 0
        self._latest_cumulative_bytes = 0
        self._ts_first = None
        self._cumulative_df_tx = DataFrame(
            columns=[
                "Packets total",
                "Bytes total",
            ]
        )
        self._interval_df_tx = DataFrame(
            columns=[
                "Packets interval",
                "Bytes interval",
            ]
        )

    def _process_snapshot(
        self, timestamp: 'Timestamp', cumulative_snapshot: 'StreamResultData',
        interval_snapshot: 'StreamResultData'
    ) -> None:
        self._cumulative_df_tx.loc[timestamp] = [
            self._latest_cumulative_packets,
            self._latest_cumulative_bytes,
        ]

    def summarize(self) -> None:
        super().summarize()
        self._frame_count_data._total_bytes += self._latest_cumulative_bytes
        self._frame_count_data._total_vlan_bytes += (
            self._latest_cumulative_packets * self._tx_vlan_header_size
        )
        self._frame_count_data._total_packets += (
            self._latest_cumulative_packets
        )
        self._frame_count_data._timestamp_first = to_datetime(
            self._ts_first, unit='ns', utc=True
        )

        self._frame_count_data._over_time = (
            self._frame_count_data._over_time.add(
                self._cumulative_df_tx,
                fill_value=0,
            ).add(
                self._interval_df_tx,
                fill_value=0,
            )
        )

    def persist_current_stream_results(self) -> None:
        # Refresh the history
        self._tx_result.Refresh()

        # Add all the history interval results
        self._persist_history_snapshots()

        # Cumulative results
        #
        # NOTE: Updating cumulative packet/byte count must be done:
        #
        # 1. *after* persisting the cumulative history
        #    We must persist the history with the *previous* cumulative counts
        #    This stream run has not finished in these older snapshots!
        #
        # 2. *before* persisting the current cumulative/interval results.
        #    When the next stream run does not have a snapshot in this second,
        #    it won't have the correct cumulative counts either.
        #
        cumulative_snapshot: 'StreamResultData' = (
            self._tx_result.CumulativeLatestGet()
        )
        tx_packet_count = cumulative_snapshot.PacketCountGet()
        if self._ts_first is None and tx_packet_count:
            self._ts_first = cumulative_snapshot.TimestampFirstGet()
        self._latest_cumulative_packets += tx_packet_count
        self._latest_cumulative_bytes += cumulative_snapshot.ByteCountGet()

        # Add the remaining interval results
        ts_ns: int = cumulative_snapshot.TimestampGet()
        tx_interval: 'StreamResultData' = \
            self._tx_result.IntervalGetByTime(ts_ns)
        timestamp = to_datetime(ts_ns, unit='ns', utc=True)
        self._interval_df_tx.loc[timestamp] = [
            tx_interval.PacketCountGet(),
            tx_interval.ByteCountGet(),
        ]
        # NOTE: Actually the interval_snapshot is not needed
        #       in (our) _process_snapshot, but kept here
        #       for consistency.
        interval_snapshot: 'StreamResultData' = (
            self._tx_result.IntervalGetByTime(ts_ns)
        )
        # NOTE: Must be done *after* updating cumulative packet/byte count !
        self._process_snapshot(
            timestamp, cumulative_snapshot, interval_snapshot
        )

        # Clear the history
        self._tx_result.Clear()

    def realtime_packet_count(self) -> int:
        self._tx_result.Refresh()
        tx: 'StreamResultData' = self._tx_result.CumulativeLatestGet()
        tx_packets = tx.PacketCountGet()
        return self._latest_cumulative_packets + tx_packets

    def elapsed_duration(self) -> timedelta:
        self._tx_result.Refresh()
        tx: 'StreamResultData' = self._tx_result.CumulativeLatestGet()
        tx_packets = tx.PacketCountGet()
        if not tx_packets:
            return timedelta()
        ts_tx_first_ns = self._ts_first or tx.TimestampFirstGet()
        ts_tx_last_ns = tx.TimestampLastGet()
        elapsed_ns = ts_tx_last_ns - ts_tx_first_ns
        elapsed = timedelta(seconds=elapsed_ns * 1e-9)
        return elapsed
