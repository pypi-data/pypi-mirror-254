import logging
from typing import Optional, Sequence  # for type hinting

from byteblower_test_framework._analysis.data_analysis.frameblasting import (
    FrameCountAnalyser,
    LatencyCDFAnalyser,
)
from byteblower_test_framework._analysis.data_gathering.data_gatherer import \
    DataGatherer  # for type hinting
from byteblower_test_framework._analysis.latencyanalyser import (
    DEFAULT_LOSS_PERCENTAGE,
    DEFAULT_MAX_LATENCY_THRESHOLD,
    DEFAULT_QUANTILE,
    LatencyCDFFrameLossAnalyser,
)
from byteblower_test_framework._analysis.render.frameblasting import (
    LatencyCDFRenderer,
)
from byteblower_test_framework._analysis.storage.trigger import (
    LatencyDistributionData,
)
from byteblower_test_framework._report.options import Layer2Speed
from pandas import DataFrame  # for type hinting
from pandas import concat

from ._definitions import MAX_PERCENTILE, MIN_PERCENTILE


class LatencyOutlierDataAnalyser(LatencyCDFAnalyser):

    def __init__(
        self,
        data: LatencyDistributionData,
        max_threshold_latency: float,
        quantile: float,
        min_percentile: float,
        max_percentile: float,
    ) -> None:
        super().__init__(data, max_threshold_latency, quantile)
        self.min_percentile = min_percentile
        self.max_percentile = max_percentile
        # NOTE: Official term "Trimmed mean" / "Truncated mean"
        #       See https://en.wikipedia.org/wiki/Truncated_mean
        self._trimmed_avg_latency: Optional[float] = None

    def analyse(self) -> None:

        packet_count_buckets = self._data.packet_count_buckets
        bucket_width = self._data.bucket_width
        final_avg_latency = self.final_avg_latency

        try:
            trimmed_latencies_sum, trimmed_packet_count = (
                _trimmed_latency_calculator(
                    packet_count_buckets,
                    bucket_width,
                    self.min_percentile,
                    self.max_percentile,
                )
            )
            # Calculate the trimmed average latency
            self._trimmed_avg_latency = (
                trimmed_latencies_sum / trimmed_packet_count
            )
        except Exception:
            # In case of any error (no packets were received, ...)
            self._trimmed_avg_latency = self.final_avg_latency

        # TODO: Avoid hard-coded value(s).
        #     ! Also update (Base)LatencyCDFFrameCountDataGatherer accordingly
        latency_range_min = 0.0 / 1e6
        latency_range_max = len(packet_count_buckets) * bucket_width / 1e6
        assert (latency_range_max == int(50 * self._max_threshold_latency)), (
            "Invalid latency range. Expected hard-coded maximum value"
            " of 50 * max latency threshold."
        )
        self._df_latency = DataFrame(columns=["latency", "percentile"])
        final_min_latency = self._data.final_min_latency
        final_max_latency = self._data.final_max_latency
        final_avg_jitter = self._data.final_avg_jitter
        final_packet_count_valid = self._data.final_packet_count_valid
        # final_packet_count_invalid = self._data.final_packet_count_invalid
        final_packet_count_below_min = self._data.final_packet_count_below_min
        final_packet_count_above_max = self._data.final_packet_count_above_max

        # Build percentiles
        percentiles = []
        i = 0.00
        incr = 10.0
        while i <= 100.00:
            i += incr
            logging.debug("Adding percentile %s", i)
            percentiles.append(i)
            # I know this seems strange, but comparing floats is very tricky.
            # This doesn't work:
            # if ( 100.0 - i ) < incr
            # See  https://stackoverflow.com/questions/3049101/floating-point-equality-in-python-and-in-general  # noqa: E501 # pylint: disable=line-too-long
            if (100.0 - i - incr) < (incr / 10):
                incr /= 10
                if incr < 0.01:
                    break

        # Process latency
        self._set_result(True)
        if final_packet_count_valid == 0:
            self._set_log("No packets received. Test has failed.")
            self._set_result(False)
            self._add_failure_cause(
                "Did not receive any packets with valid latency tag."
            )
            return

        total_packet_count_in_buckets = sum(packet_count_buckets)
        if (total_packet_count_in_buckets + final_packet_count_below_min +
                final_packet_count_above_max) != final_packet_count_valid:
            logging.warning(
                'Packet count: %r (total in buckets) + %r (below min) '
                '+ %r (above max) != %r (valid): Latency sampling'
                ' was likely active on the ByteBlower server',
                total_packet_count_in_buckets, final_packet_count_below_min,
                final_packet_count_above_max, final_packet_count_valid
            )

        if total_packet_count_in_buckets == 0:
            summary_log = []
            failure_cause = (
                "Failed to validate results. All packets"
                " received outside latency histogram range"
                f" [{latency_range_min}, {latency_range_max}] ms"
            )
            summary_log.append(failure_cause)
            summary_log.append(
                "Number of packets below minimum latency"
                f": {final_packet_count_below_min}"
            )
            summary_log.append(
                "Number of packets above maximum latency"
                f": {final_packet_count_above_max}"
            )

            self._set_log('\n'.join(summary_log))
            self._set_result(False)
            self._add_failure_cause(failure_cause)
            return

        if final_packet_count_below_min:
            logging.warning(
                'Latency CDF data analysis: Number of packets (%r) with'
                ' latency values below minimum are not taken into'
                ' account for the CDF calculation.',
                final_packet_count_below_min
            )

        if final_packet_count_above_max:
            logging.warning(
                'Latency CDF data analysis: Number of packets (%r) with'
                ' latency values above maximum are not taken into'
                ' account for the CDF calculation.',
                final_packet_count_above_max
            )

        log = [
            f"Latency is below {self._max_threshold_latency} ms"
            " for all percentile values."
        ]

        for percentile in percentiles:
            # Let's calculate the latency
            percentile_factor = percentile / 100.0
            if (final_packet_count_above_max / total_packet_count_in_buckets
                    > (1.0 - percentile_factor)
                    and percentile <= self._quantile):
                if self.has_passed:
                    failure_cause = (
                        "Latency is larger"
                        f" than {self._max_threshold_latency} ms"
                        f" for quantile {percentile}"
                    )
                    self._set_result(False)
                    self._add_failure_cause(failure_cause)
                    log = [failure_cause]
            # The user will need to know the latency percentile.
            threshold = percentile_factor * total_packet_count_in_buckets
            cumul = 0
            for bucket_number, packet_count_bucket in enumerate(
                    packet_count_buckets, start=1):

                cumul += packet_count_bucket
                if cumul > threshold:
                    df_latency_update = DataFrame(
                        {
                            'latency': [bucket_number * bucket_width],
                            'percentile': percentile,
                        }
                    )

                    # Avoid FutureWarning:
                    #   The behavior of DataFrame concatenation with empty
                    #   or all-NA entries is deprecated. In a future version,
                    #   this will no longer exclude empty or all-NA columns
                    #   when determining the result dtypes. To retain the
                    #   old behavior, exclude the relevant entries before
                    #   the concat operation.
                    if self._df_latency.empty:
                        self._df_latency = df_latency_update
                    else:
                        self._df_latency = concat(
                            [self._df_latency, df_latency_update],
                            ignore_index=True,
                        )

                    if not self.has_passed:
                        bucket_latency = (
                            bucket_number * bucket_width / 1000000.0
                        )
                        log.append(
                            f"\tLatency for quantile {percentile}"
                            f" is {bucket_latency:0.2f}ms."
                        )
                    break

        if final_max_latency is None:
            # NOTE - If we did not receive any data,
            #        we will not have latency values.
            self._set_result(False)
            self._add_failure_cause("No latency related data received")
        elif final_max_latency > self._max_threshold_latency:
            self._set_result(False)
            self._add_failure_cause(
                "Latency has exceeded the maximum allowed latency"
                f" of {self._max_threshold_latency:0.2f} ms"
            )

        # Add latency summary information to the log
        summary_log = []
        summary_log.append(
            f"Minimum latency: {_format_milliseconds(final_min_latency)}"
        )
        summary_log.append(
            f"Maximum latency: {_format_milliseconds(final_max_latency)}"
        )
        summary_log.append(
            "Full range average latency:"
            f" {_format_milliseconds(final_avg_latency)}"
        )
        # NOTE: Official term "Trimmed mean" / "Truncated mean"
        #       See https://en.wikipedia.org/wiki/Truncated_mean
        summary_log.append(
            "Trimmed Average latency:"
            f" {_format_milliseconds(self._trimmed_avg_latency)}"
        )
        summary_log.append(
            f"Average latency jitter: {_format_milliseconds(final_avg_jitter)}"
        )
        summary_log.append(
            "Number of packets below minimum latency"
            f": {final_packet_count_below_min}"
        )
        summary_log.append(
            "Number of packets above maximum latency"
            f": {final_packet_count_above_max}"
        )

        self._set_log('\n'.join((*summary_log, *log)))


class LatencyOutlierFrameLossAnalyser(LatencyCDFFrameLossAnalyser):
    """Analyse latency CDF and total frame count.

    The analyser provides the latency CDF graph, RX and TX frame count
    and byte loss over the duration of the test.
    For the latency results you will also have the average, trimmed average,
    minimum and maximum latency and average latency jitter.

    """

    __slots__ = (
        "_min_percentile",
        "_max_percentile",
    )

    def __init__(
        self,
        layer2_speed: Layer2Speed = Layer2Speed.frame,
        max_loss_percentage: float = DEFAULT_LOSS_PERCENTAGE,
        max_threshold_latency: float = DEFAULT_MAX_LATENCY_THRESHOLD,
        quantile: float = DEFAULT_QUANTILE,
        min_percentile: float = MIN_PERCENTILE,
        max_percentile: float = MAX_PERCENTILE,
    ):
        """Create the latency CDF and total frame count analyser.

        The latency for the CDF graph will be analysed over a range of
        ``[0, 50 * max_threshold_latency[``.

        :param layer2_speed: Configuration setting to select the layer 2
           speed reporting, defaults to :attr:`~.options.Layer2Speed.frame`
        :type layer2_speed: Layer2Speed, optional
        :param max_loss_percentage: Maximum allowed byte loss in %,
           defaults to :const:`DEFAULT_LOSS_PERCENTAGE`
        :type max_loss_percentage: float, optional
        :param max_threshold_latency: _description_,
           defaults to :const:`DEFAULT_MAX_LATENCY_THRESHOLD`
        :type max_threshold_latency: float, optional
        :param quantile: Quantile for which the latency must be less than the
           given maximum average latency, defaults to :const:`DEFAULT_QUANTILE`
        :type quantile: float, optional
        :param min_percentile: Lower boundary of latency outliers,
           defaults to :const:`MIN_PERCENTILE`
        :type min_percentile: float, optional
        :param max_percentile: Upper boundary of latency outliers,
           defaults to :const:`MAX_PERCENTILE`
        :type max_percentile: float, optional
        """
        self._min_percentile = min_percentile
        self._max_percentile = max_percentile
        super().__init__(
            layer2_speed, max_loss_percentage, max_threshold_latency, quantile
        )

    def _initialize(self) -> None:
        flow = self.flow
        flow.require_stream_data_gatherer()
        self._data_gatherer: DataGatherer = self._DATA_GATHERER_CLASS(
            self._data_framecount, self._data_latencydistribution,
            self._max_threshold_latency, self.flow
        )
        self._framecount_analyser = FrameCountAnalyser(
            flow.stream_frame_count_data, self._data_framecount,
            self._layer2_speed, self._max_loss_percentage
        )
        self._latency_cdf_analyser = LatencyOutlierDataAnalyser(
            self._data_latencydistribution, self._max_threshold_latency,
            self._quantile, self._min_percentile, self._max_percentile
        )
        self._renderer = LatencyCDFRenderer(
            self._framecount_analyser, self._latency_cdf_analyser
        )


def _trimmed_latency_calculator(
    packet_count_buckets: Sequence[int],
    bucket_width: int,
    min_percentile: float,
    max_percentile: float,
):
    # Latency outliers are latencies of packets that are out of
    # the percentile range [min_boundary,max_boundary] (boundaries included)

    # Min & Max boundaries
    min_boundary = int(sum(packet_count_buckets) * min_percentile / 100) - 1
    max_boundary = int(sum(packet_count_buckets) * max_percentile / 100 + 1)
    trimmed_latencies_sum = 0
    trimmed_packet_count = 0
    useful_packet_count = 0
    cumul = 0
    # Preparation to calculate the trimmed average latency
    for bucket_count, packet_count_bucket in enumerate(packet_count_buckets):
        if packet_count_bucket != 0:
            cumul += packet_count_bucket

            # If the min_boundary value is in the between
            # the current and last cumul,
            # consider adding only packet count between
            # the min_boundary and current cumul
            if cumul - packet_count_bucket <= min_boundary <= cumul:
                useful_packet_count = cumul - min_boundary + 1
                bucket_latency_sum = 0
                for i in range(useful_packet_count):
                    bucket_latency_sum += (bucket_width / 1e6) * (
                        bucket_count + i / packet_count_bucket
                    )
                trimmed_packet_count += useful_packet_count
                trimmed_latencies_sum += bucket_latency_sum

            elif cumul in range(min_boundary, max_boundary):
                average_bucket_latency = (bucket_width / 1e6) * (
                    bucket_count + 1 / 2
                )
                trimmed_packet_count += packet_count_bucket
                trimmed_latencies_sum += (
                    packet_count_bucket * average_bucket_latency
                )

            # If the max_boundary value is in the between
            # the current and last cumul,
            # consider adding only packet count between
            # the min_boundary and current cumul
            elif cumul - packet_count_bucket <= max_boundary <= cumul:
                useful_packet_count = max_boundary - (
                    cumul - packet_count_bucket
                ) + 1
                bucket_latency_sum = 0
                for i in range(useful_packet_count):
                    bucket_latency_sum += (bucket_width / 1e6) * (
                        bucket_count + i / packet_count_bucket
                    )
                trimmed_packet_count += useful_packet_count
                trimmed_latencies_sum += bucket_latency_sum
            elif cumul > max_boundary:
                break

    return trimmed_latencies_sum, trimmed_packet_count


def _format_milliseconds(value: Optional[float]) -> str:
    if value is not None:
        return f"{value:0.3f} ms"
    return "n/a"
