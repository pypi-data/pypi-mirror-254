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
import copy
from abc import ABC
from abc import abstractmethod
from typing import Dict
from typing import Optional

import numpy as np

from .types import CentroidHistogram


def _inf_with_nan(value: float) -> float:
    if np.isinf(value):
        return np.nan
    return value


def preserve_none(accumulate, default):
    """Accumulate values but preserve None values if both arguments are None"""

    def _preserve_none(x, y):
        if x is None and y is None:
            return None
        if x is None:
            x = default
        if y is None:
            y = default
        return accumulate(x, y)

    return _preserve_none


class Aggregate(ABC):
    @property
    @abstractmethod
    def count(self) -> int:
        pass

    @property
    @abstractmethod
    def missing_count(self) -> int:
        pass

    @abstractmethod
    def merge(self, other: 'Aggregate') -> 'Aggregate':
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass


class NumericAggregate(Aggregate):
    def __init__(
        self,
        value_count: int = 0,
        missing_count: int = 0,
        value_min: float = np.nan,
        value_max: float = np.nan,
        value_sum: float = 0.0,
        value_sum_of_squares: float = 0.0,
        value_bh_tt_histogram: CentroidHistogram = CentroidHistogram([]),
    ):
        self._value_count = value_count
        self._missing_count = missing_count
        self._value_min = value_min
        self._value_max = value_max
        self._value_sum = value_sum
        self._value_sum_of_squares = value_sum_of_squares
        self._value_bh_tt_histogram = value_bh_tt_histogram

    @property
    def count(self) -> int:
        return self._value_count

    @property
    def missing_count(self) -> int:
        return self._missing_count

    @property
    def min(self) -> float:
        return self._value_min

    @property
    def max(self) -> float:
        return self._value_max

    @property
    def sum(self) -> float:
        return self._value_sum

    @property
    def sum_of_squares(self) -> float:
        return self._value_sum_of_squares

    @property
    def histogram(self) -> CentroidHistogram:
        return self._value_bh_tt_histogram

    def merge(self, other: 'Aggregate') -> 'Aggregate':
        if not isinstance(other, NumericAggregate):
            raise ValueError(
                'Cannot merge instances of {} and {} types.'.format(
                    type(self).__name__, type(other).__name__
                )
            )
        return NumericAggregate(
            value_count=self._value_count + other._value_count,
            missing_count=self._missing_count + other._missing_count,
            value_min=np.nanmin([self._value_min, other._value_min]),
            value_max=np.nanmax([self._value_max, other._value_max]),
            value_bh_tt_histogram=CentroidHistogram.merge(
                self._value_bh_tt_histogram, other._value_bh_tt_histogram
            ),
            value_sum=self._value_sum + other._value_sum,
            value_sum_of_squares=self._value_sum_of_squares + other._value_sum_of_squares,
        )

    def to_dict(self):
        return {
            "value_count": self._value_count,
            "missing_count": self._missing_count,
            "value_min": self._value_min,
            "value_max": self._value_max,
            "value_sum": self._value_sum,
            "value_sum_of_squares": self._value_sum_of_squares,
            "value_bh_tt_histogram": self._value_bh_tt_histogram.to_dict(),
        }

    def _asdict(self):
        """
        Backward compatible method, as this structure used to be a named tuple.

        Returns
        -------
        Dict with old names of attributes.

        """
        return {
            "count": self._value_count,
            "missing_count": self._missing_count,
            "min": self._value_min,
            "max": self._value_max,
            "sum": self._value_sum,
            "sum_of_squares": self._value_sum_of_squares,
            "histogram": self._value_bh_tt_histogram,
        }

    def __repr__(self):
        return str(self.to_dict())

    @classmethod
    def from_dict(cls, **kwargs):
        params = copy.deepcopy(kwargs)
        params['value_bh_tt_histogram'] = CentroidHistogram.from_dict(
            **params['value_bh_tt_histogram']
        )
        return cls(**params)


class CategoricalAggregate(Aggregate):
    def __init__(
        self,
        value_count: int = 0,
        missing_count: int = 0,
        text_words_count: Optional[int] = None,
        category_counts: Optional[Dict[str, int]] = None,
    ):
        self._value_count = value_count
        self._missing_count = missing_count
        self._text_words_count = text_words_count
        self._category_counts: Dict[str, int] = category_counts or {}

    @property
    def count(self) -> int:
        return self._value_count

    @property
    def missing_count(self) -> int:
        return self._missing_count

    @property
    def text_word_count(self) -> Optional[int]:
        return self._text_words_count

    @property
    def category_counts(self) -> Dict[str, int]:
        return self._category_counts

    def merge(self, other: 'Aggregate') -> 'Aggregate':
        if not isinstance(other, CategoricalAggregate):
            raise ValueError(
                'Cannot merge instances of {} and {} types.'.format(
                    type(self).__name__, type(other).__name__
                )
            )
        category_counts = dict(self._category_counts)
        for category_name, count in other._category_counts.items():
            current_count = category_counts.get(category_name, 0)
            category_counts[category_name] = current_count + count
        text_words_count = None
        if self._text_words_count is not None and other._text_words_count is not None:
            text_words_count = self._text_words_count + other._text_words_count
        return CategoricalAggregate(
            value_count=self._value_count + other._value_count,
            missing_count=self._missing_count + other._missing_count,
            text_words_count=text_words_count,
            category_counts=category_counts,
        )

    def to_dict(self):
        return {
            "value_count": self._value_count,
            "missing_count": self._missing_count,
            "text_words_count": self._text_words_count,
            "category_counts": self._category_counts,
        }

    def _asdict(self):
        """
        Backward compatible method, as this structure used to be a named tuple.

        Returns
        -------
        Dict with old names of attributes.

        """
        return {
            "count": self._value_count,
            "missing_count": self._missing_count,
            "text_word_count": self._text_words_count,
            "category_counts": self._category_counts,
        }

    def __repr__(self):
        return str(self.to_dict())

    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**kwargs)


class AccuracyAggregate(Aggregate, ABC):
    def __init__(
        self,
        actual_count: int = 0,
        actual_min: float = np.nan,
        actual_max: float = np.nan,
        actual_sum: float = 0.0,
        actual_sum_of_squares: float = 0.0,
        error_count: int = 0,
        error_min: float = np.nan,
        error_max: float = np.nan,
        error_sum: float = 0.0,
        error_sum_of_squares: float = 0.0,
        error_bh_tt_histogram: CentroidHistogram = CentroidHistogram([]),
    ):
        self._actual_count = actual_count
        self._actual_min = actual_min
        self._actual_max = actual_max
        self._actual_sum = actual_sum
        self._actual_sum_of_squares = actual_sum_of_squares
        self._error_count = error_count
        self._error_bh_tt_histogram = error_bh_tt_histogram
        self._error_min = error_min
        self._error_max = error_max
        self._error_sum = error_sum
        self._error_sum_of_squares = error_sum_of_squares

    @property
    def count(self) -> int:
        return self._actual_count

    @property
    def missing_count(self) -> int:
        return 0

    def merge(self, other: 'Aggregate') -> 'Aggregate':
        if not isinstance(other, type(self)):
            raise ValueError(
                'Cannot merge instances of {} and {} types.'.format(
                    type(self).__name__, type(other).__name__
                )
            )
        params = {
            'actual_count': self._actual_count + other._actual_count,
            'actual_min': np.nanmin([self._actual_min, other._actual_min]),
            'actual_max': np.nanmax([self._actual_max, other._actual_max]),
            'actual_sum': self._actual_sum + other._actual_sum,
            'actual_sum_of_squares': self._actual_sum_of_squares + other._actual_sum_of_squares,
            'error_count': self._error_count + other._error_count,
            'error_min': np.nanmin([self._error_min, other._error_min]),
            'error_max': np.nanmax([self._error_max, other._error_max]),
            'error_bh_tt_histogram': self._error_bh_tt_histogram.merge(
                other._error_bh_tt_histogram
            ),
            'error_sum': self._error_sum + other._error_sum,
            'error_sum_of_squares': self._error_sum_of_squares + other._error_sum_of_squares,
        }
        params.update(self._merge_specific(other))
        return self.__class__(**params)

    @abstractmethod
    def _merge_specific(self, other: 'AccuracyAggregate') -> dict:
        pass

    def to_dict(self):
        return {
            'actual_count': self._actual_count,
            'actual_min': self._actual_min,
            'actual_max': self._actual_max,
            'actual_sum': self._actual_sum,
            'actual_sum_of_squares': self._actual_sum_of_squares,
            'error_count': self._error_count,
            'error_min': self._error_min,
            'error_max': self._error_max,
            'error_bh_tt_histogram': self._error_bh_tt_histogram.to_dict(),
            'error_sum': self._error_sum,
            'error_sum_of_squares': self._error_sum_of_squares,
        }

    def __repr__(self):
        return str(self.to_dict())


class RegressionAccuracyAggregate(AccuracyAggregate):
    def __init__(
        self,
        actual_count: int = 0,
        actual_min: float = np.nan,
        actual_max: float = np.nan,
        actual_sum: float = 0.0,
        actual_sum_of_squares: float = 0.0,
        error_count: int = 0,
        error_min: float = np.nan,
        error_max: float = np.nan,
        error_sum: float = 0.0,
        error_sum_of_squares: float = 0.0,
        error_bh_tt_histogram: CentroidHistogram = CentroidHistogram([]),
        actual_bh_tt_histogram: CentroidHistogram = CentroidHistogram([]),
        error_percent_sum: float = 0.0,
        error_sum_of_squared_log1p: float = 0.0,
        gamma_deviance_sum: float = 0.0,
        poisson_deviance_sum: float = 0.0,
        tweedie_deviance_sum: float = 0.0,
    ):
        super().__init__(
            actual_count=actual_count,
            actual_min=actual_min,
            actual_max=actual_max,
            actual_sum=actual_sum,
            actual_sum_of_squares=actual_sum_of_squares,
            error_count=error_count,
            error_min=error_min,
            error_max=error_max,
            error_sum=error_sum,
            error_sum_of_squares=error_sum_of_squares,
            error_bh_tt_histogram=error_bh_tt_histogram,
        )
        self._actual_bh_tt_histogram = actual_bh_tt_histogram
        self._error_percent_sum = error_percent_sum
        self._error_sum_of_squared_log1p = error_sum_of_squared_log1p
        self._gamma_deviance_sum = gamma_deviance_sum
        self._poisson_deviance_sum = poisson_deviance_sum
        self._tweedie_deviance_sum = tweedie_deviance_sum

    def _merge_specific(self, other: 'AccuracyAggregate') -> dict:
        if not isinstance(other, type(self)):
            raise ValueError(
                'Cannot merge instances of {} and {} types.'.format(
                    type(self).__name__, type(other).__name__
                )
            )
        return {
            'actual_bh_tt_histogram': self._actual_bh_tt_histogram.merge(
                other._actual_bh_tt_histogram
            ),
            'error_percent_sum': self._error_percent_sum + other._error_percent_sum,
            'error_sum_of_squared_log1p': self._error_sum_of_squared_log1p
            + other._error_sum_of_squared_log1p,
            'gamma_deviance_sum': self._gamma_deviance_sum + other._gamma_deviance_sum,
            'poisson_deviance_sum': self._poisson_deviance_sum + other._poisson_deviance_sum,
            'tweedie_deviance_sum': self._tweedie_deviance_sum + other._tweedie_deviance_sum,
        }

    def to_dict(self):
        result = super().to_dict()
        result.update(
            {
                'actual_bh_tt_histogram': self._actual_bh_tt_histogram.to_dict(),
                'error_percent_sum': self._error_percent_sum,
                'error_sum_of_squared_log1p': self._error_sum_of_squared_log1p,
                'gamma_deviance_sum': self._gamma_deviance_sum,
                'poisson_deviance_sum': self._poisson_deviance_sum,
                'tweedie_deviance_sum': self._tweedie_deviance_sum,
            }
        )
        return result

    @classmethod
    def from_dict(cls, **kwargs):
        params = copy.deepcopy(kwargs)
        params['error_bh_tt_histogram'] = CentroidHistogram.from_dict(
            **params['error_bh_tt_histogram']
        )
        params['actual_bh_tt_histogram'] = CentroidHistogram.from_dict(
            **params['actual_bh_tt_histogram']
        )
        return cls(**params)


class ClassificationAccuracyAggregate(AccuracyAggregate):
    def __init__(
        self,
        actual_count: int = 0,
        actual_min: float = np.nan,
        actual_max: float = np.nan,
        actual_sum: float = 0.0,
        actual_sum_of_squares: float = 0.0,
        error_count: int = 0,
        error_min: float = np.nan,
        error_max: float = np.nan,
        error_sum: float = 0.0,
        error_sum_of_squares: float = 0.0,
        error_bh_tt_histogram: CentroidHistogram = CentroidHistogram([]),
        error_sum_of_logs: float = 0.0,
        decision_with_actual_count: int = 0,
        correct_decision_count: int = 0,
        pos_value_count: int = 0,
        pos_value_bh_tt_histogram: CentroidHistogram = CentroidHistogram([]),
        pos_value_min: Optional[float] = None,
        pos_value_max: Optional[float] = None,
    ):
        super().__init__(
            actual_count=actual_count,
            actual_min=actual_min,
            actual_max=actual_max,
            actual_sum=actual_sum,
            actual_sum_of_squares=actual_sum_of_squares,
            error_count=error_count,
            error_min=error_min,
            error_max=error_max,
            error_sum=error_sum,
            error_sum_of_squares=error_sum_of_squares,
            error_bh_tt_histogram=error_bh_tt_histogram,
        )
        self._error_sum_of_logs = error_sum_of_logs
        self._decision_with_actual_count = decision_with_actual_count
        self._correct_decision_count = correct_decision_count
        self._pos_value_count = pos_value_count
        self._pos_value_bh_tt_histogram = pos_value_bh_tt_histogram
        self._pos_value_min = pos_value_min
        self._pos_value_max = pos_value_max

    def _merge_specific(self, other: 'AccuracyAggregate') -> dict:
        if not isinstance(other, type(self)):
            raise ValueError(
                'Cannot merge instances of {} and {} types.'.format(
                    type(self).__name__, type(other).__name__
                )
            )
        pos_min_func = preserve_none(min, float("+inf"))
        pos_max_func = preserve_none(max, float("-inf"))
        return {
            'error_sum_of_logs': self._error_sum_of_logs + other._error_sum_of_logs,
            'decision_with_actual_count': self._decision_with_actual_count
            + other._decision_with_actual_count,
            'correct_decision_count': self._correct_decision_count + other._correct_decision_count,
            'pos_value_count': self._pos_value_count + other._pos_value_count,
            'pos_value_bh_tt_histogram': self._pos_value_bh_tt_histogram.merge(
                other._pos_value_bh_tt_histogram
            ),
            'pos_value_min': pos_min_func(self._pos_value_min, other._pos_value_min),
            'pos_value_max': pos_max_func(self._pos_value_max, other._pos_value_max),
        }

    def to_dict(self):
        result = super().to_dict()
        result.update(
            {
                'error_sum_of_logs': self._error_sum_of_logs,
                'decision_with_actual_count': self._decision_with_actual_count,
                'correct_decision_count': self._correct_decision_count,
                'pos_value_count': self._pos_value_count,
                'pos_value_bh_tt_histogram': self._pos_value_bh_tt_histogram.to_dict(),
                'pos_value_min': self._pos_value_min,
                'pos_value_max': self._pos_value_max,
            }
        )
        return result

    @classmethod
    def from_dict(cls, **kwargs):
        params = copy.deepcopy(kwargs)
        params['error_bh_tt_histogram'] = CentroidHistogram.from_dict(
            **params['error_bh_tt_histogram']
        )
        params['pos_value_bh_tt_histogram'] = CentroidHistogram.from_dict(
            **params['pos_value_bh_tt_histogram']
        )
        return cls(**params)
