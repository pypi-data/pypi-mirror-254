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

class CellCircularReferenceException(aspose.slides.PptxEditException):
    def __init__(self):
        ...

    def __init__(self, message: string):
        ...

    def __init__(self, message: string, reference: string):
        ...

    @property
    def reference(self) -> string:
        ...

    ...

class CellInvalidFormulaException(aspose.slides.PptxEditException):
    def __init__(self):
        ...

    def __init__(self, message: string):
        ...

    def __init__(self, message: string, reference: string):
        ...

    @property
    def reference(self) -> string:
        ...

    ...

class CellInvalidReferenceException(aspose.slides.PptxEditException):
    def __init__(self):
        ...

    def __init__(self, message: string):
        ...

    def __init__(self, message: string, reference: string):
        ...

    @property
    def reference(self) -> string:
        ...

    ...

class CellUnsupportedDataException(aspose.slides.PptxEditException):
    def __init__(self):
        ...

    def __init__(self, message: string):
        ...

    ...

