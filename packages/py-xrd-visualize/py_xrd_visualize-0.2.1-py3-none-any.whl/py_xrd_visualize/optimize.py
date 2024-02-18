from abc import ABC, abstractmethod
import math

from typing import Sequence
import numpy as np


import scipy


class Optimizer(ABC):
    """
    Fitting class

    description
    ------------
    generate initial parameters and reserve optimization parameters order.
    optimize fitting parameters order is always `amp`, `center`, `width`.
    each subclass implement `initparam` , `func` , `fwhm` , `center` and `param2str`.
    """

    @staticmethod
    @abstractmethod
    def initparam(amp, center, width) -> list[float]:
        pass

    @staticmethod
    @abstractmethod
    def func(x, amp, center, widthlike, *args) -> float:
        """fitting function"""
        pass

    @staticmethod
    @abstractmethod
    def fwhm(popt: Sequence[float]) -> float:
        pass

    @staticmethod
    def center(popt: Sequence[float]) -> float:
        return popt[1]

    @staticmethod
    @abstractmethod
    def param2str(popt: Sequence[float], sig_digs: int = 3) -> str:
        pass

    def width2str(self, popt: Sequence[float], sig_digs: int = 3) -> str:
        FWHM = self.fwhm(popt)
        return f"{FWHM=:#.{sig_digs}g}"

    def toString(self, popt: Sequence[float], sig_digs: int = 3) -> str:
        return f"{self.param2str(popt, sig_digs)},{self.width2str(popt, sig_digs)}"


class Gauss(Optimizer):
    @staticmethod
    def initparam(amp, center, width) -> list[float]:
        sigma = width
        bg_c = 0
        return [amp, center, sigma, bg_c]

    @staticmethod
    def func(x, amp, center, sigma, bg_c) -> float:  # type: ignore
        """
        parameter order:
            [amp, center, sigma]
            `bg_c`: constant background
        """
        return amp * np.exp(-((x - center) ** 2) / (2 * sigma**2)) + bg_c

    @staticmethod
    def fwhm(popt: Sequence[float]) -> float:
        sigma = popt[2]
        return 2 * math.sqrt(2 * math.log(2)) * sigma

    @staticmethod
    def param2str(popt: Sequence[float], sig_digs: int = 3) -> str:
        amp = popt[0]
        center = popt[1]
        sigma = popt[2]
        return (
            f"gauss,{amp=:#.{sig_digs}g},{center=:#.{sig_digs}g},{sigma=:#.{sig_digs}g}"
        )


class Voigt(Optimizer):
    @staticmethod
    def initparam(amp, center, width) -> list[float]:
        lw = width
        gw = 1
        bg_c = 0
        return [amp, center, lw, gw, bg_c]

    @staticmethod
    def func(x, amp, center, lw, gw, bg_c) -> float:  # type: ignore
        """
        https://qiita.com/yamadasuzaku/items/4fccdc90fa13746af1e1
        Parameters:
            `amp` : amplitude
            `center `: center of Lorentzian line
            `lw` : HWHM of Lorentzian
            `gw` : sigma of the gaussian
            `bg_c`: constant background
        """
        z = (x - center + 1j * lw) / (gw * np.sqrt(2.0))
        w = scipy.special.wofz(z)
        y = amp * (w.real) / (gw * np.sqrt(2.0 * np.pi)) + bg_c
        return y

    @staticmethod
    def fwhm(popt: Sequence[float]) -> float:
        _, _, lw, gw, _ = popt
        """https://en.wikipedia.org/wiki/Voigt_profile"""
        fl = 2 * lw
        fg = 2 * math.sqrt(2 * math.log(2)) * gw
        return 0.5346 * fl + np.sqrt(0.2166 * fl**2 + fg**2)

    @staticmethod
    def param2str(popt: Sequence[float], sig_digs: int = 3) -> str:
        amp = popt[0]
        center = popt[1]
        lw = popt[2]
        gw = popt[3]

        return f"voigt,{amp=:#.{sig_digs}g},{center=:#.{sig_digs}g},{lw=:#.{sig_digs}g},{gw=:#.{sig_digs}g}"
