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

from __future__ import absolute_import

from typing import Dict
from typing import List
from typing import Optional

import pandas as pd

from .stats import AggregatedStats
from .stats import Stats
from .types import FeatureTypes


def aggregate_stats(
    features: Optional[pd.DataFrame] = None,
    feature_types: Optional[FeatureTypes] = None,
    predictions: Optional[pd.DataFrame] = None,
    segment_attributes: Optional[List[str]] = None,
    histogram_bin_count: Optional[int] = None,
    distinct_category_count: Optional[int] = None,
    segment_value_per_attribute_count: Optional[int] = None,
    actuals: Optional[pd.DataFrame] = None,
    class_mapping: Optional[Dict[str, str]] = None,
    name: Optional[str] = None,
) -> Stats:
    """
    Aggregates features and predictions into statistics for model monitoring.

    Parameters
    ----------
    features
        DataFrame of feature values (and segment values if those are not aggregated as features).
        Columns in this DataFrame that are not included in `feature_types` will not be aggregated.
    feature_types
        List of feature names, types and format. following this format
        [
          {
            "name": "f1"
            "featureType": "numeric"
          },
          {
            "name": "f2_date"
            "featureType": "date"
            "format": "MM-dd-yy"
          }
          ....
        ]
    predictions
        DataFrame of prediction values.
        - For regression models, the DataFrame will contain a single column for the prediction values.
        - For classification models, each column contains prediction probabilities for a particular class.
    segment_attributes
        Feature names that should be used to slice statistics by those feature values.
    histogram_bin_count
        Count of histogram bins to populate for each numeric feature. If unspecified, a configured default is used.
    distinct_category_count
        Count of distinct categories to count for each categorical feature. If unspecified, a configured default is used.
    segment_value_per_attribute_count
        Count of segment values tracked per segment attribute. If unspecified, a configured default is used.
    actuals
        Actual values for the predicted value to compute accuracy errors.
    class_mapping
        If you are providing actuals and you have a classification problem you need to provide a mapping of
        predictions columns for each of the class to the particular class name that actuals consist of.
        {'target_0_PREDICTION': '0', 'target_1_PREDICTION: '1'}
    name
        Name of the result statistics entity.

    Returns
    -------
    Statistics about features and predictions, both overall and segmented by the specified attributes. For classification
    models, prediction statistics are ordered in the same order as columns in the input `predictions` DataFrame.
    """
    stats = AggregatedStats(name=name, feature_types=feature_types)
    return stats.aggregate(
        features=features,
        feature_types=feature_types,
        predictions=predictions,
        segment_attributes=segment_attributes,
        segment_value_per_attribute_count=segment_value_per_attribute_count,
        actuals=actuals,
        distinct_category_count=distinct_category_count,
        histogram_bin_count=histogram_bin_count,
        class_mapping=class_mapping,
    )
