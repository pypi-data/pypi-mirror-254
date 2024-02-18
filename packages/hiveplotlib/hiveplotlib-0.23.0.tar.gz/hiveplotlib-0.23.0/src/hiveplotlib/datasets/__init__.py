# datasets.py

"""
Quick example datasets for use in ``hiveplotlib``.

For Hive Plots, many excellent network datasets are available online, including many graphs that can be generated using
`networkx <https://networkx.org/documentation/stable/reference/generators.html>`_ and
`pytorch-geometric <https://pytorch-geometric.readthedocs.io/en/latest/notes/data_cheatsheet.html#>`_.
The `Stanford Large Network Dataset Collection <https://snap.stanford.edu/data/>`_ is also a great general source of
network datasets. If working with ``networkx`` graphs,
users can also take advantage of the ``hiveplotlib.converters.networkx_to_nodes_edges()`` method to quickly get those
graphs into a ``hiveplotlib``-ready format.

For Polar Parallel Coordinates Plots (P2CPs), many datasets are available through packages including
`statsmodels <https://www.statsmodels.org/stable/datasets/index.html>`_ and
`scikit-learn <https://scikit-learn.org/stable/datasets.html>`_.
"""

import json
import numpy as np
from hiveplotlib import hive_plot_n_axes, HivePlot, Node
import pandas as pd
from pathlib import Path
from typing import Dict, Optional, Tuple, Union


def international_trade_data(
    year: int = 2019, hs92_code: int = 8112, path: Optional[Union[str, Path]] = None
) -> Tuple[pd.DataFrame, Dict]:
    """
    Read in international trade data network from the Harvard Growth Lab.

    .. note::
        Only a limited number of subsets of the data are shipped with ``hiveplotlib``, as each year of trade data is
        roughly 300mb. However, the raw data are available at the
        `Harvard Growth Lab's website <https://doi.org/10.7910/DVN/T4CHWJ>`_, and the runner to produce the necessary
        files to use this reader function is available in the
        `repository <https://gitlab.com/geomdata/hiveplotlib/-/blob/master/runners/make_trade_network_dataset.py>`_
        (``make_trade_network_dataset.py``).

        If you are using the runner to make your own trade datasets that you will read in locally with this
        function, then you will need to specify the local ``path`` accordingly.

    :param year: which year of data to pull. If the year of data is not available, an error will be raised.
    :param hs92_code: which HS 92 code of export data to pull. If the code requested is not available, an error will
        be raised. There are different numbers of digits (e.g. 2, 4), where more digits leads to more specificity of
        trade group. For a reference to what trade groups these codes correspond to, see
        `this resource <https://dataweb.usitc.gov/classification/commodity-description/HTS/4>`_.
    :param path: directory containing both the data and metadata for loading. Default ``None`` assumes you are using one
        of the datasets shipped with ``hiveplotlib``. If you are using the ``make_trade_network_dataset.py``
        runner discussed above to make your own datasets, then you will need to specify the path to the directory where
        you saved both the data and metadata files (which must be in the same directory).
    :return: ``pandas.DataFrame`` of trade data, dictionary of metadata explaining meaning of data's columns,
        data provenance, citations, etc.
    :raises: ``AssertionError`` if the requested files cannot be found.
    """
    # path when grabbing files shipped with hiveplotlib
    internal_path = Path(__path__[0]).joinpath("trade_data_harvard_growth_lab")

    if path is None:
        path = internal_path
    else:
        path = Path(path)

    # grab the shipped year, hs92 values to present what's available on failure
    csv_files = [
        i.stem for i in sorted(internal_path.glob("international_exports*.csv"))
    ]
    csv_years = [i.split("_")[2] for i in csv_files]
    csv_hs92 = [i.split("_")[-1] for i in csv_files]
    hiveplotlib_supported_values = pd.DataFrame(
        np.c_[csv_years, csv_hs92], columns=["Year", "Trade Code"]
    )

    # check that our implied data and metadata files exist
    data_path = path.joinpath(f"international_exports_{year}_{hs92_code}.csv")
    metadata_path = path.joinpath(
        f"international_exports_metadata_{year}_{hs92_code}.json"
    )
    assert data_path.exists() and metadata_path.exists(), (
        f"Could not find data and / or metadata under specified `path`. If you specified your own path, double check "
        f"that the path is correct. Your file names should be "
        f"If you are using `hiveplotlib` supported data, note that only the following `year`, "
        f"`hs29_code` values are supported:\n{hiveplotlib_supported_values}"
    )

    data = pd.read_csv(data_path)
    with open(metadata_path, "r") as openfile:
        metadata = json.load(openfile)

    return data, metadata


def four_gaussian_blobs_3d(
    num_points: int = 50, noise: float = 0.5, random_seed: int = 0
) -> pd.DataFrame:
    """
    Generate a ``pandas`` dataframe of four Gaussian blobs in 3d.

    This dataset serves as a simple example for showing 3d viz using Polar Parallel Coordinates Plots (P2CPs) instead
    of 3d plotting.

    :param num_points: number of points in each blob.
    :param noise: noisiness of Gaussian blobs.
    :param random_seed: random seed to generate consistent data between calls.
    :return: ``(num_points * 4, 4)`` ``pd.DataFrame`` of X, Y, Z, and blob labels.
    """
    # dimension of data (e.g. 3 => 3d data)
    dim = 3

    # keeping a subset of the corner blobs to plot
    corners_to_keep = [0, 1, 2, 4]

    # name of the features we will create for each set of data generated below
    feature_names = ["X", "Y", "Z", "Label"]

    # set seed for consistent data
    rng = np.random.default_rng(random_seed)

    # build list of arrays of Gaussian blobs at each corner of a cube
    b_list = []
    coords = []
    for i in [0, 5]:
        for j in [0, 5]:
            for k in [0, 5]:
                b = rng.normal(scale=noise, size=num_points * dim).reshape(
                    num_points, dim
                )
                b[:, 0] += i
                b[:, 1] += j
                b[:, 2] += k
                b = np.c_[b, np.repeat(len(b_list), b.shape[0])]
                b_list.append(b)
                coords.append((i, j, k))

    # put our 4 blobs of interest into a single dataframe
    df = pd.DataFrame(
        np.row_stack([b_list[i] for i in corners_to_keep]), columns=feature_names
    )

    # make the labels ints
    df.Label = df.Label.astype(int)
    # replace the 4s with 3s so our labels are just range(4)
    df.Label.values[df.Label.values == 4] = 3

    return df


def example_hive_plot(
    num_nodes: int = 15,
    num_edges: int = 30,
    seed: int = 0,
    **hive_plot_n_axes_kwargs,
) -> HivePlot:
    """
    Generate example hive plot with ``"Low"``, ``"Medium"``, and ``"High"`` axes (plus repeat axes).

    Nodes and edges will be generated and placed randomly.

    :param num_nodes: number of nodes to generate.
    :param num_edges: number of edges to generate.
    :param seed: random seed to use when generating nodes and edges.
    :param hive_plot_n_axes_kwargs: additional keyword arguments for the underlying
        :py:func:`hiveplotlib.hive_plot.hive_plot_n_axes()` call.
    :return: resulting ``HivePlot`` instance.
    """
    color_dict = {
        "Low": {"Low_repeat": "#006BA4", "High_repeat": "#FF800E"},
        "High": {"Medium_repeat": "#ABABAB", "High_repeat": "#595959"},
        "Medium": {"Medium_repeat": "#5F9ED1", "Low_repeat": "#C85200"},
        "Low_repeat": {"Low": "#006BA4", "Medium": "#C85200"},
        "Medium_repeat": {"Medium": "#5F9ED1", "High": "#ABABAB"},
        "High_repeat": {"High": "#595959", "Low": "#FF800E"},
    }

    rng = np.random.default_rng(seed)
    data = pd.DataFrame(
        np.c_[
            rng.uniform(low=0, high=10, size=num_nodes),
            rng.uniform(low=10, high=20, size=num_nodes),
            rng.uniform(low=20, high=30, size=num_nodes),
        ],
        columns=["low", "med", "high"],
    )

    # convert into dict for later use
    node_data = data.to_dict(orient="records")

    # use the dataframe's index as unique id
    node_ids = data.index.values

    nodes = [
        Node(unique_id=node_id, data=node_data[i]) for i, node_id in enumerate(node_ids)
    ]

    edges = rng.choice(node_ids, size=num_edges * 2).reshape(-1, 2)

    hp = hive_plot_n_axes(
        node_list=nodes,
        edges=edges,
        axes_assignments=[
            np.arange(num_nodes)[: num_nodes // 3],
            np.arange(num_nodes)[num_nodes // 3 : 2 * num_nodes // 3],
            np.arange(num_nodes)[2 * num_nodes // 3 :],
        ],
        sorting_variables=["low", "med", "high"],
        repeat_axes=[True, True, True],
        axes_names=["Low", "Medium", "High"],
        orient_angle=-30,
        **hive_plot_n_axes_kwargs,
    )

    # set colors according to above-defined color dictionary
    #  (so we can replicate more easily in other viz later)
    for e1 in color_dict:
        for e2 in color_dict[e1]:
            hp.add_edge_kwargs(axis_id_1=e1, axis_id_2=e2, color=color_dict[e1][e2])

    return hp
