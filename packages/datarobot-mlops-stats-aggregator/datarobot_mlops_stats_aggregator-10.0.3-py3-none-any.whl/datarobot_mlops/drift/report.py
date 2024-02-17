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
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional

from datarobot_mlops.collections.feature_list import FeatureList
from datarobot_mlops.drift.feature_distributions import FeatureDistributions
from datarobot_mlops.drift.metrics import METRICS
from datarobot_mlops.drift.metrics import MetricNames
from datarobot_mlops.drift.utils import construct_category_histogram
from datarobot_mlops.drift.utils import construct_numeric_distribution
from datarobot_mlops.stats_aggregator.aggregates import CategoricalAggregate
from datarobot_mlops.stats_aggregator.aggregates import NumericAggregate
from datarobot_mlops.stats_aggregator.stats import Stats
from datarobot_mlops.stats_aggregator.types import FeatureDescriptor

DEFAULT_METRIC_NAME = MetricNames.PSI


class DriftReport(object):
    """
    Class to hold all features drift metrics.
    """

    def __init__(self, metric_name: str):
        self.metrics: Dict[str, float] = {}
        self.metric_name: str = metric_name
        self._distributions: Dict[str, FeatureDistributions] = {}

    @classmethod
    def compute(
        cls,
        baseline_stats: Stats,
        current_stats: Stats,
        descriptors: List[FeatureDescriptor],
        metric_name: Optional[str] = None,
        custom_metric: Optional[Callable[[FeatureDistributions], float]] = None,
        features: Optional[List[str]] = None,
    ):
        """
        Construct a drift report based on baseline histogram and aggregated stats.

        Parameters
        ----------
        baseline_stats
            model baseline stats.
        current_stats
            aggregated statistics for production data.
        descriptors
            feature descriptors.
        metric_name
            metric name to compute. default to PSI_INDEX.
        custom_metric
            custom logic to compute a metric, you can override it's name
            by providing metric_name="NEW_METRIC"
        features
            you can compute a report only for certain feature, by default
            all feature from aggregated stats are used.

        Returns
        -------
        An instance of a drift report with computed metrics for features.
        """
        if not metric_name and custom_metric:
            metric_name = MetricNames.CUSTOM
        if not metric_name and not custom_metric:
            metric_name = DEFAULT_METRIC_NAME
        if not metric_name:
            raise ValueError('Please provide metric name')
        if metric_name and custom_metric and metric_name in METRICS:
            raise ValueError(
                f'{metric_name} metric name is reserved by internal metrics. '
                'Please either change metric_name or remove custom_metric'
            )
        if metric_name and not custom_metric and metric_name not in METRICS:
            raise ValueError(
                f'Unknown metric name [{metric_name}]. Supported metrics: {METRICS.keys()}. '
                f'Or provide custom_metric'
            )
        metric = custom_metric
        if not metric:
            metric = METRICS[metric_name]
        report = DriftReport(metric_name)
        feature_list = FeatureList(descriptors)
        current_numeric_stats = current_stats.numeric_stats
        baseline_numeric_stats = baseline_stats.numeric_stats
        current_categorical_stats = current_stats.categorical_stats
        baseline_categorical_stats = baseline_stats.categorical_stats
        if (
            not isinstance(current_numeric_stats, dict)
            or not isinstance(current_categorical_stats, dict)
            or not isinstance(baseline_numeric_stats, dict)
            or not isinstance(baseline_categorical_stats, dict)
        ):
            raise ValueError("Unexpected types")
        for feature, stats in current_numeric_stats.items():
            if features and feature not in features:
                continue
            baseline_num_stats = baseline_numeric_stats[feature]
            # pylint: disable=isinstance-second-argument-not-valid-type
            if not isinstance(stats, NumericAggregate) or not isinstance(
                baseline_num_stats, NumericAggregate
            ):
                raise ValueError("Unexpected types")
            feature_type = feature_list[feature]
            feature_distributions = construct_numeric_distribution(
                feature, feature_type, baseline_num_stats, stats
            )
            report.add(feature_distributions, metric(feature_distributions))
        for feature, cat_stats in current_categorical_stats.items():
            if features and feature not in features:
                continue
            baseline_cat_stats = baseline_categorical_stats[feature]
            # pylint: disable=isinstance-second-argument-not-valid-type
            if not isinstance(cat_stats, CategoricalAggregate) or not isinstance(
                baseline_cat_stats, CategoricalAggregate
            ):
                raise ValueError("Unexpected types")
            feature_type = feature_list[feature]
            feature_distributions = construct_category_histogram(
                feature, feature_type, baseline_cat_stats, cat_stats
            )
            report.add(feature_distributions, metric(feature_distributions))
        return report

    def __getitem__(self, feature: str) -> float:
        return self.metrics[feature]

    @property
    def features(self):
        """
        List of feature names in the report.
        """
        return self._distributions.keys()

    def add(self, feature_distributions: FeatureDistributions, score: float):
        self.metrics[feature_distributions.feature_name] = score
        self._distributions[feature_distributions.feature_name] = feature_distributions

    def get_distributions(self, feature_name: str) -> FeatureDistributions:
        return self._distributions[feature_name]

    def get_drift_score(self, feature_name: str) -> float:
        return self[feature_name]

    def get_drifted_features(
        self,
        drift_threshold: float = 0.3,
        number_of_rows_to_define: int = 10,
    ):
        result = []
        for f in self.metrics.keys():
            if self._is_drifted(
                f,
                drift_threshold=drift_threshold,
                number_of_rows_to_define=number_of_rows_to_define,
            ):
                result.append(f)
        return result

    def _is_drifted(
        self, feature_name, drift_threshold: float = 0.3, number_of_rows_to_define: int = 10
    ):
        drift_score = self.metrics[feature_name]
        feature_distributions = self._distributions[feature_name]
        actual_sample_size = feature_distributions.actual_sample_size
        is_drifted = drift_score is not None and drift_score >= drift_threshold
        is_representative = (
            actual_sample_size is not None and actual_sample_size >= number_of_rows_to_define
        )
        return is_drifted and is_representative

    def __repr__(self):
        return f'{self.metric_name}: {self.metrics}'
