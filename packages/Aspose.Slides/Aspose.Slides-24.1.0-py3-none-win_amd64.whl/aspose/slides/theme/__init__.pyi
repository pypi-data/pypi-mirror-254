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

class BaseOverrideThemeManager(BaseThemeManager):
    '''Base class for classes that provide access to different types of overriden themes.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.'''
        ...

    @property
    def override_theme(self) -> IOverrideTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IOverrideTheme):
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class BaseThemeManager:
    '''Base class for classes that provide access to different types of themes.'''
    ...

class ChartThemeManager(BaseOverrideThemeManager):
    '''Provides access to chart theme overriden.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.'''
        ...

    @property
    def override_theme(self) -> IOverrideTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IOverrideTheme):
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class ColorScheme:
    '''Stores theme-defined colors.'''
    @property
    def dark1(self) -> IColorFormat:
        ...

    @property
    def light1(self) -> IColorFormat:
        ...

    @property
    def dark2(self) -> IColorFormat:
        ...

    @property
    def light2(self) -> IColorFormat:
        ...

    @property
    def accent1(self) -> IColorFormat:
        ...

    @property
    def accent2(self) -> IColorFormat:
        ...

    @property
    def accent3(self) -> IColorFormat:
        ...

    @property
    def accent4(self) -> IColorFormat:
        ...

    @property
    def accent5(self) -> IColorFormat:
        ...

    @property
    def accent6(self) -> IColorFormat:
        ...

    @property
    def hyperlink(self) -> IColorFormat:
        ...

    @property
    def followed_hyperlink(self) -> IColorFormat:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_slide_component(self) -> ISlideComponent:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    ...

class EffectStyle:
    '''Represents an effect style.'''
    @property
    def effect_format(self) -> IEffectFormat:
        ...

    @property
    def three_d_format(self) -> IThreeDFormat:
        ...

    ...

class EffectStyleCollection:
    '''Represents a collection of effect styles.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IEffectStyle
        '''Returns an element at specified position.
                    Read-only :py:class:`aspose.slides.theme.EffectStyle`.'''
        ...

    ...

class ExtraColorScheme:
    '''Represents an additional color scheme which can be assigned to a slide.'''
    @property
    def name(self) -> string:
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    ...

class ExtraColorSchemeCollection:
    '''Represents a collection of additional color schemes.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IExtraColorScheme
        '''Returns an color scheme by index.
                    Read-only :py:class:`aspose.slides.theme.ExtraColorScheme`.'''
        ...

    ...

class FillFormatCollection:
    '''Represents the collection of fill styles.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IFillFormat
        '''Gets the element at the specified index.
                    Read-only :py:class:`aspose.slides.IFillFormat`.'''
        ...

    ...

class FontScheme:
    '''Stores theme-defined fonts.'''
    @property
    def minor(self) -> IFonts:
        ...

    @property
    def major(self) -> IFonts:
        ...

    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    ...

class FormatScheme:
    '''Stores theme-defined formats for the shapes.'''
    @property
    def fill_styles(self) -> IFillFormatCollection:
        ...

    @property
    def line_styles(self) -> ILineFormatCollection:
        ...

    @property
    def effect_styles(self) -> IEffectStyleCollection:
        ...

    @property
    def background_fill_styles(self) -> IFillFormatCollection:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_slide_component(self) -> ISlideComponent:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    ...

class IColorScheme:
    @property
    def dark1(self) -> IColorFormat:
        ...

    @property
    def light1(self) -> IColorFormat:
        ...

    @property
    def dark2(self) -> IColorFormat:
        ...

    @property
    def light2(self) -> IColorFormat:
        ...

    @property
    def accent1(self) -> IColorFormat:
        ...

    @property
    def accent2(self) -> IColorFormat:
        ...

    @property
    def accent3(self) -> IColorFormat:
        ...

    @property
    def accent4(self) -> IColorFormat:
        ...

    @property
    def accent5(self) -> IColorFormat:
        ...

    @property
    def accent6(self) -> IColorFormat:
        ...

    @property
    def hyperlink(self) -> IColorFormat:
        ...

    @property
    def followed_hyperlink(self) -> IColorFormat:
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

    ...

class IColorSchemeEffectiveData:
    @property
    def dark1(self) -> aspose.pydrawing.Color:
        ...

    @property
    def light1(self) -> aspose.pydrawing.Color:
        ...

    @property
    def dark2(self) -> aspose.pydrawing.Color:
        ...

    @property
    def light2(self) -> aspose.pydrawing.Color:
        ...

    @property
    def accent1(self) -> aspose.pydrawing.Color:
        ...

    @property
    def accent2(self) -> aspose.pydrawing.Color:
        ...

    @property
    def accent3(self) -> aspose.pydrawing.Color:
        ...

    @property
    def accent4(self) -> aspose.pydrawing.Color:
        ...

    @property
    def accent5(self) -> aspose.pydrawing.Color:
        ...

    @property
    def accent6(self) -> aspose.pydrawing.Color:
        ...

    @property
    def hyperlink(self) -> aspose.pydrawing.Color:
        ...

    @property
    def followed_hyperlink(self) -> aspose.pydrawing.Color:
        ...

    ...

class IEffectStyle:
    @property
    def effect_format(self) -> IEffectFormat:
        ...

    @property
    def three_d_format(self) -> IThreeDFormat:
        ...

    ...

class IEffectStyleCollection:
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IEffectStyle
        ...

    ...

class IEffectStyleCollectionEffectiveData:
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IEffectStyleEffectiveData
        ...

    ...

class IEffectStyleEffectiveData:
    @property
    def effect_format(self) -> IEffectFormatEffectiveData:
        ...

    @property
    def three_d_format(self) -> IThreeDFormatEffectiveData:
        ...

    ...

class IExtraColorScheme:
    @property
    def name(self) -> string:
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    ...

class IExtraColorSchemeCollection:
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IExtraColorScheme
        ...

    ...

class IFillFormatCollection:
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IFillFormat
        ...

    ...

class IFillFormatCollectionEffectiveData:
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IFillFormatEffectiveData
        ...

    ...

class IFontScheme:
    @property
    def minor(self) -> IFonts:
        ...

    @property
    def major(self) -> IFonts:
        ...

    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    ...

class IFontSchemeEffectiveData:
    @property
    def minor(self) -> IFontsEffectiveData:
        ...

    @property
    def major(self) -> IFontsEffectiveData:
        ...

    @property
    def name(self) -> string:
        ...

    ...

class IFormatScheme:
    @property
    def fill_styles(self) -> IFillFormatCollection:
        ...

    @property
    def line_styles(self) -> ILineFormatCollection:
        ...

    @property
    def effect_styles(self) -> IEffectStyleCollection:
        ...

    @property
    def background_fill_styles(self) -> IFillFormatCollection:
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

    ...

class IFormatSchemeEffectiveData:
    def get_fill_styles(self, style_color: aspose.pydrawing.Color) -> IFillFormatCollectionEffectiveData:
        ...

    def get_line_styles(self, style_color: aspose.pydrawing.Color) -> ILineFormatCollectionEffectiveData:
        ...

    def get_effect_styles(self, style_color: aspose.pydrawing.Color) -> IEffectStyleCollectionEffectiveData:
        ...

    def get_background_fill_styles(self, style_color: aspose.pydrawing.Color) -> IFillFormatCollectionEffectiveData:
        ...

    ...

class ILineFormatCollection:
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ILineFormat
        ...

    ...

class ILineFormatCollectionEffectiveData:
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ILineFormatEffectiveData
        ...

    ...

class IMasterTheme:
    def get_effective(self) -> IThemeEffectiveData:
        ...

    @property
    def extra_color_schemes(self) -> IExtraColorSchemeCollection:
        ...

    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    @property
    def as_i_theme(self) -> ITheme:
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    @property
    def font_scheme(self) -> IFontScheme:
        ...

    @property
    def format_scheme(self) -> IFormatScheme:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    ...

class IMasterThemeManager:
    def create_theme_effective(self) -> IThemeEffectiveData:
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @is_override_theme_enabled.setter
    def is_override_theme_enabled(self, value: bool):
        ...

    @property
    def override_theme(self) -> IMasterTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IMasterTheme):
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class IMasterThemeable:
    def create_theme_effective(self) -> IThemeEffectiveData:
        ...

    @property
    def theme_manager(self) -> IMasterThemeManager:
        ...

    @property
    def as_i_themeable(self) -> IThemeable:
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

    ...

class IOverrideTheme:
    def init_color_scheme(self) -> None:
        ...

    def init_color_scheme_from(self, color_scheme: IColorScheme) -> None:
        ...

    def init_color_scheme_from_inherited(self) -> None:
        ...

    def init_font_scheme(self) -> None:
        ...

    def init_font_scheme_from(self, font_scheme: IFontScheme) -> None:
        ...

    def init_font_scheme_from_inherited(self) -> None:
        ...

    def init_format_scheme(self) -> None:
        ...

    def init_format_scheme_from(self, format_scheme: IFormatScheme) -> None:
        ...

    def init_format_scheme_from_inherited(self) -> None:
        ...

    def clear(self) -> None:
        ...

    def get_effective(self) -> IThemeEffectiveData:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def as_i_theme(self) -> ITheme:
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    @property
    def font_scheme(self) -> IFontScheme:
        ...

    @property
    def format_scheme(self) -> IFormatScheme:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    ...

class IOverrideThemeManager:
    def create_theme_effective(self) -> IThemeEffectiveData:
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @property
    def override_theme(self) -> IOverrideTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IOverrideTheme):
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class IOverrideThemeable:
    def create_theme_effective(self) -> IThemeEffectiveData:
        ...

    @property
    def theme_manager(self) -> IOverrideThemeManager:
        ...

    @property
    def as_i_themeable(self) -> IThemeable:
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

    ...

class ITheme:
    def get_effective(self) -> IThemeEffectiveData:
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    @property
    def font_scheme(self) -> IFontScheme:
        ...

    @property
    def format_scheme(self) -> IFormatScheme:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    ...

class IThemeEffectiveData:
    def get_color_scheme(self, style_color: aspose.pydrawing.Color) -> IColorSchemeEffectiveData:
        ...

    @property
    def font_scheme(self) -> IFontSchemeEffectiveData:
        ...

    @property
    def format_scheme(self) -> IFormatSchemeEffectiveData:
        ...

    ...

class IThemeManager:
    def create_theme_effective(self) -> IThemeEffectiveData:
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        ...

    ...

class IThemeable:
    def create_theme_effective(self) -> IThemeEffectiveData:
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

    ...

class LayoutSlideThemeManager(BaseOverrideThemeManager):
    '''Provides access to layout slide theme overriden.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.'''
        ...

    @property
    def override_theme(self) -> IOverrideTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IOverrideTheme):
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class LineFormatCollection:
    '''Represents the collection of line styles.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ILineFormat
        '''Gets the element at the specified index.
                    Read-only :py:class:`aspose.slides.ILineFormat`.'''
        ...

    ...

class MasterTheme(Theme):
    '''Represents a master theme.'''
    def get_effective(self) -> IThemeEffectiveData:
        '''Gets effective theme data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.theme.IThemeEffectiveData`.'''
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    @property
    def font_scheme(self) -> IFontScheme:
        ...

    @property
    def format_scheme(self) -> IFormatScheme:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def extra_color_schemes(self) -> IExtraColorSchemeCollection:
        ...

    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def as_i_theme(self) -> ITheme:
        ...

    ...

class MasterThemeManager(BaseThemeManager):
    '''Provides access to presentation master theme.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.'''
        ...

    @property
    def override_theme(self) -> IMasterTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IMasterTheme):
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @is_override_theme_enabled.setter
    def is_override_theme_enabled(self, value: bool):
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class NotesSlideThemeManager(BaseOverrideThemeManager):
    '''Provides access to notes slide theme overriden.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.'''
        ...

    @property
    def override_theme(self) -> IOverrideTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IOverrideTheme):
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class OverrideTheme(Theme):
    '''Represents a overriding theme.'''
    def get_effective(self) -> IThemeEffectiveData:
        '''Gets effective theme data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.theme.IThemeEffectiveData`.'''
        ...

    def init_color_scheme(self) -> None:
        '''Init ColorScheme with new object for overriding ColorScheme of InheritedTheme.'''
        ...

    def init_color_scheme_from(self, color_scheme: IColorScheme) -> None:
        '''Init ColorScheme with new object for overriding ColorScheme of InheritedTheme.
        :param color_scheme: Data to initialize from.'''
        ...

    def init_color_scheme_from_inherited(self) -> None:
        '''Init ColorScheme with new object for overriding ColorScheme of InheritedTheme. And initialize data of this new object with data of the ColorScheme of InheritedTheme.'''
        ...

    def init_font_scheme(self) -> None:
        '''Init FontScheme with new object for overriding FontScheme of InheritedTheme.'''
        ...

    def init_font_scheme_from(self, font_scheme: IFontScheme) -> None:
        '''Init FontScheme with new object for overriding FontScheme of InheritedTheme.
        :param font_scheme: Data to initialize from.'''
        ...

    def init_font_scheme_from_inherited(self) -> None:
        '''Init FontScheme with new object for overriding FontScheme of InheritedTheme. And initialize data of this new object with data of the FontScheme of InheritedTheme.'''
        ...

    def init_format_scheme(self) -> None:
        '''Init FormatScheme with new object for overriding FormatScheme of InheritedTheme.'''
        ...

    def init_format_scheme_from(self, format_scheme: IFormatScheme) -> None:
        '''Init FormatScheme with new object for overriding FormatScheme of InheritedTheme.
        :param format_scheme: Data to initialize from.'''
        ...

    def init_format_scheme_from_inherited(self) -> None:
        '''Init FormatScheme with new object for overriding FormatScheme of InheritedTheme. And initialize data of this new object with data of the FormatScheme of InheritedTheme.'''
        ...

    def clear(self) -> None:
        '''Set ColorScheme, FontScheme, FormatScheme to null to disable any overriding with this theme object.'''
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    @property
    def font_scheme(self) -> IFontScheme:
        ...

    @property
    def format_scheme(self) -> IFormatScheme:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def as_i_theme(self) -> ITheme:
        ...

    ...

class SlideThemeManager(BaseOverrideThemeManager):
    '''Provides access to slide theme overriden.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.'''
        ...

    @property
    def override_theme(self) -> IOverrideTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IOverrideTheme):
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class Theme:
    '''Represents a theme.'''
    def get_effective(self) -> IThemeEffectiveData:
        '''Gets effective theme data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.theme.IThemeEffectiveData`.'''
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    @property
    def font_scheme(self) -> IFontScheme:
        ...

    @property
    def format_scheme(self) -> IFormatScheme:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    ...

