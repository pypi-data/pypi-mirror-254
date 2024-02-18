from random import randint
from typing import TYPE_CHECKING
from typing import Any


from typing import Optional

from typing import Union

from compas.colors import Color
from compas.geometry import Point
from compas.geometry import Transformation
from compas.geometry import transform_points_numpy
from compas.scene import SceneObject
from compas.utilities import flatten
from numpy import array
from numpy import average
from numpy import identity

from compas_viewer.configurations import SceneConfig
from compas_viewer.utilities.gl import make_index_buffer
from compas_viewer.utilities.gl import make_vertex_buffer
from compas_viewer.utilities.gl import update_index_buffer
from compas_viewer.utilities.gl import update_vertex_buffer

if TYPE_CHECKING:
    from compas_viewer import Viewer
    from compas_viewer.components.renderer.shaders import Shader

# Type template of point/line/face data for generating the buffers.
DataType = tuple[list[Point], list[Color], list[list[int]]]


class ViewerSceneObject(SceneObject):
    """
    Base class for all Viewer scene objects
    which also includes the  GL buffer creation and drawing methods.

    Parameters
    ----------
    viewer : :class:`compas_viewer.viewer.Viewer`
        The viewer object.
    is_selected : bool
        Whether the object is selected.
    is_locked : bool
        Whether the object is locked.
    is_visible : bool
        Whether to show object.
    show_points : bool, optional
        Whether to show points/vertices of the object. It will override the value in the config file.
    show_lines : bool, optional
        Whether to show lines/edges of the object. It will override the value in the config file.
    show_faces : bool, optional
        Whether to show faces of the object. It will override the value in the config file.
    pointscolor : Union[:class:`compas.colors.Color`, dict[Any, :class:`compas.colors.Color`]], optional
        The color or the dict of colors of the points. It will override the value in the config file.
    linescolor : Union[:class:`compas.colors.Color`, dict[Any, :class:`compas.colors.Color`]], optional
        The color or the dict of colors of the lines. It will override the value in the config file.
    facescolor : Union[:class:`compas.colors.Color`, dict[Any, :class:`compas.colors.Color`]], optional
        The color or the dict of colors the faces. It will override the value in the config file.
    lineswidth : float, optional
        The line width to be drawn on screen. It will override the value in the config file.
    pointssize : float, optional
        The point size to be drawn on screen. It will override the value in the config file.
    opacity : float, optional
        The opacity of the object. It will override the value in the config file.
    config: :class:`compas_viewer.configurations.scene_config.SceneConfig`.
        The configuration of the scene object. Defaults to None.
        It should be assigned though the :class:`compas_viewer.viewer.Viewer.add` method.
        Otherwise a exception will be raised.
    **kwargs : dict, optional
        Additional visualization options for specific objects.

    Attributes
    ----------
    is_selected : bool
        Whether the object is selected.
    is_locked : bool
        Whether the object is locked (selectable).
        The global grid is a typical object that is not selectable.
    is_visible : bool
        Whether to show object.
    show_points : bool
        Whether to show points/vertices of the object.
    show_lines : bool
        Whether to show lines/edges of the object.
    show_faces : bool
        Whether to show faces of the object.
    pointscolor : dict[Any, :class:`compas.colors.Color`]
        The color of the points.
    linescolor : dict[Any, :class:`compas.colors.Color`]
        The color of the lines.
    facescolor : dict[Any, :class:`compas.colors.Color`]
        The color of the faces.
    lineswidth : float
        The line width to be drawn on screen
    pointssize : float
        The point size to be drawn on screen.
    opacity : float
        The opacity of the object.
    background : bool
        Whether the object is drawn on the background with depth test disabled.
    bounding_box : list[float], read-only
        The min and max corners of object bounding box, as a numpy array of shape (2, 3).
    bounding_box_center : :class:`compas.geometry.Point`, read-only
        The center of object bounding box, as a point.

    See Also
    --------
    :class:`compas.scene.SceneObject`

    """

    LINEARDEFLECTION = 0.2

    def __init__(
        self,
        viewer: "Viewer",
        is_selected: bool,
        is_locked: bool,
        is_visible: bool,
        show_points: Optional[bool] = None,
        show_lines: Optional[bool] = None,
        show_faces: Optional[bool] = None,
        pointscolor: Optional[Union[Color, dict[Any, Color]]] = None,
        linescolor: Optional[Union[Color, dict[Any, Color]]] = None,
        facescolor: Optional[Union[Color, dict[Any, Color]]] = None,
        lineswidth: Optional[float] = None,
        pointssize: Optional[float] = None,
        opacity: Optional[float] = None,
        config: Optional[SceneConfig] = None,
        **kwargs,
    ):
        if config is None:
            raise ValueError(
                "No SceneConfig specified for the ViewerSceneObject. "
                + "Check if the object is added by the function `Viewer.add`."
            )
        #  Basic
        self.config = config
        super(ViewerSceneObject, self).__init__(config=self.config, **kwargs)
        self.viewer = viewer
        self.is_visible = is_visible

        #  Selection
        self.is_locked = is_locked
        self.is_selected = not is_locked and is_selected
        self.instance_color = Color.from_rgb255(randint(0, 255), randint(0, 255), randint(0, 255))

        #  Visual
        self.show_points = show_points if show_points is not None else self.config.show_points
        self.show_lines = show_lines if show_lines is not None else self.config.show_lines
        self.show_faces = show_faces if show_faces is not None else self.config.show_faces

        if pointscolor is None:
            self.pointscolor = {"_default": self.config.pointscolor}
        elif isinstance(pointscolor, Color):
            self.pointscolor = {"_default": pointscolor}
        else:
            self.pointscolor = pointscolor
            self.pointscolor["_default"] = self.config.pointscolor

        if linescolor is None:
            self.linescolor = {"_default": self.config.linescolor}
        elif isinstance(linescolor, Color):
            self.linescolor = {"_default": linescolor}
        else:
            self.linescolor = linescolor
            self.linescolor["_default"] = self.config.linescolor

        if facescolor is None:
            self.facescolor = {"_default": self.config.facescolor}
        elif isinstance(facescolor, Color):
            self.facescolor = {"_default": facescolor}
        else:
            self.facescolor = facescolor
            self.facescolor["_default"] = self.config.facescolor

        self.lineswidth = lineswidth or self.config.lineswidth
        self.pointssize = pointssize or self.config.pointssize
        self.opacity = opacity or self.config.opacity
        self.background: bool = False

        #  Geometric
        self.transformation: Optional[Transformation] = None
        self._matrix_buffer: Optional[list[list[float]]] = None
        self._bounding_box: Optional[list[float]] = None
        self._bounding_box_center: Optional[Point] = None
        self._is_collection = False

        #  Primitive
        self._points_data: Optional[DataType] = None
        self._lines_data: Optional[DataType] = None
        self._frontfaces_data: Optional[DataType] = None
        self._backfaces_data: Optional[DataType] = None
        self._points_buffer: Optional[dict[str, Any]] = None
        self._lines_buffer: Optional[dict[str, Any]] = None
        self._frontfaces_buffer: Optional[dict[str, Any]] = None
        self._backfaces_buffer: Optional[dict[str, Any]] = None

    @property
    def bounding_box(self):
        return self._bounding_box

    @property
    def bounding_box_center(self):
        return self._bounding_box_center

    # ==========================================================================
    # Reading geometric data, downstream classes should implement these properties.
    # ==========================================================================

    def _read_points_data(self) -> Optional[DataType]:
        """Read points data from the object."""
        pass

    def _read_lines_data(self) -> Optional[DataType]:
        """Read lines data from the object."""
        pass

    def _read_frontfaces_data(self) -> Optional[DataType]:
        """Read frontfaces data from the object."""
        pass

    def _read_backfaces_data(self) -> Optional[DataType]:
        """Read backfaces data from the object."""
        pass

    # ==========================================================================
    # general
    # ==========================================================================

    def _update_matrix(self):
        """Update the matrix from object's translation, rotation and scale"""
        if self.transformation is not None:
            self._matrix_buffer = list(array(self.worldtransformation.matrix).flatten())

        if self.children:
            for child in self.children:
                child._update_matrix()

    # ==========================================================================
    # buffer
    # ==========================================================================

    def make_buffer_from_data(self, data: DataType) -> dict[str, Any]:
        """Create buffers from point/line/face data.

        Parameters
        ----------
        data : tuple[list[:class:`compas.geometry.Point`], list[:class:`compas.colors.Color`], list[int]]
            Contains positions, colors, elements for the buffer.

        Returns
        -------
        buffer_dict : dict[str, Any]
            A dict with created buffer indexes.
        """
        positions, colors, elements = data
        return {
            "positions": make_vertex_buffer(list(flatten(positions))),
            "colors": make_vertex_buffer(list(flatten(colors))),
            "elements": make_index_buffer(list(flatten(elements))),
            "n": len(list(flatten(elements))),
        }

    def update_buffer_from_data(
        self,
        data: DataType,
        buffer: dict[str, Any],
        update_positions: bool,
        update_colors: bool,
        update_elements: bool,
    ):
        """Update existing buffers from point/line/face data.

        Parameters
        ----------
        data : tuple[list[:class:`compas.geometry.Point`], list[:class:`compas.colors.Color`], list[int]]
            Contains positions, colors, elements for the buffer.
        buffer : dict[str, Any]
            The dict with created buffer indexes
        update_positions : bool
            Whether to update positions in the buffer dict.
        update_colors : bool
            Whether to update colors in the buffer dict.
        update_elements : bool
            Whether to update elements in the buffer dict.
        """
        positions, colors, elements = data
        if update_positions:
            update_vertex_buffer(list(flatten(positions)), buffer["positions"])
        if update_colors:
            update_vertex_buffer(list(flatten(colors)), buffer["colors"])
        if update_elements:
            update_index_buffer(list(flatten(elements)), buffer["elements"])
        buffer["n"] = len(list(flatten(elements)))

    def make_buffers(self):
        """Create all buffers from object's data"""
        if self._points_data is not None:
            data = self._points_data
            self._points_buffer = self.make_buffer_from_data(data)
            if data[0]:
                self._update_bounding_box(data[0])
        if self._lines_data is not None:
            data = self._lines_data
            self._lines_buffer = self.make_buffer_from_data(data)
            if data[0] and self._bounding_box_center is None:
                self._update_bounding_box(data[0])
        if self._frontfaces_data is not None:
            data = self._frontfaces_data
            self._frontfaces_buffer = self.make_buffer_from_data(data)
            if data[0] and self._bounding_box_center is None:
                self._update_bounding_box(data[0])
        if self._backfaces_data is not None:
            data = self._backfaces_data
            self._backfaces_buffer = self.make_buffer_from_data(data)
            if data[0] and self._bounding_box_center is None:
                self._update_bounding_box(data[0])

    def update_buffers(self):
        """Update all buffers from object's data"""

        if self._points_data is not None:
            assert self._points_buffer is not None
            # boolean values are keys for improving the performance, true for now to update all, will flag them later.
            self.update_buffer_from_data(self._points_data, self._points_buffer, True, True, True)
        if self._lines_data is not None:
            assert self._lines_buffer is not None
            self.update_buffer_from_data(self._lines_data, self._lines_buffer, True, True, True)
        if self._frontfaces_data is not None:
            assert self._frontfaces_buffer is not None
            self.update_buffer_from_data(self._frontfaces_data, self._frontfaces_buffer, True, True, True)
        if self._backfaces_data is not None:
            assert self._backfaces_buffer is not None
            self.update_buffer_from_data(self._backfaces_data, self._backfaces_buffer, True, True, True)

    def init(self):
        """Initialize the object"""
        self._points_data = self._read_points_data() if self.show_points else None
        self._lines_data = self._read_lines_data() if self.show_lines else None
        self._frontfaces_data = self._read_frontfaces_data() if self.show_faces else None
        self._backfaces_data = self._read_backfaces_data() if self.show_faces else None
        self.make_buffers()
        self._update_matrix()

    def update(self):
        """Update the object"""
        self._update_matrix()
        self.update_buffers()
        self.viewer.renderer.update()

    def _update_bounding_box(self, positions: Optional[list[Point]] = None):
        """Update the bounding box of the object"""
        if positions is None:
            positions = []
            if self._points_data is not None:
                positions += self._points_data[0]
            if self._lines_data is not None:
                positions += self._lines_data[0]
            if self._frontfaces_data is not None:
                positions += self._frontfaces_data[0]
            if not positions:
                return

        _positions = array(positions)
        self._bounding_box = list(
            transform_points_numpy(array([_positions.min(axis=0), _positions.max(axis=0)]), self.worldtransformation)
        )
        self._bounding_box_center = Point(*list(average(a=array(self.bounding_box), axis=0)))

    def draw(self, shader: "Shader", wireframe: bool, is_lighted: bool):
        """Draw the object from its buffers"""

        shader.enable_attribute("position")
        shader.enable_attribute("color")
        shader.uniform1i("is_selected", self.is_selected)
        if self._matrix_buffer is not None:
            shader.uniform4x4("transform", self._matrix_buffer)
        shader.uniform1i("is_lighted", is_lighted)
        shader.uniform1f("object_opacity", self.opacity)
        shader.uniform1i("element_type", 2)
        if self._frontfaces_buffer is not None and not wireframe:
            shader.uniform3f("single_color", self.facescolor["_default"].rgb)
            shader.uniform1i(
                "use_single_color",
                not self.facescolor and not self._is_collection and not getattr(self, "use_vertexcolors", False),
            )
            shader.bind_attribute("position", self._frontfaces_buffer["positions"])
            shader.bind_attribute("color", self._frontfaces_buffer["colors"])
            shader.draw_triangles(
                elements=self._frontfaces_buffer["elements"], n=self._frontfaces_buffer["n"], background=self.background
            )
        if self._backfaces_buffer is not None and not wireframe:
            shader.uniform3f("single_color", self.facescolor["_default"].rgb)
            shader.uniform1i(
                "use_single_color",
                not self.facescolor and not self._is_collection and not getattr(self, "use_vertexcolors", False),
            )
            shader.bind_attribute("position", self._backfaces_buffer["positions"])
            shader.bind_attribute("color", self._backfaces_buffer["colors"])
            shader.draw_triangles(
                elements=self._backfaces_buffer["elements"], n=self._backfaces_buffer["n"], background=self.background
            )
        shader.uniform1i("is_lighted", False)
        shader.uniform1i("element_type", 1)
        if self._lines_buffer is not None:
            shader.uniform3f("single_color", self.linescolor["_default"].rgb)
            shader.uniform1i("use_single_color", not self.linescolor and not self._is_collection)
            shader.bind_attribute("position", self._lines_buffer["positions"])
            shader.bind_attribute("color", self._lines_buffer["colors"])
            shader.draw_lines(
                width=self.lineswidth,
                elements=self._lines_buffer["elements"],
                n=self._lines_buffer["n"],
                background=self.background,
            )
        shader.uniform1i("element_type", 0)
        if self._points_buffer is not None:
            shader.uniform3f("single_color", self.pointscolor["_default"].rgb)
            shader.uniform1i("use_single_color", not self.pointscolor and not self._is_collection)
            shader.bind_attribute("position", self._points_buffer["positions"])
            shader.bind_attribute("color", self._points_buffer["colors"])
            shader.draw_points(
                size=self.pointssize,
                elements=self._points_buffer["elements"],
                n=self._points_buffer["n"],
                background=self.background,
            )

        shader.uniform1i("is_selected", 0)
        shader.uniform1f("object_opacity", 1)
        if self._matrix_buffer is not None:
            shader.uniform4x4("transform", list(identity(4).flatten()))
        shader.disable_attribute("position")
        shader.disable_attribute("color")

    def draw_instance(self, shader, wireframe: bool):
        """Draw the object instance for picking"""
        shader.enable_attribute("position")
        shader.uniform3f("instance_color", self.instance_color.rgb)
        if self._matrix_buffer is not None:
            shader.uniform4x4("transform", self._matrix_buffer)
        if self._points_buffer is not None and self.show_points:
            shader.bind_attribute("position", self._points_buffer["positions"])
            shader.draw_points(
                size=self.pointssize, elements=self._points_buffer["elements"], n=self._points_buffer["n"]
            )
        if self._lines_buffer is not None and (self.show_lines or wireframe):
            shader.bind_attribute("position", self._lines_buffer["positions"])
            shader.draw_lines(
                width=self.lineswidth + self.viewer.renderer.selector.PIXEL_SELECTION_INCREMENTAL,
                elements=self._lines_buffer["elements"],
                n=self._lines_buffer["n"],
            )
        if self._frontfaces_buffer is not None and not wireframe:
            shader.bind_attribute("position", self._frontfaces_buffer["positions"])
            shader.draw_triangles(elements=self._frontfaces_buffer["elements"], n=self._frontfaces_buffer["n"])
            assert self._backfaces_buffer is not None
            shader.bind_attribute("position", self._backfaces_buffer["positions"])
            shader.draw_triangles(elements=self._backfaces_buffer["elements"], n=self._backfaces_buffer["n"])
        if self._matrix_buffer is not None:
            shader.uniform4x4("transform", identity(4).flatten())
        shader.uniform3f("instance_color", [0, 0, 0])
        shader.disable_attribute("position")

    def clear(self):
        """Clear the object"""
        raise NotImplementedError("clear() method is not implemented.")
