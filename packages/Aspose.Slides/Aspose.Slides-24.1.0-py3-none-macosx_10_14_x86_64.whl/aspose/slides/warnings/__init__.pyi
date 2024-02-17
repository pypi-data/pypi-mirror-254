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

class IKnownIssueWarningInfo:
    def send_warning(self, receiver: IWarningCallback) -> None:
        ...

    @property
    def as_i_warning_info(self) -> IWarningInfo:
        ...

    @property
    def warning_type(self) -> WarningType:
        ...

    @property
    def description(self) -> string:
        ...

    ...

class INotImplementedWarningInfo:
    def send_warning(self, receiver: IWarningCallback) -> None:
        ...

    @property
    def as_i_warning_info(self) -> IWarningInfo:
        ...

    @property
    def warning_type(self) -> WarningType:
        ...

    @property
    def description(self) -> string:
        ...

    ...

class IObsoletePresLockingBehaviorWarningInfo:
    def send_warning(self, receiver: IWarningCallback) -> None:
        ...

    @property
    def as_i_warning_info(self) -> IWarningInfo:
        ...

    @property
    def warning_type(self) -> WarningType:
        ...

    @property
    def description(self) -> string:
        ...

    ...

class IPresentationSignedWarningInfo:
    def send_warning(self, receiver: IWarningCallback) -> None:
        ...

    @property
    def as_i_warning_info(self) -> IWarningInfo:
        ...

    @property
    def warning_type(self) -> WarningType:
        ...

    @property
    def description(self) -> string:
        ...

    ...

class IWarningCallback:
    def warning(self, warning: IWarningInfo) -> ReturnAction:
        ...

    ...

class IWarningInfo:
    def send_warning(self, receiver: IWarningCallback) -> None:
        ...

    @property
    def warning_type(self) -> WarningType:
        ...

    @property
    def description(self) -> string:
        ...

    ...

class ReturnAction:
    @classmethod
    @property
    def CONTINUE(cls) -> ReturnAction:
        ...

    @classmethod
    @property
    def ABORT(cls) -> ReturnAction:
        ...

    ...

class WarningType:
    @classmethod
    @property
    def SOURCE_FILE_CORRUPTION(cls) -> WarningType:
        ...

    @classmethod
    @property
    def DATA_LOSS(cls) -> WarningType:
        ...

    @classmethod
    @property
    def MAJOR_FORMATTING_LOSS(cls) -> WarningType:
        ...

    @classmethod
    @property
    def MINOR_FORMATTING_LOSS(cls) -> WarningType:
        ...

    @classmethod
    @property
    def COMPATIBILITY_ISSUE(cls) -> WarningType:
        ...

    @classmethod
    @property
    def UNEXPECTED_CONTENT(cls) -> WarningType:
        ...

    ...

