# datashader.py

"""
Datashading capabilities for ``hiveplotlib``.
"""

from hiveplotlib import HivePlot, P2CP
from hiveplotlib.viz.input_checks import input_check
from hiveplotlib.viz.matplotlib import axes_viz
import matplotlib.colors as colors
from matplotlib.image import AxesImage
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Hashable, Optional, Tuple, Union
import warnings

try:
    import datashader as ds
    import seaborn as sns
except ImportError:  # pragma: no cover
    raise ImportError(
        "Datashader or seaborn not installed, but can be installed by running "
        "`pip install hiveplotlib[datashader]`"
    )


def datashade_edges_mpl(
    instance: Union[HivePlot, P2CP],
    tag: Optional[Hashable] = None,
    cmap: Union[str, colors.ListedColormap] = sns.color_palette(
        "ch:start=.2,rot=-.3", as_cmap=True
    ),
    vmin: float = 1,
    vmax: Optional[float] = None,
    log_cmap: bool = True,
    pixel_spread: int = 2,
    reduction: callable = ds.count(),
    buffer: float = 0.1,
    fig: Optional[plt.Figure] = None,
    ax: Optional[plt.Axes] = None,
    figsize: Tuple[float, float] = (10, 10),
    dpi: int = 300,
    axes_off: bool = True,
    fig_kwargs: Optional[dict] = None,
    **im_kwargs,
) -> Tuple[plt.Figure, plt.Axes, AxesImage]:
    """
    ``matplotlib`` visualization of constructed edges in a ``HivePlot`` or ``P2CP`` instance using ``datashader``.

    The main idea of ``datashader`` is rather than plot all the lines on top of each other in a figure, one can instead
    essentially build up a single 2d image of the lines in 2-space. We can then plot just this rasterization, which is
    much smaller. By using the default reduction function ``reduction=ds.count`` (counting values in bins),
    we are essentially building a 2d histogram. For more on reductions in ``datashader``, see the
    `datashader documentation <https://datashader.org/getting_started/Pipeline.html#d-reductions>`__, and for a complete
    list of reduction functions available, see the
    `datashader API docs <https://datashader.org/api.html#reductions>`__.

    .. note::
        A high ``dpi`` value is recommended when datashading to allow for more nuance in the rasterization. This is why
        this visualization function defaults to a ``dpi`` value of 300 when ``fig=None`` and ``ax=None``.

        Experimentation with different (low) values for ``pixel_spread`` is encouraged. As the name suggests, this
        parameter spreads out calculated pixel values in the rasterization radially. Values that are too low tends to
        result in the thinner, more isolated curves "breaking apart" in the final visualization. For more on spreading,
        see the `datashader documentation <https://datashader.org/getting_started/Pipeline.html#spreading>`__.

    :param instance: ``HivePlot`` or ``P2CP`` instance for which we want to draw edges.
    :param tag: which tag of data to plot. If ``None`` is provided, then plotting will occur if there is only one tag
        in the instance. For more on data tags, see further discussion in the Comparing Network Subgroups
        `Notebook <https://geomdata.gitlab.io/hiveplotlib/comparing_network_subgroups.html#Lower-level-Functionality>`_.
    :param cmap: which colormap to use for the datashaded edges. Default is a ``seaborn`` colormap similar to the
        ``matplotlib`` ``"Blues"`` colormap.
    :param vmin: minimum value used in the colormap for plotting the rasterization of curves. Default 1.
    :param vmax: maximum value used in the colormap for plotting the rasterization of curves. Default ``None`` finds and
        uses the maximum bin value of the calculated rasterization.
    :param log_cmap: whether to use a logarithmic (base 10) scale for the colormap. Default ``True``.
    :param reduction: the means of projecting from data space to pixel space for the rasterization. Default
        ``ds.count()`` essentially builds a 2d histogram. For more on reductions in ``datashader``, see the
        `datashader documentation <https://datashader.org/getting_started/Pipeline.html#d-reductions>`__, and for a
        complete list of reduction functions available, see the
        `datashader API docs <https://datashader.org/api.html#reductions>`__.
    :param pixel_spread: amount of pixel units in which to "spread" pixel values in the resulting rasterization before
        plotting. Default amount of spreading is 2 pixels. For more on spreading,
        see the `datashader documentation <https://datashader.org/getting_started/Pipeline.html#spreading>`__.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` to 0.1 will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param fig: default ``None`` builds new figure. If a figure is specified, ``Axis`` instances will be
        drawn on that figure. Note: ``fig`` and ``ax`` must BOTH be ``None`` to instantiate new figure and axes.
    :param ax: default ``None`` builds new axis. If an axis is specified, ``Axis`` instances will be drawn on that
        axis. Note: ``fig`` and ``ax`` must BOTH be ``None`` to instantiate new figure and axes.
    :param figsize: size of figure. Note: only works if instantiating new figure and axes (e.g. ``fig`` and ``ax`` are
        ``None``).
    :param dpi: resolution (Dots Per Inch) of resulting figure. A higher-than-usual DPI is recommended to show more
        pixels in the final rasterization, which will show more nuance.
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``matplotlib`` figure (default ``True``
        hides the x and y axes).
    :param fig_kwargs: additional values to be called in ``plt.subplots()`` call. Note if ``figsize`` is added here,
        then it will be prioritized over the ``figsize`` parameter.
    :param im_kwargs: additional params that will be applied to the final ``plt.imshow()`` call on the rasterization.
    :return: ``matplotlib`` figure, axis, image.
    """
    hive_plot, _, warning_raised = input_check(instance, objects_to_plot="edges")

    # stop plotting if there are no edges to plot
    if warning_raised:
        return None

    # check for all tags in instance if no tag specified
    #  warn that we are only plotting one tag if multiple tags found
    if tag is None:
        tags = set()
        for g1 in hive_plot.edges:
            for g2 in hive_plot.edges[g1]:
                tags |= set(hive_plot.edges[g1][g2].keys())
        tag = list(tags)[0]
        if len(tags) > 1:
            warnings.warn(
                f"Multiple tags detected between edges. Only plotting tag {tag}",
                stacklevel=2,
            )

    if fig_kwargs is None:
        fig_kwargs = dict()

    # allow for plotting onto specified figure, axis
    if fig is None and ax is None:
        if "figsize" not in fig_kwargs:
            fig_kwargs["figsize"] = figsize
        if dpi not in fig_kwargs:
            fig_kwargs["dpi"] = dpi
        fig, ax = plt.subplots(**fig_kwargs)

    # always base the extent of the rasterization on the extent of the underlying hive plot / P2CP
    max_radius = max([axis.polar_end for axis in hive_plot.axes.values()])
    # throw in a minor buffer
    buffer_radius = buffer * max_radius
    max_radius += buffer_radius
    xlim = (-max_radius, max_radius)
    ylim = (-max_radius, max_radius)

    # base pixel density of rasterization on DPI of image
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width, bbox.height
    width *= fig.dpi
    height *= fig.dpi

    cvs = ds.Canvas(
        x_range=xlim, y_range=ylim, plot_height=int(height), plot_width=int(width)
    )

    # aggregate the edges into a single dataframe before datashading
    all_edges = []
    for g1 in hive_plot.edges:
        for g2 in hive_plot.edges[g1]:
            all_edges.append(hive_plot.edges[g1][g2][tag]["curves"])
    all_edges = np.row_stack(all_edges)

    temp_df = pd.DataFrame(all_edges, columns=["x", "y"])

    lines = ds.transfer_functions.spread(
        cvs.line(temp_df, "x", "y", agg=reduction), px=pixel_spread
    )

    lines_np = lines.to_numpy()

    if vmax is None:
        vmax = lines_np.max()

    if log_cmap:
        im_kwargs["norm"] = colors.LogNorm(vmin=vmin, vmax=vmax)

    if axes_off:
        ax.axis("off")

    im = ax.imshow(
        np.ma.masked_where(lines_np == 0, lines_np),
        extent=[*xlim, *ylim],
        origin="lower",
        cmap=cmap,
        **im_kwargs,
    )

    return fig, ax, im


def datashade_nodes_mpl(
    instance: Union[HivePlot, P2CP],
    cmap: Union[str, colors.ListedColormap] = "copper",
    vmin: float = 1,
    vmax: Optional[float] = None,
    log_cmap: bool = True,
    pixel_spread: int = 15,
    reduction: callable = ds.count(),
    buffer: float = 0.1,
    fig: Optional[plt.Figure] = None,
    ax: Optional[plt.Axes] = None,
    figsize: Tuple[float, float] = (10, 10),
    dpi: int = 300,
    axes_off: bool = True,
    fig_kwargs: Optional[dict] = None,
    **im_kwargs,
) -> Tuple[plt.Figure, plt.Axes, AxesImage]:
    """
    ``matplotlib`` visualization of nodes / points in a ``HivePlot`` / ``P2CP`` instance using ``datashader``.

    The main idea of ``datashader`` is rather than plot all the points on top of each other in a figure, one can instead
    essentially build up a single 2d image of the points in 2-space. We can then plot just this rasterization, which is
    much smaller. By using the default reduction function ``reduction=ds.count`` (counting values in bins),
    we are essentially building a 2d histogram. For more on reductions in ``datashader``, see the
    `datashader documentation <https://datashader.org/getting_started/Pipeline.html#d-reductions>`__, and for a complete
    list of reduction functions available, see the
    `datashader API docs <https://datashader.org/api.html#reductions>`__.

    .. note::
        A high ``dpi`` value is recommended when datashading to allow for more nuance in the rasterization. This is why
        this visualization function defaults to a ``dpi`` value of 300 when ``fig=None`` and ``ax=None``. Since we are
        interested in *positions* rather than the *lines* from ``hiveplotlib.viz.datashader.datashade_edges_mpl()``,
        though, one will likely need a much larger ``pixel_spread`` value here, on the order of 10 times larger, to see
        the node density well in the final visualization.

        Experimentation with different values for ``pixel_spread`` is encouraged. As the name suggests, this
        parameter spreads out calculated pixel values in the rasterization radially. Values that are too low tends to
        result in smaller, harder to see points in the final visualization. For more on spreading,
        see the `datashader documentation <https://datashader.org/getting_started/Pipeline.html#spreading>`__.

    :param instance: ``HivePlot`` or ``P2CP`` instance for which we want to draw edges.
    :param cmap: which colormap to use for the datashaded nodes. Default "copper".
    :param vmin: minimum value used in the colormap for plotting the rasterization of curves. Default 1.
    :param vmax: maximum value used in the colormap for plotting the rasterization of curves. Default ``None`` finds and
        uses the maximum bin value of the calculated rasterization.
    :param log_cmap: whether to use a logarithmic (base 10) scale for the colormap. Default ``True``.
    :param reduction: the means of projecting from data space to pixel space for the rasterization. Default
        ``ds.count()`` essentially builds a 2d histogram. For more on reductions in ``datashader``, see the
        `datashader documentation <https://datashader.org/getting_started/Pipeline.html#d-reductions>`__, and for a
        complete list of reduction functions available, see the
        `datashader API docs <https://datashader.org/api.html#reductions>`__.
    :param pixel_spread: amount of pixel units in which to "spread" pixel values in the resulting rasterization before
        plotting. Default amount of spreading is 15 pixels. For more on spreading,
        see the `datashader documentation <https://datashader.org/getting_started/Pipeline.html#spreading>`_.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` to 0.1 will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param fig: default ``None`` builds new figure. If a figure is specified, ``Axis`` instances will be
        drawn on that figure. Note: ``fig`` and ``ax`` must BOTH be ``None`` to instantiate new figure and axes.
    :param ax: default ``None`` builds new axis. If an axis is specified, ``Axis`` instances will be drawn on that
        axis. Note: ``fig`` and ``ax`` must BOTH be ``None`` to instantiate new figure and axes.
    :param figsize: size of figure. Note: only works if instantiating new figure and axes (e.g. ``fig`` and ``ax`` are
        ``None``).
    :param dpi: resolution (Dots Per Inch) of resulting figure. A higher-than-usual DPI is recommended to show more
        pixels in the final rasterization, which will show more nuance.
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``matplotlib`` figure (default ``True``
        hides the x and y axes).
    :param fig_kwargs: additional values to be called in ``plt.subplots()`` call. Note if ``figsize`` is added here,
        then it will be prioritized over the ``figsize`` parameter.
    :param im_kwargs: additional params that will be applied to the final ``plt.imshow()`` call on the rasterization.
    :return: ``matplotlib`` figure, axis, image.
    """
    hive_plot, name, warning_raised = input_check(instance, objects_to_plot="nodes")

    # p2cp warning only happens when axes don't exist
    if name == "P2CP" and warning_raised:
        return None

    if fig_kwargs is None:
        fig_kwargs = dict()

    # allow for plotting onto specified figure, axis
    if fig is None and ax is None:
        if "figsize" not in fig_kwargs:
            fig_kwargs["figsize"] = figsize
        if dpi not in fig_kwargs:
            fig_kwargs["dpi"] = dpi
        fig, ax = plt.subplots(**fig_kwargs)

    # always base the extent of the rasterization on the extent of the underlying hive plot / P2CP
    max_radius = max([axis.polar_end for axis in hive_plot.axes.values()])
    # throw in a minor buffer
    buffer_radius = buffer * max_radius
    max_radius += buffer_radius
    xlim = (-max_radius, max_radius)
    ylim = (-max_radius, max_radius)

    # base pixel density of rasterization on DPI of image
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width, bbox.height
    width *= fig.dpi
    height *= fig.dpi

    cvs = ds.Canvas(
        x_range=xlim, y_range=ylim, plot_height=int(height), plot_width=int(width)
    )

    # aggregate the edges into a single dataframe before datashading
    node_placements = pd.concat(
        [
            hive_plot.axes[axis_id].node_placements.loc[:, ["x", "y"]]
            for axis_id in hive_plot.axes
        ]
    )

    temp_df = pd.DataFrame(node_placements, columns=["x", "y"])

    points = ds.transfer_functions.spread(
        cvs.points(temp_df, "x", "y", agg=reduction), px=pixel_spread
    )

    points_np = points.to_numpy()

    if vmax is None:
        vmax = points_np.max()

    if log_cmap:
        im_kwargs["norm"] = colors.LogNorm(vmin=vmin, vmax=vmax)

    if axes_off:
        ax.axis("off")

    im = ax.imshow(
        np.ma.masked_where(points_np == 0, points_np),
        extent=[*xlim, *ylim],
        origin="lower",
        cmap=cmap,
        **im_kwargs,
    )

    return fig, ax, im


def datashade_hive_plot_mpl(
    instance: Union[HivePlot, P2CP],
    tag: Optional[Hashable] = None,
    cmap_edges: Union[str, colors.ListedColormap] = sns.color_palette(
        "ch:start=.2,rot=-.3", as_cmap=True
    ),
    cmap_nodes: Union[str, colors.ListedColormap] = "copper",
    vmin_nodes: float = 1,
    vmax_nodes: Optional[float] = None,
    vmin_edges: float = 1,
    vmax_edges: Optional[float] = None,
    log_cmap: bool = True,
    pixel_spread_nodes: int = 15,
    pixel_spread_edges: int = 2,
    reduction: callable = ds.count(),
    fig: Optional[plt.Figure] = None,
    ax: Optional[plt.Axes] = None,
    figsize: Tuple[float, float] = (10, 10),
    dpi: int = 300,
    axes_off: bool = True,
    buffer: float = 0.1,
    show_axes_labels: bool = True,
    axes_labels_buffer: float = 1.1,
    axes_labels_fontsize: int = 16,
    axes_kwargs: Optional[dict] = None,
    text_kwargs: Optional[dict] = None,
    fig_kwargs: Optional[dict] = None,
    **im_kwargs,
) -> Tuple[plt.Figure, plt.Axes, AxesImage, AxesImage]:
    """
    ``matplotlib`` visualization of a ``HivePlot`` or ``P2CP`` instance using ``datashader``.

    Plots both nodes and edges with datashader along with standard hive plot / P2CP axes.

    The main idea of ``datashader`` is rather than plot all the lines on top of each other in a figure, one can instead
    essentially build up a single 2d image of the lines in 2-space. We can then plot just this rasterization, which is
    much smaller. By using the default reduction function ``reduction=ds.count`` (counting values in bins),
    we are essentially building a 2d histogram. For more on reductions in ``datashader``, see the
    `datashader documentation <https://datashader.org/getting_started/Pipeline.html#d-reductions>`__, and for a complete
    list of reduction functions available, see the
    `datashader API docs <https://datashader.org/api.html#reductions>`__.

    .. note::
        A high ``dpi`` value is recommended when datashading to allow for more nuance in the rasterization. This is why
        this visualization function defaults to a ``dpi`` value of 300 when ``fig=None`` and ``ax=None``.

        Experimentation with different (low) values for ``pixel_spread_nodes`` and ``pixel_spread_edges`` is encouraged.
        As the name suggests, this parameter spreads out calculated pixel values in the rasterization radially. Values
        that are too low tends to result in the thinner, more isolated curves "breaking apart" in the final
        visualization. For more on spreading, see the
        `datashader documentation <https://datashader.org/getting_started/Pipeline.html#spreading>`__.

    :param instance: ``HivePlot`` or ``P2CP`` instance for which we want to draw edges.
    :param tag: which tag of data to plot. If ``None`` is provided, then plotting will occur if there is only one tag
        in the instance. For more on data tags, see further discussion in the Comparing Network Subgroups
        `Notebook <https://geomdata.gitlab.io/hiveplotlib/comparing_network_subgroups.html#Lower-level-Functionality>`_.
    :param cmap_edges: which colormap to use for the datashaded edges. Default is a ``seaborn`` colormap similar to the
        ``matplotlib`` ``"Blues"`` colormap.
    :param cmap_nodes: which colormap to use for the datashaded nodes. Default "copper".
    :param vmin_nodes: minimum value used in the colormap for plotting the rasterization of nodes. Default 1.
    :param vmax_nodes: maximum value used in the colormap for plotting the rasterization of nodes. Default ``None``
        finds and uses the maximum bin value of the calculated rasterization.
    :param vmin_edges: minimum value used in the colormap for plotting the rasterization of edges. Default 1.
    :param vmax_edges: maximum value used in the colormap for plotting the rasterization of edges. Default ``None``
        finds and uses the maximum bin value of the calculated rasterization.
    :param log_cmap: whether to use a logarithmic (base 10) scale for the colormap. Default ``True``.
    :param reduction: the means of projecting from data space to pixel space for the rasterization. Default
        ``ds.count()`` essentially builds a 2d histogram. For more on reductions in ``datashader``, see the
        `datashader documentation <https://datashader.org/getting_started/Pipeline.html#d-reductions>`__, and for a
        complete list of reduction functions available, see the
        `datashader API docs <https://datashader.org/api.html#reductions>`__.
    :param pixel_spread_nodes: amount of pixel units in which to "spread" pixel values in the resulting rasterization
        before plotting. Default amount of spreading is 15 pixels. For more on spreading,
        see the `datashader documentation <https://datashader.org/getting_started/Pipeline.html#spreading>`__.
    :param pixel_spread_edges: amount of pixel units in which to "spread" pixel values in the resulting rasterization
        before plotting. Default amount of spreading is 2 pixels. For more on spreading,
        see the `datashader documentation <https://datashader.org/getting_started/Pipeline.html#spreading>`__.
    :param fig: default ``None`` builds new figure. If a figure is specified, ``Axis`` instances will be
        drawn on that figure. Note: ``fig`` and ``ax`` must BOTH be ``None`` to instantiate new figure and axes.
    :param ax: default ``None`` builds new axis. If an axis is specified, ``Axis`` instances will be drawn on that
        axis. Note: ``fig`` and ``ax`` must BOTH be ``None`` to instantiate new figure and axes.
    :param figsize: size of figure. Note: only works if instantiating new figure and axes (e.g. ``fig`` and ``ax`` are
        ``None``).
    :param dpi: resolution (Dots Per Inch) of resulting figure. A higher-than-usual DPI is recommended to show more
        pixels in the final rasterization, which will show more nuance.
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``matplotlib`` figure (default ``True``
        hides the x and y axes).
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` to 0.1 will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param show_axes_labels: whether to label the hive plot axes in the figure (uses ``Axis.long_name`` for each
        ``Axis``.)
    :param axes_labels_buffer: fraction which to radially buffer axes labels (e.g. setting ``axes_label_buffer`` to 1.1
        will be 10% further past the end of the axis moving from the origin of the plot).
    :param axes_labels_fontsize: font size for hive plot axes labels.
    :param axes_kwargs: additional params that will be applied to all axes. Note, these are kwargs that affect
        a ``plt.plot()`` call.
    :param text_kwargs: additional kwargs passed to ``plt.text()`` call.
    :param fig_kwargs: additional values to be called in ``plt.subplots()`` call. Note if ``figsize`` is added here,
        then it will be prioritized over the ``figsize`` parameter.
    :param im_kwargs: additional params that will be applied to the final ``plt.imshow()`` call on the rasterization.
    :return: ``matplotlib`` figure, axis, the image corresponding to node data, and the image corresponding to edge
        data.
    """
    if axes_kwargs is None:
        axes_kwargs = dict()

    fig, ax, im_edges = datashade_edges_mpl(
        instance=instance,
        tag=tag,
        fig=fig,
        ax=ax,
        buffer=buffer,
        cmap=cmap_edges,
        vmin=vmin_edges,
        vmax=vmax_edges,
        log_cmap=log_cmap,
        reduction=reduction,
        pixel_spread=pixel_spread_edges,
        figsize=figsize,
        dpi=dpi,
        axes_off=axes_off,
        fig_kwargs=fig_kwargs,
        **im_kwargs,
    )

    axes_viz(
        instance=instance,
        fig=fig,
        ax=ax,
        buffer=buffer,
        show_axes_labels=show_axes_labels,
        axes_labels_buffer=axes_labels_buffer,
        axes_labels_fontsize=axes_labels_fontsize,
        axes_off=axes_off,
        text_kwargs=text_kwargs,
        **axes_kwargs,
    )

    fig, ax, im_nodes = datashade_nodes_mpl(
        instance=instance,
        fig=fig,
        ax=ax,
        buffer=buffer,
        cmap=cmap_nodes,
        vmin=vmin_nodes,
        vmax=vmax_nodes,
        log_cmap=log_cmap,
        reduction=reduction,
        pixel_spread=pixel_spread_nodes,
        axes_off=axes_off,
        **im_kwargs,
        zorder=2,
    )

    return fig, ax, im_nodes, im_edges
