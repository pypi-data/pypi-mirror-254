from math import cos
from math import pi
from math import sin
from math import sqrt

from compas.geometry import Ellipse
from compas.geometry import Frame
from compas.scene import GeometryObject
from compas.utilities import pairwise

from .sceneobject import DataType
from .sceneobject import ViewerSceneObject


class EllipseObject(ViewerSceneObject, GeometryObject):
    """Viewer scene object for displaying COMPAS Ellipse geometry.

    See Also
    --------
    :class:`compas.geometry.Ellipse`
    """

    def __init__(self, ellipse: Ellipse, **kwargs):
        self.geometry = ellipse
        self.u = kwargs.get("u", int(self._proximate_circumference / self.LINEARDEFLECTION))
        self.u_points = self._calculate_ellipse_points(ellipse)
        super().__init__(geometry=ellipse, close=True, **kwargs)

    @property
    def _proximate_circumference(self):
        return 2 * pi * sqrt((self.geometry.major**2 + self.geometry.minor**2) / 2)

    def _calculate_ellipse_points(self, ellipse):
        frame = Frame.from_plane(ellipse.plane)
        return [
            frame.to_world_coordinates(
                [
                    cos(i * pi * 2 / self.u) * ellipse.major,
                    sin(i * pi * 2 / self.u) * ellipse.minor,
                    0,
                ]
            )
            for i in range(self.u)
        ]

    def _read_points_data(self) -> DataType:
        positions = []
        colors = []
        elements = []
        i = 0

        for i, u_point in enumerate(self.u_points):
            positions.append(u_point)
            colors.append(self.pointscolor.get(i, self.pointscolor["_default"]))  # type: ignore
            elements.append([i])
            i += 1

        return positions, colors, elements

    def _read_lines_data(self) -> DataType:
        positions = []
        colors = []
        elements = []
        i = 0
        count = 0
        lines = pairwise(self.u_points + [self.u_points[0]])
        count = 0
        for i, (pt1, pt2) in enumerate(lines):
            positions.append(pt1)
            positions.append(pt2)
            colors.append(self.pointscolor.get(i, self.pointscolor["_default"]))  # type: ignore
            colors.append(self.pointscolor.get(i, self.pointscolor["_default"]))  # type: ignore
            elements.append([count, count + 1])
            count += 2
        return positions, colors, elements
