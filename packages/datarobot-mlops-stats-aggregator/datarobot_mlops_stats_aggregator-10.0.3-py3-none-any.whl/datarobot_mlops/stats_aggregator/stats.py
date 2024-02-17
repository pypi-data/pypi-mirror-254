#  --------------------------------------------------------------------------------
#  Copyright (c) 2024 DataRobot, Inc. and its affiliates. All rights reserved.
#  Last updated 2024.
#
#  DataRobot, Inc. Confidential.
#  This is proprietary source code of DataRobot, Inc. and its affiliates.
#
#  This file and its contents are subject to DataRobot Tool and Utility Agreement.
#  For details, see
#  https://www.datarobot.com/wp-content/uploads/2021/07/DataRobot-Tool-and-Utility-Agreement.pdf.
#
#  --------------------------------------------------------------------------------
from abc import ABC
from abc import abstractmethod
from collections import Counter  # pylint: disable = no-name-in-module
from collections import defaultdict
from typing import Any
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple

import pandas as pd

from .aggregates import AccuracyAggregate
from .aggregates import CategoricalAggregate
from .aggregates import NumericAggregate
from .constants import DEFAULT_DISTINCT_SEGMENT_VALUE_COUNT
from .type_conversion import convert_features_for_aggregation
from .types import FeatureDescriptor
from .types import FeatureTypes
from .utils import accuracy_aggregate_from_dict
from .utils import aggregate_accuracy
from .utils import aggregate_category_stats
from .utils import aggregate_feature_stats
from .utils import aggregate_numeric_stats
from .utils import get_default_class_mapping
from .utils import get_random_string
from .utils import validate_arguments


class Stats(ABC):
    @property
    @abstractmethod
    def numeric_stats(self) -> Dict[str, NumericAggregate]:
        """
        Dictionary of feature names to their numeric aggregates.
        """

    @property
    @abstractmethod
    def categorical_stats(self) -> Dict[str, CategoricalAggregate]:
        """
        Dictionary of feature names to their categorical aggregates.
        """

    @property
    @abstractmethod
    def prediction_stats(self) -> List[NumericAggregate]:
        """
        List of numeric aggregates for predictions.
        Regression models have a list of 1 item, for classification
        models there will be one item per class.
        """

    @property
    @abstractmethod
    def accuracy_stats(self) -> List[AccuracyAggregate]:
        """
        List of numeric aggregates for accuracy metrics.
        Regression models have a list of 1 item, for classification
        models there will be one item per class.
        """

    @property
    @abstractmethod
    def segment_stats(self) -> Dict[str, Dict[str, 'Stats']]:
        """
        Statistics for different segments.
        First level key is the name of the attribute by which data was grouped,
        and second level key is actual value of this attribute.
        """

    @property
    @abstractmethod
    def class_names(self) -> Optional[List[str]]:
        """
        None for Regression, and a list of class names for classification.
        """

    @property
    @abstractmethod
    def feature_types(self) -> FeatureTypes:
        """
        List of feature type descriptors
        """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        To simplify handling statistics you might want to use some
        name here, if not provided a random name will be generated.
        """

    @abstractmethod
    def aggregate(
        self,
        features: Optional[pd.DataFrame] = None,
        feature_types: Optional[FeatureTypes] = None,
        predictions: Optional[pd.DataFrame] = None,
        segment_attributes: Optional[List[str]] = None,
        histogram_bin_count: Optional[int] = None,
        distinct_category_count: Optional[int] = None,
        segment_value_per_attribute_count: Optional[int] = None,
        actuals: Optional[pd.DataFrame] = None,
        class_mapping: Optional[Dict[str, str]] = None,
    ) -> 'Stats':
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

        Returns
        -------
        Statistics about features and predictions, both overall and segmented by the specified attributes. For classification
        models, prediction statistics are ordered in the same order as columns in the input `predictions` DataFrame.
        """

    @abstractmethod
    def merge(self, other: 'Stats', name: Optional[str] = None) -> 'Stats':
        """
        Merges this statistics with another one.

        Parameters
        ----------
        other
            Multiple outputs of `aggregate_stats` to merge into a single output.
        name
            Merged statistics name.

        Returns
        -------
        Single instance of aggregated statistics.
        """

    @abstractmethod
    def copy(self, name: Optional[str] = None) -> 'Stats':
        """
        Shallow copy of this structure
        Parameters
        ----------
        name
            Name of the copy.

        Returns
        -------
        New instance of stats with a new name.
        """

    @abstractmethod
    def to_dict(self):
        """
        Converts statistics to a dict.
        """


class AggregatedStats(Stats):
    def __init__(
        self,
        feature_types: Optional[FeatureTypes] = None,
        numeric_stats: Optional[Dict[str, NumericAggregate]] = None,
        categorical_stats: Optional[Dict[str, CategoricalAggregate]] = None,
        prediction_stats: Optional[List[NumericAggregate]] = None,
        accuracy_stats: Optional[List[AccuracyAggregate]] = None,
        segment_stats: Optional[Dict[str, Dict[str, Stats]]] = None,
        class_names: Optional[List[str]] = None,
        name: Optional[str] = None,
    ):
        super().__init__()
        self._feature_types = feature_types or []
        self._numeric_stats = numeric_stats or {}
        self._categorical_stats = categorical_stats or {}
        self._prediction_stats = prediction_stats or []
        self._accuracy_stats = accuracy_stats or []
        self._segment_stats = segment_stats or {}
        self._class_names = class_names
        self._name = name or get_random_string(6)

    def __getitem__(self, key: str):
        """
        Backward compatible method, as this structure used to be a dict.

        Returns
        -------
        Return attribute of this structure by name.
        """
        return getattr(self, key)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Backward compatible method, as this structure used to be a dict.

        Returns
        -------
        Return attribute of this structure by name if no attribute found returns
        default value.
        """
        if not hasattr(self, key):
            return default
        return getattr(self, key)

    def items(self) -> Iterator[Tuple[str, Any]]:
        """
        Backward compatible method, as this structure used to be a dict.

        Returns
        -------
        Return iterator over old attributes of this structure.
        """
        yield 'numeric_stats', self.numeric_stats
        yield 'categorical_stats', self.categorical_stats
        yield 'prediction_stats', self.prediction_stats
        yield 'segment_stats', self.segment_stats

    def __repr__(self):
        segments = set()
        for attr_name in self._segment_stats.keys():
            for attr_value in self._segment_stats[attr_name].keys():
                if len(segments) == 5:
                    break
                segments.add(f'{attr_name}_{attr_value}')
            if len(segments) == 5:
                segments.add('...')
                break
        return (
            f'name={self._name} | '
            f'num_count={len(self._numeric_stats)} | '
            f'cat_count={len(self._categorical_stats)} | '
            f'pred_count={len(self._prediction_stats)} | '
            f'accuracy_count={len(self._accuracy_stats)} | '
            f'segments=[{",".join(segments)}]'
        )

    @property
    def numeric_stats(self) -> Dict[str, NumericAggregate]:
        return self._numeric_stats

    @property
    def categorical_stats(self) -> Dict[str, CategoricalAggregate]:
        return self._categorical_stats

    @property
    def prediction_stats(self) -> List[NumericAggregate]:
        return self._prediction_stats

    @property
    def accuracy_stats(self) -> List[AccuracyAggregate]:
        return self._accuracy_stats

    @property
    def segment_stats(self) -> Dict[str, Dict[str, Stats]]:
        return self._segment_stats

    @property
    def class_names(self) -> Optional[List[str]]:
        return self._class_names

    @property
    def feature_types(self) -> FeatureTypes:
        return self._feature_types

    @property
    def name(self) -> str:
        return self._name

    def aggregate(
        self,
        features: Optional[pd.DataFrame] = None,
        feature_types: Optional[FeatureTypes] = None,
        predictions: Optional[pd.DataFrame] = None,
        segment_attributes: Optional[List[str]] = None,
        histogram_bin_count: Optional[int] = None,
        distinct_category_count: Optional[int] = None,
        segment_value_per_attribute_count: Optional[int] = None,
        actuals: Optional[pd.DataFrame] = None,
        class_mapping: Optional[Dict[str, str]] = None,
    ) -> Stats:
        if not class_mapping:
            class_mapping = get_default_class_mapping(predictions)
        validate_arguments(
            features=features,
            feature_types=feature_types,
            predictions=predictions,
            segment_attributes=segment_attributes,
            histogram_bin_count=histogram_bin_count,
            distinct_category_count=distinct_category_count,
            segment_value_per_attribute_count=segment_value_per_attribute_count,
            actuals=actuals,
            class_mapping=class_mapping,
        )
        numeric_stats = None
        categorical_stats = None
        prediction_stats = None
        accuracy_stats = None
        segment_stats: Dict[str, Dict[str, Stats]] = defaultdict(dict)
        class_names = None
        if features is not None and feature_types is not None:
            features = convert_features_for_aggregation(features, feature_types)
            numeric_stats, categorical_stats = aggregate_feature_stats(
                features, feature_types, histogram_bin_count, distinct_category_count
            )
            if self.numeric_stats:
                numeric_stats = {
                    feature: self.numeric_stats[feature].merge(stats)
                    for feature, stats in numeric_stats.items()
                }
            if self.categorical_stats:
                categorical_stats = {
                    feature: self.categorical_stats[feature].merge(stats)
                    for feature, stats in categorical_stats.items()
                }
        if predictions is not None and class_mapping:
            class_names = [class_mapping[col] for col in predictions.columns]
        if predictions is not None:
            prediction_stats = [
                aggregate_numeric_stats(predictions[col], histogram_bin_count)
                for col in predictions
            ]
            if self.prediction_stats:
                prediction_stats = [
                    original.merge(stats)
                    for original, stats in zip(self.prediction_stats, prediction_stats)
                ]

        if predictions is not None and actuals is not None:
            accuracy_stats = aggregate_accuracy(predictions, actuals, class_mapping=class_mapping)
            if self.accuracy_stats:
                accuracy_stats = [
                    original.merge(stats)
                    for original, stats in zip(self.accuracy_stats, accuracy_stats)
                ]
        if segment_attributes and features is not None:
            segment_stats.update(self.segment_stats)
            for seg_attribute in segment_attributes:
                # Reprocess the segment feature without limiting the number of categories to keep
                seg_feature = features[seg_attribute]
                seg_value_counts = Counter(aggregate_category_stats(seg_feature).category_counts)
                seg_values = [
                    value
                    for value, _ in seg_value_counts.most_common(
                        segment_value_per_attribute_count or DEFAULT_DISTINCT_SEGMENT_VALUE_COUNT
                    )
                ]

                for seg_value in seg_values:
                    # Filter features and predictions to only those for the specified segment value
                    seg_filter = seg_feature == seg_value
                    seg_features = features[seg_filter]
                    seg_predictions = predictions[seg_filter] if predictions is not None else None
                    seg_actuals = predictions[seg_filter] if actuals is not None else None
                    aggregated_stats = segment_stats.get(seg_attribute, {}).get(
                        seg_value, self.__class__()
                    )
                    aggregated_stats = aggregated_stats.aggregate(
                        features=seg_features,
                        feature_types=feature_types,
                        predictions=seg_predictions,
                        histogram_bin_count=histogram_bin_count,
                        distinct_category_count=distinct_category_count,
                        class_mapping=class_mapping,
                        actuals=seg_actuals,
                    )
                    segment_stats[seg_attribute][seg_value] = aggregated_stats
        return AggregatedStats(
            feature_types=feature_types,
            numeric_stats=numeric_stats,
            categorical_stats=categorical_stats,
            prediction_stats=prediction_stats,
            accuracy_stats=accuracy_stats,
            segment_stats=segment_stats,
            class_names=class_names,
            name=self._name,
        )

    def merge(self, other: Stats, name: Optional[str] = None) -> Stats:
        if self._is_empty():
            return other.copy(name=name)
        return self._merge(self, other, name=name)

    def copy(self, name: Optional[str] = None) -> Stats:
        return AggregatedStats(
            feature_types=self._feature_types,
            numeric_stats=self._numeric_stats,
            categorical_stats=self._categorical_stats,
            prediction_stats=self._prediction_stats,
            accuracy_stats=self._accuracy_stats,
            segment_stats=self._segment_stats,
            class_names=self._class_names,
            name=name,
        )

    def _is_empty(self) -> bool:
        no_numeric = not bool(self._numeric_stats)
        no_categorical = not bool(self._categorical_stats)
        no_predictions = not bool(self._prediction_stats)
        no_accuracy = not bool(self._accuracy_stats)
        no_segments = not bool(self._segment_stats)
        return no_numeric and no_categorical and no_predictions and no_accuracy and no_segments

    def _merge(self, first: Stats, second: Stats, name: Optional[str] = None) -> Stats:
        numeric_stats = {}
        for feature_name, second_num_aggregate in second.numeric_stats.items():
            if feature_name not in first.numeric_stats:
                raise ValueError('Merging not allowed on a different feature set.')
            first_num_aggregate = first.numeric_stats[feature_name]
            num_merged_stats = first_num_aggregate.merge(second_num_aggregate)
            if not isinstance(num_merged_stats, NumericAggregate):
                raise ValueError('Merging produced unexpected type')
            numeric_stats[feature_name] = num_merged_stats
        categorical_stats = {}
        for feature_name, second_cat_aggregate in second.categorical_stats.items():
            if feature_name not in first.categorical_stats:
                raise ValueError('Merging not allowed on a different feature set.')
            first_cat_aggregate = first.categorical_stats[feature_name]
            cat_merged_stats = first_cat_aggregate.merge(second_cat_aggregate)
            if not isinstance(cat_merged_stats, CategoricalAggregate):
                raise ValueError('Merging produced unexpected type')
            categorical_stats[feature_name] = cat_merged_stats

        if len(first.prediction_stats) != len(second.prediction_stats):
            raise ValueError('Merging statistics with different configuration is not allowed.')

        prediction_stats = []
        for pred_aggregate_idx in range(len(first.prediction_stats)):
            first_pred_aggregate = first.prediction_stats[pred_aggregate_idx]
            second_pred_aggregate = second.prediction_stats[pred_aggregate_idx]
            num_merged_stats = first_pred_aggregate.merge(second_pred_aggregate)
            if not isinstance(num_merged_stats, NumericAggregate):
                raise ValueError('Merging produced unexpected type')
            prediction_stats.append(num_merged_stats)

        if len(first.accuracy_stats) != len(second.accuracy_stats):
            raise ValueError('Merging statistics with different configuration is not allowed.')

        accuracy_stats = []
        for pred_aggregate_idx in range(len(first.accuracy_stats)):
            first_accuracy_aggregate = first.accuracy_stats[pred_aggregate_idx]
            second_accuracy_aggregate = second.accuracy_stats[pred_aggregate_idx]
            accuracy_merged_stats = first_accuracy_aggregate.merge(second_accuracy_aggregate)
            if not isinstance(accuracy_merged_stats, AccuracyAggregate):
                raise ValueError('Merging produced unexpected type')
            accuracy_stats.append(accuracy_merged_stats)
        if first.segment_stats and not second.segment_stats:
            raise ValueError('Second stats doesn\'t contain segment stats')

        if not first.segment_stats and second.segment_stats:
            raise ValueError('First stats doesn\'t contain segment stats')

        segment_stats: Dict[str, Dict[str, Stats]] = defaultdict(dict)
        for attr_name, attr_value_to_stats in first.segment_stats.items():
            for attr_value, stats in attr_value_to_stats.items():
                if attr_value not in second.segment_stats.get(attr_name, {}):
                    segment_stats[attr_name][attr_value] = stats
                else:
                    second_stats = second.segment_stats[attr_name][attr_value]
                    segment_stats[attr_name][attr_value] = stats.merge(second_stats)
        for attr_name, attr_value_to_stats in second.segment_stats.items():
            for attr_value, stats in attr_value_to_stats.items():
                if attr_value in first.segment_stats.get(attr_name, {}):
                    continue
                segment_stats[attr_name][attr_value] = stats

        return AggregatedStats(
            feature_types=self.feature_types,
            numeric_stats=numeric_stats,
            categorical_stats=categorical_stats,
            prediction_stats=prediction_stats,
            accuracy_stats=accuracy_stats,
            segment_stats=segment_stats,
            class_names=self.class_names,
            name=name,
        )

    def to_dict(self):
        result = {
            'name': self.name,
            'numeric_stats': {
                name: aggregate.to_dict() for name, aggregate in self._numeric_stats.items()
            },
            'categorical_stats': {
                name: aggregate.to_dict() for name, aggregate in self._categorical_stats.items()
            },
            'prediction_stats': [aggregate.to_dict() for aggregate in self._prediction_stats],
            'accuracy_stats': [aggregate.to_dict() for aggregate in self._accuracy_stats],
            'segment_stats': {
                name: {value: stats.to_dict() for value, stats in grouped_stats.items()}
                for name, grouped_stats in self.segment_stats.items()
            },
            'feature_types': [
                {
                    'name': fd.name,
                    'feature_type': fd.feature_type,
                    'format': fd.format,
                }
                for fd in self._feature_types
            ],
        }
        if self.class_names:
            result['class_names'] = self.class_names
        return result

    @classmethod
    def from_dict(cls, **kwargs):
        parmas = {
            'numeric_stats': {
                name: NumericAggregate.from_dict(**aggregate)
                for name, aggregate in kwargs.get('numeric_stats', {}).items()
            },
            'categorical_stats': {
                name: CategoricalAggregate.from_dict(**aggregate)
                for name, aggregate in kwargs.get('categorical_stats', {}).items()
            },
            'prediction_stats': [
                NumericAggregate.from_dict(**aggregate)
                for aggregate in kwargs.get('prediction_stats', [])
            ],
            'accuracy_stats': [
                accuracy_aggregate_from_dict(**aggregate)
                for aggregate in kwargs.get('accuracy_stats', [])
            ],
            'segment_stats': {
                name: {value: cls.from_dict(**stats) for value, stats in grouped_stats.items()}
                for name, grouped_stats in kwargs.get('segment_stats', {}).items()
            },
            'class_names': kwargs.get('class_names'),
            'name': kwargs.get('name'),
        }
        feature_types = kwargs.get('feature_types')
        if feature_types:
            parmas['feature_types'] = [FeatureDescriptor(**ft_dict) for ft_dict in feature_types]
        return cls(**parmas)
