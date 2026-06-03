"""Reusable spatial analysis utilities — NHIS Uninsurance Ghana."""
import numpy as np


def compute_moran_i(values: list, weights_matrix) -> dict:
    """Compute Global Moran's I for spatial autocorrelation."""
    n = len(values)
    mean_v = np.mean(values)
    z = np.array(values) - mean_v
    numerator = n * sum(
        weights_matrix[i][j] * z[i] * z[j]
        for i in range(n) for j in range(n)
    )
    w_sum = sum(weights_matrix[i][j] for i in range(n) for j in range(n))
    denominator = w_sum * np.sum(z ** 2)
    return {"moran_i": numerator / denominator if denominator else 0}
