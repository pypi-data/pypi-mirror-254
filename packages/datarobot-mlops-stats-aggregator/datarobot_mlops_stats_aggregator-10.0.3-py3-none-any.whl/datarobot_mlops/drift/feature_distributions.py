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
from typing import List
from typing import NamedTuple
from typing import Union

import pandas as pd


class FeatureDistributions(NamedTuple):
    """
    Class containing all necessary info to compute drift metrics.
    """

    feature_name: str
    feature_type: str
    bin_values: List[str]
    ref_histogram: Union[List[int], List[float]]
    expected_sample_size: int
    com_histogram: Union[List[int], List[float]]
    actual_sample_size: int

    def to_df(self):
        return pd.DataFrame(
            {
                'Bin Values': self.bin_values,
                'Ref Histogram': self.ref_histogram,
                'Com Histogram': self.com_histogram,
            }
        )
