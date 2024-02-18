# hiveplot.py

"""
Definition of ``HivePlot`` instance and helper static methods for generating and working with ``HivePlot`` instances.
"""

from copy import deepcopy
from hiveplotlib.node import Node
from hiveplotlib.axis import Axis
from hiveplotlib.utils import polar2cartesian, bezier_all
import json
import numpy as np
import pandas as pd
from typing import Dict, Hashable, List, Optional, Union
import warnings


class HivePlot:
    """
    Hive Plots built from combination of ``Axis`` and ``Node`` instances.

    This class is essentially methods for creating and maintaining the nested dictionary attribute ``edges``,
    which holds constructed Bézier curves, edge ids, and matplotlib keyword arguments for various sets of edges to be
    plotted. The nested dictionary structure can be abstracted to the below example.

    .. highlight:: python
    .. code-block:: python

        HivePlot.edges["starting axis"]["ending axis"]["tag"]

    The resulting dictionary value holds the edge information relating to an addition of edges that are tagged as
    "tag," specifically the edges going *FROM* the axis named "starting axis" *TO* the axis named "ending axis." This
    value is in fact another dictionary, meant to hold the discretized Bézier curves (``curves``), the matplotlib
    keyword arguments for plotting (``edge_kwargs``), and the abstracted edge ids (an ``(m, 2) np.ndarray``) between
    which we are drawing Bézier curves (``ids``).
    """

    def __init__(self):
        """
        Initialize ``HivePlot`` object.
        """
        # keep dictionary of axes, so we can find axes by label
        self.axes = dict()

        # keep dictionary of nodes with keys as unique IDs
        self.nodes = dict()

        # maintain dictionary of node assignments to axes
        #  (note, this may not always be a partition, e.g. repeat axis)
        self.node_assignments = dict()

        # maintain dictionary of dictionaries of dictionaries of edge information
        self.edges = dict()

        # maintain the largest polar end point from the axes (for plotting)
        self.max_polar_end = None

    def add_axes(self, axes: List[Axis]):
        """
        Add list of ``Axis`` instances to ``HivePlot.axes``.

        .. note::
            All resulting Axis IDs *must* be unique.

        :param axes: ``Axis`` objects to add to `HivePlot` instance.
        :return: ``None``.
        """
        current_ids = list(self.axes.keys())
        new_ids = [axis.axis_id for axis in axes]
        combined_ids = current_ids + new_ids
        assert len(combined_ids) == len(
            set(combined_ids)
        ), "New specified axis IDs combined with existing IDs led to non-unique IDs. Not adding specified axes."

        for axis in axes:
            self.axes[axis.axis_id] = axis
            self.node_assignments[axis.axis_id] = None

        # update overall largest max polar end point
        self.max_polar_end = max([axis.polar_end for axis in self.axes.values()])

        return None

    def add_nodes(self, nodes: List[Node], check_uniqueness: bool = True):
        """
        Add ``Node`` instances to ``HivePlot.nodes``.

        :param nodes: collection of ``Node`` instances, will be added to ``HivePlot.nodes`` dict with unique IDs as
            keys.
        :param check_uniqueness: whether to formally check for uniqueness.
            WARNING: the only reason to turn this off is if the dataset becomes big enough that this operation becomes
            expensive, and you have already established uniqueness another way (for example, you are pulling data from
            a database and the key in your table is the unique ID). If you add non-unique IDs with
            ``check_uniqueness=False``, we make no promises about output.
        :return: ``None``.
        """
        # make sure ids are unique or things could break later
        if check_uniqueness:
            current_ids = list(self.nodes.keys())
            new_ids = [node.unique_id for node in nodes]
            combined_ids = current_ids + new_ids
            assert len(combined_ids) == len(
                set(combined_ids)
            ), "New specified IDs combined with existing IDs led to non-unique IDs. Not adding specified nodes."

        for node in nodes:
            self.nodes[node.unique_id] = node

        return None

    def _allocate_nodes_to_axis(self, unique_ids: List[Hashable], axis_id: Hashable):
        """
        Allocate a set of nodes (pointers by unique node id's) to a single ``Axis`` (specified by a unique ``axis_id``).

        .. note::
            This is NOT sufficient for plotting nodes, only an underlying setter method called in
            ``HivePlot.place_nodes_on_axis()``.

        :param unique_ids: list of node IDs to place on specified axis.
        :param axis_id: unique ID of ``Axis`` assigned to ``HivePlot`` instance on which we want to place nodes.
        :return: ``None``.
        """
        self.node_assignments[axis_id] = unique_ids

        return None

    def place_nodes_on_axis(
        self,
        axis_id: Hashable,
        unique_ids: Union[Optional[List[Hashable]], np.ndarray] = None,
        sorting_feature_to_use: Optional[Hashable] = None,
        vmin: Optional[float] = None,
        vmax: Optional[float] = None,
    ):
        """
        Set node positions on specific ``Axis``.

        Cartesian coordinates will be normalized to specified ``vmin`` and ``vmax``. Those ``vmin`` and ``vmax``
        values will then be normalized to span the length of the axis when plotted.

        :param axis_id: which axis (as specified by the keys from ``HivePlot.axes``) for which to plot nodes.
        :param unique_ids: list of node IDs to assign to this axis. If previously set with
            ``HivePlot._allocate_nodes_to_axis()``, this will overwrite those node assignments. If ``None``, method
            will check and confirm there are existing node ID assignments.
        :param sorting_feature_to_use: which feature in the node data to use to align nodes on an axis.
            Default ``None`` uses the feature previously assigned via
            ``HivePlot.axes[axis_id]._set_node_placement_label()``.
        :param vmin: all values less than ``vmin`` will be set to ``vmin``. Default ``None`` sets as global minimum of
            feature values for all ``Node`` instances on specified ``Axis``.
        :param vmax: all values greater than ``vmax`` will be set to ``vmin``. Default ``None`` sets as global maximum
            of feature values for all ``Node`` instances on specified ``Axis``.
        :return: ``None``.
        """
        # ToDo: allow rescaling option before thresholding on min and max values (e.g. put in log scale)

        if unique_ids is None:
            assert (
                self.node_assignments[axis_id] is not None
            ), f"No existing node IDs assigned to axis {axis_id}. Please provide `unique_ids` to place on this axis."
        else:
            self._allocate_nodes_to_axis(unique_ids=unique_ids, axis_id=axis_id)

        # assign which data label to use
        if sorting_feature_to_use is not None:
            self.axes[axis_id]._set_node_placement_label(label=sorting_feature_to_use)

        else:
            assert self.axes[axis_id].node_placement_label is not None, (
                "Must either specify which feature to use in "
                "`HivePlot.place_nodes_on_axis(feature_to_use=<Hashable>)` "
                "or set the feature directly on the `Axis._set_node_placement_label(label=<Hashable>)`."
            )

        axis = self.axes[axis_id]

        assert (
            axis.node_placement_label is not None
        ), "Must choose a node feature on which to order points with `Axis._set_node_placement_label()`"

        all_node_ids = self.node_assignments[axis_id]
        all_vals = np.array(
            [
                self.nodes[node_id].data[axis.node_placement_label]
                for node_id in all_node_ids
            ]
        ).astype(float)

        if vmin is None:
            vmin = np.min(all_vals)
        if vmax is None:
            vmax = np.max(all_vals)

        # handle case of one point on an axis but no vmin or vmax specified (put it at the midpoint)
        if all_vals.size == 1 and vmin == vmax:
            vmin -= 1
            vmax += 1

        # handle case of one unique value on an axis but no vmin or vmax specified (put it at the midpoint)
        if np.unique(all_vals).size == 1 and vmin == vmax:
            vmin -= 1
            vmax += 1

        # scale values to [vmin, vmax]
        all_vals[all_vals < vmin] = vmin
        all_vals[all_vals > vmax] = vmax

        # normalize to vmin = 0, vmax = 1
        all_vals -= vmin
        all_vals /= vmax - vmin
        # scale to length of axis
        all_vals *= np.abs(axis.polar_end - axis.polar_start)
        # shift to correct starting point which could be off the origin
        all_vals += axis.polar_start

        # translate into cartesian coords
        x_coords, y_coords = polar2cartesian(all_vals, axis.angle)

        # update pandas dataframe of cartesian coordinate information and polar rho coordinates
        axis._set_node_placements(
            x=x_coords, y=y_coords, node_ids=all_node_ids, rho=all_vals
        )

        # remove any curves that were previously pointing to this axis
        #  (since they were based on a different alignment of nodes)
        for a0 in list(self.edges.keys()):
            for a1 in list(self.edges[a0].keys()):
                if a0 == axis_id or a1 == axis_id:
                    for k in self.edges[a0][a1].keys():
                        if "curves" in self.edges[a0][a1][k]:
                            del self.edges[a0][a1][k]["curves"]

        return None

    def reset_edges(
        self,
        axis_id_1: Optional[Hashable] = None,
        axis_id_2: Optional[Hashable] = None,
        tag: Optional[Hashable] = None,
        a1_to_a2: bool = True,
        a2_to_a1: bool = True,
    ):
        """
        Reset ``HivePlot.edges``.

        Setting all the parameters to ``None`` deletes any stored connections between axes previously computed. If any
        subset of the parameters is not ``None``, the resulting edges will be deleted:

        If ``axis_id_1``, ``axis_id_2``, and ``tag`` are all specified as *not* ``None``, the implied
        single subset of edges will be deleted. (Note, tags are required to be unique within a specified
        (axis_id_1, axis_id_2) pair.) In this case, the default is to delete all the edges bidirectionally (e.g. going
        ``axis_id_1`` -> ``axis_id_2`` *and* ``axis_id_2`` -> ``axis_id_1``) with the specified ``tag``. To
        only delete edges in one of these directions, see the description of the ``bool`` parameters ``a1_to_a2`` and
        ``a2_to_a1`` below.

        If *only* ``axis_id_1`` and ``axis_id_2`` are provided as not ``None``, then the default is to delete all edge
        subsets bidirectionally between ``axis_id_1`` to ``axis_id_2`` (e.g. going
        ``axis_id_1`` -> ``axis_id_2`` *and* ``axis_id_2`` -> ``axis_id_1``) with the specified ``tag``. To
        only delete edges in one of these directions, see the description of the ``bool`` parameters ``a1_to_a2`` and
        ``a2_to_a1`` below.

        If *only* ``axis_id_1`` is provided as not ``None``, then all edges going *TO* and *FROM* ``axis_id_1`` will be
        deleted. To only delete edges in one of these directions, see the description of the ``bool`` parameters
        ``a1_to_a2`` and ``a2_to_a1`` below.

        :param axis_id_1: specifies edges all coming FROM the axis identified by this unique ID.
        :param axis_id_2: specifies edges all coming TO the axis identified by this unique ID.
        :param tag: tag corresponding to explicit subset of added edges.
        :param a1_to_a2: whether to remove the connections going FROM ``axis_id_1`` TO ``axis_id_2``. Note, if
            ``axis_id_1`` is specified by ``axis_id_2`` is ``None``, then this dictates whether to remove all edges
            going *from* ``axis_id_1``.
        :param a2_to_a1: whether to remove the connections going FROM ``axis_id_2`` TO ``axis_id_1``. Note, if
            ``axis_id_1`` is specified by ``axis_id_2`` is ``None``, then this dictates whether to remove all edges
            going *to* ``axis_id_1``.
        :return: ``None``.
        """
        # all None => reset all edges
        if axis_id_1 is None and axis_id_2 is None and tag is None:
            self.edges = dict()
            return None

        # all specified => reset just unique tag subset
        elif tag is not None and axis_id_2 is not None and axis_id_1 is not None:
            if a1_to_a2:
                if tag in self.edges[axis_id_1][axis_id_2].keys():
                    del self.edges[axis_id_1][axis_id_2][tag]
                else:
                    raise ValueError("Key to delete not found. No edge data deleted.")
            if a2_to_a1:
                if tag in self.edges[axis_id_2][axis_id_1].keys():
                    del self.edges[axis_id_2][axis_id_1][tag]
                else:
                    raise ValueError("Key to delete not found. No edge data deleted.")
            return None

        # just to and from axes => kill all the connections between the two axes
        elif axis_id_2 is not None and axis_id_1 is not None:
            if a1_to_a2:
                del self.edges[axis_id_1][axis_id_2]
            if a2_to_a1:
                del self.edges[axis_id_2][axis_id_1]
            return None

        # just one axis => kill all connections coming to / from it
        elif axis_id_1 is not None and axis_id_2 is None:
            # kill "from" connections
            if a1_to_a2:
                del self.edges[axis_id_1]
            # kill "to" connections
            if a2_to_a1:
                for a0 in self.edges.keys():
                    if axis_id_1 in self.edges[a0].keys():
                        del self.edges[a0][axis_id_1]
            return None

        else:
            raise NotImplementedError(
                "See the docstring for ``HivePlot.reset_edges()`` for more on supported uses."
            )

    def __check_unique_edge_subset_tag(
        self, tag: Hashable, from_axis_id: Hashable, to_axis_id: Hashable
    ):
        """
        Make sure any ``tag`` specified to represent a subset of added edges is unique in its pair of (from, to) axes.

        Raises ``ValueError`` if ``tag`` is not unique.

        :param tag: unique ID corresponding to an added edge set.
        :param from_axis_id: ID of axis that nodes are coming "from."
        :param to_axis_id: ID of axis that nodes are going "to."
        :return: ``None``.
        """
        if tag in self.edges[from_axis_id][to_axis_id].keys():
            raise ValueError(
                f"Non-unique tag ({tag}) specified from {from_axis_id} to {to_axis_id}.\n"
                "Please provide edge subset with a new unique tag."
            )
        return None

    def _find_unique_tag(
        self, from_axis_id: Hashable, to_axis_id: Hashable, bidirectional: bool = False
    ) -> Hashable:
        """
        Find the first unique, unused ``tag`` value between ``from_axis_id`` and ``to_axis_id``.

        Check by starting at 0 and incrementing up by 1 until the integer is unique.

        :param from_axis_id: ID of axis that nodes are coming "from."
        :param to_axis_id: ID of axis that nodes are going "to."
        :param bidirectional: whether to generate a tag that is unique for *both*
            ``from_axis_id`` -> ``to_axis_id`` AND ``to_axis_id`` -> ``from_axis_id``. Default ``False`` only guarantees
            the former direction.
        :return: ``Hashable`` of resulting unique tag.
        """
        tag_list = list(self.edges[from_axis_id][to_axis_id].keys())
        if bidirectional:
            # if the other direction of edges doesn't exist, then this tag would have to be unique
            if to_axis_id in self.edges:
                if from_axis_id in self.edges[to_axis_id]:
                    tag_list += list(self.edges[to_axis_id][from_axis_id].keys())

        tag = 0
        while True:
            if tag not in tag_list:
                break
            tag += 1

        return tag

    def __store_edge_ids(
        self,
        edge_ids: np.ndarray,
        from_axis_id: Hashable,
        to_axis_id: Hashable,
        tag: Optional[Hashable] = None,
        bidirectional: bool = False,
    ) -> Hashable:
        """
        Store edge ids to ``HivePlot.edges`` (e.g. the unique identifiers of nodes "from" and "to" for each edge).

        :param edge_ids: node IDs of "from" and "to" nodes.
        :param from_axis_id: ID of axis that nodes are coming "from."
        :param to_axis_id: ID of axis that nodes are going "to."
        :param tag: tag corresponding to subset of specified edges. If ``None`` is provided, the tag will be set as
            the lowest unused integer of the tags specified for this (``from_axis_id``, ``to_axis_id``) pair, starting
            at ``0`` amongst the available tags under ``HivePlot.edges[from_axis_id][to_axis_id]``.
        :param bidirectional: if ``tag`` is ``None``, this boolean value if ``True`` guarantees that the resulting tag
            that will be generated is unique  for *both* ``from_axis_id`` -> ``to_axis_id``
            AND ``to_axis_id`` -> ``from_axis_id``. Default ``False`` only guarantees uniqueness for the former
            direction. Note: edges are still only added for ``from_axis_id`` -> ``to_axis_id``. This parameter exists
            solely for validating whether a newly generated tag must be unique bidirectionally.
        :return: the resulting unique tag.
        """
        from_keys = list(self.edges.keys())
        if from_axis_id not in from_keys:
            self.edges[from_axis_id] = dict()
            self.edges[from_axis_id][to_axis_id] = dict()

        to_keys = list(self.edges[from_axis_id].keys())
        if to_axis_id not in to_keys:
            self.edges[from_axis_id][to_axis_id] = dict()

        # make sure we create a unique integer tag if no tag is specified
        if tag is None:
            tag = self._find_unique_tag(
                from_axis_id=from_axis_id,
                to_axis_id=to_axis_id,
                bidirectional=bidirectional,
            )

        # make sure tag sufficiently unique when specified
        else:
            self.__check_unique_edge_subset_tag(
                tag=tag, from_axis_id=from_axis_id, to_axis_id=to_axis_id
            )

        self.edges[from_axis_id][to_axis_id][tag] = dict()

        self.edges[from_axis_id][to_axis_id][tag]["ids"] = edge_ids

        return tag

    def add_edge_ids(
        self,
        edges: np.ndarray,
        axis_id_1: Hashable,
        axis_id_2: Hashable,
        tag: Optional[Hashable] = None,
        a1_to_a2: bool = True,
        a2_to_a1: bool = True,
    ) -> Hashable:
        """
        Find and store the edge IDs relevant to the specified pair of axes.

        Find the subset of network connections that involve nodes on ``axis_id_1`` and ``axis_id_2``.
        looking over the specified ``edges`` compared to the IDs of the ``Node`` instances currently placed on each
        ``Axis``. Edges discovered between the specified two axes (depending on the values specified by ``a1_to_a2`` and
        ``a2_to_a1``, more below) will have the relevant edge IDs stored, with other edges disregarded.

        Generates ``(j, 2)`` and ``(k, 2)`` numpy arrays of ``axis_id_1`` to ``axis_id_2`` connections and ``axis_id_2``
        to ``axis_id_1`` connections (or only 1 of those arrays depending on parameter choices for ``a1_to_a2`` and
        ``a2_to_a1``).

        The resulting arrays of relevant edge IDs (e.g. each row is a [<FROM ID>, <TO ID>] edge) will be stored
        automatically in ``HivePlot.edges``, a dictionary of dictionaries of dictionaries of edge information,
        which can later be converted into discretized edges to be plotted in Cartesian space. They are stored as
        ``HivePlot.edges[<source_axis_id>][<sink_axis_id>][<tag>]["ids"]``.

        .. note::
            If no ``tag`` is provided (e.g. default ``None``), one will be automatically generated and returned by
            this method call.

        :param edges: ``(n, 2)`` array of ``Hashable`` values representing unique IDs of specific ``Node`` instances.
            The first column is the IDs for the "from" nodes and the second column is the IDS for the "to" nodes for
            each connection.
        :param axis_id_1: pointer to first of two ``Axis`` instances in ``HivePlot.axes`` between which we want to
            find connections.
        :param axis_id_2: pointer to second of two ``Axis`` instances in ``HivePlot.axes`` between which we want to
            find connections.
        :param tag: tag corresponding to subset of specified edges. If ``None`` is provided, the tag will be set as
            the lowest unused integer starting at ``0`` amongst the available tags under
            ``HivePlot.edges[axis_id_1][axis_id_2]`` and / or ``HivePlot.edges[axis_id_2][axis_id_1]``.
        :param a1_to_a2: whether to find the connections going FROM ``axis_id_1`` TO ``axis_id_2``.
        :param a2_to_a1: whether to find the connections going FROM ``axis_id_2`` TO ``axis_id_1``.
        :return: the resulting unique tag. Note, if both ``a1_to_a2`` and ``a2_to_a1`` are ``True`` the resulting
            unique tag returned will be the same for both directions of edges.
        """
        # only need to validate a bidirectional tag if generating it from scratch
        if a1_to_a2 and a2_to_a1 and tag is None:
            bidirectional = True
        elif not a1_to_a2 and not a2_to_a1:
            raise ValueError("One of `a1_to_a2` or `a2_to_a1` must be true.")
        else:
            bidirectional = False
        # axis 1 to axis 2
        if a1_to_a2:
            a1_input = np.isin(
                edges[:, 0], self.axes[axis_id_1].node_placements.values[:, 2]
            )
            a2_output = np.isin(
                edges[:, 1], self.axes[axis_id_2].node_placements.values[:, 2]
            )
            a1_to_a2 = np.logical_and(a1_input, a2_output)
            new_tag = self.__store_edge_ids(
                edge_ids=edges[a1_to_a2],
                from_axis_id=axis_id_1,
                to_axis_id=axis_id_2,
                tag=tag,
                bidirectional=bidirectional,
            )

        # axis 2 to axis 1
        if a2_to_a1:
            a1_output = np.isin(
                edges[:, 1], self.axes[axis_id_1].node_placements.values[:, 2]
            )
            a2_input = np.isin(
                edges[:, 0], self.axes[axis_id_2].node_placements.values[:, 2]
            )
            a2_to_a1 = np.logical_and(a2_input, a1_output)
            # if doing both, be sure to supply the same tag
            if bidirectional:
                tag = new_tag
            new_tag = self.__store_edge_ids(
                edge_ids=edges[a2_to_a1],
                from_axis_id=axis_id_2,
                to_axis_id=axis_id_1,
                tag=tag,
            )

        return new_tag

    def add_edge_curves_between_axes(
        self,
        axis_id_1: Hashable,
        axis_id_2: Hashable,
        tag: Optional[Hashable] = None,
        a1_to_a2: bool = True,
        a2_to_a1: bool = True,
        num_steps: int = 100,
        short_arc: bool = True,
    ):
        """
        Construct discretized edge curves between two axes of a ``HivePlot`` instance.

        .. note::
            One must run ``HivePlot.add_edge_ids()`` first for the two axes of interest.

        Resulting discretized Bézier curves will be stored as an ``(n, 2) numpy.ndarray`` of multiple sampled curves
        where the first column is x position and the second column is y position in Cartesian coordinates.

        .. note::
            Although each curve is represented by a ``(num_steps, 2)`` array, all the curves are stored curves in a
            single collective ``numpy.ndarray`` separated by rows of ``[np.nan, np.nan]`` between each discretized
            curve. This allows ``matplotlib`` to accept a single array when plotting lines via ``plt.plot()``, which
            speeds up plotting later.

        This output will be stored in ``HivePlot.edges[axis_id_1][axis_id_2][tag]["curves"]``.

        :param axis_id_1: pointer to first of two ``Axis`` instances in ``HivePlot.axes`` between which we want to
            find connections.
        :param axis_id_2: pointer to second of two ``Axis`` instances in ``HivePlot.axes`` between which we want to
            find connections.
        :param tag: unique ID specifying which subset of edges specified by their IDs to construct
            (e.g. ``HivePlot.edges[axis_id_1][axis_id_2][tag]["ids"]``).
            Note, if no tag is specified (e.g. ``tag=None``), it is presumed there is only one tag for the specified
            set of axes to look over, which can be inferred. If no tag is specified and there are multiple tags to
            choose from, a ``ValueError`` will be raised.
        :param a1_to_a2: whether to build out the edges going FROM ``axis_id_1`` TO ``axis_id_2``.
        :param a2_to_a1: whether to build out the edges going FROM ``axis_id_2`` TO ``axis_id_1``.
        :param num_steps: number of points sampled along a given Bézier curve. Larger numbers will result in
            smoother curves when plotting later, but slower rendering.
        :param short_arc: whether to take the shorter angle arc (``True``) or longer angle arc (``False``).
            There are always two ways to traverse between axes: with one angle being x, the other option being 360 - x.
            For most visualizations, the user should expect to traverse the "short arc," hence the default ``True``.
            For full user flexibility, however, we offer the ability to force the arc the other direction, the
            "long arc" (``short_arc=False``). Note: in the case of 2 axes 180 degrees apart, there is no "wrong" angle,
            so in this case an initial decision will be made, but switching this boolean will switch the arc to the
            other hemisphere.
        :return: ``None``.
        """
        if tag is None:
            a1_to_a2_failure = False
            a2_to_a1_failure = False
            if a1_to_a2:
                assert (
                    len(list(self.edges[axis_id_1][axis_id_2].keys())) > 0
                ), "No edges specified to construct. Be sure to run `HivePlot.add_edge_ids()` first."

                a1_to_a2_tag = list(self.edges[axis_id_1][axis_id_2].keys())[0]

                if len(list(self.edges[axis_id_1][axis_id_2].keys())) > 1:
                    a1_to_a2_failure = True

            if a2_to_a1:
                assert (
                    len(list(self.edges[axis_id_2][axis_id_1].keys())) > 0
                ), "No edges specified to construct. Be sure to run `HivePlot.add_edge_ids()` first."

                a2_to_a1_tag = list(self.edges[axis_id_2][axis_id_1].keys())[0]

                if len(list(self.edges[axis_id_2][axis_id_1].keys())) > 1:
                    a2_to_a1_failure = True

            if a1_to_a2_failure and a2_to_a1_failure:
                raise ValueError(
                    "Must specify precise `tag` to handle both `a1_to_a2=True` and `a2_to_a1=True` here. "
                    "The current tags for the specified axes are:\n"
                    f"{axis_id_2} -> {axis_id_1: {list(self.edges[axis_id_2][axis_id_1].keys())}}\n"
                    f"{axis_id_2} -> {axis_id_1: {list(self.edges[axis_id_2][axis_id_1].keys())}}"
                )

            elif a1_to_a2_failure:
                raise ValueError(
                    "Must specify precise `tag` to handle `a1_to_a2=True` here. "
                    "The current tags for the specified axes are:\n"
                    f"{axis_id_1} -> {axis_id_2: {list(self.edges[axis_id_1][axis_id_2].keys())}}"
                )
            elif a2_to_a1_failure:
                raise ValueError(
                    "Must specify precise `tag` to handle `a2_to_a1=True` here. "
                    "The current tags for the specified axes are:\n"
                    f"{axis_id_2} -> {axis_id_1: {list(self.edges[axis_id_2][axis_id_1].keys())}}"
                )

        else:
            a1_to_a2_tag = tag
            a2_to_a1_tag = tag

        all_connections = []
        direction = []
        if a1_to_a2:
            try:
                ids = self.edges[axis_id_1][axis_id_2][a1_to_a2_tag]["ids"]
                temp_connections = ids.copy().astype("O")
                all_connections.append(temp_connections)
                direction.append("a1_to_a2")
            except KeyError:
                raise KeyError(
                    f"`self.edges[{axis_id_1}][{axis_id_2}][{a1_to_a2_tag}]['ids']` does not appear to exist. "
                    "It is expected you have run `self.add_edge_ids()` first for the two axes of interest."
                )
        if a2_to_a1:
            try:
                ids = self.edges[axis_id_2][axis_id_1][a2_to_a1_tag]["ids"]
                temp_connections = ids.copy().astype("O")
                all_connections.append(temp_connections)
                direction.append("a2_to_a1")
            except KeyError:
                raise KeyError(
                    f"`self.edges[{axis_id_2}][{axis_id_1}][{a2_to_a1_tag}]['ids']` does not appear to exist. "
                    "It is expected you have run `self.add_edge_ids()` first for the two axes of interest."
                )

        if len(all_connections) == 0:
            raise ValueError("One of `a1_to_a2` or `a2_to_a1` must be true.")

        for connections, edge_direction in zip(all_connections, direction):
            # left join the flattened start and stop values array with the cartesian and polar node locations
            #  Note: sorting behavior is not cooperating, so needed a trivial np.arange to re-sort at end
            #   (dropped before using `out`)
            if edge_direction == "a1_to_a2":
                start_axis = axis_id_1
                stop_axis = axis_id_2
            elif edge_direction == "a2_to_a1":
                start_axis = axis_id_2
                stop_axis = axis_id_1

            start = (
                pd.DataFrame(np.c_[connections[:, 0], np.arange(connections.shape[0])])
                .merge(
                    self.axes[start_axis].node_placements,
                    left_on=0,
                    right_on="unique_id",
                    how="left",
                )
                .sort_values(1)
                .drop(columns=[0, 1, "unique_id"])
                .values
            )

            stop = (
                pd.DataFrame(np.c_[connections[:, 1], np.arange(connections.shape[0])])
                .merge(
                    self.axes[stop_axis].node_placements,
                    left_on=0,
                    right_on="unique_id",
                    how="left",
                )
                .sort_values(1)
                .drop(columns=[0, 1, "unique_id"])
                .values
            )

            start_arr = start[:, :2]
            end_arr = stop[:, :2]

            # we only want one rho for the start, stop pair (using the mean rho)
            control_rho = (start[:, 2] + stop[:, 2]) / 2

            # all interactions between same two axes, so only one angle
            angles = [self.axes[axis_id_1].angle, self.axes[axis_id_2].angle]
            angle_diff = angles[1] - angles[0]

            # make sure we take the short arc if requested
            if short_arc:
                if np.abs(angle_diff) > 180:
                    # flip the direction in this case and angle between is now "360 minus"
                    control_angle = (
                        angles[0]
                        + -1 * np.sign(angle_diff) * (360 - np.abs(angle_diff)) / 2
                    )
                else:
                    control_angle = angles[0] + angle_diff / 2
            # long arc
            else:
                if np.abs(angle_diff) <= 180:
                    # flip the direction in this case and angle between is now "360 minus"
                    control_angle = (
                        angles[0]
                        + -1 * np.sign(angle_diff) * (360 - np.abs(angle_diff)) / 2
                    )
                else:
                    control_angle = angles[0] + angle_diff / 2

            control_cartesian = polar2cartesian(control_rho, control_angle)
            bezier_output = np.column_stack(
                [
                    bezier_all(
                        start_arr=start_arr[:, i],
                        end_arr=end_arr[:, i],
                        control_arr=control_cartesian[i],
                        num_steps=num_steps,
                    )
                    for i in range(2)
                ]
            )

            # put `np.nan` spacers in
            bezier_output = np.insert(
                arr=bezier_output,
                obj=np.arange(bezier_output.shape[0], step=num_steps) + num_steps,
                values=np.nan,
                axis=0,
            )

            # store the output in the right place(s)
            if edge_direction == "a1_to_a2":
                self.edges[axis_id_1][axis_id_2][a1_to_a2_tag]["curves"] = bezier_output

            elif edge_direction == "a2_to_a1":
                self.edges[axis_id_2][axis_id_1][a2_to_a1_tag]["curves"] = bezier_output

        return None

    def construct_curves(self, num_steps: int = 100, short_arc: bool = True):
        """
        Construct Bézier curves for any connections for which we've specified the edges to draw.

        (e.g. ``HivePlot.edges[axis_0][axis_1][<tag>]["ids"]`` is non-empty but
        ``HivePlot.edges[axis_0][axis_1][<tag>]["curves"]`` does not yet exist).

        .. note::
            Checks all <tag> values between axes.

        :param num_steps: number of points sampled along a given Bézier curve. Larger numbers will result in
            smoother curves when plotting later, but slower rendering.
        :param short_arc: whether to take the shorter angle arc (``True``) or longer angle arc (``False``).
            There are always two ways to traverse between axes: with one angle being x, the other option being 360 - x.
            For most visualizations, the user should expect to traverse the "short arc," hence the default ``True``.
            For full user flexibility, however, we offer the ability to force the arc the other direction, the
            "long arc" (``short_arc=False``). Note: in the case of 2 axes 180 degrees apart, there is no "wrong" angle,
            so in this case an initial decision will be made, but switching this boolean will switch the arc to the
            other hemisphere.
        :return: ``None``.
        """
        for a0 in list(self.edges.keys()):
            for a1 in list(self.edges[a0].keys()):
                for tag in list(self.edges[a0][a1].keys()):
                    if (
                        "ids" in self.edges[a0][a1][tag]
                        and "curves" not in self.edges[a0][a1][tag]
                    ):
                        self.add_edge_curves_between_axes(
                            axis_id_1=a0,
                            axis_id_2=a1,
                            a2_to_a1=False,
                            tag=tag,
                            num_steps=num_steps,
                            short_arc=short_arc,
                        )
        return None

    def add_edge_kwargs(
        self,
        axis_id_1: Hashable,
        axis_id_2: Hashable,
        tag: Optional[Hashable] = None,
        a1_to_a2: bool = True,
        a2_to_a1: bool = True,
        **edge_kwargs,
    ):
        """
        Add edge kwargs to the constructed ``HivePlot.edges`` between two axes of a ``HivePlot``.

        For a given set of edges for which edge kwargs were already set, any redundant edge kwargs specified by this
        method call will overwrite the previously set kwargs.

        Expected to have found edge IDs between the two axes before calling this method, which can be done either
        by calling ``HivePlot.connect_axes()`` method or the lower-level ``HivePlot.add_edge_ids()`` method for the two
        axes of interest.

        Resulting kwargs will be stored as a dict. This output will be stored in
        ``HivePlot.edges[axis_id_1][axis_id_2][tag]["edge_kwargs"]``.

        .. note::
            There is special handling in here for when the two provided axes have names ``"<axis_name>"`` and
            ``"<axis_name>_repeat"``. This is for use with ``hiveplotlib.hive_plot_n_axes()``, which when creating
            repeat axes always names the repeated one ``"<axis_name>_repeat"``. By definition, the edges between an axis
            and its repeat are the same, and therefore edges between these two axes should *only* be plotted in one
            direction. If one is running this method on a ``Hiveplot`` instance from ``hiveplotlib.hive_plot_n_axes()``
            though, a warning of a lack of edges in both directions for repeat edges is not productive, so we formally
            catch this case.

        :param axis_id_1: Hashable pointer to the first ``Axis`` instance in ``HivePlot.axes`` we want to add plotting
            kwargs to.
        :param axis_id_2: Hashable pointer to the second ``Axis`` instance in ``HivePlot.axes`` we want to add plotting
            kwargs to.
        :param tag: which subset of curves to modify kwargs for.
            Note, if no tag is specified (e.g. ``tag=None``), it is presumed there is only one tag for the specified
            set of axes to look over and that will be inferred. If no tag is specified and there are multiple tags to
            choose from, a ``ValueError`` will be raised.
        :param a1_to_a2: whether to add kwargs for connections going FROM ``axis_id_1`` TO ``axis_id_2``.
        :param a2_to_a1: whether to add kwargs for connections going FROM ``axis_id_2`` TO ``axis_id_1``.
        :param edge_kwargs: additional ``matplotlib`` keyword arguments that will be applied to the specified edges.
        :return: ``None``.
        """
        if tag is None:
            a1_to_a2_failure = False
            a2_to_a1_failure = False

            # special warning if repeat axes have no edges between each other
            if (
                a1_to_a2
                and a2_to_a1
                and str(axis_id_2).rstrip("_repeat") == str(axis_id_1).rstrip("_repeat")
            ):
                repeat_edges_defined = False
                if axis_id_1 in self.edges.keys():
                    if axis_id_2 in self.edges[axis_id_1].keys():
                        if len(list(self.edges[axis_id_1][axis_id_2].keys())) > 0:
                            repeat_edges_defined = True
                if axis_id_2 in self.edges.keys():
                    if axis_id_1 in self.edges[axis_id_2].keys():
                        if len(list(self.edges[axis_id_2][axis_id_1].keys())) > 0:
                            repeat_edges_defined = True
                if not repeat_edges_defined:
                    warnings.warn(
                        f"Repeat axes {axis_id_1} and {axis_id_2} have no edges."
                        "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                        "first.",
                        stacklevel=2,
                    )
            if a1_to_a2:
                if axis_id_1 in self.edges.keys():
                    if axis_id_2 not in self.edges[axis_id_1].keys():
                        # special handling for the "_repeat" axis
                        #  we check and warn with respect to repeat axes above
                        if str(axis_id_2).rstrip("_repeat") != str(axis_id_1).rstrip(
                            "_repeat"
                        ):
                            warnings.warn(
                                f"No edges exist between axes {axis_id_1} -> {axis_id_2}."
                                "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                                "first.",
                                stacklevel=2,
                            )
                        a1_to_a2 = False
                    elif len(list(self.edges[axis_id_1][axis_id_2].keys())) == 0:
                        warnings.warn(
                            f"No edges exist between axes {axis_id_1} -> {axis_id_2}."
                            "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                            "first.",
                            stacklevel=2,
                        )
                        a1_to_a2 = False

                    else:
                        a1_to_a2_tag = list(self.edges[axis_id_1][axis_id_2].keys())[0]

                        if len(list(self.edges[axis_id_1][axis_id_2].keys())) > 1:
                            a1_to_a2_failure = True
                else:
                    if str(axis_id_2).rstrip("_repeat") != str(axis_id_1).rstrip(
                        "_repeat"
                    ):
                        warnings.warn(
                            f"No edges exist between axes {axis_id_1} -> {axis_id_2}."
                            "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                            "first.",
                            stacklevel=2,
                        )
                    a1_to_a2 = False

            if a2_to_a1:
                if axis_id_2 in self.edges.keys():
                    if axis_id_1 not in self.edges[axis_id_2].keys():
                        # special handling for the "_repeat" axis
                        #  we check and warn with respect to repeat axes above
                        if str(axis_id_2).rstrip("_repeat") != str(axis_id_1).rstrip(
                            "_repeat"
                        ):
                            warnings.warn(
                                f"No edges exist between axes {axis_id_2} -> {axis_id_1}."
                                "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                                "first.",
                                stacklevel=2,
                            )
                        a2_to_a1 = False
                    elif len(list(self.edges[axis_id_2][axis_id_1].keys())) == 0:
                        warnings.warn(
                            f"No edges exist between axes {axis_id_2} -> {axis_id_1}."
                            "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                            "first.",
                            stacklevel=2,
                        )
                        a2_to_a1 = False

                    else:
                        a2_to_a1_tag = list(self.edges[axis_id_2][axis_id_1].keys())[0]

                        if len(list(self.edges[axis_id_2][axis_id_1].keys())) > 1:
                            a2_to_a1_failure = True
                else:
                    if str(axis_id_2).rstrip("_repeat") != str(axis_id_1).rstrip(
                        "_repeat"
                    ):
                        warnings.warn(
                            f"No edges exist between axes {axis_id_2} -> {axis_id_1}."
                            "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                            "first.",
                            stacklevel=2,
                        )
                    a2_to_a1 = False

            if a1_to_a2_failure and a2_to_a1_failure:
                raise ValueError(
                    "Must specify precise `tag` to handle both `a1_to_a2=True` and `a2_to_a1=True` here. "
                    "The current tags for the specified axes are:\n"
                    f"{axis_id_2} -> {axis_id_1}: {list(self.edges[axis_id_2][axis_id_1].keys())}\n"
                    f"{axis_id_2} -> {axis_id_1}: {list(self.edges[axis_id_2][axis_id_1].keys())}"
                )
            elif a1_to_a2_failure:
                raise ValueError(
                    "Must specify precise `tag` to handle `a1_to_a2=True` here. "
                    "The current tags for the specified axes are:\n"
                    f"{axis_id_1} -> {axis_id_2}: {list(self.edges[axis_id_1][axis_id_2].keys())}"
                )
            elif a2_to_a1_failure:
                raise ValueError(
                    "Must specify precise `tag` to handle `a2_to_a1=True` here. "
                    "The current tags for the specified axes are:\n"
                    f"{axis_id_2} -> {axis_id_1}: {list(self.edges[axis_id_2][axis_id_1].keys())}"
                )

        else:
            a1_to_a2_tag = tag
            a2_to_a1_tag = tag

        axes = []
        tags = []
        if a1_to_a2:
            try:
                if "ids" in self.edges[axis_id_1][axis_id_2][a1_to_a2_tag]:
                    axes.append([axis_id_1, axis_id_2])
                    tags.append(a1_to_a2_tag)
            except KeyError:
                raise KeyError(
                    f"`self.edges[{axis_id_1}][{axis_id_2}][{a1_to_a2_tag}]['ids']` does not appear to exist. "
                    "It is expected you have run `HivePlot.connect_axes()` or `HivePlot.add_edge_ids()` first "
                    "for the two axes of interest with a specified tag."
                )
        if a2_to_a1:
            try:
                if "ids" in self.edges[axis_id_2][axis_id_1][a2_to_a1_tag]:
                    axes.append([axis_id_2, axis_id_1])
                    tags.append(a2_to_a1_tag)
            except KeyError:
                raise KeyError(
                    f"`self.edges[{axis_id_2}][{axis_id_1}][{a2_to_a1_tag}]['ids']` does not appear to exist. "
                    "It is expected you have run `HivePlot.connect_axes()` or `HivePlot.add_edge_ids()` first "
                    "for the two axes of interest with a specified tag."
                )
        # store the kwargs
        for [a1, a2], t in zip(axes, tags):
            # being sure to include existing kwargs
            if "edge_kwargs" in self.edges[a1][a2][t].keys():
                for k in list(self.edges[a1][a2][t]["edge_kwargs"]):
                    if k not in edge_kwargs.keys():
                        edge_kwargs[k] = self.edges[a1][a2][t]["edge_kwargs"][k]

            self.edges[a1][a2][t]["edge_kwargs"] = edge_kwargs

        return None

    def connect_axes(
        self,
        edges: np.ndarray,
        axis_id_1: Hashable,
        axis_id_2: Hashable,
        tag: Optional[Hashable] = None,
        a1_to_a2: bool = True,
        a2_to_a1: bool = True,
        num_steps: int = 100,
        short_arc: bool = True,
        **edge_kwargs,
    ) -> Hashable:
        """
        Construct all the curves and set all the curve kwargs between ``axis_id_1`` and ``axis_id_2``.

        Based on the specified ``edges`` parameter, build out the resulting Bézier curves, and set any kwargs for those
        edges for later visualization.

        The curves will be tracked by a unique ``tag``, and the resulting constructions will be stored in
        ``HivePlot.edges[axis_id_1][axis_id_2][tag]`` if ``a1_to_a2`` is ``True`` and
        ``HivePlot.edges[axis_id_2][axis_id_1][tag]`` if ``a2_to_a1`` is ``True``.

        .. note::
            If trying to draw different subsets of edges with different kwargs, one can run this method multiple times
            with different subsets of the entire edges array, providing unique ``tag`` values with each subset of
            ``edges``, and specifying different ``edge_kwargs`` each time. The resulting ``HivePlot`` instance would be
            plotted showing each set of edges styled with each set of unique kwargs.

        .. note::
            You can choose to construct edges in only one of either directions by specifying `a1_to_a2` or `a2_to_a1`
            as False (both are True by default).

        :param edges: ``(n, 2)`` array of ``Hashable`` values representing pointers to specific ``Node`` instances.
            The first column is the "from" and the second column is the "to" for each connection.
        :param axis_id_1: Hashable pointer to the first ``Axis`` instance in ``HivePlot.axes`` we want to find
            connections between.
        :param axis_id_2: Hashable pointer to the second ``Axis`` instance in ``HivePlot.axes`` we want to find
            connections between.
        :param tag: tag corresponding to specified ``edges``. If ``None`` is provided, the tag will be set as
            the lowest unused integer starting at ``0`` amongst the available tags under
            ``HivePlot.edges[from_axis_id][to_axis_id]`` and / or ``HivePlot.edges[to_axis_id][from_axis_id]``.
        :param a1_to_a2: whether to find and build the connections going FROM ``axis_id_1`` TO ``axis_id_2``.
        :param a2_to_a1: whether to find and build the connections going FROM ``axis_id_2`` TO ``axis_id_1``.
        :param num_steps: number of points sampled along a given Bézier curve. Larger numbers will result in
            smoother curves when plotting later, but slower rendering.
        :param short_arc: whether to take the shorter angle arc (``True``) or longer angle arc (``False``).
            There are always two ways to traverse between axes: with one angle being x, the other option being 360 - x.
            For most visualizations, the user should expect to traverse the "short arc," hence the default ``True``.
            For full user flexibility, however, we offer the ability to force the arc the other direction, the
            "long arc" (``short_arc=False``). Note: in the case of 2 axes 180 degrees apart, there is no "wrong" angle,
            so in this case an initial decision will be made, but switching this boolean will switch the arc to the
            other hemisphere.
        :param edge_kwargs: additional ``matplotlib`` params that will be applied to the related edges.
        :return: ``Hashable`` tag that identifies the generated curves and kwargs.
        """
        # if `tag` is `None`, will be relevant to store the new tag, otherwise `new_tag` will just be the same as `tag`
        new_tag = self.add_edge_ids(
            edges=edges,
            tag=tag,
            axis_id_1=axis_id_1,
            axis_id_2=axis_id_2,
            a1_to_a2=a1_to_a2,
            a2_to_a1=a2_to_a1,
        )

        self.add_edge_curves_between_axes(
            axis_id_1=axis_id_1,
            axis_id_2=axis_id_2,
            tag=new_tag,
            a1_to_a2=a1_to_a2,
            a2_to_a1=a2_to_a1,
            num_steps=num_steps,
            short_arc=short_arc,
        )

        self.add_edge_kwargs(
            axis_id_1=axis_id_1,
            axis_id_2=axis_id_2,
            tag=new_tag,
            a1_to_a2=a1_to_a2,
            a2_to_a1=a2_to_a1,
            **edge_kwargs,
        )

        return new_tag

    def copy(self) -> "HivePlot":
        """
        Return a copy of the ``HivePlot`` instance.

        :return: ``HivePlot`` instance.
        """
        return deepcopy(self)

    def to_json(self, deprecated_version: bool = False) -> str:
        """
        Return the information from the axes, nodes, and edges in Cartesian space as a serialized JSON string.

        This allows users to visualize hive plots with arbitrary libraries, even outside of python.

        The dictionary structure of the resulting JSON will consist of two top-level keys:

        "axes" - contains the information for plotting each axis, plus the nodes on each axis in Cartesian space.

        "edges" - contains the information for plotting the discretized edges in Cartesian space, plus the corresponding
        *to* and *from* IDs that go with each edge, as well as any kwargs that were set for plotting each set of edges.

        :param deprecated_version: whether to use the deprecating version of JSON output or not. To be deleted in
            version ``0.24.0``.
        :return: JSON output of axis, node, and edge information.
        """
        # axis endpoints and node placements (both in Cartesian space).
        axis_node_dict = dict()

        for axis in self.axes:
            # endpoints of axis in Cartesian space
            start, end = self.axes[axis].start, self.axes[axis].end

            temp_dict = dict(
                start=start,
                end=end,
                nodes=self.axes[axis]
                .node_placements.loc[:, ["unique_id", "x", "y"]]
                .to_dict(orient="list"),
            )
            axis_node_dict[axis] = temp_dict

        edge_info = deepcopy(self.edges)

        # edge ids, discretized curves (in Cartesian space), and kwargs
        for e1 in edge_info:
            for e2 in edge_info[e1]:
                for tag in edge_info[e1][e2]:
                    for i in ["ids", "curves"]:
                        # curves have nan values, must revise to `None` then coax to list
                        if i == "curves":
                            if deprecated_version:  # noqa: F401 # pragma: no cover
                                warnings.warn(
                                    "This output structure for the 'curves' key will be deleted in "
                                    "Hiveplotlib v0.24.0. To switch to the changing version, run "
                                    "``HivePlot.to_json(deprecated_version=False)``\nNote this version is "
                                    "not D3-compatible either.",
                                    category=DeprecationWarning,
                                    stacklevel=2,
                                )
                                arr = edge_info[e1][e2][tag][i]
                                temp = arr.astype("O")
                                temp[np.where(np.isnan(arr))] = None
                                edge_info[e1][e2][tag][i] = temp.tolist()
                            else:
                                arr = edge_info[e1][e2][tag][i]
                                split_arrays = np.split(
                                    arr, np.where(np.isnan(arr[:, 0]))[0]
                                )
                                # be sure to drop the extra array at the end that is just a NaN value
                                split_arrays_str = [
                                    arr[~np.isnan(arr[:, 0]), :].astype("O")
                                    for arr in split_arrays
                                ][:-1]
                                split_arrays_list = [
                                    arr.tolist() for arr in split_arrays_str
                                ]
                                edge_info[e1][e2][tag][i] = split_arrays_list
                        # ids don't have nan values, can be converted to list right away
                        elif i == "ids":
                            edge_info[e1][e2][tag][i] = edge_info[e1][e2][tag][
                                i
                            ].tolist()

        collated_output = dict(axes=axis_node_dict, edges=edge_info)

        return json.dumps(collated_output)


def hive_plot_n_axes(
    node_list: List[Node],
    edges: Union[np.ndarray, List[np.ndarray]],
    axes_assignments: List[List[Union[Hashable, None]]],
    sorting_variables: List[Hashable],
    axes_names: Optional[List[Hashable]] = None,
    repeat_axes: Optional[List[bool]] = None,
    vmins: Optional[List[float]] = None,
    vmaxes: Optional[List[float]] = None,
    angle_between_repeat_axes: float = 40,
    orient_angle: float = 0,
    all_edge_kwargs: Optional[Dict] = None,
    edge_list_kwargs: Optional[List[Dict]] = None,
    cw_edge_kwargs: Optional[Dict] = None,
    ccw_edge_kwargs: Optional[Dict] = None,
    repeat_edge_kwargs: Optional[Dict] = None,
) -> HivePlot:
    """
    Generate a ``HivePlot`` Instance with an arbitrary number of axes, as specified by passing a partition of node IDs.

    Repeat axes can be generated for any desired subset of axes, but repeat axes will be sorted by the same variable
    as the original axis.

    Axes will be added in counterclockwise order.

    Axes will all be the same length and position from the origin.

    Changes to all the edge kwargs can be affected with the ``all_edge_kwargs`` parameter. If providing multiple sets
    of edges (e.g. a ``list`` input for the ``edges`` parameter), one can also provide unique kwargs for each set of
    edges by specifying a corresponding ``list`` of kwargs with the ``edge_list_kwargs`` parameter.

    Edges directed counterclockwise will be drawn as solid lines by default. Clockwise edges will be drawn as solid
    lines by default. All CW / CCW lines kwargs can be changed with the ``cw_edge_kwargs`` and ``ccw_edge_kwargs``
    parameters, respectively. Edges between repeat axes will be drawn as solid lines by default. Repeat edges operate
    under their own set of visual kwargs (``repeat_edge_kwargs``) as clockwise vs counterclockwise edges don't have much
    meaning when looking within a single group.

    Specific edge kwargs can also be changed by running the ``add_edge_kwargs()`` method on the resulting ``HivePlot``
    instance, where the specified ``tag`` of ``edges`` to change will be the index value in the list of
    lists in ``edges`` (note: a tag is only necessary if the ``indices`` input is a list of lists, otherwise there
    would only be a single tag of edges, which can be inferred).

    There is a hierarchy to these various kwarg arguments. That is, if redundant / overlapping kwargs are provided for
    different kwarg parameters, a warning will be raised and priority will be given according to the below hierarchy
    (Note: ``cw_edge_kwargs, ``ccw_edge_kwargs``, and ``repeat_edge_kwargs`` do not interact with each other in
    practice, and are therefore equal in the hierarchy):

    ``edge_list_kwargs`` > ``cw_edge_kwargs`` / ``ccw_edge_kwargs`` / ``repeat_edge_kwargs`` > ``all_edge_kwargs``.

    :param node_list: List of ``Node`` instances to go into output ``HivePlot`` instance.
    :param edges: ``(n, 2)`` array of ``Hashable`` values representing pointers to specific ``Node`` instances.
        The first column is the "from" and the second column is the "to" for each connection.
        Alternatively, one can provide a list of two-column arrays, which will allow for plotting different sets of
        edges with different kwargs.
    :param axes_assignments: list of lists of node unique IDs. Each list of node IDs will be assigned to a separate axis
        in the resulting ``HivePlot`` instance, built out in counterclockwise order. If ``None`` is provided as one of
        the elements instead of a list of node IDs, then all unassigned nodes will be aggregated onto this axis.
    :param sorting_variables: list of ``Hashable`` variables on which to sort each axis, where the ith index
        ``Hashable`` corresponds to the ith index list of nodes in ``axes_assignments`` (e.g. the ith axis of the
        resulting ``HivePlot``).
    :param axes_names: list of ``Hashable`` names for each axis, where the ith index ``Hashable`` corresponds to the ith
        index list of nodes in ``axes_assignments`` (e.g. the ith axis of the resulting ``HivePlot``). Default ``None``
        names the groups as "Group 1," "Group 2," etc.
    :param repeat_axes: list of ``bool`` values of whether to generate a repeat axis, where the ith index bool
        corresponds to the ith index list of nodes in ``axes_assignments`` (e.g. the ith axis of the resulting
        ``HivePlot``). A ``True`` value generates a repeat axis. Default ``None`` assumes no repeat axes (e.g. all
        ``False``).
    :param vmins: list of ``float`` values (or ``None`` values) specifying the vmin for each axis, where the ith index
        value corresponds to the ith index list of nodes in ``axes_assignments`` (e.g. the ith axis of the resulting
        ``HivePlot``). A ``None`` value infers the global min for that axis. Default ``None`` uses the global min for
        all the axes.
    :param vmaxes: list of ``float`` values (or ``None`` values) specifying the vmax for each axis, where the ith index
        value corresponds to the ith index list of nodes in ``axes_assignments`` (e.g. the ith axis of the resulting
        ``HivePlot``). A ``None`` value infers the global max for that axis. Default ``None`` uses the global max for
        all the axes.
    :param angle_between_repeat_axes: angle between repeat axes. Default 40 degrees.
    :param orient_angle: rotates all axes counterclockwise from their initial angles (default 0 degrees).
    :param all_edge_kwargs: kwargs for all edges. Default ``None`` specifies no additional kwargs.
    :param edge_list_kwargs: list of dictionaries of kwargs for each element of ``edges`` when ``edges`` is a ``list``.
        The ith set of kwargs in ``edge_list_kwargs`` will only be applied to edges constructed from the ith element of
        ``edges``. Default ``None`` provides no additional kwargs. Note, list must be same length as ``edges``.
    :param cw_edge_kwargs: kwargs for edges going clockwise. Default ``None`` specifies a solid line.
    :param ccw_edge_kwargs: kwargs for edges going counterclockwise. Default ``None`` specifies a solid line.
    :param repeat_edge_kwargs: kwargs for edges between repeat axes. Default ``None`` specifies a solid line.
    :return: ``HivePlot`` instance.
    """
    # make sure kwarg arguments are correct
    if all_edge_kwargs is None:
        all_edge_kwargs = dict()

    if isinstance(edges, list):
        if edge_list_kwargs is not None:
            assert len(edges) == len(edge_list_kwargs), (
                f"Must provide same number of sets of edges (currently len(edges) = {len(edges)}) as edge kwargs"
                f"(currently len(edge_list_kwargs) = {len(edge_list_kwargs)}"
            )
            for idx, k in enumerate(edge_list_kwargs):
                if k is None:
                    edge_list_kwargs[idx] = dict()
        else:
            edge_list_kwargs = [dict() for _ in edges]
    else:
        edge_list_kwargs = [dict()]

    if cw_edge_kwargs is None:
        cw_edge_kwargs = dict()
    if ccw_edge_kwargs is None:
        ccw_edge_kwargs = dict()
    if repeat_edge_kwargs is None:
        repeat_edge_kwargs = dict()
    # make sure specified instructions match the number of specified axes
    assert len(axes_assignments) == len(sorting_variables), (
        "Must specify a sorting variable (`sorting_variables`) for every axis (`axes_assignments`). "
        f"Currently have {len(sorting_variables)} sorting variables and {len(axes_assignments)} axes assignments."
    )

    if axes_names is not None:
        assert len(axes_assignments) == len(axes_names), (
            "Must specify a axis name (`axes_names`) for every axis (`axes_assignments`). "
            f"Currently have {len(axes_names)} axes names and {len(axes_assignments)} axes assignments."
        )

    else:
        axes_names = [f"Group {i + 1}" for i in range(len(axes_assignments))]

    if repeat_axes is not None:
        assert len(axes_assignments) == len(repeat_axes), (
            "Must specify a repeat axis (`repeat_axes`) for every axis (`axes_assignments`). "
            f"Currently have {len(repeat_axes)} repeat axes specified and {len(axes_assignments)} axes assignments."
        )
    else:
        repeat_axes = [False] * len(axes_assignments)

    if vmins is not None:
        assert len(axes_assignments) == len(vmins), (
            "Must specify a vmin (`vmins`) for every axis (`axes_assignments`). "
            f"Currently have {len(vmins)} vmins specified and {len(axes_assignments)} axes assignments."
        )
    else:
        vmins = [None] * len(axes_assignments)

    if vmaxes is not None:
        assert len(axes_assignments) == len(vmaxes), (
            "Must specify a vmax (`vmaxes`) for every axis (`axes_assignments`). "
            f"Currently have {len(vmaxes)} vmaxes specified and {len(axes_assignments)} axes assignments."
        )
    else:
        vmaxes = [None] * len(axes_assignments)

    hp = HivePlot()
    hp.add_nodes(nodes=node_list)

    # space out axes evenly
    spacing = 360 / len(axes_assignments)

    if spacing <= angle_between_repeat_axes:
        warnings.warn(
            f"Your angle between repeat axes ({angle_between_repeat_axes}) is going to cause repeat axes to cross "
            "past other axes, which will lead to overlapping edges in the final Hive Plot visualization. "
            f"To space out axes equally, they are {spacing} degrees apart. "
            "We recommend setting a lower value for `angle_between_repeat_axes`.",
            stacklevel=2,
        )

    # if we get a `None` axis assignment, assign those nodes to be the diff of all node IDs minus the assigned nodes
    none_in_axes_assignments = False
    for a in axes_assignments:
        if a is None:
            none_in_axes_assignments = True
    if none_in_axes_assignments:
        all_node_ids = [i.unique_id for i in node_list]
        nodes_placed = []
        for nlist in axes_assignments:
            if nlist is not None:
                nodes_placed += list(nlist)

        none_axes_assignment = list(set(all_node_ids).difference(nodes_placed))
        for i, nlist in enumerate(axes_assignments):
            if nlist is None:
                axes_assignments[i] = none_axes_assignment

    for i, assignment in enumerate(axes_assignments):
        angle = spacing * i
        sorting_variable = sorting_variables[i]
        axis_name = axes_names[i]
        repeat_axis = repeat_axes[i]
        vmin = vmins[i]
        vmax = vmaxes[i]

        # add axis / axes
        if not repeat_axis:
            temp_axis = Axis(
                axis_id=axis_name, start=1, end=5, angle=angle + orient_angle
            )
            hp.add_axes([temp_axis])
        else:
            # space out on either side of the well-spaced angle
            temp_axis = Axis(
                axis_id=axis_name,
                start=1,
                end=5,
                angle=angle - angle_between_repeat_axes / 2 + orient_angle,
            )
            temp_axis_repeat = Axis(
                axis_id=f"{axis_name}_repeat",
                start=1,
                end=5,
                angle=angle + angle_between_repeat_axes / 2 + orient_angle,
                long_name=axis_name,
            )
            hp.add_axes([temp_axis, temp_axis_repeat])

        # place nodes on the axis / axes
        hp.place_nodes_on_axis(
            axis_id=axis_name,
            unique_ids=assignment,
            sorting_feature_to_use=sorting_variable,
            vmin=vmin,
            vmax=vmax,
        )
        # also place values on the repeat axis if we have one
        if repeat_axis:
            hp.place_nodes_on_axis(
                axis_id=f"{axis_name}_repeat",
                unique_ids=assignment,
                sorting_feature_to_use=sorting_variable,
                vmin=vmin,
                vmax=vmax,
            )

    # add in edges
    if not isinstance(edges, list):
        edges = [edges]
    for i, axis_name in enumerate(axes_names):
        first_axis_name = axis_name

        # figure out next axis to connect to
        if i != len(axes_names) - 1:
            next_axis_name = axes_names[i + 1]
        # circle back to first axis
        else:
            next_axis_name = axes_names[0]

        # repeat axis kwarg handling and connecting
        if repeat_axes[i]:
            for idx, e in enumerate(edges):
                # gather kwargs according to hierarchy
                collated_kwargs = edge_list_kwargs[idx].copy()
                for k in list(repeat_edge_kwargs.keys()):
                    if k in collated_kwargs.keys():
                        warnings.warn(
                            f"Specified kwarg {k} in `repeat_edge_kwargs` but already set as kwarg for "
                            f"edge set index {idx} with `edge_list_kwargs`. Preserving kwargs in `edge_list_kwargs`",
                            stacklevel=2,
                        )
                    else:
                        collated_kwargs[k] = repeat_edge_kwargs[k]
                for k in list(all_edge_kwargs.keys()):
                    if k in collated_kwargs.keys():
                        warnings.warn(
                            f"Specified kwarg {k} in `all_edge_kwargs` but already set as kwarg for "
                            f"edge set index {idx} with `edge_list_kwargs` or `repeat_edge_kwargs`. "
                            f"Disregarding `all_edge_kwargs` here.",
                            stacklevel=2,
                        )
                    else:
                        collated_kwargs[k] = all_edge_kwargs[k]

                # add repeat axis edges (only in ccw direction) if we have a repeat axis
                hp.connect_axes(
                    edges=e,
                    axis_id_1=first_axis_name,
                    axis_id_2=f"{first_axis_name}_repeat",
                    a2_to_a1=False,
                    **collated_kwargs,
                )
                # the following intergroup edges will instead come off of the repeat edge
            first_axis_name += "_repeat"

        for idx, e in enumerate(edges):
            # gather kwargs according to hierarchy
            collated_kwargs_cw = edge_list_kwargs[idx].copy()
            for k in list(cw_edge_kwargs.keys()):
                if k in collated_kwargs_cw.keys():
                    warnings.warn(
                        f"Specified kwarg {k} in `cw_edge_kwargs` but already set as kwarg for "
                        f"edge set index {idx} with `edge_list_kwargs`. Preserving kwargs in `edge_list_kwargs`",
                        stacklevel=2,
                    )
                else:
                    collated_kwargs_cw[k] = cw_edge_kwargs[k]
            for k in list(all_edge_kwargs.keys()):
                if k in collated_kwargs_cw.keys():
                    warnings.warn(
                        f"Specified kwarg {k} in `all_edge_kwargs` but already set as kwarg for "
                        f"edge set index {idx} with `edge_list_kwargs` or `cw_edge_kwargs`. "
                        f"Disregarding `all_edge_kwargs` here.",
                        stacklevel=2,
                    )
                else:
                    collated_kwargs_cw[k] = all_edge_kwargs[k]

            hp.connect_axes(
                edges=e,
                axis_id_1=first_axis_name,
                axis_id_2=next_axis_name,
                a1_to_a2=False,
                **collated_kwargs_cw,
            )

            # gather kwargs according to hierarchy
            collated_kwargs_ccw = edge_list_kwargs[idx].copy()
            for k in list(ccw_edge_kwargs.keys()):
                if k in collated_kwargs_ccw.keys():
                    warnings.warn(
                        f"Specified kwarg {k} in `ccw_edge_kwargs` but already set as kwarg for "
                        f"edge set index {idx} with `edge_list_kwargs`. Preserving kwargs in `edge_list_kwargs`",
                        stacklevel=2,
                    )
                else:
                    collated_kwargs_ccw[k] = ccw_edge_kwargs[k]
            for k in list(all_edge_kwargs.keys()):
                if k in collated_kwargs_ccw.keys():
                    warnings.warn(
                        f"Specified kwarg {k} in `all_edge_kwargs` but already set as kwarg for "
                        f"edge set index {idx} with `edge_list_kwargs` or `ccw_edge_kwargs."
                        f"Disregarding `all_edge_kwargs` here.",
                        stacklevel=2,
                    )
                else:
                    collated_kwargs_ccw[k] = all_edge_kwargs[k]

            hp.connect_axes(
                edges=e,
                axis_id_1=first_axis_name,
                axis_id_2=next_axis_name,
                a2_to_a1=False,
                **collated_kwargs_ccw,
            )

    return hp
