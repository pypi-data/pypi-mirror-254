#  --------------------------------------------------------------------------------
#  Copyright (c) 2021 DataRobot, Inc. and its affiliates. All rights reserved.
#  Last updated 2023.
#
#  DataRobot, Inc. Confidential.
#  This is proprietary source code of DataRobot, Inc. and its affiliates.
#
#  This file and its contents are subject to DataRobot Tool and Utility Agreement.
#  For details, see
#  https://www.datarobot.com/wp-content/uploads/2021/07/DataRobot-Tool-and-Utility-Agreement.pdf.
#
#  --------------------------------------------------------------------------------
import json
from typing import Dict
from typing import Iterable
from typing import List
from typing import Tuple
from typing import Union

import numpy as np
from datarobot_mlops.drift.feature_distributions import FeatureDistributions
from datarobot_mlops.stats_aggregator import FeatureType
from datarobot_mlops.stats_aggregator.aggregates import CategoricalAggregate
from datarobot_mlops.stats_aggregator.aggregates import NumericAggregate
from datarobot_mlops.stats_aggregator.histogram import CentroidBucket
from datarobot_mlops.stats_aggregator.histogram import CentroidHistogram
from datarobot_mlops.stats_aggregator.stats import AggregatedStats
from datarobot_mlops.stats_aggregator.stats import Stats
from datarobot_mlops.stats_aggregator.types import FeatureDescriptor


def _extract_feature_descriptor(feature: str, histogram: dict) -> FeatureDescriptor:
    feature_type = _get_type(histogram)
    types = histogram['eda']['types']
    conversion = ''
    if types['currency'] or types['date']:
        conversion = types['conversion']
    return FeatureDescriptor(feature, feature_type, conversion)


def _get_type(histogram: dict) -> str:
    types = histogram['eda']['types']
    dtype = FeatureType.CATEGORY
    if types['numeric']:
        dtype = FeatureType.NUMERIC
    if types['category']:
        dtype = FeatureType.CATEGORY
    if types['text']:
        dtype = FeatureType.TEXT_WORDS
    if types['length']:
        dtype = FeatureType.LENGTH
    if types['percentage']:
        dtype = FeatureType.PERCENTAGE
    if types['currency']:
        dtype = FeatureType.CURRENCY
    if types['date']:
        dtype = FeatureType.DATE
    return dtype


def parse_baseline_from_disk(
    drift_baseline_json_path: str,
) -> Tuple[Stats, List[FeatureDescriptor]]:
    with open(drift_baseline_json_path) as f:
        return parse_baseline_from_string(f.read())


def parse_baseline_from_string(
    drift_baseline_json: str,
) -> Tuple[Stats, List[FeatureDescriptor]]:
    baseline_dict = json.loads(drift_baseline_json)
    descriptors = []
    numeric_stats = {}
    categorical_stats = {}
    for feature, histogram in baseline_dict.items():
        descriptor = _extract_feature_descriptor(feature, histogram)
        descriptors.append(descriptor)
        if descriptor.feature_type in [
            FeatureType.CATEGORY,
            FeatureType.TEXT_WORDS,
            FeatureType.TEXT_CHARS,
        ]:
            categorical_stats[feature] = _to_categorical_aggregate(histogram)
        else:
            numeric_stats[feature] = _to_numeric_aggregate(histogram)
    result = AggregatedStats(
        numeric_stats=numeric_stats,
        categorical_stats=categorical_stats,
    )
    return result, descriptors


def _compute_missng_ratio(histogram: Union[List[int], List[float]], missing_count: int) -> float:
    sum_histogram = sum(histogram) or 0
    missing_ratio = 0.0
    if sum_histogram + missing_count:
        missing_ratio = missing_count / (sum_histogram + missing_count)
    return missing_ratio


def _get_count_vector(
    sorted_values: Iterable[str], count_dict: Dict[str, int], oov_token=None
) -> List[int]:
    index_lookup = {f: i for i, f in enumerate(sorted_values)}
    if oov_token:
        index_lookup[oov_token] = len(index_lookup)
    result = [0 for _ in range(len(index_lookup))]
    for name, count in count_dict.items():
        index = index_lookup.get(name, -1 if not oov_token else index_lookup[oov_token])
        if index < 0:
            continue
        result[index] += count
    return result


def _construct_numeric_bin_names(boundaries: List[Union[int, float]]) -> List[str]:
    result = ["(-Inf, {:.4f})".format(boundaries[0])]
    for i in range(1, len(boundaries) - 1):
        result.append("[{:.4f}, {:.4f})".format(boundaries[i - 1], boundaries[i]))
    result.append("[{:.4f}, +Inf)".format(boundaries[-2]))
    return result


def _get_small_histogram(
    buckets: List[CentroidBucket], min_value: float, max_value: float
) -> List[List[float]]:
    useful_buckets = buckets
    k = 1e-10
    b = 1e-23
    num_bins = 10
    max_value = max_value + abs((max_value * k) + b)
    bucket_width = (max_value - min_value) / num_bins
    bucket_names = []
    for i in range(num_bins + 1):
        bucket_names.append(min_value + i * bucket_width)
    if not useful_buckets:
        return [bucket_names, [0 for _ in range(12)]]

    def get_centroid(bucket: CentroidBucket) -> float:
        return bucket.centroid

    useful_buckets.sort(key=get_centroid)
    useful_values = np.array([bucket.centroid for bucket in useful_buckets])
    useful_weights = np.array([bucket.count for bucket in useful_buckets])

    np_histogram = np.histogram(
        useful_values, num_bins, (min_value, max_value), weights=useful_weights
    )
    len_values_under_min = len(useful_values[useful_values < min_value])
    len_values_over_max = len(useful_values[useful_values >= max_value])
    min_bucket_value = sum(useful_weights[:len_values_under_min]) if len_values_under_min else 0
    max_bucket_value = sum(useful_weights[-len_values_over_max:]) if len_values_over_max else 0
    histogram = [min_bucket_value] + list(np_histogram[0].astype(int)) + [max_bucket_value]
    return [bucket_names, histogram]


def _to_categorical_aggregate(stats: dict) -> CategoricalAggregate:
    return CategoricalAggregate(
        value_count=stats['aggregation']['value_count'],
        missing_count=stats['aggregation']['missing_count'],
        text_words_count=stats['aggregation']['text_words_count'],
        category_counts=stats['category_counts'],
    )


def _to_numeric_aggregate(stats: dict) -> NumericAggregate:
    buckets: List[Union[CentroidBucket, tuple, list]] = []
    for centroid, count in stats['aggregation']['value_bh_tt_histogram']:
        buckets.append(CentroidBucket(centroid, count))
    histogram = CentroidHistogram(buckets, max_length=len(buckets))
    return NumericAggregate(
        value_count=stats['aggregation']['value_count'],
        missing_count=stats['aggregation']['missing_count'],
        value_min=stats['aggregation']['value_min'],
        value_max=stats['aggregation']['value_max'],
        value_bh_tt_histogram=histogram,
        value_sum=stats['aggregation']['value_sum'],
        value_sum_of_squares=stats['aggregation']['value_sum_of_squares'],
    )


def construct_numeric_distribution(
    feature: str, feature_type: str, baseline: NumericAggregate, current: NumericAggregate
) -> FeatureDistributions:
    ref_histogram = _get_small_histogram(baseline.histogram.buckets, baseline.min, baseline.max)
    com_histogram = _get_small_histogram(current.histogram.buckets, baseline.min, baseline.max)
    assert ref_histogram[0] == com_histogram[0]
    bin_values = _construct_numeric_bin_names(ref_histogram[0])
    expected_sample_size = baseline.count
    actual_sample_size = current.count
    feature_distributions = FeatureDistributions(
        feature_name=feature,
        feature_type=feature_type,
        bin_values=bin_values,
        ref_histogram=ref_histogram[1],
        expected_sample_size=expected_sample_size,
        com_histogram=com_histogram[1],
        actual_sample_size=actual_sample_size,
    )
    return _prepare_feature_for_drift_compute(
        feature_distributions, baseline.missing_count, current.missing_count
    )


def construct_category_histogram(
    feature: str, feature_type: str, baseline: CategoricalAggregate, current: CategoricalAggregate
):
    bin_values = list(baseline.category_counts.keys())
    bin_values = sorted(bin_values)
    oov_token = None
    if feature_type == FeatureType.CATEGORY:
        oov_token = '<OOV>'
    ref_histogram = _get_count_vector(bin_values, baseline.category_counts, oov_token=oov_token)
    com_histogram = _get_count_vector(bin_values, current.category_counts, oov_token=oov_token)
    expected_sample_size = baseline.count
    actual_sample_size = current.count
    feature_distributions = FeatureDistributions(
        feature_name=feature,
        feature_type=feature_type,
        bin_values=bin_values,
        ref_histogram=ref_histogram,
        expected_sample_size=expected_sample_size,
        com_histogram=com_histogram,
        actual_sample_size=actual_sample_size,
    )
    return _prepare_feature_for_drift_compute(
        feature_distributions, baseline.missing_count, current.missing_count
    )


def _prepare_feature_for_drift_compute(
    feature_distributions: FeatureDistributions,
    ref_missing,
    com_missing,
) -> FeatureDistributions:
    feature = feature_distributions.feature_name
    feature_type = feature_distributions.feature_type
    ref_histogram = feature_distributions.ref_histogram
    com_histogram = feature_distributions.com_histogram
    expected_sample_size = feature_distributions.expected_sample_size
    actual_sample_size = feature_distributions.actual_sample_size
    bin_names = feature_distributions.bin_values
    ref_missing_ratio = _compute_missng_ratio(ref_histogram, ref_missing)
    com_missing_ratio = _compute_missng_ratio(com_histogram, com_missing)

    if ref_missing_ratio < com_missing_ratio and (
        expected_sample_size > 0 or actual_sample_size > 0
    ):
        if feature_type == FeatureType.TEXT_WORDS:
            sum_ref_histogram = sum(ref_histogram)
            sum_com_histogram = sum(com_histogram)
            ref_weight = expected_sample_size / sum_ref_histogram if sum_ref_histogram else 0
            com_weight = actual_sample_size / sum_com_histogram if sum_com_histogram else 0

            ref_histogram = [v * ref_weight for v in ref_histogram]
            com_histogram = [v * com_weight for v in com_histogram]

        ref_histogram.append(ref_missing)
        com_histogram.append(com_missing)
        bin_names.append("__missing__")
        expected_sample_size += ref_missing
        actual_sample_size += com_missing

    return FeatureDistributions(
        feature_name=feature,
        feature_type=feature_distributions.feature_type,
        bin_values=bin_names,
        ref_histogram=ref_histogram,
        expected_sample_size=expected_sample_size,
        com_histogram=com_histogram,
        actual_sample_size=actual_sample_size,
    )
