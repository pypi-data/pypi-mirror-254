# node.py

"""
Definition of ``Node`` instance and helper static methods for generating and working with ``Node`` instances.
"""

import numpy as np
import pandas as pd
from typing import Dict, Hashable, List, Optional, Union


class Node:
    """
    ``Node`` instances hold the data for individual network node.

    Each instance is initialized with a ``unique_id`` for identification. These IDs must be ``Hashable``.
    One can also initialize with a dictionary of ``data``, but data can also be added later with the ``add_data()``
    method.

    :example:

        .. highlight:: python
        .. code-block:: python

            my_node = Node(unique_id="my_unique_node_id", data=my_dataset)

            my_second_node = Node(unique_id="my_second_unique_node_id")
            my_second_node.add_data(data=my_second_dataset)
    """

    def __init__(self, unique_id: Hashable, data: Optional[Dict] = None):
        """
        Initialize ``Node`` instance.

        :param unique_id: identifier for the instance (intended to be unique).
        :param data: dictionary of data.
        """
        self.unique_id = unique_id
        self.data = dict()
        if data is None:
            data = dict()
        self.add_data(data, overwrite_old_data=True)
        # Hashable value that points to which `Axis` instance the node is assigned to
        #  (this will point to an `Axis` instance via `HivePlot.axes[label]`)
        self.axis_label = None

    def __repr__(self) -> str:
        """
        Make printable representation (repr) for ``Node`` instance.
        """
        return f"hiveplotlib.Node {self.unique_id}"

    def add_data(self, data: Dict, overwrite_old_data: bool = False):
        """
        Add dictionary of data to ``Node.data``.

        :param data: dict of data to associate with ``Node`` instance.
        :param overwrite_old_data: whether to delete existing data dict and overwrite with ``data``. Default ``False``.
        :return: ``None``.
        """
        assert isinstance(data, dict), "`data` must be dictionary."

        if overwrite_old_data:
            self.data = data

        else:
            for k in data.keys():
                self.data[k] = data[k]

        return None


def split_nodes_on_variable(
    node_list: List[Node],
    variable_name: Hashable,
    cutoffs: Optional[Union[List[float], int]] = None,
    labels: Optional[List[Hashable]] = None,
) -> Dict[Hashable, List[Node]]:
    r"""
    Split a ``list`` of ``Node`` instances into a partition of node IDs.

    By default, splits will group node IDs on *unique values* of ``variable_name``.

    If ``variable_name`` corresponds to numerical data, and a ``list`` of ``cutoffs``
    is provided, node IDs will be separated into bins according to the following binning scheme:

    (-inf, ``cutoff[0]``], (``cutoff[0]``, ``cutoff[1]``], ... , (``cutoff[-1]``, inf]

    If ``variable_name`` corresponds to numerical data, and ``cutoffs`` is provided as an ``int``, node IDs will be
    separated into ``cutoffs`` equal-sized quantiles.

    .. note::
        This method currently only supports splits where ``variable_name`` corresponds to *numerical* data.

    :param node_list: list of ``Node`` instances to partition.
    :param variable_name: which variable in each ``Node`` instances to group by.
    :param cutoffs: cutoffs to use in binning nodes according to data under ``variable_name``. Default ``None`` will bin
        nodes by unique values of ``variable_name``. When provided as a ``list``, the specified cutoffs will bin
        according to (-inf, ``cutoffs[0]``], `(`cutoffs[0]``, ``cutoffs[1]``], ... , (``cutoffs[-1]``, inf).
        When provided as an ``int``, the exact numerical break points will be determined to create ``cutoffs``
        equally-sized quantiles.
    :param labels: labels assigned to each bin. Only referenced when ``cutoffs`` is not ``None``. Default ``None``
        labels each bin as a string based on its range of values. Note, when ``cutoffs`` is a list, ``len(labels)`` must
        be 1 greater than ``len(cutoffs)``. When ``cutoffs`` is an ``int``, ``len(labels)`` must be equal to
        ``cutoffs``.
    :return: ``dict`` whose values are lists of ``Node`` unique IDs. If ``cutoffs`` is ``None``, keys will be the unique
        values for the variable. Otherwise, each key will be the string representation of a bin range.
    """
    if cutoffs is None:
        output = dict()
        for node in node_list:
            val = node.data[variable_name]
            if val not in output.keys():
                output[val] = []

            output[val].append(node.unique_id)

        return output

    else:
        data_dict = {}
        for node in node_list:
            data_dict[node.unique_id] = node.data[variable_name]

        # int cutoffs dictates quantile cut, otherwise cut
        if not isinstance(cutoffs, int):
            if labels is not None:
                assert (
                    len(labels) == len(cutoffs) + 1
                ), "Must have 1 more label than `cutoffs` (n cutoffs => n + 1 bins)"

            bins = [-np.inf, *cutoffs, np.inf]
            # create pandas categorical array with binning information
            node_bin_cuts = pd.cut(list(data_dict.values()), bins=bins, labels=labels)
        else:
            if labels is not None:
                assert (
                    len(labels) == cutoffs
                ), "Must have 1 label per `cutoffs` (n quantiles => n labels)"

            node_bin_cuts = pd.qcut(list(data_dict.values()), q=cutoffs, labels=labels)

        # convert to np array with shape `len(node_list)` whose values are bin assignments (labels)
        node_bin_assignments = node_bin_cuts.to_numpy().astype(str)

        output = dict()
        for i, node in enumerate(node_list):
            val = node_bin_assignments[i]
            if val not in output.keys():
                output[val] = []

            output[val].append(node.unique_id)

        return output


def dataframe_to_node_list(df: pd.DataFrame, unique_id_column: Hashable) -> List[Node]:
    """
    Convert a dataframe into ``Node`` instances, where each *row* will be turned into a single instance.

    :param df: dataframe to use to generate ``Node`` instances.
    :param unique_id_column: which column corresponds to unique IDs for the eventual nodes.
    :return: list of ``Node`` instances.
    """
    assert (
        df[unique_id_column].values.size == np.unique(df[unique_id_column].values).size
    ), "Param `unique_id_column` contains non-unique values, cannot be used as unique IDs for nodes"

    additional_data = df.drop(columns=unique_id_column).to_dict(orient="records")

    node_list = [
        Node(unique_id=val, data=additional_data[i])
        for i, val in enumerate(df[unique_id_column].values)
    ]

    return node_list
