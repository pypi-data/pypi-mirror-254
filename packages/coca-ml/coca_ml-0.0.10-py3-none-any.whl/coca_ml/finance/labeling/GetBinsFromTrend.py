from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
from scipy.stats import linregress
from numba import njit, objmode, types

__all__ = ["GetBinsFromTrend"]

_NUMBA_TYPES = types.float64


@njit()
def _getBinsFromTrend(data, spans):
    n = data.shape[0]
    out = np.zeros((n, 3), dtype=np.float64)
    for i in range(n):
        if i + spans.max() > n:
            out[i] = np.array([np.nan] * 3)
            continue
        arr = np.zeros((spans.max(), 3), dtype=np.float64)
        for j, span in enumerate(spans):
            arr[j] = _tValLinR(data[i : i + span, 0])
        imax = np.abs(arr[:, 1]).argmax()
        out[i] = arr[imax]
    return out


@njit(types.Tuple((_NUMBA_TYPES, _NUMBA_TYPES, _NUMBA_TYPES))(_NUMBA_TYPES[:]))
def _tValLinR(arr):
    x = np.arange(len(arr))
    with objmode(
        slope=_NUMBA_TYPES,
        stderr=_NUMBA_TYPES,
        pvalue=_NUMBA_TYPES,
    ):
        res = linregress(x, arr)
        slope, stderr, pvalue = res.slope, res.stderr, res.pvalue  # type: ignore
    tval = (slope / stderr) if stderr != 0 else (slope / 1e-10)
    return slope, tval, pvalue


class GetBinsFromTrend(BaseEstimator, TransformerMixin):
    def __init__(self, rng: range):
        self.rng = rng

    def fit(self, X: pd.DataFrame):
        return self

    def transform(self, X: pd.DataFrame):
        indexes = X.index
        data = X.values
        spans = np.array(self.rng)
        arr = _getBinsFromTrend(data, spans)
        df = pd.DataFrame(
            arr, index=indexes, columns=["slope", "t_val", "p_val"]
        )
        return df
