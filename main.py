import numpy as np
from scipy.fft import fftfreq
import matplotlib.pyplot as plt
from fft import fft

def demo1():
    # sample spacing
    T = 1.0 / 800.0

    # Number of sample points
    N_arr = [100, 1000, 10000]

    fig, axs = plt.subplots(len(N_arr))
    for i in range(len(N_arr)):
        N = N_arr[i]

        

        x = np.linspace(0.0, N*T, N, endpoint=False)
        y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
        yf = fft(y)
        xf = fftfreq(N, T)[:N//2]
        
        axs[i].set_title(str(N) + " Samples")
        axs[i].plot(xf, 2.0/N * np.abs(yf[0:N//2]))

    plt.suptitle("Increasing Sample Points Demo")
    plt.show()

def demo2():
    # sample spacing
    T = 1.0 / 800.0

    N = 100000

    x = np.linspace(0.0, N*T, N, endpoint=False)
    y = sum([np.sin(t * 2.0*np.pi*x) for t in range(0,400,10)])
    yf = fft(y)
    xf = fftfreq(N, T)[:N//2]
    
    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

    plt.suptitle("10Hz Harmonic Demo")
    plt.show()

demo1()
demo2()
