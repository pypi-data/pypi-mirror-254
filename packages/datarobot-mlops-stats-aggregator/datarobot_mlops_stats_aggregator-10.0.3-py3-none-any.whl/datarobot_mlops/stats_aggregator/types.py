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

from __future__ import absolute_import

from typing import List
from typing import NamedTuple

from .histogram import CentroidHistogram

_ = CentroidHistogram


class FeatureDescriptor(NamedTuple):
    name: str
    feature_type: str
    format: str = ""


FeatureTypes = List[FeatureDescriptor]


class FeatureType:
    """Type of feature, used to determine how to convert and aggregate feature values.

    Mostly corresponds to EdaTypeEnum, except text is split based on how it is tokenized.
    """

    DATE = "date"
    PERCENTAGE = "percentage"
    LENGTH = "length"
    CURRENCY = "currency"
    NUMERIC = "numeric"
    CATEGORY = "category"
    TEXT_WORDS = "text-words"  # Text that should be split on word boundaries
    TEXT_CHARS = "text-chars"  # Chinese/Japanese text that should be split by characters

    ALL = [DATE, PERCENTAGE, LENGTH, CURRENCY, NUMERIC, CATEGORY, TEXT_CHARS, TEXT_WORDS]

    @classmethod
    def from_name(cls, name):
        name = name.lower()
        if name not in cls.ALL:
            raise ValueError("'{}' name not found, allowed values: {}".format(name, cls.ALL))
        return name
