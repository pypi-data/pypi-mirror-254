# base.py

"""
Base (viz back-end-agnostic) functionality for visualizations in ``hiveplotlib``.
"""

from hiveplotlib import Axis
from typing import Literal, Tuple


def get_axis_label_alignment(
    axis: Axis,
    backend: Literal = ["matplotlib", "bokeh", "plotly"],
    horizontal_angle_span: float = 60,
    vertical_angle_span: float = 60,
) -> Tuple[Literal["bottom", "middle", "top"], Literal["left", "center", "right"]]:
    """
    Generate appropriate horizontal and vertical alignment for text at the radial end point of an ``Axis`` instance.

    ``horizontal_angle_span`` and ``vertical_angle_span`` dictate the text alignment partition, measured in degrees. See
    the below parameter descriptions for how each value is used to partition the angle space.

    :param axis: ``Axis`` for which to generate the appropriate text alignment.
    :param backend: which plotting back end to use. (Different back ends have different string names for their
        alignment options.)
    :param horizontal_angle_span: ``[-horizontal_angle_span, horizontal_angle_span]`` will be ``"left"`` aligned.
        ``[180 - horizontal_angle_span, 180 + horizontal_angle_span]`` will be ``right`` aligned, and all other angles
        will be ``"center"`` aligned.
    :param vertical_angle_span: ``[90 - vertical_angle_span, 90 + vertical_angle_span]`` will be ``"bottom"`` aligned.
        ``[270 - vertical_angle_span, 270 + vertical_angle_span]`` will be ``top`` aligned, and all other angles
        will be ``"middle"`` aligned.
    :return: vertical alignment string and horizontal alignment string appropriate for the edge of the provided
        ``Axis`` instance.
    """
    horizontal_alignment_dict = dict(left="left", center="center", right="right")
    vertical_alignment_dict = dict(bottom="bottom", middle="middle", top="top")

    # matplotlib has different naming convention than default
    if backend == "matplotlib":
        vertical_alignment_dict["middle"] = "center"

    # range in each direction from 0, 180 to specify horizontal alignment
    if (
        axis.angle >= 360 - horizontal_angle_span
        or axis.angle <= 0 + horizontal_angle_span
    ):
        horizontalalignment = horizontal_alignment_dict["left"]
    elif 180 + horizontal_angle_span >= axis.angle >= 180 - horizontal_angle_span:
        horizontalalignment = horizontal_alignment_dict["right"]
    else:
        horizontalalignment = horizontal_alignment_dict["center"]

    # range in each direction from 90, 270 to specify vertical alignment
    if 90 + vertical_angle_span >= axis.angle >= 90 - vertical_angle_span:
        verticalalignment = vertical_alignment_dict["bottom"]
    elif 270 - vertical_angle_span <= axis.angle <= 270 + vertical_angle_span:
        verticalalignment = vertical_alignment_dict["top"]
    else:
        verticalalignment = vertical_alignment_dict["middle"]

    return verticalalignment, horizontalalignment
