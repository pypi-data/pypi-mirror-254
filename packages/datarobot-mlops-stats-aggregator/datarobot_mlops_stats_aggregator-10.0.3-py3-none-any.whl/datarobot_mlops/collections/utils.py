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

from datarobot_mlops.collections.batch_data_histogram import BatchDataHistogram
from datarobot_mlops.collections.data_histogram import DataHistogram
from datarobot_mlops.collections.lru_data_histogram import LruDataHistogram
from datarobot_mlops.stats_aggregator.types import FeatureDescriptor
from pandas import Timedelta


def get_data_histogram(
    feature_list: List[FeatureDescriptor],
    target_name: str,
    histogram_bin_count: int = 1000,
    distinct_category_count: int = 30347,
    batch_size: int = 500,
    latest: Optional[Union[Timedelta, int]] = None,
    class_mapping: Optional[Dict[str, str]] = None,
) -> DataHistogram:
    features_to_track = [f for f in feature_list if f.name != target_name]
    if not latest:
        return BatchDataHistogram(
            features_to_track,
            batch_size,
            histogram_bin_count=histogram_bin_count,
            distinct_category_count=distinct_category_count,
            target_name=target_name,
            class_mapping=class_mapping,
        )
    return LruDataHistogram(
        features_to_track,
        latest,
        histogram_bin_count=histogram_bin_count,
        distinct_category_count=distinct_category_count,
        target_name=target_name,
        class_mapping=class_mapping,
    )
