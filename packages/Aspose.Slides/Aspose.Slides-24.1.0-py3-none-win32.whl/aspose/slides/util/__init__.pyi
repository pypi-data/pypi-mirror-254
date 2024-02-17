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

class ShapeUtil:
    '''Offer methods which helps to process shapes objects.'''
    @staticmethod
    def graphics_path_to_geometry_path(graphics_path: aspose.pydrawing.Drawing2D.GraphicsPath) -> IGeometryPath:
        '''Converts a :py:class:`aspose.pydrawing.Drawing2D.GraphicsPath` to the :py:class:`aspose.slides.IGeometryPath`
        :param graphics_path: Graphics path
        :returns: Geometry path'''
        ...

    @staticmethod
    def geometry_path_to_graphics_path(geometry_path: IGeometryPath) -> aspose.pydrawing.Drawing2D.GraphicsPath:
        ...

    ...

class SlideUtil:
    '''Offer methods which help to search shapes and text in a presentation.'''
    @overload
    @staticmethod
    def find_shape(pres: IPresentation, alt_text: string) -> IShape:
        ...

    @overload
    @staticmethod
    def find_shape(slide: IBaseSlide, alt_text: string) -> IShape:
        ...

    @overload
    @staticmethod
    def align_shapes(alignment_type: ShapesAlignmentType, align_to_slide: bool, shapes: IShapeCollection) -> None:
        ...

    @overload
    @staticmethod
    def align_shapes(alignment_type: ShapesAlignmentType, align_to_slide: bool, slide: IBaseSlide) -> None:
        ...

    @overload
    @staticmethod
    def align_shapes(alignment_type: ShapesAlignmentType, align_to_slide: bool, slide: IBaseSlide, shape_indexes: List[int]) -> None:
        ...

    @overload
    @staticmethod
    def align_shapes(alignment_type: ShapesAlignmentType, align_to_slide: bool, group_shape: IGroupShape) -> None:
        ...

    @overload
    @staticmethod
    def align_shapes(alignment_type: ShapesAlignmentType, align_to_slide: bool, group_shape: IGroupShape, shape_indexes: List[int]) -> None:
        ...

    @staticmethod
    def find_and_replace_text(presentation: IPresentation, with_masters: bool, find: string, replace: string, format: PortionFormat) -> None:
        ...

    @staticmethod
    def get_all_text_boxes(slide: IBaseSlide) -> List[ITextFrame]:
        ...

    @staticmethod
    def get_all_text_frames(pres: IPresentation, with_masters: bool) -> List[ITextFrame]:
        ...

    ...

