from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
from numba import njit

__all__ = ["FracDiff_FFD"]


class FracDiff_FFD(BaseEstimator, TransformerMixin):
    def __init__(self, d: float, thresh=1e-5):
        self.d = d
        self.thresh = thresh

    def fit(self, X: pd.DataFrame):
        return self

    def transform(self, X: pd.DataFrame):
        w = _getWeights_FFD(self.d, self.thresh)

        data = X.values
        out = np.zeros(data.shape, dtype=np.float64)
        for i_col in range(data.shape[1]):
            target = (
                X.iloc[:, i_col].ffill().dropna().values.astype(np.float64)
            )
            _setFracDiff_FFD(target, data, out, i_col, w)
        df = pd.DataFrame(out, index=X.index, columns=X.columns)
        return df[df[X.columns] != 0].dropna()


@njit
def _getWeights_FFD(d, thres):
    w, k = [1.0], 1
    while True:
        w_ = -w[-1] / k * (d - k + 1)
        if abs(w_) < thres:
            break
        w.append(w_)
        k += 1
    return np.array(w[::-1]).reshape(-1, 1)


@njit
def _setFracDiff_FFD(target, data, out, i_col, w):
    width = len(w) - 1
    for i_row in range(width, target.shape[0]):
        i_loc0, i_loc1 = i_row - width, i_row
        if not np.isfinite(data[i_row, i_col]):
            continue
        out[i_row, i_col] = np.dot(w.T, target[i_loc0 : i_loc1 + 1])[0]
