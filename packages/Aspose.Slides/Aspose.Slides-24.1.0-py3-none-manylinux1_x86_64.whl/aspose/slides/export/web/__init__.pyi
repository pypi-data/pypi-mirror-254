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

class IOutputFile:
    def write(self, stream: System.IO.Stream) -> None:
        ...

    ...

class IOutputSaver:
    def save(self, path: string, output_file: IOutputFile) -> None:
        ...

    ...

class ITemplateEngine:
    def add_template(self, key: string, template: string, model_type: Type) -> None:
        ...

    def compile(self, key: string, model: any) -> string:
        ...

    ...

class Input:
    '''Represents a collection of input elements (templates).'''
    ...

class Output:
    '''Represents a collection of output elements for :py:class:`IWebDocument`.'''
    @overload
    def add(self, path: string, image: IPPImage) -> IOutputFile:
        ...

    @overload
    def add(self, path: string, image: aspose.pydrawing.Image) -> IOutputFile:
        '''Adds an output element for the image.
        :param path: Output path.
        :param image: Image to output.
        :returns: :py:class:`aspose.slides.export.web.IOutputFile` object for the image.'''
        ...

    @overload
    def add(self, path: string, video: IVideo) -> IOutputFile:
        ...

    @overload
    def add(self, path: string, font_data: IFontData, font_style: aspose.pydrawing.FontStyle) -> IOutputFile:
        ...

    @overload
    def add(self, path: string, text_content: string) -> IOutputFile:
        '''Adds an output element for the text content.
        :param path: Output path.
        :param text_content: Content to output.
        :returns: :py:class:`aspose.slides.export.web.IOutputFile` object for the text content.'''
        ...

    def bind_resource(self, output_file: IOutputFile, obj: any) -> None:
        '''Binds resource to output file.
        :param output_file: Output file.
        :param obj: Resource object.'''
        ...

    def get_resource_path(self, obj: any) -> string:
        '''Returns the path for a given resource.
        :param obj: Resource object.
        :returns: Resource path.'''
        ...

    ...

class OutputFile:
    '''Represents an output file.'''
    def write(self, stream: System.IO.Stream) -> None:
        '''Writes the file content to the stream.
        :param stream: Destination stream.'''
        ...

    ...

class Storage:
    '''Represents a temporary data storage for :py:class:`aspose.slides.export.web.WebDocument`.'''
    def __init__(self):
        ...

    def contains_key(self, key: string) -> bool:
        '''Determines whether the storage contains an element with the specified key.
        :param key: Key of the value.
        :returns: True if the storage contains an element with the specified key, false otherwise.'''
        ...

    ...

class WebDocument:
    '''Represents a transition form of the presentation for saving into a web format.'''
    def __init__(self, options: WebDocumentOptions):
        ''':py:class:`aspose.slides.export.web.WebDocument` constructor.
        :param options: Options set for the document.
        :returns: A new instance of :py:class:`aspose.slides.export.web.WebDocument`.'''
        ...

    def save(self) -> None:
        '''Saves the document output.'''
        ...

    @property
    def input(self) -> Input:
        ...

    @property
    def output(self) -> Output:
        ...

    ...

class WebDocumentOptions:
    '''Represents an options set for :py:class:`aspose.slides.export.web.WebDocument` saving.'''
    def __init__(self):
        ...

    @property
    def template_engine(self) -> ITemplateEngine:
        ...

    @template_engine.setter
    def template_engine(self, value: ITemplateEngine):
        ...

    @property
    def output_saver(self) -> IOutputSaver:
        ...

    @output_saver.setter
    def output_saver(self, value: IOutputSaver):
        ...

    @property
    def embed_images(self) -> bool:
        ...

    @embed_images.setter
    def embed_images(self, value: bool):
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

    ...

