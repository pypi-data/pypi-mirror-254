import jax
import matplotlib.pyplot as plt
import numpy as np
import tinygp
from jax import numpy as jnp

jax.config.update("jax_enable_x64", True)


def transit(t, t0=None, D=None, d=1.0, c=12, P=None):
    if P is None:
        return d * single_transit(t, t0=t0, D=D, c=c).__array__()
    else:
        return d * periodic_transit(t, t0, D, P=P, c=c)


@jax.jit
def single_transit(t, t0=None, D=None, c=12):
    a = 0.5 * c
    b = c * t / D
    b0 = c * t0 / D

    return -0.5 * (jnp.tanh(a - b + b0) + jnp.tanh(a + b - b0))


def periodic_transit(t, t0, D, P=1, c=12):
    _t = P * np.sin(np.pi * (t - t0) / P) / (np.pi * D)
    return -0.5 * np.tanh(c * (_t + 1 / 2)) + 0.5 * np.tanh(c * (_t - 1 / 2))


def interp_split_times(time, p, dphi=0.01):
    tmax, tmin = np.max(time), np.min(time)
    total = tmax - tmin
    # since for very small periods we might fold on few points only, it's better to impose
    # at least 200 phases, to compare period folds more fairly
    phase = np.arange(0, 1, np.min([1 / 200, dphi / p]))
    n = np.arange(np.ceil(total / p))  # number of 'folds'
    # this line is important so that different time-series have the same phase 0
    tmin -= tmin % p
    pt0s = np.array([tmin + phase * p + j * p for j in n])  # corresponding t0s
    has_time = np.any([np.abs(time - _t0) < p / 2 for _t0 in pt0s.mean(1)], 1)
    pt0s = pt0s[has_time]

    return pt0s


def phase(t, t0, p):
    return (t - t0 + 0.5 * p) % p - 0.5 * p


def tv_dv(duration, depth, omega, sigma):
    return np.pi / (omega * duration), 2 * sigma / depth


def binn(x, y, n):
    N = int(len(x) / n)
    ns = np.histogram(x, N)[0]
    bx = np.histogram(x, N, weights=x)[0] / ns
    by = np.histogram(x, N, weights=y)[0] / ns
    return bx, by


def log_gauss_product_integral(a, va, b, vb):
    """Log of the product ot two Normal distributions (normalized)

    Parameters
    ----------
    a : float
        mean of distribution A
    va : float
        variance of distribution A
    b : float
        mean of distribution B
    vb : float
        variance of distribution B

    Returns
    -------
    float
        log of the integral of A*B
    """
    return (
        -0.5 * np.square(a - b) / (va + vb)
        - 0.5 * np.log(va + vb)
        - 0.5 * np.log(np.pi)
        - np.log(2) / 2
    )


def Ps(lls, zs, vzs):
    vZ = 1 / np.sum(1 / vzs, 0)
    Z = vZ * np.sum(zs / vzs, 0)

    P1 = np.sum(lls, 0)
    P2 = P1 + np.sum(log_gauss_product_integral(zs, vzs, Z, vZ), 0)
    return P1, P2


def simulated(
    t0=0.2, D=0.05, depth=0.02, P=0.7, time=None, kernel=None, error=0.001, w=None
):
    if time is None:
        time = np.arange(0, 4, 2 / 60 / 24)

    X = np.vander(time, N=4, increasing=True).T
    if w is None:
        w = [1.0, 5e-4, -2e-4, -5e-4]

    true_transit = depth * periodic_transit(time, t0, D, P=P)

    if kernel is None:
        kernel = tinygp.kernels.quasisep.SHO(np.pi / (6 * D), 45.0, depth)

    gp = tinygp.GaussianProcess(kernel, time, diag=error**2, mean=0.0)
    flux = gp.sample(jax.random.PRNGKey(40)) + true_transit + w @ X

    return (time, flux, error), X, gp


def plot_search(nu, search, bins=7 / 60 / 24):
    """Plot result of a the periodic search

    Parameters
    ----------
    nu : _type_
        _description_
    search : _type_
        _description_
    """
    t0, D, P = search.best

    plt.subplot(2, 2, (1, 3))
    plt.plot(search.periods, search.Q_snr)
    plt.title(f"{P:.5f} days")

    mean, astro, noise = nu.models(t0, D, P)

    plt.subplot(2, 2, 2)
    plt.plot(nu.flux - mean, ".", c="0.8")
    plt.plot(astro, c="k", label="found")
    ylim = plt.ylim()
    _ = plt.legend()

    plt.subplot(2, 2, 4)
    mean, astro, noise = nu.models(t0, D, P)
    phi = phase(nu.time, t0, P)
    detrended = nu.flux - noise - mean
    plt.plot(phi, detrended, ".", c=".8")
    bx, by, be = binn_time(phi, detrended, bins=bins)
    plt.errorbar(bx, by, yerr=be, fmt=".", c="k")
    plt.xlim(*(np.array([-1, 1]) * 10 * D))
    plt.ylim(*(np.array([-1, 1]) * float(np.abs(astro.min())) * 4))


def clean_periods(periods, period, tol=0.02):
    close = periods / period
    return periods[np.abs(close - np.rint(close)) > tol]


def index_binning(x, size):
    if isinstance(size, float):
        bins = np.arange(np.min(x), np.max(x), size)
    else:
        x = np.arange(0, len(x))
        bins = np.arange(0.0, len(x), size)

    d = np.digitize(x, bins)
    n = np.max(d) + 2
    indexes = []

    for i in range(0, n):
        s = np.where(d == i)
        if len(s[0]) > 0:
            s = s[0]
            indexes.append(s)

    return indexes


def binn_time(time, flux, bins=7 / 24 / 60):
    indexes = index_binning(time, bins)
    binned_time = np.array([np.mean(time[i]) for i in indexes])
    binned_flux = np.array([np.mean(flux[i]) for i in indexes])
    binned_error = np.array([np.std(flux[i]) / np.sqrt(len(i)) for i in indexes])
    return binned_time, binned_flux, binned_error
