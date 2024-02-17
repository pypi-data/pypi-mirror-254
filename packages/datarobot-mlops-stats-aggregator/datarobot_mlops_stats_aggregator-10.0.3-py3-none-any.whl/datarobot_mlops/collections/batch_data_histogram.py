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
from typing import Dict
from typing import List
from typing import Optional

import pandas as pd
from datarobot_mlops.collections.data_histogram import DataHistogram
from datarobot_mlops.collections.feature_list import FeatureList
from datarobot_mlops.stats_aggregator.stats import AggregatedStats
from datarobot_mlops.stats_aggregator.stats import Stats
from datarobot_mlops.stats_aggregator.types import FeatureDescriptor


class BatchDataHistogram(DataHistogram):
    """
    Class to aggregate data by the event of accumulating at least
    some number of rows. As storing histograms is a more memory
    efficient method than storing all raw data this class can help
    to keep track of stats for a longer period of time.
    """

    def __init__(
        self,
        feature_list: List[FeatureDescriptor],
        batch_size: int = 500,
        histogram_bin_count: int = 1000,
        distinct_category_count: int = 30347,
        target_name: Optional[str] = None,
        class_mapping: Optional[Dict[str, str]] = None,
    ):
        """
        Constructor for the Batch Data Histogram.

        Parameters
        ----------
        feature_list
            description of the features that we want to aggregate stats for
        batch_size
            max number of raw data to keep in memory.
        histogram_bin_count
            bin count for histograms.
        distinct_category_count
            how many distinct categories to track.
        """
        self._feature_list = FeatureList(feature_list)
        self._batch_size = batch_size
        self._histogram_bin_count = histogram_bin_count
        self._distinct_category_count = distinct_category_count
        self._stats: Stats = AggregatedStats(feature_types=feature_list)
        self._data: List[pd.DataFrame] = []
        self._predictions: List[pd.DataFrame] = []
        self._size = 0
        self._unmerged_size = 0
        self._target_name = target_name
        self._class_mapping = class_mapping

    def push(self, input_data: pd.DataFrame, predictions: pd.DataFrame) -> None:
        self._data.append(input_data)
        self._predictions.append(predictions)
        self._size += input_data.shape[0]
        self._unmerged_size += input_data.shape[0]
        if self._unmerged_size >= self._batch_size:
            self._merge()

    def get(self) -> Stats:
        self._merge()
        return self._stats

    @property
    def size(self) -> int:
        return self._size

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    def _merge(self):
        if self._unmerged_size == 0:
            return
        features_df = pd.concat(self._data, ignore_index=True)
        predictions_df = pd.concat(self._predictions, ignore_index=True)
        feature_types = []
        feature_names = []
        for name in features_df.columns:
            if name in self._feature_list.features:
                feature_names.append(name)
                feature_types.append(self._feature_list.get_feature_descriptor(name))
        actuals = None
        if self._target_name and self._target_name in features_df.columns:
            actuals = features_df[[self._target_name]]
        self._stats = self._stats.aggregate(
            features=features_df[feature_names],
            feature_types=feature_types,
            predictions=predictions_df,
            histogram_bin_count=self._histogram_bin_count,
            distinct_category_count=self._distinct_category_count,
            actuals=actuals,
            class_mapping=self._class_mapping,
        )
        self._unmerged_size = 0
        self._data = []
        self._predictions = []
