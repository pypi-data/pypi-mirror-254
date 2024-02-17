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
from abc import ABC
from abc import abstractmethod

import pandas as pd
from datarobot_mlops.stats_aggregator.stats import Stats


class DataHistogram(ABC):
    """
    An interface for accumulating aggregated statistics for
    features and predictions.
    """

    @abstractmethod
    def push(self, input_data: pd.DataFrame, predictions: pd.DataFrame) -> None:
        """
        Accumulate new input data and predictions.

        Parameters
        ----------
        input_data
            raw data used for computing predictions
        predictions
            predictions computed with the raw data
        """

    @abstractmethod
    def get(self) -> Stats:
        """
        Get accumulated statistics.

        Returns
        -------
        Accumulated statistics.
        """

    @property
    @abstractmethod
    def size(self) -> int:
        """
        Number of raw rows that stats are computed for.
        """

    @property
    @abstractmethod
    def is_empty(self) -> bool:
        """
        True if no data were pushed, false otherwise.
        """
