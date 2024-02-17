
from numba import njit


@njit(cache=True, fastmath=True)
def compute_fb_fft(div_vb_fft, N, vz_fft):
    fb_fft = div_vb_fft
    fb_fft[:] = -div_vb_fft - N ** 2 * vz_fft
    return fb_fft


__transonic__ = ('0.5.3',)
