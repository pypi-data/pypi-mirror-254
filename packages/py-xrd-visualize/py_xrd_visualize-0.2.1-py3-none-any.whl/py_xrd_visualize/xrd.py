from io import TextIOBase

from pathlib import Path
from typing import Sequence


from matplotlib import pyplot as plt, ticker
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import numpy as np
from scipy.optimize import curve_fit

from py_xrd_visualize.XYs import (
    XY,
    normalize_y_cps,
    read_xys,
    reorder_x,
    roll_x,
    shift_x_center_rough,
    shift_x0,
    slide_y_log,
    range_from_xys_widest,
)


from py_xrd_visualize.optimize import (
    Optimizer,
    Gauss,
)

from py_xrd_visualize.visualize import (
    ax_conf_default,
    ax_conf_pass,
    ax_label,
    ax_legends,
    ax_plots,
    axis_conf_func,
    complete_ax,
    complete_fig,
    fig_conf_func,
    fig_conf_show,
    fig_legend,
    multi_ax_func,
)


def make_fig_1axis(
    ax_func: axis_conf_func,
    fig_funcs: Sequence[fig_conf_func],
) -> Figure:
    fig, _ = plt.subplots(nrows=1, sharex=True, squeeze=False)

    complete_fig(ax_funcs=[ax_func], fig_funcs=[fig_conf_show(), *fig_funcs])(fig)
    return fig


def ax_format_y_log_arbunits(ax: Axes):
    # y axis: log scale
    ax.yaxis.set_major_locator(ticker.LogLocator(10))

    # show minor ticks
    ax.yaxis.set_minor_locator(
        ticker.LogLocator(numticks=10, subs=(np.arange(1, 10) * 0.1).tolist())
    )
    # don't show y value
    ax.yaxis.set_major_formatter(ticker.NullFormatter())
    ax.yaxis.set_minor_formatter(ticker.NullFormatter())


def calc_xys_2θ_ω(
    xys: list[XY], scantimes_sec: list[float], slide_exp: float, slide_base: float
):
    normalize_y_cps(xys, scantimes_sec)
    slide_y_log(xys, slide_exp, slide_base)


def ax_2θ_ω(
    paths: list[TextIOBase | str | Path],
    scantimes_sec: list[float],
    range_: tuple[float, float] | None = None,
    xlabel: str = "2θ(deg.)",
    ylabel: str = "Intensity(arb. unit)",
    legends: list[str] | None = None,
    legend_title: str = "",
    legend_reverse: bool = False,
    slide_exp: float = 2,
    slide_base: float = 1.0,
    ax_funcs: list[axis_conf_func] = [],
) -> axis_conf_func:
    xys = read_xys(paths)
    calc_xys_2θ_ω(xys, scantimes_sec, slide_exp, slide_base)

    if range_ is None:
        range_ = range_from_xys_widest(xys)

    return complete_ax(
        ax_plots=ax_plots(xys),
        ax_legends=ax_legends(legends, legend_title, legend_reverse),
        ax_funcs=[
            ax_conf_default(range_, xscale="linear", yscale="log"),
            ax_format_y_log_arbunits,
            ax_label(xlabel, ylabel),
            *ax_funcs,
        ],
    )


def calc_xys_ω_scan(
    xys: list[XY], amps: list[float], optimizers: list[Optimizer]
) -> list[list[float]]:
    shift_x_center_rough(xys)

    pinits = []
    # init param ; center is ~0 by shift_x_center_rough
    for optimizer, amp in zip(optimizers, amps):
        pinits.append(optimizer.initparam(amp, 0, 1))

    # fitting
    popts = []
    for xy, optimizer, pinit in zip(xys, optimizers, pinits):
        popt, _ = curve_fit(optimizer.func, xdata=xy.x, ydata=xy.y, p0=pinit)
        popts.append(popt)

    # centering and normalize
    for xy, optimizer, popt in zip(xys, optimizers, popts):
        center = optimizer.center(popt)
        xy.x -= center
        xy.y /= optimizer.func(center, *popt)

    return popts


def ax_ω_format(ax: Axes):
    # show range includes amp(=1.0),
    ax.set_ylim(ymin=0, ymax=1.5)

    # y axis: linear scale
    ax.yaxis.set_major_locator(ticker.LinearLocator())
    ax.yaxis.set_minor_locator(ticker.LinearLocator(21))

    # don't show y value
    ax.yaxis.set_major_formatter(ticker.NullFormatter())


def ax_ω_plot_opts(
    legends: list[str] | None,
    range_: tuple[float, float],
    popts: list[list[float]],
    optimizers: list[Optimizer],
    noshow: bool = False,
):
    if not noshow:
        return ax_conf_pass

    if legends is None:
        legends = [f"{i}" for i, _ in enumerate(popts)]

    ann_texts = []

    def ax_func(ax: Axes):
        for popt, legend, optimizer in zip(popts, legends, optimizers):
            ann_text = f"{legend}:{optimizer.toString(popt)}"
            ann_texts.append(ann_text)

            x = np.linspace(*range_)
            # plot ideal func (center=0)
            popt_center = [popt[0], 0, *popt[2:]]
            y = np.vectorize(optimizer.func)(x, *popt_center)

            # normalize y to 1 on x=0
            ymax = np.max(y)
            y /= ymax

            # plot fit curve
            ax.plot(x, y)

            hwhm = optimizer.fwhm(popt) / 2
            # 1.8 is arbitrary
            xy = (hwhm, optimizer.func(hwhm, *popt_center) / ymax * 1.8)
            ax.annotate(
                ann_text,
                xy=xy,
                horizontalalignment="left",
                verticalalignment="baseline",
            )
        print("optimized param")
        for ann_text in ann_texts:
            print(ann_text)

    return ax_func


def ax_ω(
    paths: list[TextIOBase | str | Path],
    amps: list[float],
    range_: tuple[float, float] | None = None,
    xlabel: str = "ω(deg.)",
    ylabel: str = "Intensity(arb. unit)",
    legends: list[str] | None = None,
    legend_title: str = "",
    legend_reverse: bool = False,
    optimizer: Optimizer = Gauss(),
    show_optparam: bool = False,
    ax_funcs: list[axis_conf_func] = [],
) -> axis_conf_func:
    xys = read_xys(paths)

    optimizers = [(optimizer) for _ in amps]
    popts = calc_xys_ω_scan(xys, amps, optimizers)

    if range_ is None:
        range_ = range_from_xys_widest(xys)

    return complete_ax(
        ax_plots=ax_plots(xys),
        ax_legends=ax_legends(legends, legend_title, legend_reverse),
        ax_funcs=[
            ax_conf_default(range_, xscale="linear", yscale="linear"),
            ax_ω_plot_opts(legends, range_, popts, optimizers, show_optparam),
            ax_label(xlabel, ylabel),
            ax_ω_format,
            *ax_funcs,
        ],
    )


def calc_xys_φ(
    xys: list[XY],
    scantimes_sec: list[float],
    roll_x_deg: float,
    slide_exp: float,
    slide_base: float,
):
    normalize_y_cps(xys, scantimes_sec)
    shift_x0(xys)
    roll_x(xys, roll_x_deg)
    reorder_x(xys)
    slide_y_log(xys, slide_exp, slide_base)


def ax_φ_format(base: float):
    def ax_func(ax: Axes):
        ax_format_y_log_arbunits(ax)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(base))

    return ax_func


def ax_φ(
    paths: list[TextIOBase | str | Path],
    scantimes_sec: list[float],
    range_: tuple[float, float] = (0, 360),
    ax_funcs: list[axis_conf_func] = [],
    xlabel: str = "φ(deg.)",
    ylabel: str = "Intensity(arb. unit)",
    legends: list[str] | None = None,
    legend_title: str = "",
    legend_reverse: bool = False,
    roll_x_deg: float = 0,
    slide_exp: float = 2,
    slide_base: float = 1.0,
    xtick: float = 45,
) -> axis_conf_func:
    xys = read_xys(paths)

    calc_xys_φ(xys, scantimes_sec, roll_x_deg, slide_exp, slide_base)

    return complete_ax(
        ax_plots=ax_plots(xys),
        ax_legends=ax_legends(legends, legend_title, legend_reverse),
        ax_funcs=[
            ax_conf_default(range_, xscale="linear", yscale="log"),
            ax_label(xlabel, ylabel),
            ax_φ_format(xtick),
            *ax_funcs,
        ],
    )


def make_any_scan_1axis(
    paths: list[TextIOBase | str | Path],
) -> Figure:
    xys = read_xys(paths)

    def ax_func(ax: Axes):
        for xy, path in zip(xys, paths):
            ax.annotate(
                str(path),
                (xy.x[0], xy.y[0]),
            )

    return make_fig_1axis(
        ax_func=multi_ax_func(
            ax_plots(xys),
            ax_func,
        ),
        fig_funcs=[],
    )


def make_any_scan_naxis(
    paths: list[TextIOBase | str | Path],
) -> Figure:
    xys = read_xys(paths)

    # sharex = False
    fig, _ = plt.subplots(nrows=len(xys), sharex=False, squeeze=False)

    ax_funcs = []
    for xy in xys:
        ax_funcs.append(
            complete_ax(
                ax_plots=ax_plots([xy]),
                ax_legends=ax_conf_pass,
            )
        )

    complete_fig(
        ax_funcs=ax_funcs,
        fig_funcs=[
            fig_legend([str(path) for path in paths]),
            fig_conf_show(),
        ],
    )(fig)

    return fig
