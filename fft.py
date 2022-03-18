import numpy as np

def fft(a, w=0):
    a = np.asarray(a, dtype=float)
    n = len(a) # n must be a power of 2

    if n == 1:
        return a 
    w = np.exp(-2j * np.pi * np.arange(n) / n)
    even = fft(a[::2], w**2)
    odd = fft(a[1::2], w**2)
    r = [0] * n
    for i in range(n//2):
        r[i] = even[i] + w[i] * odd[i]
        r[i + n//2] = even[i] - w[i] * odd[i]
    return r