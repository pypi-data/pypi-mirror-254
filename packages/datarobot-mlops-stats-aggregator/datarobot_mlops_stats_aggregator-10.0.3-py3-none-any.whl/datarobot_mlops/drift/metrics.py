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
import numpy as np
from datarobot_mlops.drift.feature_distributions import FeatureDistributions


def _check_frequencies(expected_frequency, actual_frequency):
    # Check if both are populated and that their lengths are equal
    if expected_frequency is None or actual_frequency is None:
        raise ValueError("Could not find frequency tables")
    if len(expected_frequency) != len(actual_frequency):
        msg = 'Expected and actual frequency tables should be of the same size'
        raise ValueError(msg)


def kl_divergence(expected_frequency, actual_frequency):
    """
    Computes the Kullback-Leibler (KL) Divergence between 2 samples. This tests
    whether a population has shifted over time using contingency tables.
    The KL-Divergence is an example of a divergence measure,
    similar to the Hellinger divergence. However unlike Hellinger, KL-divergence
    divergence is an assymmetric metric. A score of 0.05 of higher is considered
    a drift in the population.
    Calculating the KL distance requires all bins in the contingency table
    to have a frequency greater than 0. To adjust for this for Drift Detection,
    1 is added to all 0 frequency levels.
    Returns
    -------
    KL Distance
        d : float
    References
    ----------
    .. [1] Kullback-Leibler Divergence Explained
    `[link]
    <https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained>`__
    """
    _check_frequencies(expected_frequency, actual_frequency)

    total_expected = np.sum(expected_frequency)
    total_actual = np.sum(actual_frequency)
    if total_expected == 0 or total_actual == 0:
        return None

    d = 0
    for expected_val, actual_val in zip(expected_frequency, actual_frequency):
        correction = 0
        if expected_val == 0 and actual_val == 0:
            continue
        elif expected_val == 0 or actual_val == 0:
            correction = 1
        expected_pct = (expected_val + correction) / float(total_expected + correction)
        actual_pct = (actual_val + correction) / float(total_actual + correction)
        kl = actual_pct * np.log(actual_pct / expected_pct)
        d += kl
    return d


def hellinger(expected_frequency, actual_frequency):
    """
    The Hellinger distance is an example of a divergence measure,
    similar to the Kullback-Leibler (KL) divergence. However, unlike
    KL-divergence, the Hellinger divergence is a symmetric metric.
    It is the probabilistic analog of the Euclidean distance. It is
    used for quantifying the difference between two probability distributions.
    Hellinger is a bounded metric and returns a distance between 0 and 1. Zero
    frequency bins do not have to be adjusted to compute the Hellinger distance.
    Returns
    -------
    Hellinger Distance
        d : float
    References
    ----------
    .. [1] Hellinger Distance Based Drift Detection for Nonstationary
    Environments
    `[link]
    <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.728.3224&rep=rep1&type=pdf>`__
    """
    _check_frequencies(expected_frequency, actual_frequency)

    total_expected = np.sum(expected_frequency)
    total_actual = np.sum(actual_frequency)
    if total_expected == 0 or total_actual == 0:
        return None

    d = 0
    for expected_val, actual_val in zip(expected_frequency, actual_frequency):
        if expected_val == 0 and actual_val == 0:
            continue
        expected_pct = expected_val / float(total_expected)
        actual_pct = actual_val / float(total_actual)
        he = (np.sqrt(expected_pct) - np.sqrt(actual_pct)) ** 2
        d += he
    d = np.sqrt(d) / np.sqrt(2)
    return d


def hist_intersection(expected_frequency, actual_frequency):
    """
    Histogram intersection calculates the similarity of two discretized
    probability distributions (histograms) and returns the dissimilarity (1 - similarity).
    It is a bounded metric with the value of the dissimilarity lying between 0 (identical)
    and 1 (no overlap).
    Returns
    -------
    Dissimilarity
    d : float
    References
    ----------
    .. [1] Histogram intersection for change detection
    `[link]
    <http://blog.datadive.net/histogram-intersection-for-change-detection/>`__
    """
    _check_frequencies(expected_frequency, actual_frequency)
    total_expected = np.sum(expected_frequency)
    total_actual = np.sum(actual_frequency)
    if total_expected == 0 or total_actual == 0:
        return None
    d = 0
    for expected_val, actual_val in zip(expected_frequency, actual_frequency):
        if expected_val == 0 and actual_val == 0:
            continue
        expected_pct = expected_val / float(total_expected)
        actual_pct = actual_val / float(total_actual)
        d += min(expected_pct, actual_pct)
    return 1 - d


def js_divergence(expected_frequency, actual_frequency):
    """
    Computes the Jensen–Shannon divergence JSD(P||Q) on 2 samples P, Q.
    JSD(P||Q) = 1/2 ( D(P||M) + D(Q||M) ), where: M = (P + Q)/2,
    P is actual_frequency, Q is expected_frequency, and the
    function D is the Kullback–Leibler (KL) divergence.
    In contrast to KL divergence, JSD has the following properties:
    1) JSD is bounded in range [0, 1], (or [0, ln(2)] for log base e),
    2) JSD is a symmetric measure,
    3) JSD=0, if and only if P=Q,
    4) JSD is finite even when there are 0s in P and Q.
    Returns
    -------
    JSD Distance
        d : float
    References
    ----------
    .. [1] Jensen-Shannon Divergence
    `[link]
    <https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence>`__
    """
    _check_frequencies(expected_frequency, actual_frequency)
    if np.sum(expected_frequency) == 0 or np.sum(actual_frequency) == 0:
        return None
    p = np.array(actual_frequency) / np.linalg.norm(actual_frequency, ord=1)
    q = np.array(expected_frequency) / np.linalg.norm(expected_frequency, ord=1)
    m = 0.5 * (p + q)
    return 0.5 * (kl_divergence(m, p) + kl_divergence(m, q))


def psi_index(expected_frequency, actual_frequency) -> float:
    """
    Computes the Population Stability Index on 2 samples. This tests
    whether a population has shifted over time using contingency tables.
    As a Rule-of-Thumb, if the PSI is less than 0.1, there is insignificant
    change; for PSI between 0.1 - 0.25, there is some minor change; for PSI
    greater than 0.25, there is a major shift in the population.
    Calculating the PSI requires all bins in the contingency table
    to have a frequency greater than 0. To adjust for this for Drift Detection,
    1 is added to all 0 frequency levels.
    Returns
    -------
    PSI score
        d : float
    References
    ----------
    .. [1] Population Stability Index (PSI) - Banking Case (Part 6)
    `[link]
    <http://ucanalytics.com/blogs/population-stability-index-psi-banking-case-study/>`__
    """
    _check_frequencies(expected_frequency, actual_frequency)

    total_expected = np.sum(expected_frequency)
    total_actual = np.sum(actual_frequency)
    if total_expected == 0 or total_actual == 0:
        return 0.0
    d = 0
    for expected_val, actual_val in zip(expected_frequency, actual_frequency):
        psi = _psi_for_bin(expected_val, actual_val, total_expected, total_actual)
        if psi is not None:
            d += psi
    return d


def _psi_for_bin(expected_val, actual_val, total_expected, total_actual):
    """Part of psi contributed by a single bin"""
    correction = 0
    if expected_val == 0 and actual_val == 0:
        return None
    elif expected_val == 0 or actual_val == 0:
        correction = 1
    expected_pct = (expected_val + correction) / float(total_expected + correction)
    actual_pct = (actual_val + correction) / float(total_actual + correction)
    return (actual_pct - expected_pct) * np.log(actual_pct / expected_pct)


def adapt(metric_func):
    def proxy_metric_func(feature_distributions: FeatureDistributions):
        expected_frequency = feature_distributions.ref_histogram
        actual_frequency = feature_distributions.com_histogram
        return metric_func(expected_frequency, actual_frequency)

    return proxy_metric_func


class MetricNames:
    """
    Constants for metric names
    """

    PSI = 'psi'
    KL_DIVERGENCE = 'kl_divergence'
    HELLINGER = 'hellinger'
    DISSIMILARITY = 'dissimilarity'
    JS_DIVERGENCE = 'js_divergence'
    CUSTOM = 'CUSTOM'


METRICS = {
    MetricNames.PSI: adapt(psi_index),
    MetricNames.KL_DIVERGENCE: adapt(kl_divergence),
    MetricNames.HELLINGER: adapt(hellinger),
    MetricNames.DISSIMILARITY: adapt(hist_intersection),
    MetricNames.JS_DIVERGENCE: adapt(js_divergence),
}
