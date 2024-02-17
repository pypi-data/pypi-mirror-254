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

class EmbedAllFontsHtmlController:
    '''The formatting controller class to use for embedding all presentation fonts in WOFF format.'''
    def __init__(self):
        '''Creates new instance'''
        ...

    def __init__(self, font_name_exclude_list: List[string]):
        '''Creates new instance
        :param font_name_exclude_list: Fonts to be excluded from embedding'''
        ...

    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_all_fonts(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_font(self, generator: IHtmlGenerator, original_font: IFontData, substituted_font: IFontData, font_style: string, font_weight: string, font_data: bytes) -> None:
        ...

    ...

class EmbeddedEotFontsHtmlController:
    '''The formatting controller class to use for fonts embedding in EOT format'''
    def __init__(self):
        '''Creates new instance.'''
        ...

    def __init__(self, controller: IHtmlFormattingController):
        '''Creates new instance.
        :param controller: HTML formatting controller.'''
        ...

    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    ...

class EmbeddedWoffFontsHtmlController:
    '''The formatting controller class to use for fonts embedding in WOFF format'''
    def __init__(self):
        '''Creates new instance.'''
        ...

    def __init__(self, controller: IHtmlFormattingController):
        '''Creates new instance.
        :param controller: HTML formatting controller.'''
        ...

    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    ...

class FrameTickEventArgs:
    '''Represents arguments of the  event.'''
    def get_frame(self) -> aspose.pydrawing.Bitmap:
        '''Get the current :py:class:`aspose.slides.export.PresentationPlayer` frame.'''
        ...

    @property
    def player(self) -> PresentationPlayer:
        ...

    ...

class GifOptions(SaveOptions):
    '''Represents GIF exporting options.'''
    def __init__(self):
        '''Initializes a new instance of the GifOptions class.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    @property
    def frame_size(self) -> aspose.pydrawing.Size:
        ...

    @frame_size.setter
    def frame_size(self, value: aspose.pydrawing.Size):
        ...

    @property
    def export_hidden_slides(self) -> bool:
        ...

    @export_hidden_slides.setter
    def export_hidden_slides(self, value: bool):
        ...

    @property
    def transition_fps(self) -> int:
        ...

    @transition_fps.setter
    def transition_fps(self, value: int):
        ...

    @property
    def default_delay(self) -> int:
        ...

    @default_delay.setter
    def default_delay(self, value: int):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class HandoutLayoutingOptions:
    '''Represents the handout presentation layout mode for export.'''
    def __init__(self):
        '''Initializes the default values.'''
        ...

    @property
    def handout(self) -> HandoutType:
        ...

    @handout.setter
    def handout(self, value: HandoutType):
        ...

    @property
    def print_slide_numbers(self) -> bool:
        ...

    @print_slide_numbers.setter
    def print_slide_numbers(self, value: bool):
        ...

    @property
    def print_frame_slide(self) -> bool:
        ...

    @print_frame_slide.setter
    def print_frame_slide(self, value: bool):
        ...

    @property
    def print_comments(self) -> bool:
        ...

    @print_comments.setter
    def print_comments(self, value: bool):
        ...

    ...

class Html5Options(SaveOptions):
    '''Represents a HTML5 exporting options.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    @property
    def animate_transitions(self) -> bool:
        ...

    @animate_transitions.setter
    def animate_transitions(self, value: bool):
        ...

    @property
    def animate_shapes(self) -> bool:
        ...

    @animate_shapes.setter
    def animate_shapes(self, value: bool):
        ...

    @property
    def embed_images(self) -> bool:
        ...

    @embed_images.setter
    def embed_images(self, value: bool):
        ...

    @property
    def output_path(self) -> string:
        ...

    @output_path.setter
    def output_path(self, value: string):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class HtmlFormatter:
    '''Represents HTML file template.'''
    @staticmethod
    def create_document_formatter(css: string, show_slide_title: bool) -> HtmlFormatter:
        '''Creates and returns HTML formatter for a simple document view which consists of sequences of slides one below another.
        :param css: Specifies CSS for this file.
        :param show_slide_title: Add slide title if there is one above slide image.'''
        ...

    @staticmethod
    def create_slide_show_formatter(css: string, show_slide_title: bool) -> HtmlFormatter:
        '''Creates and returns HTML formatter for a simple slide show html which shows slides one after another.
        :param css: Specifies URL of CCS file used.
        :param show_slide_title: Add slide title if there is one above slide image.'''
        ...

    @staticmethod
    def create_custom_formatter(formatting_controller: IHtmlFormattingController) -> HtmlFormatter:
        '''Creates and returns HTML formatter for custom callback-driven html generation.
        :param formatting_controller: Callback interface which controls html file generation.'''
        ...

    ...

class HtmlGenerator:
    '''Html generator.'''
    @overload
    def add_html(self, html: string) -> None:
        '''Adds formatted HTML text.
        :param html: Text to add.'''
        ...

    @overload
    def add_html(self, html: List[char]) -> None:
        '''Adds formatted HTML text.
        :param html: Text to add.'''
        ...

    @overload
    def add_html(self, html: List[char], start_index: int, length: int) -> None:
        '''Adds formatted HTML text.
        :param html: Text to add.
        :param start_index: Start index of the portion to add.
        :param length: Length of the portion to add.'''
        ...

    @overload
    def add_text(self, text: string) -> None:
        '''Adds plain text to the html files, replacing special characters with html entities.
                    Linebreaks and whitespaces aren't replaced.
        :param text: Text to add.'''
        ...

    @overload
    def add_text(self, text: List[char]) -> None:
        '''Adds plain text to the html files, replacing special characters with html entities.
                    Linebreaks and whitespaces aren't replaced.
        :param text: Text to add.'''
        ...

    @overload
    def add_text(self, text: List[char], start_index: int, length: int) -> None:
        '''Adds plain text to the html files, replacing special characters with html entities.
                    Linebreaks and whitespaces aren't replaced.
        :param text: Text to add.
        :param start_index: Start index of the portion to add.
        :param length: Length of the portion to add.'''
        ...

    @overload
    def add_attribute_value(self, value: string) -> None:
        '''Quotes attribute value and adds it to the html file.
        :param value: Attribute value string.'''
        ...

    @overload
    def add_attribute_value(self, value: List[char]) -> None:
        '''Quotes attribute value and adds it to the html file.
        :param value: Attribute value string.'''
        ...

    @overload
    def add_attribute_value(self, value: List[char], start_index: int, length: int) -> None:
        '''Quotes attribute value and adds it to the html file.
        :param value: Attribute value string.
        :param start_index: Start index of the portion to add.
        :param length: Length of the portion to add.'''
        ...

    @property
    def slide_image_size(self) -> aspose.pydrawing.SizeF:
        ...

    @property
    def slide_image_size_unit(self) -> SvgCoordinateUnit:
        ...

    @property
    def slide_image_size_unit_code(self) -> string:
        ...

    @property
    def previous_slide_index(self) -> int:
        ...

    @property
    def slide_index(self) -> int:
        ...

    @property
    def next_slide_index(self) -> int:
        ...

    ...

class HtmlOptions(SaveOptions):
    '''Represents a HTML exporting options.'''
    def __init__(self, link_embed_controller: ILinkEmbedController):
        '''Creates a new HtmlOptions object specifiing callback.
        :param link_embed_controller: Callback object which controls saving project.'''
        ...

    def __init__(self):
        '''Creates a new HtmlOptions object for saving into single HTML file.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def html_formatter(self) -> IHtmlFormatter:
        ...

    @html_formatter.setter
    def html_formatter(self, value: IHtmlFormatter):
        ...

    @property
    def slide_image_format(self) -> ISlideImageFormat:
        ...

    @slide_image_format.setter
    def slide_image_format(self, value: ISlideImageFormat):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def pictures_compression(self) -> PicturesCompression:
        ...

    @pictures_compression.setter
    def pictures_compression(self, value: PicturesCompression):
        ...

    @property
    def delete_pictures_cropped_areas(self) -> bool:
        ...

    @delete_pictures_cropped_areas.setter
    def delete_pictures_cropped_areas(self, value: bool):
        ...

    @property
    def svg_responsive_layout(self) -> bool:
        ...

    @svg_responsive_layout.setter
    def svg_responsive_layout(self, value: bool):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class IEmbeddedEotFontsHtmlController:
    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    ...

class IEmbeddedWoffFontsHtmlController:
    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    ...

class IGifOptions:
    @property
    def frame_size(self) -> aspose.pydrawing.Size:
        ...

    @frame_size.setter
    def frame_size(self, value: aspose.pydrawing.Size):
        ...

    @property
    def export_hidden_slides(self) -> bool:
        ...

    @export_hidden_slides.setter
    def export_hidden_slides(self, value: bool):
        ...

    @property
    def transition_fps(self) -> int:
        ...

    @transition_fps.setter
    def transition_fps(self, value: int):
        ...

    @property
    def default_delay(self) -> int:
        ...

    @default_delay.setter
    def default_delay(self, value: int):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class IHtml5Options:
    @property
    def animate_transitions(self) -> bool:
        ...

    @animate_transitions.setter
    def animate_transitions(self, value: bool):
        ...

    @property
    def animate_shapes(self) -> bool:
        ...

    @animate_shapes.setter
    def animate_shapes(self, value: bool):
        ...

    @property
    def embed_images(self) -> bool:
        ...

    @embed_images.setter
    def embed_images(self, value: bool):
        ...

    @property
    def output_path(self) -> string:
        ...

    @output_path.setter
    def output_path(self, value: string):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class IHtmlFormatter:
    ...

class IHtmlFormattingController:
    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    ...

class IHtmlGenerator:
    @overload
    def add_html(self, html: string) -> None:
        ...

    @overload
    def add_html(self, html: List[char]) -> None:
        ...

    @overload
    def add_html(self, html: List[char], start_index: int, length: int) -> None:
        ...

    @overload
    def add_text(self, text: string) -> None:
        ...

    @overload
    def add_text(self, text: List[char]) -> None:
        ...

    @overload
    def add_text(self, text: List[char], start_index: int, length: int) -> None:
        ...

    @overload
    def add_attribute_value(self, value: string) -> None:
        ...

    @overload
    def add_attribute_value(self, value: List[char]) -> None:
        ...

    @overload
    def add_attribute_value(self, value: List[char], start_index: int, length: int) -> None:
        ...

    @property
    def slide_image_size(self) -> aspose.pydrawing.SizeF:
        ...

    @property
    def slide_image_size_unit(self) -> SvgCoordinateUnit:
        ...

    @property
    def slide_image_size_unit_code(self) -> string:
        ...

    @property
    def previous_slide_index(self) -> int:
        ...

    @property
    def slide_index(self) -> int:
        ...

    @property
    def next_slide_index(self) -> int:
        ...

    ...

class IHtmlOptions:
    @property
    def html_formatter(self) -> IHtmlFormatter:
        ...

    @html_formatter.setter
    def html_formatter(self, value: IHtmlFormatter):
        ...

    @property
    def slide_image_format(self) -> ISlideImageFormat:
        ...

    @slide_image_format.setter
    def slide_image_format(self, value: ISlideImageFormat):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def pictures_compression(self) -> PicturesCompression:
        ...

    @pictures_compression.setter
    def pictures_compression(self, value: PicturesCompression):
        ...

    @property
    def delete_pictures_cropped_areas(self) -> bool:
        ...

    @delete_pictures_cropped_areas.setter
    def delete_pictures_cropped_areas(self, value: bool):
        ...

    @property
    def svg_responsive_layout(self) -> bool:
        ...

    @svg_responsive_layout.setter
    def svg_responsive_layout(self, value: bool):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class IInkOptions:
    @property
    def hide_ink(self) -> bool:
        ...

    @hide_ink.setter
    def hide_ink(self, value: bool):
        ...

    @property
    def interpret_mask_op_as_opacity(self) -> bool:
        ...

    @interpret_mask_op_as_opacity.setter
    def interpret_mask_op_as_opacity(self, value: bool):
        ...

    ...

class ILinkEmbedController:
    def get_object_storing_location(self, id: int, entity_data: bytes, semantic_name: string, content_type: string, recomended_extension: string) -> LinkEmbedDecision:
        ...

    def get_url(self, id: int, referrer: int) -> string:
        ...

    def save_external(self, id: int, entity_data: bytes) -> None:
        ...

    ...

class INotesCommentsLayoutingOptions:
    @property
    def notes_position(self) -> NotesPositions:
        ...

    @notes_position.setter
    def notes_position(self, value: NotesPositions):
        ...

    @property
    def comments_position(self) -> CommentsPositions:
        ...

    @comments_position.setter
    def comments_position(self, value: CommentsPositions):
        ...

    @property
    def comments_area_color(self) -> aspose.pydrawing.Color:
        ...

    @comments_area_color.setter
    def comments_area_color(self, value: aspose.pydrawing.Color):
        ...

    @property
    def comments_area_width(self) -> int:
        ...

    @comments_area_width.setter
    def comments_area_width(self, value: int):
        ...

    @property
    def show_comments_by_no_author(self) -> bool:
        ...

    @show_comments_by_no_author.setter
    def show_comments_by_no_author(self, value: bool):
        ...

    ...

class IPdfOptions:
    @property
    def text_compression(self) -> PdfTextCompression:
        ...

    @text_compression.setter
    def text_compression(self, value: PdfTextCompression):
        ...

    @property
    def best_images_compression_ratio(self) -> bool:
        ...

    @best_images_compression_ratio.setter
    def best_images_compression_ratio(self, value: bool):
        ...

    @property
    def embed_true_type_fonts_for_ascii(self) -> bool:
        ...

    @embed_true_type_fonts_for_ascii.setter
    def embed_true_type_fonts_for_ascii(self, value: bool):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def additional_common_font_families(self) -> List[string]:
        ...

    @additional_common_font_families.setter
    def additional_common_font_families(self, value: List[string]):
        ...

    @property
    def embed_full_fonts(self) -> bool:
        ...

    @embed_full_fonts.setter
    def embed_full_fonts(self, value: bool):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def compliance(self) -> PdfCompliance:
        ...

    @compliance.setter
    def compliance(self, value: PdfCompliance):
        ...

    @property
    def password(self) -> string:
        ...

    @password.setter
    def password(self, value: string):
        ...

    @property
    def access_permissions(self) -> PdfAccessPermissions:
        ...

    @access_permissions.setter
    def access_permissions(self, value: PdfAccessPermissions):
        ...

    @property
    def save_metafiles_as_png(self) -> bool:
        ...

    @save_metafiles_as_png.setter
    def save_metafiles_as_png(self, value: bool):
        ...

    @property
    def sufficient_resolution(self) -> float:
        ...

    @sufficient_resolution.setter
    def sufficient_resolution(self, value: float):
        ...

    @property
    def draw_slides_frame(self) -> bool:
        ...

    @draw_slides_frame.setter
    def draw_slides_frame(self, value: bool):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def image_transparent_color(self) -> aspose.pydrawing.Color:
        ...

    @image_transparent_color.setter
    def image_transparent_color(self, value: aspose.pydrawing.Color):
        ...

    @property
    def apply_image_transparent(self) -> bool:
        ...

    @apply_image_transparent.setter
    def apply_image_transparent(self, value: bool):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class IPptOptions:
    @property
    def root_directory_clsid(self) -> Guid:
        ...

    @root_directory_clsid.setter
    def root_directory_clsid(self, value: Guid):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class IPptxOptions:
    @property
    def conformance(self) -> Conformance:
        ...

    @conformance.setter
    def conformance(self, value: Conformance):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class IPresentationAnimationPlayer:
    '''Represents a player of the animation.'''
    def set_time_position(self, time: float) -> None:
        '''Set the animation time position within the :py:attr:`aspose.slides.export.IPresentationAnimationPlayer.duration`.'''
        ...

    def get_frame(self) -> aspose.pydrawing.Bitmap:
        '''Get the frame for the current time position previously set with the :py:func:`Aspose.Slides.Export.IPresentationAnimationPlayer.SetTimePosition(Syste.` method.'''
        ...

    @property
    def duration(self) -> float:
        ...

    ...

class IRenderingOptions:
    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class IResponsiveHtmlController:
    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    ...

class ISVGOptions:
    @property
    def vectorize_text(self) -> bool:
        ...

    @vectorize_text.setter
    def vectorize_text(self, value: bool):
        ...

    @property
    def metafile_rasterization_dpi(self) -> int:
        ...

    @metafile_rasterization_dpi.setter
    def metafile_rasterization_dpi(self, value: int):
        ...

    @property
    def disable_3d_text(self) -> bool:
        ...

    @disable_3d_text.setter
    def disable_3d_text(self, value: bool):
        ...

    @property
    def disable_gradient_split(self) -> bool:
        ...

    @disable_gradient_split.setter
    def disable_gradient_split(self, value: bool):
        ...

    @property
    def disable_line_end_cropping(self) -> bool:
        ...

    @disable_line_end_cropping.setter
    def disable_line_end_cropping(self, value: bool):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def shape_formatting_controller(self) -> ISvgShapeFormattingController:
        ...

    @shape_formatting_controller.setter
    def shape_formatting_controller(self, value: ISvgShapeFormattingController):
        ...

    @property
    def pictures_compression(self) -> PicturesCompression:
        ...

    @pictures_compression.setter
    def pictures_compression(self, value: PicturesCompression):
        ...

    @property
    def delete_pictures_cropped_areas(self) -> bool:
        ...

    @delete_pictures_cropped_areas.setter
    def delete_pictures_cropped_areas(self, value: bool):
        ...

    @property
    def use_frame_size(self) -> bool:
        ...

    @use_frame_size.setter
    def use_frame_size(self, value: bool):
        ...

    @property
    def use_frame_rotation(self) -> bool:
        ...

    @use_frame_rotation.setter
    def use_frame_rotation(self, value: bool):
        ...

    @property
    def external_fonts_handling(self) -> SvgExternalFontsHandling:
        ...

    @external_fonts_handling.setter
    def external_fonts_handling(self, value: SvgExternalFontsHandling):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class ISaveOptions:
    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class ISaveOptionsFactory:
    def create_pptx_options(self) -> IPptxOptions:
        ...

    ...

class ISlideImageFormat:
    ...

class ISlidesLayoutOptions:
    ...

class ISvgShape:
    def set_event_handler(self, event_type: SvgEvent, handler: string) -> None:
        ...

    @property
    def id(self) -> string:
        ...

    @id.setter
    def id(self, value: string):
        ...

    ...

class ISvgShapeAndTextFormattingController:
    def format_text(self, svg_t_span: ISvgTSpan, portion: IPortion, text_frame: ITextFrame) -> None:
        ...

    def format_shape(self, svg_shape: ISvgShape, shape: IShape) -> None:
        ...

    @property
    def as_i_svg_shape_formatting_controller(self) -> ISvgShapeFormattingController:
        ...

    ...

class ISvgShapeFormattingController:
    def format_shape(self, svg_shape: ISvgShape, shape: IShape) -> None:
        ...

    ...

class ISvgTSpan:
    @property
    def id(self) -> string:
        ...

    @id.setter
    def id(self, value: string):
        ...

    ...

class ISwfOptions:
    @property
    def compressed(self) -> bool:
        ...

    @compressed.setter
    def compressed(self, value: bool):
        ...

    @property
    def viewer_included(self) -> bool:
        ...

    @viewer_included.setter
    def viewer_included(self, value: bool):
        ...

    @property
    def show_page_border(self) -> bool:
        ...

    @show_page_border.setter
    def show_page_border(self, value: bool):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def show_full_screen(self) -> bool:
        ...

    @show_full_screen.setter
    def show_full_screen(self, value: bool):
        ...

    @property
    def show_page_stepper(self) -> bool:
        ...

    @show_page_stepper.setter
    def show_page_stepper(self, value: bool):
        ...

    @property
    def show_search(self) -> bool:
        ...

    @show_search.setter
    def show_search(self, value: bool):
        ...

    @property
    def show_top_pane(self) -> bool:
        ...

    @show_top_pane.setter
    def show_top_pane(self, value: bool):
        ...

    @property
    def show_bottom_pane(self) -> bool:
        ...

    @show_bottom_pane.setter
    def show_bottom_pane(self, value: bool):
        ...

    @property
    def show_left_pane(self) -> bool:
        ...

    @show_left_pane.setter
    def show_left_pane(self, value: bool):
        ...

    @property
    def start_open_left_pane(self) -> bool:
        ...

    @start_open_left_pane.setter
    def start_open_left_pane(self, value: bool):
        ...

    @property
    def enable_context_menu(self) -> bool:
        ...

    @enable_context_menu.setter
    def enable_context_menu(self, value: bool):
        ...

    @property
    def logo_image_bytes(self) -> bytes:
        ...

    @logo_image_bytes.setter
    def logo_image_bytes(self, value: bytes):
        ...

    @property
    def logo_link(self) -> string:
        ...

    @logo_link.setter
    def logo_link(self, value: string):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class ITextToHtmlConversionOptions:
    @property
    def add_clipboard_fragment_header(self) -> bool:
        ...

    @add_clipboard_fragment_header.setter
    def add_clipboard_fragment_header(self, value: bool):
        ...

    @property
    def text_inheritance_limit(self) -> TextInheritanceLimit:
        ...

    @text_inheritance_limit.setter
    def text_inheritance_limit(self, value: TextInheritanceLimit):
        ...

    @property
    def link_embed_controller(self) -> ILinkEmbedController:
        ...

    @link_embed_controller.setter
    def link_embed_controller(self, value: ILinkEmbedController):
        ...

    @property
    def encoding_name(self) -> string:
        ...

    @encoding_name.setter
    def encoding_name(self, value: string):
        ...

    ...

class ITiffOptions:
    @property
    def image_size(self) -> aspose.pydrawing.Size:
        ...

    @image_size.setter
    def image_size(self, value: aspose.pydrawing.Size):
        ...

    @property
    def dpi_x(self) -> int:
        ...

    @dpi_x.setter
    def dpi_x(self, value: int):
        ...

    @property
    def dpi_y(self) -> int:
        ...

    @dpi_y.setter
    def dpi_y(self, value: int):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def compression_type(self) -> TiffCompressionTypes:
        ...

    @compression_type.setter
    def compression_type(self, value: TiffCompressionTypes):
        ...

    @property
    def pixel_format(self) -> ImagePixelFormat:
        ...

    @pixel_format.setter
    def pixel_format(self, value: ImagePixelFormat):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def bw_conversion_mode(self) -> BlackWhiteConversionMode:
        ...

    @bw_conversion_mode.setter
    def bw_conversion_mode(self, value: BlackWhiteConversionMode):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class IVideoPlayerHtmlController:
    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def format_shape(self, svg_shape: ISvgShape, shape: IShape) -> None:
        ...

    def get_object_storing_location(self, id: int, entity_data: bytes, semantic_name: string, content_type: string, recomended_extension: string) -> LinkEmbedDecision:
        ...

    def get_url(self, id: int, referrer: int) -> string:
        ...

    def save_external(self, id: int, entity_data: bytes) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    @property
    def as_i_svg_shape_formatting_controller(self) -> ISvgShapeFormattingController:
        ...

    @property
    def as_i_link_embed_controller(self) -> ILinkEmbedController:
        ...

    ...

class IVideoPlayerHtmlControllerFactory:
    def create_video_player_html_controller(self, path: string, file_name: string, base_uri: string) -> IVideoPlayerHtmlController:
        ...

    ...

class IXpsOptions:
    @property
    def save_metafiles_as_png(self) -> bool:
        ...

    @save_metafiles_as_png.setter
    def save_metafiles_as_png(self, value: bool):
        ...

    @property
    def draw_slides_frame(self) -> bool:
        ...

    @draw_slides_frame.setter
    def draw_slides_frame(self, value: bool):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class InkOptions:
    '''Provides options that control the look of Ink objects in exported document.'''
    @property
    def hide_ink(self) -> bool:
        ...

    @hide_ink.setter
    def hide_ink(self, value: bool):
        ...

    @property
    def interpret_mask_op_as_opacity(self) -> bool:
        ...

    @interpret_mask_op_as_opacity.setter
    def interpret_mask_op_as_opacity(self, value: bool):
        ...

    ...

class MarkdownSaveOptions(SaveOptions):
    '''Represents options that control how presentation should be saved to markdown.'''
    def __init__(self):
        '''Ctor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    @property
    def export_type(self) -> MarkdownExportType:
        ...

    @export_type.setter
    def export_type(self, value: MarkdownExportType):
        ...

    @property
    def base_path(self) -> string:
        ...

    @base_path.setter
    def base_path(self, value: string):
        ...

    @property
    def images_save_folder_name(self) -> string:
        ...

    @images_save_folder_name.setter
    def images_save_folder_name(self, value: string):
        ...

    @property
    def new_line_type(self) -> NewLineType:
        ...

    @new_line_type.setter
    def new_line_type(self, value: NewLineType):
        ...

    @property
    def show_comments(self) -> bool:
        ...

    @show_comments.setter
    def show_comments(self, value: bool):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def show_slide_number(self) -> bool:
        ...

    @show_slide_number.setter
    def show_slide_number(self, value: bool):
        ...

    @property
    def flavor(self) -> Flavor:
        ...

    @flavor.setter
    def flavor(self, value: Flavor):
        ...

    ...

class NotesCommentsLayoutingOptions:
    '''Provides options that control the look of layouting of notes and comments in exported document.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def show_comments_by_no_author(self) -> bool:
        ...

    @show_comments_by_no_author.setter
    def show_comments_by_no_author(self, value: bool):
        ...

    @property
    def notes_position(self) -> NotesPositions:
        ...

    @notes_position.setter
    def notes_position(self, value: NotesPositions):
        ...

    @property
    def comments_position(self) -> CommentsPositions:
        ...

    @comments_position.setter
    def comments_position(self, value: CommentsPositions):
        ...

    @property
    def comments_area_color(self) -> aspose.pydrawing.Color:
        ...

    @comments_area_color.setter
    def comments_area_color(self, value: aspose.pydrawing.Color):
        ...

    @property
    def comments_area_width(self) -> int:
        ...

    @comments_area_width.setter
    def comments_area_width(self, value: int):
        ...

    ...

class PdfOptions(SaveOptions):
    '''Provides options that control how a presentation is saved in Pdf format.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def text_compression(self) -> PdfTextCompression:
        ...

    @text_compression.setter
    def text_compression(self, value: PdfTextCompression):
        ...

    @property
    def best_images_compression_ratio(self) -> bool:
        ...

    @best_images_compression_ratio.setter
    def best_images_compression_ratio(self, value: bool):
        ...

    @property
    def embed_true_type_fonts_for_ascii(self) -> bool:
        ...

    @embed_true_type_fonts_for_ascii.setter
    def embed_true_type_fonts_for_ascii(self, value: bool):
        ...

    @property
    def additional_common_font_families(self) -> List[string]:
        ...

    @additional_common_font_families.setter
    def additional_common_font_families(self, value: List[string]):
        ...

    @property
    def embed_full_fonts(self) -> bool:
        ...

    @embed_full_fonts.setter
    def embed_full_fonts(self, value: bool):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def compliance(self) -> PdfCompliance:
        ...

    @compliance.setter
    def compliance(self, value: PdfCompliance):
        ...

    @property
    def password(self) -> string:
        ...

    @password.setter
    def password(self, value: string):
        ...

    @property
    def access_permissions(self) -> PdfAccessPermissions:
        ...

    @access_permissions.setter
    def access_permissions(self, value: PdfAccessPermissions):
        ...

    @property
    def save_metafiles_as_png(self) -> bool:
        ...

    @save_metafiles_as_png.setter
    def save_metafiles_as_png(self, value: bool):
        ...

    @property
    def sufficient_resolution(self) -> float:
        ...

    @sufficient_resolution.setter
    def sufficient_resolution(self, value: float):
        ...

    @property
    def draw_slides_frame(self) -> bool:
        ...

    @draw_slides_frame.setter
    def draw_slides_frame(self, value: bool):
        ...

    @property
    def image_transparent_color(self) -> aspose.pydrawing.Color:
        ...

    @image_transparent_color.setter
    def image_transparent_color(self, value: aspose.pydrawing.Color):
        ...

    @property
    def apply_image_transparent(self) -> bool:
        ...

    @apply_image_transparent.setter
    def apply_image_transparent(self, value: bool):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class PptOptions(SaveOptions):
    '''Provides options that control how a presentation is saved in PPT format.'''
    def __init__(self):
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    @property
    def root_directory_clsid(self) -> Guid:
        ...

    @root_directory_clsid.setter
    def root_directory_clsid(self, value: Guid):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class PptxOptions(SaveOptions):
    '''Represents options for saving OpenXml presentations (PPTX, PPSX, POTX, PPTM, PPSM, POTM).'''
    def __init__(self):
        '''Creates new instance of PptxOptions'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    @property
    def conformance(self) -> Conformance:
        ...

    @conformance.setter
    def conformance(self, value: Conformance):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class PresentationAnimationsGenerator:
    '''Represents a generator of the animations in the :py:class:`aspose.slides.Presentation`.'''
    def __init__(self, presentation: Presentation):
        ...

    def __init__(self, frame_size: aspose.pydrawing.Size):
        '''Creates a new instance of the :py:class:`aspose.slides.export.PresentationAnimationsGenerator`.
        :param frame_size: The frame size.'''
        ...

    def run(self, slides: Iterable[ISlide]) -> None:
        ...

    @property
    def default_delay(self) -> int:
        ...

    @default_delay.setter
    def default_delay(self, value: int):
        ...

    @property
    def include_hidden_slides(self) -> bool:
        ...

    @include_hidden_slides.setter
    def include_hidden_slides(self, value: bool):
        ...

    @property
    def exported_slides(self) -> int:
        ...

    @property
    def FRAME_SIZE(self) -> aspose.pydrawing.Size:
        ...

    ...

class PresentationPlayer:
    '''Represents the player of animations associated with the :py:class:`aspose.slides.Presentation`.'''
    def __init__(self, generator: PresentationAnimationsGenerator, fps: float):
        '''Creates new instance of the :py:class:`aspose.slides.export.PresentationPlayer`.
        :param fps: Frames per second (FPS)'''
        ...

    @property
    def frame_index(self) -> int:
        ...

    ...

class RenderingOptions(SaveOptions):
    '''Provides options that control how a presentation/slide is rendered.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class ResponsiveHtmlController:
    '''Responsive HTML Controller'''
    def __init__(self):
        '''Creates new instance'''
        ...

    def __init__(self, controller: IHtmlFormattingController):
        '''Creates new instance
        :param controller: HTML formatting controller'''
        ...

    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    ...

class SVGOptions(SaveOptions):
    '''Represents an SVG options.'''
    def __init__(self):
        '''Initializes a new instance of the SVGOptions class.'''
        ...

    def __init__(self, link_embed_controller: ILinkEmbedController):
        '''Initializes a new instance of the SVGOptions class specifying the link embedding controller object.
        :param link_embed_controller: The link embedding controller reference.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def use_frame_size(self) -> bool:
        ...

    @use_frame_size.setter
    def use_frame_size(self, value: bool):
        ...

    @property
    def use_frame_rotation(self) -> bool:
        ...

    @use_frame_rotation.setter
    def use_frame_rotation(self, value: bool):
        ...

    @property
    def vectorize_text(self) -> bool:
        ...

    @vectorize_text.setter
    def vectorize_text(self, value: bool):
        ...

    @property
    def metafile_rasterization_dpi(self) -> int:
        ...

    @metafile_rasterization_dpi.setter
    def metafile_rasterization_dpi(self, value: int):
        ...

    @property
    def disable_3d_text(self) -> bool:
        ...

    @disable_3d_text.setter
    def disable_3d_text(self, value: bool):
        ...

    @property
    def disable_gradient_split(self) -> bool:
        ...

    @disable_gradient_split.setter
    def disable_gradient_split(self, value: bool):
        ...

    @property
    def disable_line_end_cropping(self) -> bool:
        ...

    @disable_line_end_cropping.setter
    def disable_line_end_cropping(self, value: bool):
        ...

    @classmethod
    @property
    def default(cls) -> SVGOptions:
        ...

    @classmethod
    @property
    def simple(cls) -> SVGOptions:
        ...

    @classmethod
    @property
    def wysiwyg(cls) -> SVGOptions:
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def shape_formatting_controller(self) -> ISvgShapeFormattingController:
        ...

    @shape_formatting_controller.setter
    def shape_formatting_controller(self, value: ISvgShapeFormattingController):
        ...

    @property
    def pictures_compression(self) -> PicturesCompression:
        ...

    @pictures_compression.setter
    def pictures_compression(self, value: PicturesCompression):
        ...

    @property
    def delete_pictures_cropped_areas(self) -> bool:
        ...

    @delete_pictures_cropped_areas.setter
    def delete_pictures_cropped_areas(self, value: bool):
        ...

    @property
    def external_fonts_handling(self) -> SvgExternalFontsHandling:
        ...

    @external_fonts_handling.setter
    def external_fonts_handling(self, value: SvgExternalFontsHandling):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class SaveOptions:
    '''Abstract class with options that control how a presentation is saved.'''
    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    ...

class SaveOptionsFactory:
    '''Allows to create save options' instances'''
    def __init__(self):
        ...

    def create_pptx_options(self) -> IPptxOptions:
        '''Creates PPTX save options.
        :returns: Save options.'''
        ...

    ...

class SlideImageFormat:
    '''Determines format in which slide image will be saved for presentation to HTML export.'''
    def __init__(self):
        ...

    @staticmethod
    def svg(options: SVGOptions) -> SlideImageFormat:
        '''Slides should converted to a SVG format.
        :param options: Options for SVG export.'''
        ...

    @staticmethod
    def bitmap(scale: float, img_format: aspose.pydrawing.Imaging.ImageFormat) -> SlideImageFormat:
        '''Slides should be converted to a raster image.
        :param scale: Image scale factor.
        :param img_format: Image format.'''
        ...

    ...

class SvgShape:
    '''Represents options for SVG shape.'''
    def set_event_handler(self, event_type: SvgEvent, handler: string) -> None:
        '''Sets event handler for the shape
        :param event_type: Type of event.
        :param handler: Javascript function to handle event. Null value removes handler.'''
        ...

    @property
    def id(self) -> string:
        ...

    @id.setter
    def id(self, value: string):
        ...

    ...

class SvgTSpan:
    '''Represents options for SVG text portion ("tspan").'''
    @property
    def id(self) -> string:
        ...

    @id.setter
    def id(self, value: string):
        ...

    ...

class SwfOptions(SaveOptions):
    '''Provides options that control how a presentation is saved in Swf format.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def compressed(self) -> bool:
        ...

    @compressed.setter
    def compressed(self, value: bool):
        ...

    @property
    def viewer_included(self) -> bool:
        ...

    @viewer_included.setter
    def viewer_included(self, value: bool):
        ...

    @property
    def show_page_border(self) -> bool:
        ...

    @show_page_border.setter
    def show_page_border(self, value: bool):
        ...

    @property
    def show_full_screen(self) -> bool:
        ...

    @show_full_screen.setter
    def show_full_screen(self, value: bool):
        ...

    @property
    def show_page_stepper(self) -> bool:
        ...

    @show_page_stepper.setter
    def show_page_stepper(self, value: bool):
        ...

    @property
    def show_search(self) -> bool:
        ...

    @show_search.setter
    def show_search(self, value: bool):
        ...

    @property
    def show_top_pane(self) -> bool:
        ...

    @show_top_pane.setter
    def show_top_pane(self, value: bool):
        ...

    @property
    def show_bottom_pane(self) -> bool:
        ...

    @show_bottom_pane.setter
    def show_bottom_pane(self, value: bool):
        ...

    @property
    def show_left_pane(self) -> bool:
        ...

    @show_left_pane.setter
    def show_left_pane(self, value: bool):
        ...

    @property
    def start_open_left_pane(self) -> bool:
        ...

    @start_open_left_pane.setter
    def start_open_left_pane(self, value: bool):
        ...

    @property
    def enable_context_menu(self) -> bool:
        ...

    @enable_context_menu.setter
    def enable_context_menu(self, value: bool):
        ...

    @property
    def logo_image_bytes(self) -> bytes:
        ...

    @logo_image_bytes.setter
    def logo_image_bytes(self, value: bytes):
        ...

    @property
    def logo_link(self) -> string:
        ...

    @logo_link.setter
    def logo_link(self, value: string):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class TextToHtmlConversionOptions:
    '''Options for extracting HTML from the Pptx text.'''
    def __init__(self):
        ...

    @property
    def add_clipboard_fragment_header(self) -> bool:
        ...

    @add_clipboard_fragment_header.setter
    def add_clipboard_fragment_header(self, value: bool):
        ...

    @property
    def text_inheritance_limit(self) -> TextInheritanceLimit:
        ...

    @text_inheritance_limit.setter
    def text_inheritance_limit(self, value: TextInheritanceLimit):
        ...

    @property
    def link_embed_controller(self) -> ILinkEmbedController:
        ...

    @link_embed_controller.setter
    def link_embed_controller(self, value: ILinkEmbedController):
        ...

    @property
    def encoding_name(self) -> string:
        ...

    @encoding_name.setter
    def encoding_name(self, value: string):
        ...

    ...

class TiffOptions(SaveOptions):
    '''Provides options that control how a presentation is saved in TIFF format.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def image_size(self) -> aspose.pydrawing.Size:
        ...

    @image_size.setter
    def image_size(self, value: aspose.pydrawing.Size):
        ...

    @property
    def dpi_x(self) -> int:
        ...

    @dpi_x.setter
    def dpi_x(self, value: int):
        ...

    @property
    def dpi_y(self) -> int:
        ...

    @dpi_y.setter
    def dpi_y(self, value: int):
        ...

    @property
    def compression_type(self) -> TiffCompressionTypes:
        ...

    @compression_type.setter
    def compression_type(self, value: TiffCompressionTypes):
        ...

    @property
    def pixel_format(self) -> ImagePixelFormat:
        ...

    @pixel_format.setter
    def pixel_format(self, value: ImagePixelFormat):
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def bw_conversion_mode(self) -> BlackWhiteConversionMode:
        ...

    @bw_conversion_mode.setter
    def bw_conversion_mode(self, value: BlackWhiteConversionMode):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class VideoPlayerHtmlController:
    '''This class allows export of video and audio files into a HTML'''
    def __init__(self, path: string, file_name: string, base_uri: string):
        '''Creates a new instance of controller
        :param path: The path where video and audio files will be generated
        :param file_name: The name of the HTML file
        :param base_uri: The base URI which will be used for links generating'''
        ...

    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def format_shape(self, svg_shape: ISvgShape, shape: IShape) -> None:
        ...

    def get_object_storing_location(self, id: int, entity_data: bytes, semantic_name: string, content_type: string, recomended_extension: string) -> LinkEmbedDecision:
        ...

    def get_url(self, id: int, referrer: int) -> string:
        ...

    def save_external(self, id: int, entity_data: bytes) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    @property
    def as_i_svg_shape_formatting_controller(self) -> ISvgShapeFormattingController:
        ...

    @property
    def as_i_link_embed_controller(self) -> ILinkEmbedController:
        ...

    ...

class VideoPlayerHtmlControllerFactory:
    '''Allows to create VideoPlayerHtmlController.'''
    def __init__(self):
        ...

    def create_video_player_html_controller(self, path: string, file_name: string, base_uri: string) -> IVideoPlayerHtmlController:
        '''Creates new ``VideoPlayerHtmlController``.
        :param path: Path.
        :param file_name: File name.
        :param base_uri: Base URI.'''
        ...

    ...

class XpsOptions(SaveOptions):
    '''Provides options that control how a presentation is saved in XPS format.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> string:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: string):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def save_metafiles_as_png(self) -> bool:
        ...

    @save_metafiles_as_png.setter
    def save_metafiles_as_png(self, value: bool):
        ...

    @property
    def draw_slides_frame(self) -> bool:
        ...

    @draw_slides_frame.setter
    def draw_slides_frame(self, value: bool):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class BlackWhiteConversionMode:
    @classmethod
    @property
    def DEFAULT(cls) -> BlackWhiteConversionMode:
        ...

    @classmethod
    @property
    def DITHERING(cls) -> BlackWhiteConversionMode:
        ...

    @classmethod
    @property
    def DITHERING_FLOYD_STEINBERG(cls) -> BlackWhiteConversionMode:
        ...

    @classmethod
    @property
    def AUTO(cls) -> BlackWhiteConversionMode:
        ...

    @classmethod
    @property
    def AUTO_OTSU(cls) -> BlackWhiteConversionMode:
        ...

    @classmethod
    @property
    def THRESHOLD25(cls) -> BlackWhiteConversionMode:
        ...

    @classmethod
    @property
    def THRESHOLD50(cls) -> BlackWhiteConversionMode:
        ...

    @classmethod
    @property
    def THRESHOLD75(cls) -> BlackWhiteConversionMode:
        ...

    ...

class CommentsPositions:
    @classmethod
    @property
    def NONE(cls) -> CommentsPositions:
        ...

    @classmethod
    @property
    def BOTTOM(cls) -> CommentsPositions:
        ...

    @classmethod
    @property
    def RIGHT(cls) -> CommentsPositions:
        ...

    ...

class Conformance:
    @classmethod
    @property
    def ECMA_376_2006(cls) -> Conformance:
        ...

    @classmethod
    @property
    def ISO_29500_2008_TRANSITIONAL(cls) -> Conformance:
        ...

    @classmethod
    @property
    def ISO_29500_2008_STRICT(cls) -> Conformance:
        ...

    ...

class EmbedFontCharacters:
    @classmethod
    @property
    def ONLY_USED(cls) -> EmbedFontCharacters:
        ...

    @classmethod
    @property
    def ALL(cls) -> EmbedFontCharacters:
        ...

    ...

class Flavor:
    '''All markdown specifications used in program.'''
    @classmethod
    @property
    def GITHUB(cls) -> Flavor:
        '''Github flavor.'''
        ...

    @classmethod
    @property
    def GRUBER(cls) -> Flavor:
        '''Gruber flavor.'''
        ...

    @classmethod
    @property
    def MULTI_MARKDOWN(cls) -> Flavor:
        '''Multi markdown flavor.'''
        ...

    @classmethod
    @property
    def COMMON_MARK(cls) -> Flavor:
        '''Common mark flavor.'''
        ...

    @classmethod
    @property
    def MARKDOWN_EXTRA(cls) -> Flavor:
        '''Markdown extra flavor.'''
        ...

    @classmethod
    @property
    def PANDOC(cls) -> Flavor:
        '''Pandoc flavor.'''
        ...

    @classmethod
    @property
    def KRAMDOWN(cls) -> Flavor:
        '''Kramdown flavor.'''
        ...

    @classmethod
    @property
    def MARKUA(cls) -> Flavor:
        '''Markua flavor.'''
        ...

    @classmethod
    @property
    def MARUKU(cls) -> Flavor:
        '''Maruku flavor.'''
        ...

    @classmethod
    @property
    def MARKDOWN2(cls) -> Flavor:
        '''Markdown2 flavor.'''
        ...

    @classmethod
    @property
    def REMARKABLE(cls) -> Flavor:
        '''Remarkable flavor'''
        ...

    @classmethod
    @property
    def SHOWDOWN(cls) -> Flavor:
        '''Showdown flavor.'''
        ...

    @classmethod
    @property
    def GHOST(cls) -> Flavor:
        '''Ghost flavor.'''
        ...

    @classmethod
    @property
    def GIT_LAB(cls) -> Flavor:
        '''Gitlab flavor.'''
        ...

    @classmethod
    @property
    def HAROOPAD(cls) -> Flavor:
        '''Haroopad flavor.'''
        ...

    @classmethod
    @property
    def IA_WRITER(cls) -> Flavor:
        '''IAWriter flavor.'''
        ...

    @classmethod
    @property
    def REDCARPET(cls) -> Flavor:
        '''Redcarpet flavor.'''
        ...

    @classmethod
    @property
    def SCHOLARLY_MARKDOWN(cls) -> Flavor:
        '''Scholarly markdown flavor.'''
        ...

    @classmethod
    @property
    def TAIGA(cls) -> Flavor:
        '''Taiga flavor.'''
        ...

    @classmethod
    @property
    def TRELLO(cls) -> Flavor:
        '''Trello flavor.'''
        ...

    @classmethod
    @property
    def S9E_TEXT_FORMATTER(cls) -> Flavor:
        '''S9E text formatter flavor.'''
        ...

    @classmethod
    @property
    def X_WIKI(cls) -> Flavor:
        '''XWiki flavor.'''
        ...

    @classmethod
    @property
    def STACK_OVERFLOW(cls) -> Flavor:
        '''Stack overflow flavor.'''
        ...

    @classmethod
    @property
    def DEFAULT(cls) -> Flavor:
        '''Default markdown flavor.'''
        ...

    ...

class HandoutType:
    @classmethod
    @property
    def HANDOUTS1(cls) -> HandoutType:
        ...

    @classmethod
    @property
    def HANDOUTS2(cls) -> HandoutType:
        ...

    @classmethod
    @property
    def HANDOUTS3(cls) -> HandoutType:
        ...

    @classmethod
    @property
    def HANDOUTS_4_HORIZONTAL(cls) -> HandoutType:
        ...

    @classmethod
    @property
    def HANDOUTS_4_VERTICAL(cls) -> HandoutType:
        ...

    @classmethod
    @property
    def HANDOUTS_6_HORIZONTAL(cls) -> HandoutType:
        ...

    @classmethod
    @property
    def HANDOUTS_6_VERTICAL(cls) -> HandoutType:
        ...

    @classmethod
    @property
    def HANDOUTS_9_HORIZONTAL(cls) -> HandoutType:
        ...

    @classmethod
    @property
    def HANDOUTS_9_VERTICAL(cls) -> HandoutType:
        ...

    ...

class ImagePixelFormat:
    @classmethod
    @property
    def FORMAT_1BPP_INDEXED(cls) -> ImagePixelFormat:
        ...

    @classmethod
    @property
    def FORMAT_4BPP_INDEXED(cls) -> ImagePixelFormat:
        ...

    @classmethod
    @property
    def FORMAT_8BPP_INDEXED(cls) -> ImagePixelFormat:
        ...

    @classmethod
    @property
    def FORMAT_24BPP_RGB(cls) -> ImagePixelFormat:
        ...

    @classmethod
    @property
    def FORMAT_32BPP_ARGB(cls) -> ImagePixelFormat:
        ...

    ...

class LinkEmbedDecision:
    @classmethod
    @property
    def LINK(cls) -> LinkEmbedDecision:
        ...

    @classmethod
    @property
    def EMBED(cls) -> LinkEmbedDecision:
        ...

    @classmethod
    @property
    def IGNORE(cls) -> LinkEmbedDecision:
        ...

    ...

class MarkdownExportType:
    '''Type of rendering document.'''
    @classmethod
    @property
    def SEQUENTIAL(cls) -> MarkdownExportType:
        '''Render all items separately. One by one.'''
        ...

    @classmethod
    @property
    def TEXT_ONLY(cls) -> MarkdownExportType:
        '''Render only text.'''
        ...

    @classmethod
    @property
    def VISUAL(cls) -> MarkdownExportType:
        '''Render all items, items that are grouped - render together.'''
        ...

    ...

class NewLineType:
    '''Type of new line that will be used in generated document.'''
    @classmethod
    @property
    def WINDOWS(cls) -> NewLineType:
        ...

    @classmethod
    @property
    def UNIX(cls) -> NewLineType:
        ...

    @classmethod
    @property
    def MAC(cls) -> NewLineType:
        '''Mac (OS 9) new line - \\r'''
        ...

    ...

class NotesPositions:
    @classmethod
    @property
    def NONE(cls) -> NotesPositions:
        ...

    @classmethod
    @property
    def BOTTOM_FULL(cls) -> NotesPositions:
        ...

    @classmethod
    @property
    def BOTTOM_TRUNCATED(cls) -> NotesPositions:
        ...

    ...

class PdfAccessPermissions:
    @classmethod
    @property
    def NONE(cls) -> PdfAccessPermissions:
        ...

    @classmethod
    @property
    def PRINT_DOCUMENT(cls) -> PdfAccessPermissions:
        ...

    @classmethod
    @property
    def MODIFY_CONTENT(cls) -> PdfAccessPermissions:
        ...

    @classmethod
    @property
    def COPY_TEXT_AND_GRAPHICS(cls) -> PdfAccessPermissions:
        ...

    @classmethod
    @property
    def ADD_OR_MODIFY_FIELDS(cls) -> PdfAccessPermissions:
        ...

    @classmethod
    @property
    def FILL_EXISTING_FIELDS(cls) -> PdfAccessPermissions:
        ...

    @classmethod
    @property
    def EXTRACT_TEXT_AND_GRAPHICS(cls) -> PdfAccessPermissions:
        ...

    @classmethod
    @property
    def ASSEMBLE_DOCUMENT(cls) -> PdfAccessPermissions:
        ...

    @classmethod
    @property
    def HIGH_QUALITY_PRINT(cls) -> PdfAccessPermissions:
        ...

    ...

class PdfCompliance:
    @classmethod
    @property
    def PDF15(cls) -> PdfCompliance:
        ...

    @classmethod
    @property
    def PDF16(cls) -> PdfCompliance:
        ...

    @classmethod
    @property
    def PDF17(cls) -> PdfCompliance:
        ...

    @classmethod
    @property
    def PDF_A1B(cls) -> PdfCompliance:
        ...

    @classmethod
    @property
    def PDF_A1A(cls) -> PdfCompliance:
        ...

    @classmethod
    @property
    def PDF_A2B(cls) -> PdfCompliance:
        ...

    @classmethod
    @property
    def PDF_A2A(cls) -> PdfCompliance:
        ...

    @classmethod
    @property
    def PDF_A3B(cls) -> PdfCompliance:
        ...

    @classmethod
    @property
    def PDF_A3A(cls) -> PdfCompliance:
        ...

    @classmethod
    @property
    def PDF_UA(cls) -> PdfCompliance:
        ...

    @classmethod
    @property
    def PDF_A2U(cls) -> PdfCompliance:
        ...

    ...

class PdfTextCompression:
    @classmethod
    @property
    def NONE(cls) -> PdfTextCompression:
        ...

    @classmethod
    @property
    def FLATE(cls) -> PdfTextCompression:
        ...

    ...

class PicturesCompression:
    @classmethod
    @property
    def DPI330(cls) -> PicturesCompression:
        ...

    @classmethod
    @property
    def DPI220(cls) -> PicturesCompression:
        ...

    @classmethod
    @property
    def DPI150(cls) -> PicturesCompression:
        ...

    @classmethod
    @property
    def DPI96(cls) -> PicturesCompression:
        ...

    @classmethod
    @property
    def DPI72(cls) -> PicturesCompression:
        ...

    @classmethod
    @property
    def DOCUMENT_RESOLUTION(cls) -> PicturesCompression:
        ...

    ...

class SaveFormat:
    @classmethod
    @property
    def PPT(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def PDF(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def XPS(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def PPTX(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def PPSX(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def TIFF(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def ODP(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def PPTM(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def PPSM(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def POTX(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def POTM(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def HTML(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def SWF(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def OTP(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def PPS(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def POT(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def FODP(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def GIF(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def HTML5(cls) -> SaveFormat:
        ...

    @classmethod
    @property
    def MD(cls) -> SaveFormat:
        ...

    ...

class SvgCoordinateUnit:
    @classmethod
    @property
    def INCH(cls) -> SvgCoordinateUnit:
        ...

    @classmethod
    @property
    def CENTIMETER(cls) -> SvgCoordinateUnit:
        ...

    @classmethod
    @property
    def MILLIMETER(cls) -> SvgCoordinateUnit:
        ...

    @classmethod
    @property
    def POINT(cls) -> SvgCoordinateUnit:
        ...

    @classmethod
    @property
    def PICA(cls) -> SvgCoordinateUnit:
        ...

    @classmethod
    @property
    def EM(cls) -> SvgCoordinateUnit:
        ...

    @classmethod
    @property
    def EX(cls) -> SvgCoordinateUnit:
        ...

    @classmethod
    @property
    def PIXEL(cls) -> SvgCoordinateUnit:
        ...

    @classmethod
    @property
    def PERCENT(cls) -> SvgCoordinateUnit:
        ...

    ...

class SvgEvent:
    @classmethod
    @property
    def ON_FOCUS_IN(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_FOCUS_OUT(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_ACTIVATE(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_CLICK(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_MOUSE_DOWN(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_MOUSE_UP(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_MOUSE_OVER(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_MOUSE_MOVE(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_MOUSE_OUT(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_LOAD(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_UNLOAD(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_ABORT(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_ERROR(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_RESIZE(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_SCROLL(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_ZOOM(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_BEGIN(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_END(cls) -> SvgEvent:
        ...

    @classmethod
    @property
    def ON_REPEAT(cls) -> SvgEvent:
        ...

    ...

class SvgExternalFontsHandling:
    @classmethod
    @property
    def ADD_LINKS_TO_FONT_FILES(cls) -> SvgExternalFontsHandling:
        ...

    @classmethod
    @property
    def EMBED(cls) -> SvgExternalFontsHandling:
        ...

    @classmethod
    @property
    def VECTORIZE(cls) -> SvgExternalFontsHandling:
        ...

    ...

class TextInheritanceLimit:
    @classmethod
    @property
    def ALL(cls) -> TextInheritanceLimit:
        ...

    @classmethod
    @property
    def TEXT_BOX(cls) -> TextInheritanceLimit:
        ...

    @classmethod
    @property
    def PARAGRAPH_ONLY(cls) -> TextInheritanceLimit:
        ...

    ...

class TiffCompressionTypes:
    @classmethod
    @property
    def DEFAULT(cls) -> TiffCompressionTypes:
        ...

    @classmethod
    @property
    def NONE(cls) -> TiffCompressionTypes:
        ...

    @classmethod
    @property
    def CCITT3(cls) -> TiffCompressionTypes:
        ...

    @classmethod
    @property
    def CCITT4(cls) -> TiffCompressionTypes:
        ...

    @classmethod
    @property
    def LZW(cls) -> TiffCompressionTypes:
        ...

    @classmethod
    @property
    def RLE(cls) -> TiffCompressionTypes:
        ...

    ...

