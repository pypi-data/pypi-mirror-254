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

class IXamlOptions:
    @property
    def export_hidden_slides(self) -> bool:
        ...

    @export_hidden_slides.setter
    def export_hidden_slides(self, value: bool):
        ...

    @property
    def output_saver(self) -> IXamlOutputSaver:
        ...

    @output_saver.setter
    def output_saver(self, value: IXamlOutputSaver):
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

class IXamlOutputSaver:
    def save(self, path: string, data: bytes) -> None:
        ...

    ...

class XamlOptions(aspose.slides.export.SaveOptions):
    '''Options that control how a XAML document is saved.'''
    def __init__(self):
        '''Creates the XamlOptions instance.'''
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
    def export_hidden_slides(self) -> bool:
        ...

    @export_hidden_slides.setter
    def export_hidden_slides(self, value: bool):
        ...

    @property
    def output_saver(self) -> IXamlOutputSaver:
        ...

    @output_saver.setter
    def output_saver(self, value: IXamlOutputSaver):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

