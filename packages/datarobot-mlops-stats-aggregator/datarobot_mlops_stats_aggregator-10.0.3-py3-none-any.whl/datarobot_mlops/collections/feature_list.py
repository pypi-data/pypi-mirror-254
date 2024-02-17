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

from datarobot_mlops.stats_aggregator.types import FeatureDescriptor


class FeatureList(object):
    """
    Class that describes all features: names, types, formats, conversions
    """

    def __init__(self, features: Optional[List[FeatureDescriptor]] = None):
        """
        Constructor.

        Parameters
        ----------
        features
            list of feature descriptors.
        """
        self._feature_types: Dict[str, str] = {}
        self._conversions: Dict[str, str] = {}
        if features:
            for feature_descriptor in features:
                self._feature_types[feature_descriptor.name] = feature_descriptor.feature_type
                if feature_descriptor.format:
                    self._conversions[feature_descriptor.name] = feature_descriptor.format

    def __getitem__(self, feature_name: str) -> str:
        return self._feature_types[feature_name]

    @property
    def features(self) -> List[str]:
        """
        List for feature names.
        """
        return list(self._feature_types.keys())

    def add(self, name: str, dtype: str, conversion: Optional[str] = None):
        """
        Adds a feature to the collection.

        Parameters
        ----------
        name
            feature name
        dtype
            feature type
        conversion
            feature format (Date) or feature conversion (Currency).
        """
        self._feature_types[name] = dtype
        if not conversion:
            return
        self._conversions[name] = conversion

    def get_feature_descriptor(self, feature_name: str) -> FeatureDescriptor:
        """
        Get feature descriptor for a feature.
        Parameters
        ----------
        feature_name
            feature name to get a descriptor for.

        Returns
        -------
        Feature descriptor
        """
        return FeatureDescriptor(
            feature_name, self[feature_name], self._conversions.get(feature_name, '')
        )

    def subset(self, features: List[str]):
        """
        Limits this structure to selected.

        Parameters
        ----------
        features
            features to select.

        Returns
        -------
        A new instance of the structure with selected features.
        """
        result = FeatureList()
        for fn in features:
            result.add(fn, self._feature_types[fn], self._conversions.get(fn))
        return result
