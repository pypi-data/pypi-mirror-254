from typing import List, Optional, Dict, Iterable
import aspose.pycore
import aspose.pydrawing
import aspose.slides
import aspose.slides.animation
import aspose.slides.charts
import aspose.slides.dom.ole
import aspose.slides.effects
import aspose.slides.export
import aspose.slides.export.web
import aspose.slides.export.xaml
import aspose.slides.importing
import aspose.slides.ink
import aspose.slides.lowcode
import aspose.slides.mathtext
import aspose.slides.slideshow
import aspose.slides.smartart
import aspose.slides.spreadsheet
import aspose.slides.theme
import aspose.slides.util
import aspose.slides.vba
import aspose.slides.warnings

class ISmartArt:
    @overload
    def get_thumbnail(self) -> aspose.pydrawing.Bitmap:
        ...

    @overload
    def get_thumbnail(self, bounds: ShapeThumbnailBounds, scale_x: float, scale_y: float) -> aspose.pydrawing.Bitmap:
        ...

    @overload
    def write_as_svg(self, stream: System.IO.Stream) -> None:
        ...

    @overload
    def write_as_svg(self, stream: System.IO.Stream, svg_options: aspose.slides.export.ISVGOptions) -> None:
        ...

    def add_placeholder(self, placeholder_to_copy_from: IPlaceholder) -> IPlaceholder:
        ...

    def remove_placeholder(self) -> None:
        ...

    def get_base_placeholder(self) -> IShape:
        ...

    @property
    def all_nodes(self) -> ISmartArtNodeCollection:
        ...

    @property
    def nodes(self) -> ISmartArtNodeCollection:
        ...

    @property
    def layout(self) -> SmartArtLayoutType:
        ...

    @layout.setter
    def layout(self, value: SmartArtLayoutType):
        ...

    @property
    def quick_style(self) -> SmartArtQuickStyleType:
        ...

    @quick_style.setter
    def quick_style(self, value: SmartArtQuickStyleType):
        ...

    @property
    def color_style(self) -> SmartArtColorType:
        ...

    @color_style.setter
    def color_style(self, value: SmartArtColorType):
        ...

    @property
    def is_reversed(self) -> bool:
        ...

    @is_reversed.setter
    def is_reversed(self, value: bool):
        ...

    @property
    def as_i_graphical_object(self) -> IGraphicalObject:
        ...

    @property
    def shape_lock(self) -> IGraphicalObjectLock:
        ...

    @property
    def graphical_object_lock(self) -> IGraphicalObjectLock:
        ...

    @property
    def as_i_shape(self) -> IShape:
        ...

    @property
    def is_text_holder(self) -> bool:
        ...

    @property
    def placeholder(self) -> IPlaceholder:
        ...

    @property
    def custom_data(self) -> ICustomData:
        ...

    @property
    def raw_frame(self) -> IShapeFrame:
        ...

    @raw_frame.setter
    def raw_frame(self, value: IShapeFrame):
        ...

    @property
    def frame(self) -> IShapeFrame:
        ...

    @frame.setter
    def frame(self, value: IShapeFrame):
        ...

    @property
    def line_format(self) -> ILineFormat:
        ...

    @property
    def three_d_format(self) -> IThreeDFormat:
        ...

    @property
    def effect_format(self) -> IEffectFormat:
        ...

    @property
    def fill_format(self) -> IFillFormat:
        ...

    @property
    def hidden(self) -> bool:
        ...

    @hidden.setter
    def hidden(self, value: bool):
        ...

    @property
    def z_order_position(self) -> int:
        ...

    @property
    def connection_site_count(self) -> int:
        ...

    @property
    def rotation(self) -> float:
        ...

    @rotation.setter
    def rotation(self, value: float):
        ...

    @property
    def x(self) -> float:
        ...

    @x.setter
    def x(self, value: float):
        ...

    @property
    def y(self) -> float:
        ...

    @y.setter
    def y(self, value: float):
        ...

    @property
    def width(self) -> float:
        ...

    @width.setter
    def width(self, value: float):
        ...

    @property
    def height(self) -> float:
        ...

    @height.setter
    def height(self, value: float):
        ...

    @property
    def alternative_text(self) -> string:
        ...

    @alternative_text.setter
    def alternative_text(self, value: string):
        ...

    @property
    def alternative_text_title(self) -> string:
        ...

    @alternative_text_title.setter
    def alternative_text_title(self, value: string):
        ...

    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    @property
    def is_decorative(self) -> bool:
        ...

    @is_decorative.setter
    def is_decorative(self, value: bool):
        ...

    @property
    def unique_id(self) -> int:
        ...

    @property
    def office_interop_shape_id(self) -> int:
        ...

    @property
    def is_grouped(self) -> bool:
        ...

    @property
    def black_white_mode(self) -> BlackWhiteMode:
        ...

    @black_white_mode.setter
    def black_white_mode(self, value: BlackWhiteMode):
        ...

    @property
    def parent_group(self) -> IGroupShape:
        ...

    @property
    def as_i_hyperlink_container(self) -> IHyperlinkContainer:
        ...

    @property
    def as_i_slide_component(self) -> ISlideComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def hyperlink_click(self) -> IHyperlink:
        ...

    @hyperlink_click.setter
    def hyperlink_click(self, value: IHyperlink):
        ...

    @property
    def hyperlink_mouse_over(self) -> IHyperlink:
        ...

    @hyperlink_mouse_over.setter
    def hyperlink_mouse_over(self, value: IHyperlink):
        ...

    @property
    def hyperlink_manager(self) -> IHyperlinkManager:
        ...

    ...

class ISmartArtNode:
    def remove(self) -> bool:
        ...

    @property
    def child_nodes(self) -> ISmartArtNodeCollection:
        ...

    @property
    def shapes(self) -> ISmartArtShapeCollection:
        ...

    @property
    def text_frame(self) -> ITextFrame:
        ...

    @property
    def is_assistant(self) -> bool:
        ...

    @is_assistant.setter
    def is_assistant(self, value: bool):
        ...

    @property
    def level(self) -> int:
        ...

    @property
    def bullet_fill_format(self) -> IFillFormat:
        ...

    @property
    def position(self) -> int:
        ...

    @position.setter
    def position(self, value: int):
        ...

    @property
    def is_hidden(self) -> bool:
        ...

    @property
    def organization_chart_layout(self) -> OrganizationChartLayoutType:
        ...

    @organization_chart_layout.setter
    def organization_chart_layout(self, value: OrganizationChartLayoutType):
        ...

    ...

class ISmartArtNodeCollection:
    @overload
    def remove_node(self, index: int) -> None:
        ...

    @overload
    def remove_node(self, node_obj: ISmartArtNode) -> None:
        ...

    def add_node(self) -> ISmartArtNode:
        ...

    def add_node_by_position(self, position: int) -> ISmartArtNode:
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ISmartArtNode
        ...

    ...

class ISmartArtShape:
    @overload
    def get_thumbnail(self) -> aspose.pydrawing.Bitmap:
        ...

    @overload
    def get_thumbnail(self, bounds: ShapeThumbnailBounds, scale_x: float, scale_y: float) -> aspose.pydrawing.Bitmap:
        ...

    @overload
    def write_as_svg(self, stream: System.IO.Stream) -> None:
        ...

    @overload
    def write_as_svg(self, stream: System.IO.Stream, svg_options: aspose.slides.export.ISVGOptions) -> None:
        ...

    def get_geometry_paths(self) -> List[IGeometryPath]:
        ...

    def set_geometry_path(self, geometry_path: IGeometryPath) -> None:
        ...

    def set_geometry_paths(self, geometry_paths: List[IGeometryPath]) -> None:
        ...

    def create_shape_elements(self) -> List[IShapeElement]:
        ...

    def add_placeholder(self, placeholder_to_copy_from: IPlaceholder) -> IPlaceholder:
        ...

    def remove_placeholder(self) -> None:
        ...

    def get_base_placeholder(self) -> IShape:
        ...

    @property
    def text_frame(self) -> ITextFrame:
        ...

    @property
    def as_i_geometry_shape(self) -> IGeometryShape:
        ...

    @property
    def shape_style(self) -> IShapeStyle:
        ...

    @property
    def shape_type(self) -> ShapeType:
        ...

    @shape_type.setter
    def shape_type(self, value: ShapeType):
        ...

    @property
    def adjustments(self) -> IAdjustValueCollection:
        ...

    @property
    def as_i_shape(self) -> IShape:
        ...

    @property
    def is_text_holder(self) -> bool:
        ...

    @property
    def placeholder(self) -> IPlaceholder:
        ...

    @property
    def custom_data(self) -> ICustomData:
        ...

    @property
    def raw_frame(self) -> IShapeFrame:
        ...

    @raw_frame.setter
    def raw_frame(self, value: IShapeFrame):
        ...

    @property
    def frame(self) -> IShapeFrame:
        ...

    @frame.setter
    def frame(self, value: IShapeFrame):
        ...

    @property
    def line_format(self) -> ILineFormat:
        ...

    @property
    def three_d_format(self) -> IThreeDFormat:
        ...

    @property
    def effect_format(self) -> IEffectFormat:
        ...

    @property
    def fill_format(self) -> IFillFormat:
        ...

    @property
    def hidden(self) -> bool:
        ...

    @hidden.setter
    def hidden(self, value: bool):
        ...

    @property
    def z_order_position(self) -> int:
        ...

    @property
    def connection_site_count(self) -> int:
        ...

    @property
    def rotation(self) -> float:
        ...

    @rotation.setter
    def rotation(self, value: float):
        ...

    @property
    def x(self) -> float:
        ...

    @x.setter
    def x(self, value: float):
        ...

    @property
    def y(self) -> float:
        ...

    @y.setter
    def y(self, value: float):
        ...

    @property
    def width(self) -> float:
        ...

    @width.setter
    def width(self, value: float):
        ...

    @property
    def height(self) -> float:
        ...

    @height.setter
    def height(self, value: float):
        ...

    @property
    def alternative_text(self) -> string:
        ...

    @alternative_text.setter
    def alternative_text(self, value: string):
        ...

    @property
    def alternative_text_title(self) -> string:
        ...

    @alternative_text_title.setter
    def alternative_text_title(self, value: string):
        ...

    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    @property
    def is_decorative(self) -> bool:
        ...

    @is_decorative.setter
    def is_decorative(self, value: bool):
        ...

    @property
    def shape_lock(self) -> IBaseShapeLock:
        ...

    @property
    def unique_id(self) -> int:
        ...

    @property
    def office_interop_shape_id(self) -> int:
        ...

    @property
    def is_grouped(self) -> bool:
        ...

    @property
    def black_white_mode(self) -> BlackWhiteMode:
        ...

    @black_white_mode.setter
    def black_white_mode(self, value: BlackWhiteMode):
        ...

    @property
    def parent_group(self) -> IGroupShape:
        ...

    @property
    def as_i_hyperlink_container(self) -> IHyperlinkContainer:
        ...

    @property
    def as_i_slide_component(self) -> ISlideComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def hyperlink_click(self) -> IHyperlink:
        ...

    @hyperlink_click.setter
    def hyperlink_click(self, value: IHyperlink):
        ...

    @property
    def hyperlink_mouse_over(self) -> IHyperlink:
        ...

    @hyperlink_mouse_over.setter
    def hyperlink_mouse_over(self, value: IHyperlink):
        ...

    @property
    def hyperlink_manager(self) -> IHyperlinkManager:
        ...

    ...

class ISmartArtShapeCollection:
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ISmartArtShape
        ...

    ...

class SmartArt(aspose.slides.GraphicalObject):
    '''Represents a SmartArt diagram'''
    @overload
    def get_thumbnail(self) -> aspose.pydrawing.Bitmap:
        '''Returns shape thumbnail.
                    ShapeThumbnailBounds.Shape shape thumbnail bounds type is used by default.
        :returns: Shape thumbnail.'''
        ...

    @overload
    def get_thumbnail(self, bounds: ShapeThumbnailBounds, scale_x: float, scale_y: float) -> aspose.pydrawing.Bitmap:
        ...

    @overload
    def write_as_svg(self, stream: System.IO.Stream) -> None:
        '''Saves content of Shape as SVG file.
        :param stream: Target stream'''
        ...

    @overload
    def write_as_svg(self, stream: System.IO.Stream, svg_options: aspose.slides.export.ISVGOptions) -> None:
        '''Saves content of Shape as SVG file.
        :param stream: Target stream
        :param svg_options: SVG generation options'''
        ...

    def remove_placeholder(self) -> None:
        '''Defines that this shape isn't a placeholder.'''
        ...

    def add_placeholder(self, placeholder_to_copy_from: IPlaceholder) -> IPlaceholder:
        ...

    def get_base_placeholder(self) -> IShape:
        '''Returns a basic placeholder shape (shape from the layout and/or master slide that the current shape is inherited from).'''
        ...

    @property
    def is_text_holder(self) -> bool:
        ...

    @property
    def placeholder(self) -> IPlaceholder:
        ...

    @property
    def custom_data(self) -> ICustomData:
        ...

    @property
    def raw_frame(self) -> IShapeFrame:
        ...

    @raw_frame.setter
    def raw_frame(self, value: IShapeFrame):
        ...

    @property
    def frame(self) -> IShapeFrame:
        ...

    @frame.setter
    def frame(self, value: IShapeFrame):
        ...

    @property
    def line_format(self) -> ILineFormat:
        ...

    @property
    def three_d_format(self) -> IThreeDFormat:
        ...

    @property
    def effect_format(self) -> IEffectFormat:
        ...

    @property
    def fill_format(self) -> IFillFormat:
        ...

    @property
    def hyperlink_click(self) -> IHyperlink:
        ...

    @hyperlink_click.setter
    def hyperlink_click(self, value: IHyperlink):
        ...

    @property
    def hyperlink_mouse_over(self) -> IHyperlink:
        ...

    @hyperlink_mouse_over.setter
    def hyperlink_mouse_over(self, value: IHyperlink):
        ...

    @property
    def hyperlink_manager(self) -> IHyperlinkManager:
        ...

    @property
    def hidden(self) -> bool:
        ...

    @hidden.setter
    def hidden(self, value: bool):
        ...

    @property
    def z_order_position(self) -> int:
        ...

    @property
    def connection_site_count(self) -> int:
        ...

    @property
    def rotation(self) -> float:
        ...

    @rotation.setter
    def rotation(self, value: float):
        ...

    @property
    def x(self) -> float:
        ...

    @x.setter
    def x(self, value: float):
        ...

    @property
    def y(self) -> float:
        ...

    @y.setter
    def y(self, value: float):
        ...

    @property
    def width(self) -> float:
        ...

    @width.setter
    def width(self, value: float):
        ...

    @property
    def height(self) -> float:
        ...

    @height.setter
    def height(self, value: float):
        ...

    @property
    def black_white_mode(self) -> BlackWhiteMode:
        ...

    @black_white_mode.setter
    def black_white_mode(self, value: BlackWhiteMode):
        ...

    @property
    def unique_id(self) -> int:
        ...

    @property
    def office_interop_shape_id(self) -> int:
        ...

    @property
    def alternative_text(self) -> string:
        ...

    @alternative_text.setter
    def alternative_text(self, value: string):
        ...

    @property
    def alternative_text_title(self) -> string:
        ...

    @alternative_text_title.setter
    def alternative_text_title(self, value: string):
        ...

    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    @property
    def is_decorative(self) -> bool:
        ...

    @is_decorative.setter
    def is_decorative(self, value: bool):
        ...

    @property
    def shape_lock(self) -> IGraphicalObjectLock:
        ...

    @property
    def is_grouped(self) -> bool:
        ...

    @property
    def parent_group(self) -> IGroupShape:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def graphical_object_lock(self) -> IGraphicalObjectLock:
        ...

    @property
    def all_nodes(self) -> ISmartArtNodeCollection:
        ...

    @property
    def nodes(self) -> ISmartArtNodeCollection:
        ...

    @property
    def layout(self) -> SmartArtLayoutType:
        ...

    @layout.setter
    def layout(self, value: SmartArtLayoutType):
        ...

    @property
    def quick_style(self) -> SmartArtQuickStyleType:
        ...

    @quick_style.setter
    def quick_style(self, value: SmartArtQuickStyleType):
        ...

    @property
    def color_style(self) -> SmartArtColorType:
        ...

    @color_style.setter
    def color_style(self, value: SmartArtColorType):
        ...

    @property
    def is_reversed(self) -> bool:
        ...

    @is_reversed.setter
    def is_reversed(self, value: bool):
        ...

    @property
    def as_i_hyperlink_container(self) -> IHyperlinkContainer:
        ...

    @property
    def as_i_slide_component(self) -> ISlideComponent:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def as_i_shape(self) -> IShape:
        ...

    @property
    def as_i_graphical_object(self) -> IGraphicalObject:
        ...

    ...

class SmartArtNode:
    '''Represents node of a SmartArt object'''
    def remove(self) -> bool:
        '''Remove current node.
        :returns: ``True`` if removed succesfully, otherwise ``false``'''
        ...

    @property
    def child_nodes(self) -> ISmartArtNodeCollection:
        ...

    @property
    def shapes(self) -> ISmartArtShapeCollection:
        ...

    @property
    def text_frame(self) -> ITextFrame:
        ...

    @property
    def is_assistant(self) -> bool:
        ...

    @is_assistant.setter
    def is_assistant(self, value: bool):
        ...

    @property
    def level(self) -> int:
        ...

    @property
    def bullet_fill_format(self) -> IFillFormat:
        ...

    @property
    def position(self) -> int:
        ...

    @position.setter
    def position(self, value: int):
        ...

    @property
    def is_hidden(self) -> bool:
        ...

    @property
    def organization_chart_layout(self) -> OrganizationChartLayoutType:
        ...

    @organization_chart_layout.setter
    def organization_chart_layout(self, value: OrganizationChartLayoutType):
        ...

    ...

class SmartArtNodeCollection:
    '''Represents a collection of SmartArt nodes.'''
    @overload
    def remove_node(self, index: int) -> None:
        '''Remove node or sub node by index
        :param index: Zero-based index of node'''
        ...

    @overload
    def remove_node(self, node: ISmartArtNode) -> None:
        '''Remove node or sub node
        :param node: Node to remove'''
        ...

    def add_node(self) -> ISmartArtNode:
        '''Add new smart art node or sub node.
        :returns: Added node'''
        ...

    def add_node_by_position(self, position: int) -> ISmartArtNode:
        '''Add new node in the selected position of nodes collection
        :param position: Zero-base node position
        :returns: Added node'''
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ISmartArtNode
        '''Returns node by index'''
        ...

    ...

class SmartArtShape(aspose.slides.GeometryShape):
    '''Represents SmartArt shape'''
    @overload
    def get_thumbnail(self) -> aspose.pydrawing.Bitmap:
        '''Returns shape thumbnail.
                    ShapeThumbnailBounds.Shape shape thumbnail bounds type is used by default.
        :returns: Shape thumbnail.'''
        ...

    @overload
    def get_thumbnail(self, bounds: ShapeThumbnailBounds, scale_x: float, scale_y: float) -> aspose.pydrawing.Bitmap:
        ...

    @overload
    def write_as_svg(self, stream: System.IO.Stream) -> None:
        '''Saves content of Shape as SVG file.
        :param stream: Target stream'''
        ...

    @overload
    def write_as_svg(self, stream: System.IO.Stream, svg_options: aspose.slides.export.ISVGOptions) -> None:
        '''Saves content of Shape as SVG file.
        :param stream: Target stream
        :param svg_options: SVG generation options'''
        ...

    def remove_placeholder(self) -> None:
        '''Defines that this shape isn't a placeholder.'''
        ...

    def add_placeholder(self, placeholder_to_copy_from: IPlaceholder) -> IPlaceholder:
        ...

    def get_base_placeholder(self) -> IShape:
        '''Returns a basic placeholder shape (shape from the layout and/or master slide that the current shape is inherited from).'''
        ...

    def get_geometry_paths(self) -> List[IGeometryPath]:
        '''Returns the copy of path of the geometry shape. Coordinates are relative to the left top corner of the shape.
        :returns: Array of :py:class:`aspose.slides.IGeometryPath`'''
        ...

    def set_geometry_path(self, geometry_path: IGeometryPath) -> None:
        ...

    def set_geometry_paths(self, geometry_paths: List[IGeometryPath]) -> None:
        ...

    def create_shape_elements(self) -> List[IShapeElement]:
        '''Creates and returns array of shape's elements.
        :returns: Array of :py:class:`aspose.slides.ShapeElement`'''
        ...

    @property
    def is_text_holder(self) -> bool:
        ...

    @property
    def placeholder(self) -> IPlaceholder:
        ...

    @property
    def custom_data(self) -> ICustomData:
        ...

    @property
    def raw_frame(self) -> IShapeFrame:
        ...

    @raw_frame.setter
    def raw_frame(self, value: IShapeFrame):
        ...

    @property
    def frame(self) -> IShapeFrame:
        ...

    @frame.setter
    def frame(self, value: IShapeFrame):
        ...

    @property
    def line_format(self) -> ILineFormat:
        ...

    @property
    def three_d_format(self) -> IThreeDFormat:
        ...

    @property
    def effect_format(self) -> IEffectFormat:
        ...

    @property
    def fill_format(self) -> IFillFormat:
        ...

    @property
    def hyperlink_click(self) -> IHyperlink:
        ...

    @hyperlink_click.setter
    def hyperlink_click(self, value: IHyperlink):
        ...

    @property
    def hyperlink_mouse_over(self) -> IHyperlink:
        ...

    @hyperlink_mouse_over.setter
    def hyperlink_mouse_over(self, value: IHyperlink):
        ...

    @property
    def hyperlink_manager(self) -> IHyperlinkManager:
        ...

    @property
    def hidden(self) -> bool:
        ...

    @hidden.setter
    def hidden(self, value: bool):
        ...

    @property
    def z_order_position(self) -> int:
        ...

    @property
    def connection_site_count(self) -> int:
        ...

    @property
    def rotation(self) -> float:
        ...

    @rotation.setter
    def rotation(self, value: float):
        ...

    @property
    def x(self) -> float:
        ...

    @x.setter
    def x(self, value: float):
        ...

    @property
    def y(self) -> float:
        ...

    @y.setter
    def y(self, value: float):
        ...

    @property
    def width(self) -> float:
        ...

    @width.setter
    def width(self, value: float):
        ...

    @property
    def height(self) -> float:
        ...

    @height.setter
    def height(self, value: float):
        ...

    @property
    def black_white_mode(self) -> BlackWhiteMode:
        ...

    @black_white_mode.setter
    def black_white_mode(self, value: BlackWhiteMode):
        ...

    @property
    def unique_id(self) -> int:
        ...

    @property
    def office_interop_shape_id(self) -> int:
        ...

    @property
    def alternative_text(self) -> string:
        ...

    @alternative_text.setter
    def alternative_text(self, value: string):
        ...

    @property
    def alternative_text_title(self) -> string:
        ...

    @alternative_text_title.setter
    def alternative_text_title(self, value: string):
        ...

    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    @property
    def is_decorative(self) -> bool:
        ...

    @is_decorative.setter
    def is_decorative(self, value: bool):
        ...

    @property
    def shape_lock(self) -> IBaseShapeLock:
        ...

    @property
    def is_grouped(self) -> bool:
        ...

    @property
    def parent_group(self) -> IGroupShape:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def shape_style(self) -> IShapeStyle:
        ...

    @property
    def shape_type(self) -> ShapeType:
        ...

    @shape_type.setter
    def shape_type(self, value: ShapeType):
        ...

    @property
    def adjustments(self) -> IAdjustValueCollection:
        ...

    @property
    def text_frame(self) -> ITextFrame:
        ...

    @property
    def as_i_hyperlink_container(self) -> IHyperlinkContainer:
        ...

    @property
    def as_i_slide_component(self) -> ISlideComponent:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def as_i_shape(self) -> IShape:
        ...

    @property
    def as_i_geometry_shape(self) -> IGeometryShape:
        ...

    ...

class SmartArtShapeCollection:
    '''Represents a collection of a SmartArt shapes'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ISmartArtShape
        '''Gets the element at the specified index.
                    Read-only :py:class:`aspose.slides.smartart.SmartArtShape`.>.'''
        ...

    ...

class OrganizationChartLayoutType:
    @classmethod
    @property
    def INITIAL(cls) -> OrganizationChartLayoutType:
        ...

    @classmethod
    @property
    def STANDART(cls) -> OrganizationChartLayoutType:
        ...

    @classmethod
    @property
    def BOTH_HANGING(cls) -> OrganizationChartLayoutType:
        ...

    @classmethod
    @property
    def LEFT_HANGING(cls) -> OrganizationChartLayoutType:
        ...

    @classmethod
    @property
    def RIGHT_HANGING(cls) -> OrganizationChartLayoutType:
        ...

    ...

class SmartArtColorType:
    @classmethod
    @property
    def DARK_1_OUTLINE(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def DARK_2_OUTLINE(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def DARK_FILL(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORFUL_ACCENT_COLORS(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORFUL_ACCENT_COLORS_2TO_3(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORFUL_ACCENT_COLORS_3TO_4(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORFUL_ACCENT_COLORS_4TO_5(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORFUL_ACCENT_COLORS_5TO_6(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORED_OUTLINE_ACCENT1(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORED_FILL_ACCENT1(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def GRADIENT_RANGE_ACCENT1(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def GRADIENT_LOOP_ACCENT1(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def TRANSPARENT_GRADIENT_RANGE_ACCENT1(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORED_OUTLINE_ACCENT2(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORED_FILL_ACCENT2(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def GRADIENT_RANGE_ACCENT2(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def GRADIENT_LOOP_ACCENT2(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def TRANSPARENT_GRADIENT_RANGE_ACCENT2(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORED_OUTLINE_ACCENT3(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORED_FILL_ACCENT3(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def GRADIENT_RANGE_ACCENT3(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def GRADIENT_LOOP_ACCENT3(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def TRANSPARENT_GRADIENT_RANGE_ACCENT3(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORED_OUTLINE_ACCENT4(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORED_FILL_ACCENT4(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def GRADIENT_RANGE_ACCENT4(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def GRADIENT_LOOP_ACCENT4(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def TRANSPARENT_GRADIENT_RANGE_ACCENT4(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORED_OUTLINE_ACCENT5(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORED_FILL_ACCENT5(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def GRADIENT_RANGE_ACCENT5(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def GRADIENT_LOOP_ACCENT5(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def TRANSPARENT_GRADIENT_RANGE_ACCENT5(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORED_OUTLINE_ACCENT6(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def COLORED_FILL_ACCENT6(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def GRADIENT_RANGE_ACCENT6(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def GRADIENT_LOOP_ACCENT6(cls) -> SmartArtColorType:
        ...

    @classmethod
    @property
    def TRANSPARENT_GRADIENT_RANGE_ACCENT6(cls) -> SmartArtColorType:
        ...

    ...

class SmartArtLayoutType:
    @classmethod
    @property
    def ACCENT_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def ACCENTED_PICTURE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def ALTERNATING_FLOW(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def ALTERNATING_HEXAGONS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def ALTERNATING_PICTURE_BLOCKS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def ALTERNATING_PICTURE_CIRCLES(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def ARROW_RIBBON(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def ASCENDING_PICTURE_ACCENT_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BALANCE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BASIC_BENDING_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BASIC_BLOCK_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BASIC_CHEVRON_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BASIC_CYCLE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BASIC_MATRIX(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BASIC_PIE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BASIC_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BASIC_PYRAMID(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BASIC_RADIAL(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BASIC_TARGET(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BASIC_TIMELINE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BASIC_VENN(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BENDING_PICTURE_ACCENT_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BENDING_PICTURE_BLOCKS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BENDING_PICTURE_CAPTION(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BENDING_PICTURE_CAPTION_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BENDING_PICTURE_SEMI_TRANSPARENT_TEXT(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BLOCK_CYCLE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def BUBBLE_PICTURE_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CAPTIONED_PICTURES(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CHEVRON_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CIRCLE_ACCENT_TIMELINE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CIRCLE_ARROW_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CIRCLE_PICTURE_HIERARCHY(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CIRCLE_RELATIONSHIP(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CIRCULAR_BENDING_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CIRCULAR_PICTURE_CALLOUT(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CLOSED_CHEVRON_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CONTINUOUS_ARROW_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CONTINUOUS_BLOCK_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CONTINUOUS_CYCLE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CONTINUOUS_PICTURE_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CONVERGING_ARROWS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CONVERGING_RADIAL(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def COUNTERBALANCE_ARROWS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CYCLE_MATRIX(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def DESCENDING_BLOCK_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def DESCENDING_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def DETAILED_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def DIVERGING_ARROWS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def DIVERGING_RADIAL(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def EQUATION(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def FRAMED_TEXT_PICTURE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def FUNNEL(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def GEAR(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def GRID_MATRIX(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def GROUPED_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def HALF_CIRCLE_ORGANIZATION_CHART(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def HEXAGON_CLUSTER(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def HIERARCHY(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def HIERARCHY_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def HORIZONTAL_BULLET_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def HORIZONTAL_HIERARCHY(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def HORIZONTAL_LABELED_HIERARCHY(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def HORIZONTAL_MULTI_LEVEL_HIERARCHY(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def HORIZONTAL_ORGANIZATION_CHART(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def HORIZONTAL_PICTURE_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def INCREASING_ARROWS_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def INCREASING_CIRCLE_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def INVERTED_PYRAMID(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def LABELED_HIERARCHY(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def LINEAR_VENN(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def LINED_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def MULTIDIRECTIONAL_CYCLE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def NAMEAND_TITLE_ORGANIZATION_CHART(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def NESTED_TARGET(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def NONDIRECTIONAL_CYCLE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def OPPOSING_ARROWS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def OPPOSING_IDEAS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def ORGANIZATION_CHART(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PHASED_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PICTURE_ACCENT_BLOCKS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PICTURE_ACCENT_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PICTURE_ACCENT_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PICTURE_CAPTION_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PICTURE_GRID(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PICTURE_LINEUP(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PICTURE_STRIPS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PIE_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PLUSAND_MINUS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PROCESS_ARROWS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PROCESS_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PYRAMID_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def RADIAL_CLUSTER(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def RADIAL_CYCLE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def RADIAL_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def RADIAL_VENN(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def RANDOM_TO_RESULT_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def REPEATING_BENDING_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def REVERSE_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def SEGMENTED_CYCLE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def SEGMENTED_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def SEGMENTED_PYRAMID(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def SNAPSHOT_PICTURE_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def SPIRAL_PICTURE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def SQUARE_ACCENT_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def STACKED_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def STACKED_VENN(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def STAGGERED_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def STEP_DOWN_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def STEP_UP_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def SUB_STEP_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def TABLE_HIERARCHY(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def TABLE_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def TARGET_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def TEXT_CYCLE(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def TITLE_PICTURE_LINEUP(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def TITLED_MATRIX(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def TITLED_PICTURE_ACCENT_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def TITLED_PICTURE_BLOCKS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def TRAPEZOID_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def UPWARD_ARROW(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_ACCENT_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_ARROW_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_BENDING_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_BLOCK_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_BOX_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_BULLET_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_CHEVRON_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_CIRCLE_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_CURVED_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_EQUATION(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_PICTURE_ACCENT_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_PICTURE_LIST(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def VERTICAL_PROCESS(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def CUSTOM(cls) -> SmartArtLayoutType:
        ...

    @classmethod
    @property
    def PICTURE_ORGANIZATION_CHART(cls) -> SmartArtLayoutType:
        ...

    ...

class SmartArtQuickStyleType:
    @classmethod
    @property
    def SIMPLE_FILL(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def WHITE_OUTLINE(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def SUBTLE_EFFECT(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def MODERATE_EFFECT(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def INTENCE_EFFECT(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def POLISHED(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def INSET(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def CARTOON(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def POWDER(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def BRICK_SCENE(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def FLAT_SCENE(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def METALLIC_SCENE(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def SUNSET_SCENE(cls) -> SmartArtQuickStyleType:
        ...

    @classmethod
    @property
    def BIRDS_EYE_SCENE(cls) -> SmartArtQuickStyleType:
        ...

    ...

