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
from typing import Union

import pandas as pd
from datarobot_mlops.collections.data_histogram import DataHistogram
from datarobot_mlops.collections.feature_list import FeatureList
from datarobot_mlops.stats_aggregator.stats import AggregatedStats
from datarobot_mlops.stats_aggregator.stats import Stats
from datarobot_mlops.stats_aggregator.types import FeatureDescriptor
from pandas import Timedelta


class LruDataHistogram(DataHistogram):
    """
    Class to keep latest data based on row count or a timedelta.
    Timestamp can be picked up from a column if provided, otherwise
    a new column will be created and set to a pandas.Timestamp.utcnow()
    for each pushed chunk of data.
    """

    def __init__(
        self,
        feature_list: List[FeatureDescriptor],
        latest: Union[Timedelta, int] = 10000,
        timestamp_column: Optional[str] = None,
        histogram_bin_count: int = 1000,
        distinct_category_count: int = 30347,
        target_name: Optional[str] = None,
        class_mapping: Optional[Dict[str, str]] = None,
    ):
        """
        Constructor.

        Parameters
        ----------
        feature_list
            description of the features that we want to aggregate stats for
        latest
            Number of latest rows to compute stats for, timedelta to
            leave only latest data based on a timestamp in the range
            [Max Timestamp - TIMEDELTA, Max Timestamp]
        timestamp_column
            column with timestamps for rows, if not provided each chunk of
            data will be assigned a value of pandas.Timestamp.utcnow().
        histogram_bin_count
            bin count for histograms.
        distinct_category_count
            how many distinct categories to track.
        """
        self._size = 0
        self._feature_list = FeatureList(feature_list)
        self._histogram_bin_count = histogram_bin_count
        self._distinct_category_count = distinct_category_count
        self._latest = latest
        self._target_name = target_name
        self._is_time_based = isinstance(latest, Timedelta)
        self._data: Optional[pd.DataFrame] = None
        self._predictions: Optional[pd.DataFrame] = None
        self._timestamp_column = timestamp_column if timestamp_column else 'DR_LRU_TIMESTAMP'
        self._class_mapping = class_mapping

    def push(self, input_data: pd.DataFrame, predictions: pd.DataFrame) -> None:
        if self._is_time_based:
            self._push_time_based(input_data, predictions)
        else:
            self._push_row_based(input_data, predictions)

    def get(self) -> Stats:
        result = AggregatedStats()
        if self._predictions is None or self._data is None:
            return result
        predictions = self._predictions
        if self._is_time_based:
            predictions = self._predictions.drop([self._timestamp_column], axis=1)
        feature_types = []
        feature_names = []
        for name in self._data.columns:
            if name in self._feature_list.features:
                feature_names.append(name)
                feature_types.append(self._feature_list.get_feature_descriptor(name))
        actuals = None
        if self._target_name and self._target_name in self._data.columns:
            actuals = self._data[[self._target_name]]
        return result.aggregate(
            features=self._data[feature_names],
            feature_types=feature_types,
            predictions=predictions,
            histogram_bin_count=self._histogram_bin_count,
            distinct_category_count=self._distinct_category_count,
            actuals=actuals,
            class_mapping=self._class_mapping,
        )

    @property
    def size(self) -> int:
        return self._size

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    def _push_time_based(self, input_data: pd.DataFrame, predictions: pd.DataFrame):
        input_data = input_data.copy()
        predictions = predictions.copy()
        if self._timestamp_column == 'DR_LRU_TIMESTAMP':
            timestamp = pd.Timestamp.utcnow()
            input_data[self._timestamp_column] = timestamp
            predictions[self._timestamp_column] = timestamp
        if self._data is not None:
            input_data = pd.concat([self._data, input_data], ignore_index=True)
            predictions = pd.concat([self._predictions, predictions], ignore_index=True)
        latest_available = input_data[self._timestamp_column].max() - self._latest
        self._data = input_data[input_data[self._timestamp_column] >= latest_available]
        self._predictions = predictions[predictions[self._timestamp_column] >= latest_available]
        self._size = self._data.shape[0]

    def _push_row_based(self, input_data: pd.DataFrame, predictions: pd.DataFrame):
        if self._data is not None:
            self._data = pd.concat([self._data, input_data], ignore_index=True)
            self._predictions = pd.concat([self._predictions, predictions], ignore_index=True)
        else:
            self._data = input_data
            self._predictions = predictions
        self._size = self._data.shape[0] if self._data is not None else 0
        if self._size > self._latest:
            self._data = self._data.tail(self._latest) if self._data is not None else None
            self._predictions = (
                self._predictions.tail(self._latest) if self._predictions is not None else None
            )
            self._size = self._latest
