from dataclasses import dataclass

import matplotlib.ticker as ticker
from matplotlib.figure import Figure
from matplotlib.axes import Axes

# import Types
from typing import Callable, Literal, Sequence, Tuple, TypeAlias
from py_xrd_visualize.XYs import XY


axis_conf_func: TypeAlias = Callable[[Axes], None]
"""
    wrapper function for Axes configuration.i.e, wrap ax.method()
"""

fig_conf_func: TypeAlias = Callable[[Figure], None]
"""
    wrapper function for Figure configuration.i.e, wrap fig.method()
"""


def ax_conf_default(
    range_: tuple[float, float],
    ymax: float | None = None,
    ymin: float | None = None,
    major_locator: ticker.Locator = ticker.AutoLocator(),
    xscale: Literal["linear", "log", "symlog", "logit"] = "linear",
    yscale: Literal["linear", "log", "symlog", "logit"] = "linear",
) -> axis_conf_func:
    """
    Parameters:
    ---
        `range_`:x-axis range.

        `ymax`,`ymin`:y-axis range,option

        `major_locator`: tick setting

        `xscale`,`yscale`:x-axis,y-axis scale.

    Return
    ---
        `func(ax:Axes)`:plot xy on ax with configuration by this function
    """

    def lambda_(ax: Axes):
        # scale
        ax.set_xscale(xscale)
        ax.set_yscale(yscale)

        # x limit
        ax.set_xlim(range_)

        # y limit
        if ymin is not None:
            ax.set_ylim(ymin=ymin)

        if ymax is not None:
            ax.set_ylim(ymax=ymax)

        # x tick setting
        ax.xaxis.set_major_locator(major_locator)
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())

    return lambda_


def fig_conf_show(
    dpi: float | None = None,
    figratio: tuple[float, float] | None = None,
    pad: float = 0.4,
) -> fig_conf_func:
    def fig_conf(fig: Figure):
        if dpi is not None:
            fig.set_dpi(dpi)

        if figratio is not None:
            fig.set_size_inches(*figratio)

        fig.tight_layout(pad=pad)

    return fig_conf


def fig_func_label(xlabel, ylabel: str) -> fig_conf_func:
    def fig_conf(fig: Figure):
        fig.supxlabel(xlabel)
        fig.supylabel(ylabel)

    return fig_conf


def ax_label(xlabel, ylabel: str) -> axis_conf_func:
    def ax_conf(ax: Axes):
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

    return ax_conf


def multi_fig_func(*fig_confs: fig_conf_func) -> fig_conf_func:
    def fig_conf(fig: Figure):
        for f in fig_confs:
            f(fig)

    return fig_conf


def multi_ax_func(*ax_confs: axis_conf_func) -> axis_conf_func:
    def ax_conf(ax: Axes):
        for f in ax_confs:
            f(ax)

    return ax_conf


def ax_conf_pass(ax: Axes):
    pass


def fig_conf_pass(fig: Figure):
    pass


def fig_legend(
    legends: list[str] | None, title: str = "", reverse=False
) -> fig_conf_func:
    if legends is None:
        return fig_conf_pass

    def fig_conf(fig: Figure):
        fig.legend(legends, title=title, reverse=reverse)

    return fig_conf


def ax_legends(
    legends: list[str] | None, title: str = "", reverse=False
) -> axis_conf_func:
    if legends is None:
        return ax_conf_pass

    def axis_func(ax: Axes):
        ax.legend(legends, title=title, reverse=reverse)

    return axis_func


@dataclass
class Annotater:
    x: float
    y: float
    label: str
    label_offset: Tuple[float, float] = (0, 0)

    def label_pos(self) -> Tuple[float, float]:
        (ox, oy) = self.label_offset
        return (self.x + ox, self.y + oy)


def ax_func_horizontal_annotates(
    common_y: float, annotes: list[Annotater], textcoords="data"
) -> axis_conf_func:
    def ax_func(ax: Axes):
        for annote in annotes:
            annote.y = common_y
            ax.scatter(annote.x, annote.y)
            ax.annotate(
                text=annote.label,
                xy=(annote.x, common_y),
                xytext=annote.label_pos(),
                horizontalalignment="center",
                verticalalignment="baseline",
                textcoords=textcoords,
            )

    return ax_func


def ax_plots(xys: list[XY]) -> axis_conf_func:
    """Plot xys to one ax."""

    def ax_func(ax: Axes) -> None:
        for xy in xys:
            ax.plot(*xy.to_tuple())

    return ax_func


def complete_ax(
    ax_plots: axis_conf_func,
    ax_legends: axis_conf_func,
    ax_funcs: Sequence[axis_conf_func] | None = None,
) -> axis_conf_func:
    """
    Plot xys and apply ax configuration.
    manage ax_conf_func order.
    """

    def ax_func(ax: Axes) -> None:
        # set legends just after plot and before set somethings(like ax.annotate)
        # legend show annotation when ax.annotate is called before ax.legend
        ax_plots(ax)
        ax_legends(ax)

        if ax_funcs is None:
            return

        for f in ax_funcs:
            f(ax)

    return ax_func


def complete_fig(
    ax_funcs: Sequence[axis_conf_func],
    fig_funcs: Sequence[fig_conf_func] | None = None,
) -> fig_conf_func:
    """
    Apply each ax_funcs to each ax in fig.axes.

    Parameters:
        ax_funcs (Sequence[axis_conf_func): A list of axis configuration functions.
        fig_funcs (Sequence[fig_conf_func] | None): An optional list of figure configuration functions.

    Returns:
        fig_conf (fig_conf_func): A figure configuration function.
    """

    def fig_conf(fig: Figure) -> None:
        axs = fig.axes
        for ax, f in zip(axs, ax_funcs):
            f(ax)

        if fig_funcs is None:
            return

        for f in fig_funcs:
            f(fig)

    return fig_conf
