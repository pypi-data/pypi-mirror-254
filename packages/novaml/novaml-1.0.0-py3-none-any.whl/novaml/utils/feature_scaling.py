"""
A module that contains feature scaling utils functions.

Functions:
    divide_by_max: A function that scale x by dividing by max of x.
    mean_normalization: A function that scale x by using mean.
    z_score_normalization: A function that scale x by using mean and standard deviation.
"""
import numpy as np


def divide_by_max(x: np.ndarray) -> np.ndarray:
    """Scale x by dividing by max of x.

    Args:
        x: The x data to be scaled.

    Returns:
        The scaled x.
    """
    x_scaled = (x - x.min()) / x.max()
    return x_scaled


def mean_normalization(x: np.ndarray) -> np.ndarray:
    """Scale x by using mean.

    Args:
        x: The x data to be scaled.

    Returns:
        The scaled x.
    """
    mu = np.mean(x, axis=0)
    x_scaled = (x - mu) / (x.max() - x.min())
    return x_scaled


def z_score_normalization(x: np.ndarray) -> np.ndarray:
    """Scale x by using mean and standard deviation.

    Args:
        x: The x data to be scaled.

    Returns:
        The scaled x.
    """
    mu = np.mean(x, axis=0)
    sigma = np.std(x, axis=0)
    x_scaled = (x - mu) / sigma
    return x_scaled
