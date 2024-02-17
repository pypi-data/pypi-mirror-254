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

from typing import Iterable
from typing import Optional

from .stats import AggregatedStats
from .stats import Stats


def merge_stats(
    aggregated_stats: Iterable[Stats],
    histogram_bin_count: Optional[int] = None,
    distinct_category_count: Optional[int] = None,
    name: Optional[str] = None,
) -> Stats:
    """
    Merges multiple outputs of `aggregate_stats` into a single instance of stats.

    Parameters
    ----------
    aggregated_stats
        Multiple outputs of `aggregate_stats` to merge into a single output.
    histogram_bin_count
        Count of histogram bins to populate for each numeric feature. If unspecified, a configured default is used.
    distinct_category_count
        Count of distinct categories to count for each categorical feature. If unspecified, a configured default is used.
    name
        Merged statistics name.

    Returns
    -------
    Single instance of aggregated statistics.
    """
    _ = histogram_bin_count, distinct_category_count
    stats = list(aggregated_stats)
    result: Stats = AggregatedStats(name=name)
    for stat in stats:
        result = result.merge(stat, name=name)
    return result
