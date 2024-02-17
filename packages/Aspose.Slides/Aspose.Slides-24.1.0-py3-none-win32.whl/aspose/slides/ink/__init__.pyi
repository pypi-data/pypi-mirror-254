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

class IInk:
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
    def traces(self) -> List[IInkTrace]:
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

class IInkBrush:
    @property
    def color(self) -> aspose.pydrawing.Color:
        ...

    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...

    @property
    def size(self) -> aspose.pydrawing.SizeF:
        ...

    @size.setter
    def size(self, value: aspose.pydrawing.SizeF):
        ...

    ...

class IInkTrace:
    @property
    def brush(self) -> IInkBrush:
        ...

    @property
    def points(self) -> List[aspose.pydrawing.PointF]:
        ...

    ...

class Ink(aspose.slides.GraphicalObject):
    '''Represents an ink object on a slide.'''
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
    def traces(self) -> List[IInkTrace]:
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

class InkBrush:
    '''Represents an inkBrush object.'''
    @property
    def color(self) -> aspose.pydrawing.Color:
        ...

    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...

    @property
    def size(self) -> aspose.pydrawing.SizeF:
        ...

    @size.setter
    def size(self, value: aspose.pydrawing.SizeF):
        ...

    ...

class InkTrace:
    '''Represents an Trace object.
                A Trace element is used to record the data captured by the digitizer. 
                It contains a sequence of points encoded according to the specification given by the InkTraceFormat object.'''
    @property
    def brush(self) -> IInkBrush:
        ...

    @property
    def points(self) -> List[aspose.pydrawing.PointF]:
        ...

    ...

