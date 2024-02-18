# plotly.py

"""
``plotly``-backend visualizations in ``hiveplotlib``.
"""

try:
    import plotly.graph_objects as go
except ImportError:  # pragma: no cover
    raise ImportError(
        "plotly not installed, but can be installed by running `pip install hiveplotlib[plotly]`"
    )

from matplotlib.colors import hex2color, to_hex
import numpy as np
from hiveplotlib import HivePlot, P2CP
from hiveplotlib.utils import polar2cartesian
from hiveplotlib.viz.base import get_axis_label_alignment
from hiveplotlib.viz.input_checks import input_check
import warnings
from typing import Hashable, List, Optional, Union


def _plotly_fig_setup(
    hive_plot: HivePlot,
    fig: Optional[go.Figure] = None,
    buffer: float = 0.3,
    width: int = 600,
    height: int = 600,
    center_plot: bool = True,
    axes_off: bool = True,
    layout_kwargs: Optional[dict] = None,
) -> go.Figure:
    """
    Set up ``plotly`` figure and perform any further adjustments based on other parameter settings.

    :param hive_plot: ``HivePlot`` instance to plot. Should never take a ``P2CP`` instance.
    :param fig: figure to modify, generates one if ``None`` provided.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default. Will only run if there is at least one axis in ``hive_plot``.
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``plotly`` figure (default ``True`` hides the
        x and y axes).
    :param layout_kwargs: additional values for the ``layout`` parameter to be called in
        `plotly.graph_objects.Figure() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html>`__
        call. Note, if ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and
        ``height`` parameters.
    :return: resulting ``plotly`` figure.
    """  # noqa: E501
    if layout_kwargs is None:
        layout_kwargs = dict()

    fig_update_kwargs = dict()

    # can only center the plot if you have axes
    if center_plot and hive_plot.max_polar_end is not None:
        # center plot at (0, 0)
        max_radius = hive_plot.max_polar_end
        # throw in a minor buffer
        buffer_radius = buffer * max_radius
        max_radius += buffer_radius

        fig_update_kwargs["xaxis_range"] = [-max_radius, max_radius]
        fig_update_kwargs["yaxis_range"] = [-max_radius, max_radius]

    if axes_off:
        fig_update_kwargs["xaxis"] = dict(visible=False)
        fig_update_kwargs["yaxis"] = dict(visible=False)
    else:
        fig_update_kwargs["xaxis"] = dict(visible=True)
        fig_update_kwargs["yaxis"] = dict(visible=True)
        fig_update_kwargs["plot_bgcolor"] = None

    # allow for plotting onto specified figure
    if fig is None:
        layout_kwargs.setdefault("autosize", False)
        layout_kwargs.setdefault("showlegend", False)
        layout_kwargs.setdefault("plot_bgcolor", "white")
        layout_kwargs.setdefault("hovermode", False)
        layout_kwargs.setdefault("dragmode", "pan")
        layout_kwargs.setdefault("height", height)
        layout_kwargs.setdefault("width", width)
        fig = go.Figure(layout=layout_kwargs)

    fig.update_layout(**fig_update_kwargs)

    return fig


def _opacity_color_handler(color: str, opacity: float) -> str:
    """
    Convert a named CSS color or hex color to a ``plotly`` compatible color with an ``opacity`` value as an RGBA string.

    .. note::
        If providing an RGB / HSL / HSV string, then no revisions will be made to the input colors, as opacity is
        already exposed for these string (e.g. RGBA / HSLA / HSVA strings, respectively).

    :param color: input color string.
    :param opacity: opacity of line to set. Must be in [0, 1].
    :return: string RGBA (e.g. red, green, blue, alpha) color in the format ``"rgba(red,green,blue,alpha)"`` that
        ``plotly`` supports, where the alpha value will be ``opacity``.
    """
    assert 0 <= opacity <= 1, "Parameter `opacity` must be in [0, 1]."
    if "(" in color:
        return color

    if color[0] != "#":
        color = to_hex(color)

    # RGB values come in originally in [0, 1] but plotly expects [0, 255] range
    rgb_values = np.array(hex2color(color)) * 255
    red = int(rgb_values[0])
    green = int(rgb_values[1])
    blue = int(rgb_values[2])

    return f"rgba({red},{green},{blue},{opacity})"


def axes_viz(
    instance: Union[HivePlot, P2CP],
    fig: Optional[go.Figure] = None,
    line_width: float = 1.5,
    opacity: float = 1.0,
    buffer: float = 0.3,
    show_axes_labels: bool = True,
    axes_labels_buffer: float = 1.25,
    axes_labels_fontsize: float = 16,
    width: int = 600,
    height: int = 600,
    center_plot: bool = True,
    axes_off: bool = True,
    layout_kwargs: Optional[dict] = None,
    label_kwargs: Optional[dict] = None,
    **line_kwargs,
) -> go.Figure:
    """
    Visualize axes in a ``HivePlot`` or ``P2CP`` instance with ``plotly``.

    .. note::
        The ``line_width`` parameter corresponds to the standard ``width`` parameter for plotly lines. We are exposing
        this parameter with a different name because ``width`` is already the standard name for *figure* width
        throughout ``hiveplotlib.viz``.

        ``plotly`` out of the box does not support standard ``opacity`` for its line plots like it does for scatter
        plots, but it does support providing an alpha channel in RGBA / HSVA / HSLA strings. The ``opacity`` parameter
        in this function call will behave as ``opacity`` behaves for ``plotly`` scatter plots, as long as the
        user-provided colors are either standard named CSS colors (e.g. "blue", "navy", "green") or hex colors.

        Users who prefer to provide colors as multi-channel RGBA / HSVA / HSLA strings will override the
        ``opacity`` parameter. For more on how to provide multi-channel color strings, see the ``plotly`` docs for the
        `color parameter for lines <https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.marker.html#plotly.graph_objects.scatter.marker.Line.color>`_.

    :param instance: ``HivePlot`` or ``P2CP`` instance for which we want to draw axes.
    :param fig: default ``None`` builds new figure. If a figure is specified, axes will be drawn on that figure.
    :param line_width: width of axes.
    :param opacity: opacity of edges. Must be in [0, 1].
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param show_axes_labels: whether to label the hive plot axes in the figure (uses ``Axis.long_name`` for each
        ``Axis``.)
    :param axes_labels_buffer: fraction which to radially buffer axes labels (e.g. setting ``axes_label_buffer`` to 1.1
        will be 10% further past the end of the axis moving from the origin of the plot).
    :param axes_labels_fontsize: font size for axes labels.
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default. Will only run if there is at least one axis in ``instance``.
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``plotly`` figure (default ``True`` hides the
        x and y axes).
    :param layout_kwargs: additional values for the ``layout`` parameter to be called in
        `plotly.graph_objects.Figure() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html>`__
        call. Note, if ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and
        ``height`` parameters.
    :param label_kwargs: additional kwargs passed to the ``textfont`` parameter of ``plotly.graph_objects.Scatter()``.
        For examples of parameter options, see the `plotly docs <https://plotly.com/python/text-and-annotations/>`__.
    :param line_kwargs: additional params that will be applied to all hive plot axes. Note, these are kwargs that
        affect a
        `plotly.graph_objects.scatter.Line() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.html#plotly.graph_objects.scatter.Line>`__
        call.
    :return: ``plotly`` figure.
    """  # noqa: E501
    # some default kwargs for the axes
    line_kwargs.setdefault("color", "black")
    line_kwargs.setdefault("width", line_width)

    # opacity handling for the line color
    line_kwargs["color"] = _opacity_color_handler(
        color=line_kwargs["color"],
        opacity=opacity,
    )

    hive_plot, _, warning_raised = input_check(instance, objects_to_plot="axes")

    if warning_raised:
        return None

    if label_kwargs is None:
        label_kwargs = dict()

    fig = _plotly_fig_setup(
        hive_plot=hive_plot,
        fig=fig,
        buffer=buffer,
        width=width,
        height=height,
        center_plot=center_plot,
        axes_off=axes_off,
        layout_kwargs=layout_kwargs,
    )

    if show_axes_labels:
        fig = label_axes(
            instance=hive_plot,
            fig=fig,
            center_plot=False,
            axes_labels_buffer=axes_labels_buffer,
            axes_labels_fontsize=axes_labels_fontsize,
            axes_off=axes_off,
            **label_kwargs,
        )

    for axis in hive_plot.axes.values():
        to_plot = np.row_stack((axis.start, axis.end))
        fig.add_trace(
            go.Scatter(
                x=to_plot[:, 0],
                y=to_plot[:, 1],
                mode="lines",
                line=line_kwargs,
                showlegend=False,
            )
        )

    return fig


def label_axes(
    instance: Union[HivePlot, P2CP],
    fig: Optional[go.Figure] = None,
    axes_labels_buffer: float = 1.25,
    axes_labels_fontsize: float = 16,
    buffer: float = 0.3,
    width: int = 600,
    height: int = 600,
    center_plot: bool = True,
    axes_off: bool = True,
    layout_kwargs: Optional[dict] = None,
    **label_kwargs,
) -> go.Figure:
    """
    Visualize axis labels in a ``HivePlot`` or ``P2CP`` instance with ``plotly``.

    For ``HivePlot`` instances, each axis' ``long_name`` attribute will be used. For ``P2CP`` instances, column names in
    the ``data`` attribute will be used.

    :param instance: ``HivePlot`` or ``P2CP`` instance for which we want to draw nodes.
    :param fig: default ``None`` builds new figure. If a figure is specified, axis labels will be drawn on that figure.
    :param axes_labels_buffer: fraction which to radially buffer axes labels (e.g. setting ``axes_label_buffer`` to 1.1
        will be 10% further past the end of the axis moving from the origin of the plot).
    :param axes_labels_fontsize: font size for axes labels.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default. Will only run if there is at least one axis in ``instance``.
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``plotly`` figure (default ``True`` hides the
        x and y axes).
    :param layout_kwargs: additional values for the ``layout`` parameter to be called in
        `plotly.graph_objects.Figure() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html>`__
        call. Note, if ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and
        ``height`` parameters.
    :param label_kwargs: additional kwargs passed to the ``textfont`` parameter of ``plotly.graph_objects.Scatter()``.
        For examples of parameter options, see the `plotly docs <https://plotly.com/python/text-and-annotations/>`__.
    :return: ``plotly`` figure.
    """  # noqa: E501
    # set default kwargs for labels
    label_kwargs.setdefault("size", axes_labels_fontsize)
    label_kwargs.setdefault("color", "black")

    hive_plot, _, warning_raised = input_check(instance, objects_to_plot="axes")

    if warning_raised:
        return None

    fig = _plotly_fig_setup(
        hive_plot=hive_plot,
        fig=fig,
        buffer=buffer,
        width=width,
        height=height,
        center_plot=center_plot,
        axes_off=axes_off,
        layout_kwargs=layout_kwargs,
    )

    for axis in hive_plot.axes.values():
        # choose horizontal and vertical alignment based on axis angle in [0, 360)
        vertical_alignment, horizontal_alignment = get_axis_label_alignment(
            axis=axis,
            backend="plotly",
        )

        x, y = polar2cartesian(axes_labels_buffer * axis.polar_end, axis.angle)
        fig.add_trace(
            go.Scatter(
                x=[x],
                y=[y],
                mode="text",
                text=axis.long_name,
                textposition=f"{vertical_alignment} {horizontal_alignment}",
                textfont=dict(**label_kwargs),
                showlegend=False,
            )
        )

    return fig


def node_viz(
    instance: Union[HivePlot, P2CP],
    fig: Optional[go.Figure] = None,
    width: int = 600,
    height: int = 600,
    center_plot: bool = True,
    buffer: float = 0.3,
    axes_off: bool = True,
    layout_kwargs: Optional[dict] = None,
    **scatter_kwargs,
) -> go.Figure:
    """
    Visualize of nodes in a ``HivePlot`` or ``P2CP`` instance that have been placed on their axes in ``plotly``.

    :param instance: ``HivePlot`` or ``P2CP`` instance for which we want to draw nodes.
    :param fig: default ``None`` builds new figure. If a figure is specified, nodes will be drawn on that figure.
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default. Will only run if there is at least one axis in ``instance``.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``plotly`` figure (default ``True``
        hides the x and y axes).
    :param layout_kwargs: additional values for the ``layout`` parameter to be called in
        `plotly.graph_objects.Figure() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html>`__
        call. Note, if ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and
        ``height`` parameters.
    :param scatter_kwargs: additional params that will be applied to all hive plot nodes. Note, these are kwargs that
        affect a `plotly.graph_objects.scatter.Marker() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.html#plotly.graph_objects.scatter.Marker>`__
        call.
    :return: ``plotly`` figure.
    """  # noqa: E501
    # some default kwargs for the axes
    scatter_kwargs.setdefault("color", "black")
    scatter_kwargs.setdefault("opacity", 0.8)
    scatter_kwargs.setdefault("size", 8)

    hive_plot, _, _ = input_check(instance, objects_to_plot="nodes")

    fig = _plotly_fig_setup(
        hive_plot=hive_plot,
        fig=fig,
        buffer=buffer,
        width=width,
        height=height,
        center_plot=center_plot,
        axes_off=axes_off,
        layout_kwargs=layout_kwargs,
    )

    for axis in hive_plot.axes.values():
        to_plot = axis.node_placements.values[:, :2]
        if to_plot.shape[0] > 0:
            fig.add_trace(
                go.Scatter(
                    x=to_plot[:, 0],
                    y=to_plot[:, 1],
                    mode="markers",
                    marker=scatter_kwargs,
                    showlegend=False,
                )
            )

    return fig


def edge_viz(
    instance: Union[HivePlot, P2CP],
    fig: Optional[go.Figure] = None,
    tags: Optional[Union[Hashable, List[Hashable]]] = None,
    line_width: float = 1.5,
    opacity: float = 0.5,
    width: int = 600,
    height: int = 600,
    center_plot: bool = True,
    buffer: float = 0.3,
    axes_off: bool = True,
    layout_kwargs: Optional[dict] = None,
    **edge_kwargs,
) -> go.Figure:
    """
    Visualize constructed edges in a ``HivePlot`` or ``P2CP`` instance with ``plotly``.

    .. note::
        The ``line_width`` parameter corresponds to the standard ``width`` parameter for plotly lines. We are exposing
        this parameter with a different name because ``width`` is already the standard name for *figure* width
        throughout ``hiveplotlib.viz``.

        ``plotly`` out of the box does not support standard ``opacity`` for its line plots like it does for scatter
        plots, but it does support providing an alpha channel in RGBA / HSVA / HSLA strings. The ``opacity`` parameter
        in this function call will behave as ``opacity`` behaves for ``plotly`` scatter plots, as long as the
        user-provided colors are either standard named CSS colors (e.g. "blue", "navy", "green") or hex colors.

        Users who prefer to provide colors as multi-channel RGBA / HSVA / HSLA strings will override the
        ``opacity`` parameter. For more on how to provide multi-channel color strings, see the ``plotly`` docs for the
        `color parameter for lines <https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.marker.html#plotly.graph_objects.scatter.marker.Line.color>`_.

    :param instance: ``HivePlot`` or ``P2CP`` instance for which we want to draw edges.
    :param fig: default ``None`` builds new figure. If a figure is specified, edges will be drawn on that figure.
    :param tags: which tag(s) of data to plot. Default ``None`` plots all tags of data. Can supply either a single tag
        or list of tags.
    :param line_width: width of edges.
    :param opacity: opacity of edges. Must be in [0, 1].
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default. Will only run if there is at least one axis in ``instance``.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``plotly`` figure (default ``True``
        hides the x and y axes).
    :param layout_kwargs: additional values for the ``layout`` parameter to be called in
        `plotly.graph_objects.Figure() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html>`__
        call. Note, if ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and
        ``height`` parameters.
    :param edge_kwargs: additional params that will be applied to all edges on all axes (but kwargs specified beforehand
        in :py:meth:`hiveplotlib.HivePlot.connect_axes()` / :py:meth:`hiveplotlib.P2CP.build_edges` or
        :py:meth:`hiveplotlib.HivePlot.add_edge_kwargs()` / :py:meth:`hiveplotlib.P2CP.add_edge_kwargs()` will take
        priority). To overwrite previously set kwargs, see :py:meth:`hiveplotlib.HivePlot.add_edge_kwargs()` /
        :py:meth:`hiveplotlib.P2CP.add_edge_kwargs()` for more. Note, these are kwargs that affect a
        `plotly.graph_objects.scatter.Line() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.marker.html#plotly.graph_objects.scatter.marker.Line>`__ call.
    :return: ``plotly`` figure.
    """  # noqa: E501
    hive_plot, name, warning_raised = input_check(instance, objects_to_plot="edges")

    # stop plotting if there are no edges to plot
    if warning_raised:
        return None

    fig = _plotly_fig_setup(
        hive_plot=hive_plot,
        fig=fig,
        buffer=buffer,
        width=width,
        height=height,
        center_plot=center_plot,
        axes_off=axes_off,
        layout_kwargs=layout_kwargs,
    )

    # p2cp warnings only need to happen once per tag
    #  because all axes behave in unison
    already_warned_p2cp_tags = []

    # grouping elements of legend by tag, plotting each group as one element in the legend
    already_added_legend_tags = []

    for a0 in hive_plot.edges.keys():
        for a1 in hive_plot.edges[a0].keys():
            # use all tags if no specific tags requested
            if tags is None:
                tags_to_plot = hive_plot.edges[a0][a1].keys()
            # otherwise, make sure we have a flat list of tags
            else:
                tags_to_plot = list(np.array(tags).flatten())

            for tag in tags_to_plot:
                temp_edge_kwargs = edge_kwargs.copy()

                # only run plotting of edges that exist
                if "curves" in hive_plot.edges[a0][a1][tag]:
                    # create edge_kwargs key if needed
                    if "edge_kwargs" not in hive_plot.edges[a0][a1][tag]:
                        hive_plot.edges[a0][a1][tag]["edge_kwargs"] = dict()

                    # don't use kwargs specified in this function call if already specified
                    for k in list(temp_edge_kwargs.keys()):
                        if k in hive_plot.edges[a0][a1][tag]["edge_kwargs"]:
                            if name == "Hive Plot":
                                warnings.warn(
                                    f"Specified kwarg {k} but already set as kwarg for edge tag {tag} "
                                    f"going from edges {a0} to {a1}. Preserving kwargs already set.\n"
                                    "(These kwargs can be changed using the `add_edge_kwargs()` method "
                                    "for your `HivePlot` instance)",
                                    stacklevel=2,
                                )
                            elif name == "P2CP":
                                # only warn once per tag over all axes
                                if tag not in already_warned_p2cp_tags:
                                    warnings.warn(
                                        f"Specified kwarg {k} but already set as kwarg for edge tag {tag}. "
                                        f"Preserving kwargs already set.\n"
                                        "(These kwargs can be changed using the `add_edge_kwargs()` method "
                                        "for your `P2CP` instance)",
                                        stacklevel=2,
                                    )
                                    already_warned_p2cp_tags.append(tag)
                            del temp_edge_kwargs[k]

                    # some default kwargs for the axes if not specified anywhere
                    if (
                        "color" not in hive_plot.edges[a0][a1][tag]["edge_kwargs"]
                        and "color" not in temp_edge_kwargs
                    ):
                        temp_edge_kwargs["color"] = _opacity_color_handler(
                            color="black",
                            opacity=opacity,
                        )
                    if (
                        "width" not in hive_plot.edges[a0][a1][tag]["edge_kwargs"]
                        and "width" not in temp_edge_kwargs
                    ):
                        temp_edge_kwargs["width"] = line_width

                    # merge edge kwargs together to make sure we fix the final edge colors with opacity modification
                    merged_temp_edge_kwargs = {
                        **temp_edge_kwargs,
                        **hive_plot.edges[a0][a1][tag]["edge_kwargs"],
                    }
                    merged_temp_edge_kwargs["color"] = _opacity_color_handler(
                        color=merged_temp_edge_kwargs["color"],
                        opacity=opacity,
                    )

                    # grab the requested array of discretized curves
                    edge_arr = hive_plot.edges[a0][a1][tag]["curves"]
                    # if there's no actual edges there, don't plot
                    if edge_arr.size > 0:
                        if tag in already_added_legend_tags:
                            showlegend = False
                        else:
                            showlegend = True
                            already_added_legend_tags.append(tag)
                        fig.add_trace(
                            go.Scatter(
                                x=edge_arr[:, 0],
                                y=edge_arr[:, 1],
                                mode="lines",
                                name=str(tag),
                                legendgroup=str(tag),
                                line=dict(**merged_temp_edge_kwargs),
                                showlegend=showlegend,
                            )
                        )

    return fig


def hive_plot_viz(
    hive_plot: HivePlot,
    fig: Optional[go.Figure] = None,
    tags: Optional[Union[Hashable, List[Hashable]]] = None,
    width: int = 600,
    height: int = 600,
    center_plot: bool = True,
    buffer: float = 0.3,
    show_axes_labels: bool = True,
    axes_labels_buffer: float = 1.25,
    axes_labels_fontsize: float = 16,
    axes_off: bool = True,
    node_kwargs: Optional[dict] = None,
    axes_kwargs: Optional[dict] = None,
    label_kwargs: Optional[dict] = None,
    layout_kwargs: Optional[dict] = None,
    **edge_kwargs,
) -> go.Figure:
    """
    Create default ``plotly`` visualization of a ``HivePlot`` instance.

    .. note::
        The line width and opacity of axes can be changed by including the ``line_width`` and ``opacity`` parameters,
        respectively, in ``axes_kwargs``. See the documentation for :py:func:`hiveplotlib.viz.plotly.axes_viz()` for
        more information.

        If the line width and opacity of edges was not set in the original hive plot, then these parameters can be set
        by including the ``line_width`` and ``opacity`` parameters, respectively, as additional keyword arguments. See
        the documentation for :py:func:`hiveplotlib.viz.plotly.edge_viz()` for more information.

    :param hive_plot: ``HivePlot`` instance for which we want to draw edges.
    :param fig: default ``None`` builds new figure. If a figure is specified, hive plot will be drawn on that figure.
    :param tags: which tag(s) of data to plot. Default ``None`` plots all tags of data. Can supply either a single tag
        or list of tags.
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default. Will only run if there is at least one axis in ``hive_plot``.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param show_axes_labels: whether to label the hive plot axes in the figure (uses ``Axis.long_name`` for each
        ``Axis``.)
    :param axes_labels_buffer: fraction which to radially buffer axes labels (e.g. setting ``axes_label_buffer`` to 1.1
        will be 10% further past the end of the axis moving from the origin of the plot).
    :param axes_labels_fontsize: font size for hive plot axes labels.
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``plotly`` figure (default ``True``
        hides the x and y axes).
    :param node_kwargs: additional params that will be applied to all hive plot nodes. Note, these are kwargs that
        affect a `plotly.graph_objects.scatter.Marker() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.html#plotly.graph_objects.scatter.Marker>`__
        call.
    :param axes_kwargs: additional params that will be applied to all hive plot axes. This includes the ``line_width``
        and ``opacity`` parameters in :py:func:`hiveplotlib.viz.plotly.axes_viz()`. Note, these are kwargs that affect a
        `plotly.graph_objects.scatter.Line() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.html#plotly.graph_objects.scatter.Line>`__
        call.
    :param label_kwargs: additional kwargs passed to the ``textfont`` parameter of ``plotly.graph_objects.Scatter()``.
        For examples of parameter options, see the `plotly docs <https://plotly.com/python/text-and-annotations/>`__.
    :param layout_kwargs: additional values for the ``layout`` parameter to be called in
        `plotly.graph_objects.Figure() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html>`__
        call. Note, if ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and
        ``height`` parameters.
    :param edge_kwargs: additional params that will be applied to all edges on all axes (but kwargs specified beforehand
        in :py:meth:`hiveplotlib.HivePlot.connect_axes()` or :py:meth:`hiveplotlib.HivePlot.add_edge_kwargs()` will take
        priority). This includes the ``line_width`` and ``opacity`` parameters in
        :py:func:`hiveplotlib.viz.plotly.edge_viz()`. To overwrite previously set kwargs, see
        :py:meth:`hiveplotlib.HivePlot.add_edge_kwargs()` for more. Note, these are kwargs that affect a
        `plotly.graph_objects.scatter.Line() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.marker.html#plotly.graph_objects.scatter.marker.Line>`__
        call.
    :return: ``plotly`` figure.
    """  # noqa: E501
    if node_kwargs is None:
        node_kwargs = dict()

    if axes_kwargs is None:
        axes_kwargs = dict()

    fig = edge_viz(
        instance=hive_plot,
        fig=fig,
        width=width,
        height=height,
        tags=tags,
        center_plot=False,
        layout_kwargs=layout_kwargs,
        **edge_kwargs,
    )

    axes_viz(
        instance=hive_plot,
        fig=fig,
        center_plot=False,
        show_axes_labels=show_axes_labels,
        axes_labels_buffer=axes_labels_buffer,
        axes_labels_fontsize=axes_labels_fontsize,
        label_kwargs=label_kwargs,
        **axes_kwargs,
    )

    # do the centering / redim-ing if requested only before the last call, otherwise it will be overridden
    node_viz(
        instance=hive_plot,
        fig=fig,
        buffer=buffer,
        center_plot=center_plot,
        axes_off=axes_off,
        **node_kwargs,
    )

    return fig


def p2cp_viz(
    p2cp: P2CP,
    fig: Optional[go.Figure] = None,
    tags: Optional[Union[Hashable, List[Hashable]]] = None,
    width: int = 600,
    height: int = 600,
    center_plot: bool = True,
    buffer: float = 0.3,
    show_axes_labels: bool = True,
    axes_labels_buffer: float = 1.25,
    axes_labels_fontsize: float = 16,
    axes_off: bool = True,
    node_kwargs: Optional[dict] = None,
    axes_kwargs: Optional[dict] = None,
    label_kwargs: Optional[dict] = None,
    layout_kwargs: Optional[dict] = None,
    **edge_kwargs,
) -> go.Figure:
    """
    Create default ``plotly`` visualization of a ``P2CP`` instance.

    .. note::
        The line width and opacity of axes can be changed by including the ``line_width`` and ``opacity`` parameters,
        respectively, in ``axes_kwargs``. See the documentation for :py:func:`hiveplotlib.viz.plotly.axes_viz()` for
        more information.

        If the line width and opacity of edges was not set in the original P2CP, then these parameters can be set
        by including the ``line_width`` and ``opacity`` parameters, respectively, as additional keyword arguments. See
        the documentation for :py:func:`hiveplotlib.viz.plotly.edge_viz()` for more information.

    :param p2cp: ``P2CP`` instance we want to visualize.
    :param fig: default ``None`` builds new figure. If a figure is specified, P2CP will be drawn on that figure.
    :param tags: which tag(s) of data to plot. Default ``None`` plots all tags of data. Can supply either a single tag
        or list of tags.
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default. Will only run if there is at least one axis in ``p2cp``.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param show_axes_labels: whether to label the P2CP axes in the figure (uses ``Axis.long_name`` for each
        ``Axis``.)
    :param axes_labels_buffer: fraction which to radially buffer axes labels (e.g. setting ``axes_label_buffer`` to 1.1
        will be 10% further past the end of the axis moving from the origin of the plot).
    :param axes_labels_fontsize: font size for P2CP axes labels.
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``plotly`` figure (default ``True``
        hides the x and y axes).
    :param node_kwargs: additional params that will be applied to all P2CP nodes. Note, these are kwargs that
        affect a `plotly.graph_objects.scatter.Marker() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.html#plotly.graph_objects.scatter.Marker>`__
        call.
    :param axes_kwargs: additional params that will be applied to all P2CP axes. This includes the ``line_width``
        and ``opacity`` parameters in :py:func:`hiveplotlib.viz.plotly.axes_viz()`. Note, these are kwargs that affect a
        `plotly.graph_objects.scatter.Line() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.html#plotly.graph_objects.scatter.Line>`__
        call.
    :param label_kwargs: additional kwargs passed to the ``textfont`` parameter of ``plotly.graph_objects.Scatter()``.
        For examples of parameter options, see the `plotly docs <https://plotly.com/python/text-and-annotations/>`__.
    :param layout_kwargs: additional values for the ``layout`` parameter to be called in
        `plotly.graph_objects.Figure() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html>`__
        call. Note, if ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and
        ``height`` parameters.
    :param edge_kwargs: additional params that will be applied to all edges on all axes (but kwargs specified beforehand
        in :py:meth:`hiveplotlib.P2CP.build_edges()` or :py:meth:`hiveplotlib.P2CP.add_edge_kwargs()` will
        take priority). This includes the ``line_width`` and ``opacity`` parameters in
        :py:func:`hiveplotlib.viz.plotly.edge_viz()`. To overwrite previously set kwargs, see
        :py:meth:`hiveplotlib.P2CP.add_edge_kwargs()` for more. Note, these are kwargs that affect a
        `plotly.graph_objects.scatter.Line() <https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.marker.html#plotly.graph_objects.scatter.marker.Line>`__
        call.
    :return: ``plotly`` figure.
    """  # noqa: E501
    if node_kwargs is None:
        node_kwargs = dict()

    if axes_kwargs is None:
        axes_kwargs = dict()

    fig = edge_viz(
        instance=p2cp,
        fig=fig,
        width=width,
        height=height,
        tags=tags,
        center_plot=False,
        layout_kwargs=layout_kwargs,
        **edge_kwargs,
    )

    axes_viz(
        instance=p2cp,
        fig=fig,
        center_plot=False,
        show_axes_labels=show_axes_labels,
        axes_labels_buffer=axes_labels_buffer,
        axes_labels_fontsize=axes_labels_fontsize,
        label_kwargs=label_kwargs,
        **axes_kwargs,
    )

    # do the centering / redim-ing if requested only before the last call, otherwise it will be overridden
    node_viz(
        instance=p2cp,
        fig=fig,
        buffer=buffer,
        center_plot=center_plot,
        axes_off=axes_off,
        **node_kwargs,
    )

    return fig


def p2cp_legend(
    p2cp: P2CP,
    fig: go.Figure,
    tags: Optional[Union[List[Hashable], Hashable]] = None,
    title: str = "Tags",
    **legend_kwargs,
) -> go.Figure:
    """
    Generate a legend for a ``P2CP`` instance, where entries in the legend will be tags of data added to the instance.

    :param p2cp: ``P2CP`` instance we want to visualize.
    :param fig: ``plotly`` figure on which we will draw the legend.
    :param tags: which tags of data to include in the legend. Default ``None`` uses all tags under
        ``p2cp.tags``. This can be ignored unless explicitly wanting to *exclude* certain tags from the legend.
    :param title: title of the legend. Default "Tags".
    :param legend_kwargs: additional values for the ``legend`` parameter in the
        `plotly.graph_objects.update_layout() <https://plotly.com/python/reference/layout/#layout-legend>`__ call.
    :return: ``plotly`` figure.
    """
    legend_kwargs.setdefault("title", title)

    # need to convert tags to strings, as we needed to coax to strings to make them legend values with bokeh
    if tags is None:
        tags = [str(i) for i in p2cp.tags[:]]
    else:
        tags = list(np.array(tags).flatten().astype(str))

    # for i in fig.legend.items:
    #     if str(i.label["value"]) in tags:
    #         i.visible = True

    fig.update_layout(showlegend=True, legend=legend_kwargs)

    return fig
