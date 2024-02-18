from compas.geometry import Point
from compas.scene import GeometryObject

from .sceneobject import DataType
from .sceneobject import ViewerSceneObject


class PointObject(ViewerSceneObject, GeometryObject):
    """Viewer scene object for displaying COMPAS Point geometry.

    See Also
    --------
    :class:`compas.geometry.Point`
    """

    def __init__(self, point: Point, **kwargs):
        super(PointObject, self).__init__(geometry=point, **kwargs)
        self.geometry: Point

    def _read_points_data(self) -> DataType:
        positions = [self.geometry]
        colors = [self.pointscolor["_default"]]
        elements = [[0]]
        return positions, colors, elements

    def _read_lines_data(self):
        """No line data exist for this geometry, Return None."""
        return None
