
from numba import njit
import numpy as np


@njit(cache=True, fastmath=True)
def strfunc_from_pdf(rxs, pdf, values, order, absolute=False):
    """Compute structure function of specified order from pdf"""
    S_order = np.empty(rxs.shape)
    if absolute:
        values = abs(values)
    for irx in range(rxs.size):
        deltainc = abs(values[irx, 1] - values[irx, 0])
        S_order[irx] = deltainc * np.sum(pdf[irx] * values[irx] ** order)
    return S_order


__transonic__ = ('0.5.3',)
