# axis.py

"""
Definition of ``Axis`` instance and helper static methods for generating and working with ``Axis`` instances.
"""

from hiveplotlib.utils import polar2cartesian
import numpy as np
import pandas as pd
from typing import Hashable, List, Optional


class Axis:
    """
    ``Axis`` instance.

    ``Axis`` instances are initialized based on their intended final position when plotted. Each ``Axis`` is also
    initialized with a unique, hashable ``axis_id`` for clarity when building hive plots with multiple axes.

    The eventual size and positioning of the ``Axis`` instance is dictated in the context of polar coordinates by three
    parameters:

    ``start`` dictates the distance from the origin to the *beginning* of the axis when eventually plotted.

    ``stop`` dictates the distance from the origin to the *end* of the axis when eventually plotted.

    ``angle`` sets the angle the ``Axis`` is rotated counterclockwise. For example, ``angle=0`` points East,
    ``angle=90`` points North, and ``angle=180`` points West.

    ``Node`` instances placed on each ``Axis`` instance will be scaled to fit onto the span of the ``Axis``, but this is
    discussed further in the ``HivePlot`` class, which handles this placement.

    Since ``axis_id`` values may be shorthand for easy referencing when typing code, if one desires a formal name to
    plot against each axis when visualizing, one can provide a separate ``long_name`` that will show up as the axis
    label when running ``hiveplotlib.viz`` code. (For example, one may choose ``axis_id="a1"`` and
    ``long_name="Axis 1"``.

    .. note::
        ``long_name`` defaults to ``axis_id`` if not specified.

    :example:

        .. highlight:: python
        .. code-block:: python

            # 3 axes, spaced out 120 degrees apart, all size 4, starting 1 unit off of origin
            axis0 = Axis(axis_id="a0", start=1, end=5, angle=0, long_name="Axis 0")
            axis1 = Axis(axis_id="a1", start=1, end=5, angle=120, long_name="Axis 1")
            axis2 = Axis(axis_id="a2", start=1, end=5, angle=240, long_name="Axis 2")
    """

    def __init__(
        self,
        axis_id: Hashable,
        start: float = 1,
        end: float = 5,
        angle: float = 0,
        long_name: Optional[Hashable] = None,
    ):
        """
        Initialize ``Axis`` object with start and end positions and angle. Default to axis normalized on [0, 1].

        :param axis_id: unique name for ``Axis`` instance.
        :param start: point closest to the center of the plot (using the same positive number for multiple axes in a
            hive plot is a nice way to space out the figure).
        :param end: point farthest from the center of the plot.
        :param angle: angle to set the axis, in degrees (moving counterclockwise, e.g.
            0 degrees points East, 90 degrees points North).
        :param long_name: longer name for use when labeling on graph (but not for referencing the axis).
            Default ``None`` sets it to ``axis_id``.
        """
        self.axis_id = axis_id

        if long_name is None:
            self.long_name = str(axis_id)
        else:
            self.long_name = str(long_name)

        # keep internal angle in [0, 360)
        self.angle = angle % 360

        self.polar_start = start
        self.start = polar2cartesian(self.polar_start, self.angle)

        self.polar_end = end
        self.end = polar2cartesian(self.polar_end, self.angle)

        # key from each node's data dictionary that we will use to position the node along the `Axis`
        self.node_placement_label = None

        # hold all the cartesian coordinates, polar rho, and corresponding labels in a pandas dataframe
        self.node_placements = pd.DataFrame(columns=["x", "y", "unique_id", "rho"])

    def __repr__(self) -> str:
        """
        Make printable representation (repr) for ``Axis`` instance.
        """
        return f"hiveplotlib.Axis {self.axis_id}"

    def _set_node_placements(
        self, x: List[float], y: List[float], node_ids: List[Hashable], rho: List[float]
    ):
        """
        Set ``Axis.node_placements`` to a ``pandas.DataFrame``.

        Dataframe consists of x cartesian coordinates, y cartesian coordinates, unique node IDs, and polar *rho* values
        (e.g. distance from the origin).

        .. note::
            This is an internal setter method to be called downstream by the ``HivePlot.place_nodes_on_axis()``
            method.

        :param x: ``list-like`` of x cartesian coordinates.
        :param y: ``list-like`` of y cartesian coordinates corresponding to x coordinates.
        :param node_ids: ``list-like`` of unique node IDs corresponding to x and y coordinates.
        :param rho: ``list-like`` of polar coordinate distance values corresponding to x, y, and unique ID values.
        :return: ``None``.
        """
        assert (
            np.array(x).shape[0]
            == np.array(y).shape[0]
            == np.array(node_ids).shape[0]
            == np.array(rho).shape[0]
        ), "Must provide the same number of x values, y values, and node IDs"

        self.node_placements = pd.DataFrame.from_dict(
            {"x": x, "y": y, "unique_id": node_ids, "rho": rho}
        )

        return None

    def _set_node_placement_label(self, label: Hashable):
        """
        Set which scalar variable in each ``Node`` instance will be used to place each node on the axis when plotting.

        .. note::
            This is an internal setter method to be called downstream by the ``HivePlot.place_nodes_on_axis()``
            method.

        :param label: which scalar variable in the node data to reference.
        :return: ``None``.
        """
        self.node_placement_label = label

        return None
