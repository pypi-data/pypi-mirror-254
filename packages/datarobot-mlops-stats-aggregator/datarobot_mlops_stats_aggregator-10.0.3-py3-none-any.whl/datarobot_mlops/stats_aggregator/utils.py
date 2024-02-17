#  --------------------------------------------------------------------------------
#  Copyright (c) 2021 DataRobot, Inc. and its affiliates. All rights reserved.
#  Last updated 2022.
#
#  DataRobot, Inc. Confidential.
#  This is proprietary source code of DataRobot, Inc. and its affiliates.
#
#  This file and its contents are subject to DataRobot Tool and Utility Agreement.
#  For details, see
#  https://www.datarobot.com/wp-content/uploads/2021/07/DataRobot-Tool-and-Utility-Agreement.pdf.
#
#  --------------------------------------------------------------------------------
import random
import re
import string
from collections import Counter  # pylint: disable = no-name-in-module
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import cast

import numpy as np
import pandas as pd
import six
from datarobot_mlops.stats_aggregator.aggregates import AccuracyAggregate
from datarobot_mlops.stats_aggregator.aggregates import CategoricalAggregate
from datarobot_mlops.stats_aggregator.aggregates import ClassificationAccuracyAggregate
from datarobot_mlops.stats_aggregator.aggregates import NumericAggregate
from datarobot_mlops.stats_aggregator.aggregates import RegressionAccuracyAggregate
from datarobot_mlops.stats_aggregator.constants import DEFAULT_DISTINCT_CATEGORY_COUNT
from datarobot_mlops.stats_aggregator.constants import DEFAULT_HISTOGRAM_BIN_COUNT
from datarobot_mlops.stats_aggregator.type_conversion import feature_type_converters
from datarobot_mlops.stats_aggregator.types import FeatureType
from datarobot_mlops.stats_aggregator.types import FeatureTypes

from .types import CentroidHistogram


def get_random_string(length):
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(letters, k=length))


def validate_counts(**kwargs):
    """Validate that each specified argument is either a positive int or None"""
    for name, value in kwargs.items():
        if value is not None and value <= 0:
            raise ValueError("If specified, {name} must be a positive integer".format(name=name))


def validate_arguments(
    features: Optional[pd.DataFrame] = None,
    feature_types: Optional[FeatureTypes] = None,
    predictions: Optional[pd.DataFrame] = None,
    segment_attributes: Optional[List[str]] = None,
    histogram_bin_count: Optional[int] = None,
    distinct_category_count: Optional[int] = None,
    segment_value_per_attribute_count: Optional[int] = None,
    actuals: Optional[pd.DataFrame] = None,
    class_mapping: Optional[Dict[str, str]] = None,
):
    if (
        features is not None
        and predictions is not None
        and features.shape[0] != predictions.shape[0]
    ):
        raise ValueError("Different numbers of rows for features and predictions specified")

    if predictions is not None and predictions.isna().values.any():
        raise ValueError("Missing values are not permitted in predictions")

    if segment_attributes is not None:
        if features is None:
            raise ValueError("Features must be specified when segment attributes are specified")
        elif set(segment_attributes).difference(features.columns):
            raise ValueError("All segment attributes must be specified in features")

    if actuals is not None and len(actuals.columns) != 1:
        raise ValueError("Actuals should have exactly one column")

    if predictions is not None and len(predictions.columns) > 1 and actuals is not None:
        if not class_mapping:
            raise ValueError("To compute accuracy you need to provide class_mapping.")
        if len(predictions.columns) != len(class_mapping):
            raise ValueError(
                "Predictions has {} columns, while class_mapping has {} entries.".format(
                    len(predictions.columns), len(class_mapping)
                )
            )
        for pred_col in predictions.columns:
            if pred_col not in class_mapping:
                raise ValueError(
                    "Missing class mapping for a prediction column {}".format(pred_col)
                )
        mapped_classes = set(class_mapping.values())
        actual_classes = set(actuals[actuals.columns[0]].unique().astype(str))
        diff_classes = sorted(actual_classes - mapped_classes)
        if diff_classes:
            raise ValueError(
                "Unknown classes {}, configured classes are {}".format(
                    diff_classes, sorted(mapped_classes)
                )
            )

    validate_counts(
        histogram_bin_count=histogram_bin_count,
        distinct_category_count=distinct_category_count,
        segment_value_per_attribute_count=segment_value_per_attribute_count,
    )

    if features is not None and feature_types is not None:
        # validate features_types present in features input
        features_not_present = []
        for feature_desc in feature_types:
            if feature_desc.name not in features:
                features_not_present.append(feature_desc.name)
        if features_not_present:
            raise ValueError(
                "Feature types '{}' not present in provided dataset".format(
                    ", ".join(features_not_present)
                )
            )


true_false_mapper = {"true": 1.0, "false": 0.0}


def floatify(value: Any) -> float:
    """Convert a boolean or string (or maybe integer, etc.) value into a Numpy float"""
    try:
        # EDA treats case-insensitive booleans as numerics, so convert
        # any true/false values (case-insensitive) to 1/0 values.
        return true_false_mapper[value.lower()]
    except (KeyError, AttributeError):
        pass

    try:
        # Otherwise, just try to convert the value to a float
        return float(value)
    except ValueError:
        return float('nan')


def convert_series_to_numeric(series: pd.Series) -> pd.Series:
    """Convert a Series of mixed/non-float values into a series of type Numpy float"""
    # https://stackoverflow.com/questions/19900202/how-to-determine-whether-a-column-variable-is-numeric-or-not-in-pandas-numpy/46423535
    if not series.dtype.kind in "biufc":
        series = series.map(floatify)
    if not series.dtype == "float64":
        series = series.astype(np.float64)
    return series


def compute_counts(series: pd.Series) -> Tuple[int, int]:
    """Count missing (i.e. NA/null) and non-missing values in a series"""
    value_count = cast(int, series.count())
    missing_count = len(series) - value_count
    return value_count, missing_count


def aggregate_numeric_stats(series: pd.Series, histogram_bin_count: Optional[int]):
    """Aggregate a numeric feature series into statistics"""
    value_count, missing_count = compute_counts(series)
    series = series.dropna()
    series = convert_series_to_numeric(series)
    result = NumericAggregate(
        value_count=value_count,
        missing_count=missing_count,
        value_min=series.min(),
        value_max=series.max(),
        value_sum=series.sum(),
        value_sum_of_squares=series.pow(2).sum(),
        value_bh_tt_histogram=CentroidHistogram.from_values(
            series, max_length=histogram_bin_count or DEFAULT_HISTOGRAM_BIN_COUNT
        ),
    )
    return result


def aggregate_category_stats(
    series: pd.Series, distinct_category_count: Optional[int] = None
) -> CategoricalAggregate:
    """Aggregate a categorical feature into statistics"""
    value_count, missing_count = compute_counts(series)

    series = series[series.notnull()]
    series = series.astype(six.text_type)
    category_counts = (
        series.value_counts(ascending=False)
        .iloc[: distinct_category_count or DEFAULT_DISTINCT_CATEGORY_COUNT]
        .to_dict()
    )
    # Unlike the original function in feature_aggregations, this does not call safe_unicode.
    # I believe it's unnecessary in the library; it should be called downstream in modmon worker.

    result = CategoricalAggregate(
        value_count=value_count,
        missing_count=missing_count,
        category_counts=category_counts,
    )
    return result


# Compiled regular expressions for text tokenization
digit_pattern = re.compile(r"\d", flags=re.UNICODE)
word_pattern = re.compile(r"\b\w+\b", flags=re.UNICODE)
char_pattern = re.compile(r"\w", flags=re.UNICODE)


def aggregate_text_stats(
    series: pd.Series, feature_type: str, distinct_category_count: Optional[int]
) -> CategoricalAggregate:
    """Aggregate a text (words or characters) feature into statistics"""
    value_count, missing_count = compute_counts(series)

    # Remove numbers from the text (Port behavior of remove_numbers_from_text)
    series = (
        series.fillna("")
        .astype(six.text_type)
        .str.replace(digit_pattern, "", regex=True)
        .str.lower()
    )

    # Split each document into words or characters, depending on feature type
    # Original implementation is keyed off of language: If logographic, tokenize by characters.
    # Rather than passing in an extra map of languages, I chose to just split the feature type.
    pattern = word_pattern if feature_type == FeatureType.TEXT_WORDS else char_pattern
    series = series.str.findall(pattern)

    # Count unique words in each document (similar to CountVectorizer with binary=True)
    unigram_counter = Counter()  # type: ignore
    for unigrams in series:
        unigram_counter.update(set(unigrams))

    # Limit number of distinct words to distinct_category_count
    total_word_count = sum(unigram_counter.values())
    category_counts = dict(
        unigram_counter.most_common(distinct_category_count or DEFAULT_DISTINCT_CATEGORY_COUNT)
    )

    result = CategoricalAggregate(
        value_count=value_count,
        missing_count=missing_count,
        text_words_count=total_word_count,
        category_counts=category_counts,
    )
    return result


def aggregate_feature_stats(
    features: pd.DataFrame,
    feature_types: FeatureTypes,
    histogram_bin_count: Optional[int] = None,
    distinct_category_count: Optional[int] = None,
):
    """Aggregate each feature with a specified feature type

    Columns in the `features` DataFrame that don't have matching keys in `feature_types` will
    not be aggregated. These features may be included for segment analysis, for instance.
    """
    numeric_stats, category_stats = {}, {}
    for feature_descriptor in feature_types:
        name = feature_descriptor.name
        feature_type = feature_descriptor.feature_type
        feature = features.loc[:, name]
        if feature_type == FeatureType.NUMERIC or feature_type in feature_type_converters:
            numeric_stats[name] = aggregate_numeric_stats(feature, histogram_bin_count)
        elif feature_type == FeatureType.CATEGORY:
            category_stats[name] = aggregate_category_stats(feature, distinct_category_count)
        elif feature_type in (FeatureType.TEXT_WORDS, FeatureType.TEXT_CHARS):
            category_stats[name] = aggregate_text_stats(
                feature, feature_type, distinct_category_count
            )
    return numeric_stats, category_stats


def aggregate_accuracy(predictions, actuals, class_mapping=None):
    if len(predictions.columns) > 1:
        return _process_classification_accuracy(predictions, actuals, class_mapping)
    return _process_regresion_accuracy(predictions, actuals)


def _process_regresion_accuracy(
    predictions: pd.DataFrame,
    actuals: pd.DataFrame,
) -> List[AccuracyAggregate]:
    pred_column_name = predictions.columns[0]
    actual_column = actuals.columns[0]
    predictions = predictions[pred_column_name].astype(np.float64)
    actuals = actuals[actual_column].astype(np.float64)
    errors = predictions - actuals
    metric_df = pd.DataFrame({'actuals': actuals, 'predictions': predictions})
    record = RegressionAccuracyAggregate(
        actual_count=actuals.count(),
        actual_min=actuals.min(),
        actual_max=actuals.max(),
        actual_sum=actuals.sum(),
        actual_sum_of_squares=(actuals**2).sum(),
        actual_bh_tt_histogram=CentroidHistogram.from_values(actuals),
        error_count=errors.count(),
        error_min=errors.min(),
        error_max=errors.max(),
        error_sum=errors.abs().sum(),
        error_sum_of_squares=(errors**2).sum(),
        error_bh_tt_histogram=CentroidHistogram.from_values(errors),
        error_percent_sum=compute_metric_sum(metric_df, _mape),
        error_sum_of_squared_log1p=compute_metric_sum(metric_df, lambda a, p: _rmsle(a, p) ** 2),
        gamma_deviance_sum=compute_metric_sum(metric_df, _gamma_deviance),
        poisson_deviance_sum=compute_metric_sum(metric_df, _poisson_deviance),
        tweedie_deviance_sum=compute_metric_sum(metric_df, _tweedie_deviance),
    )
    return [record]


def _process_classification_accuracy(
    data: pd.DataFrame,
    actuals_unmapped: pd.DataFrame,
    class_mapping: Optional[Dict[str, str]],
) -> List[AccuracyAggregate]:
    result = []
    if class_mapping is None:
        raise ValueError("class_mapping is required.")
    actuals_unmapped = actuals_unmapped[actuals_unmapped.columns[0]].astype(str).values
    for pred_col in data.columns:
        class_name = class_mapping[pred_col]
        predictions = data[pred_col].values
        actuals = np.zeros(predictions.shape, dtype=np.float64)
        actuals[actuals_unmapped == class_name] = 1.0
        errors = predictions - actuals
        pos_value_min = None
        pos_value_max = None
        pos_value_bh_tt_histogram = CentroidHistogram([])
        pos_value_count = 0
        pos_predictions = predictions[actuals == 1]
        if pos_predictions.shape[0] > 0:
            pos_value_count = pos_predictions.shape[0]
            pos_value_bh_tt_histogram = CentroidHistogram.from_values(pos_predictions)
            pos_value_min = pos_predictions.min()
            pos_value_max = pos_predictions.max()
        record: AccuracyAggregate = ClassificationAccuracyAggregate(
            actual_count=actuals.shape[0],
            actual_min=actuals.min(),
            actual_max=actuals.max(),
            actual_sum=actuals.sum(),
            actual_sum_of_squares=np.square(actuals).sum(),
            error_count=errors.shape[0],
            error_bh_tt_histogram=CentroidHistogram.from_values(errors),
            error_min=errors.min(),
            error_max=errors.max(),
            error_sum=np.abs(errors).sum(),
            error_sum_of_squares=np.square(actuals).sum(),
            error_sum_of_logs=safe_log_vectorized(1 - np.abs(errors)).sum(),
            decision_with_actual_count=0,
            correct_decision_count=0,
            pos_value_count=pos_value_count,
            pos_value_bh_tt_histogram=pos_value_bh_tt_histogram,
            pos_value_min=pos_value_min,
            pos_value_max=pos_value_max,
        )
        result.append(record)
    return result


def compute_metric_sum(df, metric_func):
    if df.empty:
        return 0.0
    else:
        return metric_func(df['actuals'], df['predictions']) * len(df)


def _poisson_deviance(act, pred, weight=None):
    """
    Poisson Deviance = 2*(act*log(act/pred)-(act-pred))
    ONLY WORKS FOR POSITIVE RESPONSES
    """
    if len(pred.shape) > 1:
        pred = pred.ravel()
    pred = np.maximum(pred, 1e-8)  # ensure predictions are strictly positive
    act = np.maximum(act, 0)  # ensure actuals are non-negative
    d = np.zeros(len(act))
    d[act == 0] = pred[act == 0]
    cond = act > 0
    d[cond] = act[cond] * np.log(act[cond] / pred[cond]) - (act[cond] - pred[cond])
    d = d * 2
    if weight is not None:
        if weight.sum() == 0:
            return 0
        d = d * weight / weight.mean()
    return d.mean()


def _tweedie_deviance(act, pred, weight=None, p=1.5):
    """
    ONLY WORKS FOR POSITIVE RESPONSES
    """
    if p < 1 or p > 2:
        raise ValueError('p equal to %s is not supported' % p)

    if len(pred.shape) > 1:
        pred = pred.ravel()

    if p == 1:
        return _poisson_deviance(act, pred, weight)
    if p == 2:
        return _gamma_deviance(act, pred, weight)
    if p == 0:
        d = (act - pred) ^ 2.0
        return d.mean()
    pred = np.maximum(pred, 1e-8)  # ensure predictions are strictly positive
    act = np.maximum(act, 0)  # ensure actuals are not negative
    d = (
        (act ** (2.0 - p)) / ((1 - p) * (2 - p))
        - (act * (pred ** (1 - p))) / (1 - p)
        + (pred ** (2 - p)) / (2 - p)
    )
    d = 2 * d
    if weight is not None:
        if weight.sum() == 0:
            return 0
        d = d * weight / weight.mean()
    deviance = d.mean()
    return deviance


def _gamma_deviance(act, pred, weight=None):
    """
    Gamma Deviance = 2*(-log(act/pred)+(act-pred)/pred)
    ONLY WORKS FOR POSITIVE RESPONSES
    https://datarobot.atlassian.net/browse/TRUST-379
    """
    if len(pred.shape) > 1:
        pred = pred.ravel()
    pred = np.maximum(pred, 0.01)  # ensure predictions are stricly positive
    act = np.maximum(act, 0.01)  # ensure actuals are strictly positive
    d = 2 * (-np.log(act / pred) + (act - pred) / pred)
    if weight is not None:
        if weight.sum() == 0:
            return 0
        d = d * weight / weight.mean()
    return d.mean()


def _mape(act, pred, weight=None):
    if len(pred.shape) > 1:
        pred = pred.ravel()
    # These lines to prevent errors when running on zeros.
    # Such a case should not make it to the front, but as written
    # we currently run all regression metrics on all regression problems,
    # but just hide some of them from the frontend
    actual = scale_near_zero_values(act)
    predic = scale_near_zero_values(pred)

    rel_error = np.abs(actual - predic) / np.abs(actual)
    if weight is not None:
        total_weight = weight.sum()
        rel_error = rel_error * weight
        divisor = total_weight
    else:
        divisor = len(act)
    return rel_error.sum() * 100.0 / divisor


def _rmsle(act, pred, weight=None):
    """
    RMSLE = Root Mean Squared Logarithmic Error
        = sqrt( mean( ( log(pred+1)-log(act+1) )**2))
    ONLY WORKS FOR POSITIVE RESPONSES
    """
    if len(pred.shape) > 1:
        pred = pred.ravel()
    pred = np.maximum(pred, 0)  # ensure predictions are non-negative
    act = np.maximum(act, 0)  # ensure actuals are non-negative
    lp = np.log1p(pred)
    la = np.log1p(act)
    d = lp - la

    sd = np.power(d, 2)
    if weight is not None:
        if weight.sum() == 0:
            return 0
        sd = sd * weight / weight.mean()
    msle = sd.mean()
    return np.sqrt(msle)


def scale_near_zero_values(x, threshold=0.0001):
    """
    Adjust near-zero values in the given array to have larger absolute values.
    If x is positive and less than `threshold`, it will become `threshold`.
    If x is negative and greater than `-threshold`, it will become `-threshold`.
    If x is exactly zero, it will become `threshold`.

    Parameters
    ----------
    x : np.array
        The array to adjust

    threshold : float
        Threshold (absolute distance from zero) to adjust small values to.

    Returns
    -------
    np.array
        Array with adjusted values.
    """

    # Positive values should be >= +threshold, negative values should be <= -threshold.
    result = np.maximum(np.abs(x), threshold) * np.sign(x)

    # Sign for 0 is 0 so set zero values to +threshold.
    return np.where(result == 0, threshold, result)


def safe_log_vectorized(arr, eps=1e-15):
    # safe log an np.array with shape (n,) (a vector)
    # replace <= 0 with eps and >= 1 with 1 - eps before taking the log
    return np.log(np.fmax(np.fmin(arr, 1 - eps), eps))


def accuracy_aggregate_from_dict(**kwargs):
    clazz = RegressionAccuracyAggregate
    if 'actual_bh_tt_histogram' not in kwargs:
        clazz = ClassificationAccuracyAggregate
    return clazz.from_dict(**kwargs)


def get_default_class_mapping(predictions: Optional[pd.DataFrame]) -> Optional[Dict[str, str]]:
    """
    Get the default class mapping for provided predictions columns.
    If all columns have a format 'target_{class_name}_PREDICTION' the
    mapping will be initialized as 'target_{class_name}_PREDICTION' -> '{class_name}'.

    Parameters
    ----------
    predictions
        Predictions DataFrame

    Returns
    -------
    None if columns have a different format or number of prediction columns less than 2.
    """
    if predictions is None:
        return None
    pred_columns = predictions.columns
    if len(pred_columns) < 2:  # Regression no mapping
        return None
    result = {}
    # Scoring Code classification models return columns in format 'target_{class_name}_PREDICTION'
    for column in pred_columns:
        if (
            not isinstance(column, str)
            or not column.startswith('target_')
            or not column.endswith('_PREDICTION')
        ):
            return None
        result[column] = column.replace('target_', '').replace('_PREDICTION', '')
    return result
