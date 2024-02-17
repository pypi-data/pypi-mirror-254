"""Realeyes C++ SDK bindings for Python"""
from __future__ import annotations
import typing
import enum
import numpy
import numpy.typing


class BoundingBox():
    """Bounding Box class for the faces"""

    def __init__(self, x: int, y: int, width: int, height: int) -> None: ...

    def __repr__(self) -> str: ...

    @property
    def height(self) -> int:
        """Height of the bounding box in pixels."""

    @height.setter
    def height(self, arg0: int) -> None:
        """Height of the bounding box in pixels."""

    @property
    def width(self) -> int:
        """Width of the bounding box in pixels."""

    @width.setter
    def width(self, arg0: int) -> None:
        """Width of the bounding box in pixels."""

    @property
    def x(self) -> int:
        """X coordinate of the top-left corner."""

    @x.setter
    def x(self, arg0: int) -> None:
        """X coordinate of the top-left corner."""

    @property
    def y(self) -> int:
        """Y coordinate of the top-left corner."""

    @y.setter
    def y(self, arg0: int) -> None:
        """Y coordinate of the top-left corner."""


class Point2d():
    """Point2d class"""

    def __init__(self, x: float, y: float) -> None: ...

    def __repr__(self) -> str: ...

    @property
    def x(self) -> float:
        """X coordinate of the point"""

    @x.setter
    def x(self, arg0: float) -> None:
        """X coordinate of the point"""

    @property
    def y(self) -> float:
        """Y coordinate of the point"""

    @y.setter
    def y(self, arg0: float) -> None:
        """Y coordinate of the point"""


class Face():
    """Face Class"""
    def __init__(self, image: numpy.typing.NDArray[numpy.uint8], landmarks: typing.List[Point2d],
                 bbox: BoundingBox = BoundingBox(x=0, y=0, width=0, height=0), confidence: float = 0.0) -> None: ...

    def __repr__(self) -> str: ...

    def bounding_box(self) -> BoundingBox:
        """Returns the bounding box of the detected face."""

    def confidence(self) -> float:
        """Returns the confidence value of the detected face."""

    def landmarks(self) -> list[Point2d]:
        """Returns the landmarks of the detected face."""


class Gender(enum.Enum):
    """Gender enum."""
    FEMALE = 0
    MALE = 1


class OutputType(enum.Enum):
    """Type of the output in Output struct."""
    AGE = 0
    GENDER = 1


class Output:
    """Estimation output"""
    @property
    def name(self) -> str:
        """Name of the output"""

    @name.setter
    def name(self, arg0: str) -> None:
        """Name of the output"""

    @property
    def type(self) -> OutputType:
        """Type of the output"""

    @type.setter
    def type(self, arg0: OutputType) -> None:
        """Type of the output"""

    @property
    def value(self) -> typing.Union[Gender, float]:
        """Value of the output"""

    @value.setter
    def value(self, arg0: typing.Union[Gender, float]) -> None:
        """Value of the output"""


class DemographicEstimator():
    """The Democratic Estimator class

    Args:
        model_file: path for the used model
        max_concurrency: maximum allowed concurrency, 0 means automatic (using all cores), default: 0
    """

    def __init__(self, model_file: str, max_concurrency: int = 0) -> None: ...

    def __repr__(self) -> str: ...

    def detect_faces(self, image: numpy.typing.NDArray[numpy.uint8]) -> typing.List[Face]:
        """Detects the faces on an image.

        Args:
            image: image to detect faces on, it needs to be in RGB format [h x w x c]
        """

    def estimate(self, face: Face) -> typing.List[Output]:
        """Returns the estimated demographics of the detected face.

        Args:
            face: face object to create the embedding for
        """

    def get_model_name(self) -> str:
        """Returns the name (version etc) of the loaded model.

        Returns:
            name of the model
        """


def get_sdk_version_string() -> str:
    """Returns the version string of the SDK (and not the model)

    Returns:
        version fo the model
    """
