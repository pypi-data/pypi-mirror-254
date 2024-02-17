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

class AlphaBiLevel(ImageTransformOperation):
    '''Represents an Alpha Bi-Level effect.
                Alpha (Opacity) values less than the threshold are changed to 0 (fully transparent) and
                alpha values greater than or equal to the threshold are changed to 100% (fully opaque).'''
    def get_effective(self) -> IAlphaBiLevelEffectiveData:
        '''Gets effective Alpha Bi-Level effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaBiLevelEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def threshold(self) -> float:
        ...

    @threshold.setter
    def threshold(self, value: float):
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class AlphaCeiling(ImageTransformOperation):
    '''Represents an Alpha Ceiling effect.
                Alpha (opacity) values greater than zero are changed to 100%.
                In other words, anything partially opaque becomes fully opaque.'''
    def get_effective(self) -> IAlphaCeilingEffectiveData:
        '''Gets effective Alpha Ceiling effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaCeilingEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class AlphaFloor(ImageTransformOperation):
    '''Represents an Alpha Floor effect.
                Alpha (opacity) values less than 100% are changed to zero.
                In other words, anything partially transparent becomes fully transparent.'''
    def get_effective(self) -> IAlphaFloorEffectiveData:
        '''Gets effective Alpha Floor effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaFloorEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class AlphaInverse(ImageTransformOperation):
    '''Represents an Alpha Inverse effect.
                Alpha (opacity) values are inverted by subtracting from 100%.'''
    def get_effective(self) -> IAlphaInverseEffectiveData:
        '''Gets effective Alpha Inverse effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaInverseEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class AlphaModulate(ImageTransformOperation):
    '''Represents an Alpha Modulate effect.
                Effect alpha (opacity) values are multiplied by a fixed percentage.
                The effect container specifies an effect containing alpha values to modulate.'''
    def get_effective(self) -> IAlphaModulateEffectiveData:
        '''Gets effective Alpha Modulate effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaModulateEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class AlphaModulateFixed(ImageTransformOperation):
    '''Represents an Alpha Modulate Fixed effect.
                Effect alpha (opacity) values are multiplied by a fixed percentage.'''
    def get_effective(self) -> IAlphaModulateFixedEffectiveData:
        '''Gets effective Alpha Modulate Fixed effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaModulateFixedEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def amount(self) -> float:
        ...

    @amount.setter
    def amount(self, value: float):
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class AlphaReplace(ImageTransformOperation):
    '''Represents and Alpha Replace effect.
                Effect alpha (opacity) values are replaced by a fixed alpha.'''
    def get_effective(self) -> IAlphaReplaceEffectiveData:
        '''Gets effective Alpha Replace effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaReplaceEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class BiLevel(ImageTransformOperation):
    '''Represents a Bi-Level (black/white) effect.
                Input colors whose luminance is less than the specified threshold value are changed to black.
                Input colors whose luminance are greater than or equal the specified value are set to white.
                The alpha effect values are unaffected by this effect.'''
    def get_effective(self) -> IBiLevelEffectiveData:
        '''Gets effective Bi-Level effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IBiLevelEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class Blur(ImageTransformOperation):
    '''Represents a Blur effect that is applied to the entire shape, including its fill.
                All color channels, including alpha, are affected.'''
    def get_effective(self) -> IBlurEffectiveData:
        '''Gets effective Blur effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IBlurEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def radius(self) -> float:
        ...

    @radius.setter
    def radius(self, value: float):
        ...

    @property
    def grow(self) -> bool:
        ...

    @grow.setter
    def grow(self, value: bool):
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class ColorChange(ImageTransformOperation):
    '''Represents a Color Change effect.
                Instances of FromColor are replaced with instances of ToColor.'''
    def get_effective(self) -> IColorChangeEffectiveData:
        '''Gets effective Color Change effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IColorChangeEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def from_color(self) -> IColorFormat:
        ...

    @property
    def to_color(self) -> IColorFormat:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class ColorReplace(ImageTransformOperation):
    '''Represents a Color Replacement effect.
                All effect colors are changed to a fixed color.
                Alpha values are unaffected.'''
    def get_effective(self) -> IColorReplaceEffectiveData:
        '''Gets effective Color Replacement effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IColorReplaceEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def color(self) -> IColorFormat:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class Duotone(ImageTransformOperation):
    '''Represents a Duotone effect.
                For each pixel, combines Color1 and Color2 through a linear interpolation
                to determine the new color for that pixel.'''
    def get_effective(self) -> IDuotoneEffectiveData:
        '''Gets effective Duotone effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IDuotoneEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def color1(self) -> IColorFormat:
        ...

    @property
    def color2(self) -> IColorFormat:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class EffectFactory:
    '''Allows to create effects'''
    def __init__(self):
        ...

    def create_glow(self) -> IGlow:
        '''Creates Glow effect.
        :returns: Glow effect.'''
        ...

    def create_inner_shadow(self) -> IInnerShadow:
        '''Creates Inner shafow effect.
        :returns: Inner shafow effect.'''
        ...

    def create_outer_shadow(self) -> IOuterShadow:
        '''Creates Outer shadow effect.
        :returns: Outer shadow effect.'''
        ...

    def create_preset_shadow(self) -> IPresetShadow:
        '''Creates Preset shadow effect.
        :returns: Preset shadow effect.'''
        ...

    def create_reflection(self) -> IReflection:
        '''Creates Reflection effect.
        :returns: Reflection effect.'''
        ...

    def create_soft_edge(self) -> ISoftEdge:
        '''Creates Soft Edge effect.
        :returns: Soft Edge effect.'''
        ...

    @property
    def image_transform_operation_factory(self) -> IImageTransformOperationFactory:
        ...

    ...

class FillOverlay(ImageTransformOperation):
    '''Represents a Fill Overlay effect. A fill overlay may be used to specify
                an additional fill for an object and blend the two fills together.'''
    def get_effective(self) -> IFillOverlayEffectiveData:
        '''Gets effective Fill Overlay effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IFillOverlayEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def fill_format(self) -> IFillFormat:
        ...

    @property
    def blend(self) -> FillBlendMode:
        ...

    @blend.setter
    def blend(self, value: FillBlendMode):
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class Glow:
    '''Represents a Glow effect, in which a color blurred outline 
                is added outside the edges of the object.'''
    def get_effective(self) -> IGlowEffectiveData:
        '''Gets effective Glow effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IGlowEffectiveData`.'''
        ...

    @property
    def radius(self) -> float:
        ...

    @radius.setter
    def radius(self, value: float):
        ...

    @property
    def color(self) -> IColorFormat:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class GrayScale(ImageTransformOperation):
    '''Represents a Gray Scale effect. Converts all effect color values to a shade of gray,
                corresponding to their luminance. Effect alpha (opacity) values are unaffected.'''
    def get_effective(self) -> IGrayScaleEffectiveData:
        '''Gets effective Gray Scale effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IGrayScaleEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class HSL(ImageTransformOperation):
    '''Represents a Hue/Saturation/Luminance effect.
                The hue, saturation, and luminance may each be adjusted relative to its current value.'''
    def get_effective(self) -> IHSLEffectiveData:
        '''Gets effective Hue/Saturation/Luminance effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IHSLEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaBiLevel:
    def get_effective(self) -> IAlphaBiLevelEffectiveData:
        ...

    @property
    def threshold(self) -> float:
        ...

    @threshold.setter
    def threshold(self, value: float):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaBiLevelEffectiveData:
    @property
    def threshold(self) -> float:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IAlphaCeiling:
    def get_effective(self) -> IAlphaCeilingEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaCeilingEffectiveData:
    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IAlphaFloor:
    def get_effective(self) -> IAlphaFloorEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaFloorEffectiveData:
    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IAlphaInverse:
    def get_effective(self) -> IAlphaInverseEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaInverseEffectiveData:
    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IAlphaModulate:
    def get_effective(self) -> IAlphaModulateEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaModulateEffectiveData:
    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IAlphaModulateFixed:
    def get_effective(self) -> IAlphaModulateFixedEffectiveData:
        ...

    @property
    def amount(self) -> float:
        ...

    @amount.setter
    def amount(self, value: float):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaModulateFixedEffectiveData:
    @property
    def amount(self) -> float:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IAlphaReplace:
    def get_effective(self) -> IAlphaReplaceEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaReplaceEffectiveData:
    @property
    def alpha(self) -> float:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IBiLevel:
    def get_effective(self) -> IBiLevelEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IBiLevelEffectiveData:
    @property
    def threshold(self) -> float:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IBlur:
    def get_effective(self) -> IBlurEffectiveData:
        ...

    @property
    def radius(self) -> float:
        ...

    @radius.setter
    def radius(self, value: float):
        ...

    @property
    def grow(self) -> bool:
        ...

    @grow.setter
    def grow(self, value: bool):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IBlurEffectiveData:
    @property
    def radius(self) -> float:
        ...

    @property
    def grow(self) -> bool:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IColorChange:
    def get_effective(self) -> IColorChangeEffectiveData:
        ...

    @property
    def from_color(self) -> IColorFormat:
        ...

    @property
    def to_color(self) -> IColorFormat:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IColorChangeEffectiveData:
    @property
    def from_color(self) -> aspose.pydrawing.Color:
        ...

    @property
    def to_color(self) -> aspose.pydrawing.Color:
        ...

    @property
    def use_alpha(self) -> bool:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IColorReplace:
    def get_effective(self) -> IColorReplaceEffectiveData:
        ...

    @property
    def color(self) -> IColorFormat:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IColorReplaceEffectiveData:
    @property
    def color(self) -> aspose.pydrawing.Color:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IDuotone:
    def get_effective(self) -> IDuotoneEffectiveData:
        ...

    @property
    def color1(self) -> IColorFormat:
        ...

    @property
    def color2(self) -> IColorFormat:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IDuotoneEffectiveData:
    @property
    def color1(self) -> aspose.pydrawing.Color:
        ...

    @property
    def color2(self) -> aspose.pydrawing.Color:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IEffectEffectiveData:
    ...

class IEffectFactory:
    def create_glow(self) -> IGlow:
        ...

    def create_inner_shadow(self) -> IInnerShadow:
        ...

    def create_outer_shadow(self) -> IOuterShadow:
        ...

    def create_preset_shadow(self) -> IPresetShadow:
        ...

    def create_reflection(self) -> IReflection:
        ...

    def create_soft_edge(self) -> ISoftEdge:
        ...

    @property
    def image_transform_operation_factory(self) -> IImageTransformOperationFactory:
        ...

    ...

class IFillOverlay:
    def get_effective(self) -> IFillOverlayEffectiveData:
        ...

    @property
    def blend(self) -> FillBlendMode:
        ...

    @blend.setter
    def blend(self, value: FillBlendMode):
        ...

    @property
    def fill_format(self) -> IFillFormat:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IFillOverlayEffectiveData:
    @property
    def blend(self) -> FillBlendMode:
        ...

    @property
    def fill_format(self) -> IFillFormatEffectiveData:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IGlow:
    def get_effective(self) -> IGlowEffectiveData:
        ...

    @property
    def radius(self) -> float:
        ...

    @radius.setter
    def radius(self, value: float):
        ...

    @property
    def color(self) -> IColorFormat:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IGlowEffectiveData:
    @property
    def radius(self) -> float:
        ...

    @property
    def color(self) -> aspose.pydrawing.Color:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IGrayScale:
    def get_effective(self) -> IGrayScaleEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IGrayScaleEffectiveData:
    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IHSL:
    def get_effective(self) -> IHSLEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IHSLEffectiveData:
    @property
    def hue(self) -> float:
        ...

    @property
    def saturation(self) -> float:
        ...

    @property
    def luminance(self) -> float:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IImageTransformOCollectionEffectiveData:
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IEffectEffectiveData
        ...

    ...

class IImageTransformOperation:
    ...

class IImageTransformOperationCollection:
    def remove_at(self, index: int) -> None:
        ...

    def add_alpha_bi_level_effect(self, threshold: float) -> IAlphaBiLevel:
        ...

    def add_alpha_ceiling_effect(self) -> IAlphaCeiling:
        ...

    def add_alpha_floor_effect(self) -> IAlphaFloor:
        ...

    def add_alpha_inverse_effect(self) -> IAlphaInverse:
        ...

    def add_alpha_modulate_effect(self) -> IAlphaModulate:
        ...

    def add_alpha_modulate_fixed_effect(self, amount: float) -> IAlphaModulateFixed:
        ...

    def add_alpha_replace_effect(self, alpha: float) -> IAlphaReplace:
        ...

    def add_bi_level_effect(self, threshold: float) -> IBiLevel:
        ...

    def add_blur_effect(self, radius: float, grow: bool) -> IBlur:
        ...

    def add_color_change_effect(self) -> IColorChange:
        ...

    def add_color_replace_effect(self) -> IColorReplace:
        ...

    def add_duotone_effect(self) -> IDuotone:
        ...

    def add_fill_overlay_effect(self) -> IFillOverlay:
        ...

    def add_gray_scale_effect(self) -> IGrayScale:
        ...

    def add_hsl_effect(self, hue: float, saturation: float, luminance: float) -> IHSL:
        ...

    def add_luminance_effect(self, brightness: float, contrast: float) -> ILuminance:
        ...

    def add_tint_effect(self, hue: float, amount: float) -> ITint:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IImageTransformOperation
        ...

    ...

class IImageTransformOperationFactory:
    def create_alpha_bi_level(self, threshold: float) -> IAlphaBiLevel:
        ...

    def create_alph_ceiling(self) -> IAlphaCeiling:
        ...

    def create_alpha_floor(self) -> IAlphaFloor:
        ...

    def create_alpha_inverse(self) -> IAlphaInverse:
        ...

    def create_alpha_modulate(self) -> IAlphaModulate:
        ...

    def create_alpha_modulate_fixed(self, amount: float) -> IAlphaModulateFixed:
        ...

    def create_alpha_replace(self, alpha: float) -> IAlphaReplace:
        ...

    def create_bi_level(self, threshold: float) -> IBiLevel:
        ...

    def create_blur(self, radius: float, grow: bool) -> IBlur:
        ...

    def create_color_change(self) -> IColorChange:
        ...

    def create_color_replace(self) -> IColorReplace:
        ...

    def create_duotone(self) -> IDuotone:
        ...

    def create_fill_overlay(self) -> IFillOverlay:
        ...

    def create_gray_scale(self) -> IGrayScale:
        ...

    def create_hsl(self, hue: float, saturation: float, luminance: float) -> IHSL:
        ...

    def create_luminance(self, brightness: float, contrast: float) -> ILuminance:
        ...

    def create_tint(self, hue: float, amount: float) -> ITint:
        ...

    ...

class IInnerShadow:
    def get_effective(self) -> IInnerShadowEffectiveData:
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @blur_radius.setter
    def blur_radius(self, value: float):
        ...

    @property
    def direction(self) -> float:
        ...

    @direction.setter
    def direction(self, value: float):
        ...

    @property
    def distance(self) -> float:
        ...

    @distance.setter
    def distance(self, value: float):
        ...

    @property
    def shadow_color(self) -> IColorFormat:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IInnerShadowEffectiveData:
    @property
    def blur_radius(self) -> float:
        ...

    @property
    def direction(self) -> float:
        ...

    @property
    def distance(self) -> float:
        ...

    @property
    def shadow_color(self) -> aspose.pydrawing.Color:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class ILuminance:
    def get_effective(self) -> ILuminanceEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class ILuminanceEffectiveData:
    @property
    def brightness(self) -> float:
        ...

    @property
    def contrast(self) -> float:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IOuterShadow:
    def get_effective(self) -> IOuterShadowEffectiveData:
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @blur_radius.setter
    def blur_radius(self, value: float):
        ...

    @property
    def direction(self) -> float:
        ...

    @direction.setter
    def direction(self, value: float):
        ...

    @property
    def distance(self) -> float:
        ...

    @distance.setter
    def distance(self, value: float):
        ...

    @property
    def shadow_color(self) -> IColorFormat:
        ...

    @property
    def rectangle_align(self) -> RectangleAlignment:
        ...

    @rectangle_align.setter
    def rectangle_align(self, value: RectangleAlignment):
        ...

    @property
    def skew_horizontal(self) -> float:
        ...

    @skew_horizontal.setter
    def skew_horizontal(self, value: float):
        ...

    @property
    def skew_vertical(self) -> float:
        ...

    @skew_vertical.setter
    def skew_vertical(self, value: float):
        ...

    @property
    def rotate_shadow_with_shape(self) -> bool:
        ...

    @rotate_shadow_with_shape.setter
    def rotate_shadow_with_shape(self, value: bool):
        ...

    @property
    def scale_horizontal(self) -> float:
        ...

    @scale_horizontal.setter
    def scale_horizontal(self, value: float):
        ...

    @property
    def scale_vertical(self) -> float:
        ...

    @scale_vertical.setter
    def scale_vertical(self, value: float):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IOuterShadowEffectiveData:
    @property
    def blur_radius(self) -> float:
        ...

    @property
    def direction(self) -> float:
        ...

    @property
    def distance(self) -> float:
        ...

    @property
    def shadow_color(self) -> aspose.pydrawing.Color:
        ...

    @property
    def rectangle_align(self) -> RectangleAlignment:
        ...

    @property
    def skew_horizontal(self) -> float:
        ...

    @property
    def skew_vertical(self) -> float:
        ...

    @property
    def rotate_shadow_with_shape(self) -> bool:
        ...

    @property
    def scale_horizontal(self) -> float:
        ...

    @property
    def scale_vertical(self) -> float:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IPresetShadow:
    def get_effective(self) -> IPresetShadowEffectiveData:
        ...

    @property
    def direction(self) -> float:
        ...

    @direction.setter
    def direction(self, value: float):
        ...

    @property
    def distance(self) -> float:
        ...

    @distance.setter
    def distance(self, value: float):
        ...

    @property
    def shadow_color(self) -> IColorFormat:
        ...

    @property
    def preset(self) -> PresetShadowType:
        ...

    @preset.setter
    def preset(self, value: PresetShadowType):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IPresetShadowEffectiveData:
    @property
    def direction(self) -> float:
        ...

    @property
    def distance(self) -> float:
        ...

    @property
    def shadow_color(self) -> aspose.pydrawing.Color:
        ...

    @property
    def preset(self) -> PresetShadowType:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IReflection:
    def get_effective(self) -> IReflectionEffectiveData:
        ...

    @property
    def start_pos_alpha(self) -> float:
        ...

    @start_pos_alpha.setter
    def start_pos_alpha(self, value: float):
        ...

    @property
    def end_pos_alpha(self) -> float:
        ...

    @end_pos_alpha.setter
    def end_pos_alpha(self, value: float):
        ...

    @property
    def fade_direction(self) -> float:
        ...

    @fade_direction.setter
    def fade_direction(self, value: float):
        ...

    @property
    def start_reflection_opacity(self) -> float:
        ...

    @start_reflection_opacity.setter
    def start_reflection_opacity(self, value: float):
        ...

    @property
    def end_reflection_opacity(self) -> float:
        ...

    @end_reflection_opacity.setter
    def end_reflection_opacity(self, value: float):
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @blur_radius.setter
    def blur_radius(self, value: float):
        ...

    @property
    def direction(self) -> float:
        ...

    @direction.setter
    def direction(self, value: float):
        ...

    @property
    def distance(self) -> float:
        ...

    @distance.setter
    def distance(self, value: float):
        ...

    @property
    def rectangle_align(self) -> RectangleAlignment:
        ...

    @rectangle_align.setter
    def rectangle_align(self, value: RectangleAlignment):
        ...

    @property
    def skew_horizontal(self) -> float:
        ...

    @skew_horizontal.setter
    def skew_horizontal(self, value: float):
        ...

    @property
    def skew_vertical(self) -> float:
        ...

    @skew_vertical.setter
    def skew_vertical(self, value: float):
        ...

    @property
    def rotate_shadow_with_shape(self) -> bool:
        ...

    @rotate_shadow_with_shape.setter
    def rotate_shadow_with_shape(self, value: bool):
        ...

    @property
    def scale_horizontal(self) -> float:
        ...

    @scale_horizontal.setter
    def scale_horizontal(self, value: float):
        ...

    @property
    def scale_vertical(self) -> float:
        ...

    @scale_vertical.setter
    def scale_vertical(self, value: float):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IReflectionEffectiveData:
    @property
    def start_pos_alpha(self) -> float:
        ...

    @property
    def end_pos_alpha(self) -> float:
        ...

    @property
    def fade_direction(self) -> float:
        ...

    @property
    def start_reflection_opacity(self) -> float:
        ...

    @property
    def end_reflection_opacity(self) -> float:
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @property
    def direction(self) -> float:
        ...

    @property
    def distance(self) -> float:
        ...

    @property
    def rectangle_align(self) -> RectangleAlignment:
        ...

    @property
    def skew_horizontal(self) -> float:
        ...

    @property
    def skew_vertical(self) -> float:
        ...

    @property
    def rotate_shadow_with_shape(self) -> bool:
        ...

    @property
    def scale_horizontal(self) -> float:
        ...

    @property
    def scale_vertical(self) -> float:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class ISoftEdge:
    def get_effective(self) -> ISoftEdgeEffectiveData:
        ...

    @property
    def radius(self) -> float:
        ...

    @radius.setter
    def radius(self, value: float):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class ISoftEdgeEffectiveData:
    @property
    def radius(self) -> float:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class ITint:
    def get_effective(self) -> ITintEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class ITintEffectiveData:
    @property
    def hue(self) -> float:
        ...

    @property
    def amount(self) -> float:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class ImageTransformOCollectionEffectiveData:
    '''Immutable object that represents a readonly collection of effective image transform effects.'''
    def __init__(self):
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IEffectEffectiveData
        '''Returns element by index.'''
        ...

    ...

class ImageTransformOperation(aspose.slides.PVIObject):
    '''Represents abstract image transformation effect.'''
    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    ...

class ImageTransformOperationCollection(aspose.slides.PVIObject):
    '''Represents a collection of effects apllied to an image.'''
    def remove_at(self, index: int) -> None:
        '''Removes an image effect from a collection at the specified index.
        :param index: Index of an image effect that should be deleted.'''
        ...

    def add_alpha_bi_level_effect(self, threshold: float) -> IAlphaBiLevel:
        '''Adds the new Alpha Bi-Level effect to the end of a collection.
        :param threshold: The threshold value for the alpha bi-level effect.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_ceiling_effect(self) -> IAlphaCeiling:
        '''Adds the new Alpha Ceiling effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_floor_effect(self) -> IAlphaFloor:
        '''Adds the new Alpha Floor effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_inverse_effect(self) -> IAlphaInverse:
        '''Adds the new Alpha Inverse effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_modulate_effect(self) -> IAlphaModulate:
        '''Adds the new Alpha Modulate effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_modulate_fixed_effect(self, amount: float) -> IAlphaModulateFixed:
        '''Adds the new Alpha Modulate Fixed effect to the end of a collection.
        :param amount: The percentage amount to scale the alpha.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_replace_effect(self, alpha: float) -> IAlphaReplace:
        '''Adds the new Alpha Replace effect to the end of a collection.
        :param alpha: The new opacity value.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_bi_level_effect(self, threshold: float) -> IBiLevel:
        '''Adds the new Bi-Level (black/white) effect to the end of a collection.
        :param threshold: the luminance threshold for the Bi-Level effect.
                    Values greater than or equal to the threshold are set to white.
                    Values lesser than the threshold are set to black.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_blur_effect(self, radius: float, grow: bool) -> IBlur:
        '''Adds the new Blur effect to the end of a collection.
        :param radius: The radius of blur.
        :param grow: Specifies whether the bounds of the object should be grown as a result of the blurring.
                    True indicates the bounds are grown while false indicates that they are not.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_color_change_effect(self) -> IColorChange:
        '''Adds the new Color Change effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_color_replace_effect(self) -> IColorReplace:
        '''Adds the new Color Replacement effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_duotone_effect(self) -> IDuotone:
        '''Adds the new Duotone effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_fill_overlay_effect(self) -> IFillOverlay:
        '''Adds the new Fill Overlay effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_gray_scale_effect(self) -> IGrayScale:
        '''Adds the new Gray Scale effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_hsl_effect(self, hue: float, saturation: float, luminance: float) -> IHSL:
        '''Adds the new Hue/Saturation/Luminance effect to the end of a collection.
        :param hue: The number of degrees by which the hue is adjusted.
        :param saturation: The percentage by which the saturation is adjusted.
        :param luminance: The percentage by which the luminance is adjusted.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_luminance_effect(self, brightness: float, contrast: float) -> ILuminance:
        '''Adds the new Luminance effect to the end of a collection.
        :param brightness: The percent to change the brightness.
        :param contrast: The percent to change the contrast.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_tint_effect(self, hue: float, amount: float) -> ITint:
        '''Adds the new Tint effect to the end of a collection.
        :param hue: The hue towards which to tint.
        :param amount: Specifies by how much the color value is shifted.
        :returns: Index of the new image effect in a collection.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IImageTransformOperation
        '''Returns an :py:class:`aspose.slides.effects.ImageTransformOperation` from the collection by it's index.'''
        ...

    ...

class ImageTransformOperationFactory:
    '''Allows to create image transform operations'''
    def __init__(self):
        ...

    def create_alpha_bi_level(self, threshold: float) -> IAlphaBiLevel:
        '''Creates Alpha BiLevel effect.
        :param threshold: Threshold.
        :returns: Alpha BiLevel effect.'''
        ...

    def create_alph_ceiling(self) -> IAlphaCeiling:
        '''Creates Alpha Ceiling effect.
        :returns: Alpha Ceiling effect.'''
        ...

    def create_alpha_floor(self) -> IAlphaFloor:
        '''Creates Alpha floor effect.
        :returns: Alpha floor effect.'''
        ...

    def create_alpha_inverse(self) -> IAlphaInverse:
        '''Creates Alpha inverse effect.
        :returns: Alpha inverst effect.'''
        ...

    def create_alpha_modulate(self) -> IAlphaModulate:
        '''Creates Alpha modulate effect.
        :returns: Alpha modulate effect.'''
        ...

    def create_alpha_modulate_fixed(self, amount: float) -> IAlphaModulateFixed:
        '''Creates Alpha modulate fixed effect.
        :param amount: Amount.
        :returns: Alpha modulate fixed effect.'''
        ...

    def create_alpha_replace(self, alpha: float) -> IAlphaReplace:
        '''Creates Alpha replace effect.
        :param alpha: Alpha
        :returns: Alpha replace effect.'''
        ...

    def create_bi_level(self, threshold: float) -> IBiLevel:
        '''Creates BiLevel effect.
        :param threshold: Threshold.
        :returns: BiLevel effect.'''
        ...

    def create_blur(self, radius: float, grow: bool) -> IBlur:
        '''Creates Blur effect.
        :param radius: Radius.
        :param grow: Grow.
        :returns: Blur effect.'''
        ...

    def create_color_change(self) -> IColorChange:
        '''Creates Color change effect.
        :returns: Color change effect.'''
        ...

    def create_color_replace(self) -> IColorReplace:
        '''Creates Color replace effect.
        :returns: Color replace effect.'''
        ...

    def create_duotone(self) -> IDuotone:
        '''Creates Duotone effect.
        :returns: Duotone effect.'''
        ...

    def create_fill_overlay(self) -> IFillOverlay:
        '''Creates Fill overlay effect.
        :returns: Fill overlay effect.'''
        ...

    def create_gray_scale(self) -> IGrayScale:
        '''Creates Gray scale effect.
        :returns: Returns gray scale effect.'''
        ...

    def create_hsl(self, hue: float, saturation: float, luminance: float) -> IHSL:
        '''Creates Hue Saturation Luminance effect.
        :param hue: Hue.
        :param saturation: Saturation.
        :param luminance: Luminance.
        :returns: HSL effect.'''
        ...

    def create_luminance(self, brightness: float, contrast: float) -> ILuminance:
        '''Createtes Luminance effect.
        :param brightness: Brightness.
        :param contrast: Contrast.
        :returns: Luminance effect.'''
        ...

    def create_tint(self, hue: float, amount: float) -> ITint:
        '''Creates Tint effect.
        :param hue: Hue.
        :param amount: Amount.
        :returns: Tint effect.'''
        ...

    ...

class InnerShadow:
    '''Represents a Inner Shadow effect.'''
    def get_effective(self) -> IInnerShadowEffectiveData:
        '''Gets effective Inner Shadow effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IInnerShadowEffectiveData`.'''
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @blur_radius.setter
    def blur_radius(self, value: float):
        ...

    @property
    def direction(self) -> float:
        ...

    @direction.setter
    def direction(self, value: float):
        ...

    @property
    def distance(self) -> float:
        ...

    @distance.setter
    def distance(self, value: float):
        ...

    @property
    def shadow_color(self) -> IColorFormat:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class Luminance(ImageTransformOperation):
    '''Represents a Luminance effect.
                Brightness linearly shifts all colors closer to white or black.
                Contrast scales all colors to be either closer or further apart.'''
    def get_effective(self) -> ILuminanceEffectiveData:
        '''Gets effective Luminance effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.ILuminanceEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class OuterShadow:
    '''Represents an Outer Shadow effect.'''
    def get_effective(self) -> IOuterShadowEffectiveData:
        '''Gets effective Outer Shadow effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IOuterShadowEffectiveData`.'''
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @blur_radius.setter
    def blur_radius(self, value: float):
        ...

    @property
    def direction(self) -> float:
        ...

    @direction.setter
    def direction(self, value: float):
        ...

    @property
    def distance(self) -> float:
        ...

    @distance.setter
    def distance(self, value: float):
        ...

    @property
    def shadow_color(self) -> IColorFormat:
        ...

    @property
    def rectangle_align(self) -> RectangleAlignment:
        ...

    @rectangle_align.setter
    def rectangle_align(self, value: RectangleAlignment):
        ...

    @property
    def skew_horizontal(self) -> float:
        ...

    @skew_horizontal.setter
    def skew_horizontal(self, value: float):
        ...

    @property
    def skew_vertical(self) -> float:
        ...

    @skew_vertical.setter
    def skew_vertical(self, value: float):
        ...

    @property
    def rotate_shadow_with_shape(self) -> bool:
        ...

    @rotate_shadow_with_shape.setter
    def rotate_shadow_with_shape(self, value: bool):
        ...

    @property
    def scale_horizontal(self) -> float:
        ...

    @scale_horizontal.setter
    def scale_horizontal(self, value: float):
        ...

    @property
    def scale_vertical(self) -> float:
        ...

    @scale_vertical.setter
    def scale_vertical(self, value: float):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class PresetShadow:
    '''Represents a Preset Shadow effect.'''
    def get_effective(self) -> IPresetShadowEffectiveData:
        '''Gets effective Preset Shadow effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IPresetShadowEffectiveData`.'''
        ...

    @property
    def direction(self) -> float:
        ...

    @direction.setter
    def direction(self, value: float):
        ...

    @property
    def distance(self) -> float:
        ...

    @distance.setter
    def distance(self, value: float):
        ...

    @property
    def shadow_color(self) -> IColorFormat:
        ...

    @property
    def preset(self) -> PresetShadowType:
        ...

    @preset.setter
    def preset(self, value: PresetShadowType):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class Reflection:
    '''Represents a Reflection effect.'''
    def get_effective(self) -> IReflectionEffectiveData:
        '''Gets effective Reflection effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IReflectionEffectiveData`.'''
        ...

    @property
    def start_pos_alpha(self) -> float:
        ...

    @start_pos_alpha.setter
    def start_pos_alpha(self, value: float):
        ...

    @property
    def end_pos_alpha(self) -> float:
        ...

    @end_pos_alpha.setter
    def end_pos_alpha(self, value: float):
        ...

    @property
    def fade_direction(self) -> float:
        ...

    @fade_direction.setter
    def fade_direction(self, value: float):
        ...

    @property
    def start_reflection_opacity(self) -> float:
        ...

    @start_reflection_opacity.setter
    def start_reflection_opacity(self, value: float):
        ...

    @property
    def end_reflection_opacity(self) -> float:
        ...

    @end_reflection_opacity.setter
    def end_reflection_opacity(self, value: float):
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @blur_radius.setter
    def blur_radius(self, value: float):
        ...

    @property
    def direction(self) -> float:
        ...

    @direction.setter
    def direction(self, value: float):
        ...

    @property
    def distance(self) -> float:
        ...

    @distance.setter
    def distance(self, value: float):
        ...

    @property
    def rectangle_align(self) -> RectangleAlignment:
        ...

    @rectangle_align.setter
    def rectangle_align(self, value: RectangleAlignment):
        ...

    @property
    def skew_horizontal(self) -> float:
        ...

    @skew_horizontal.setter
    def skew_horizontal(self, value: float):
        ...

    @property
    def skew_vertical(self) -> float:
        ...

    @skew_vertical.setter
    def skew_vertical(self, value: float):
        ...

    @property
    def rotate_shadow_with_shape(self) -> bool:
        ...

    @rotate_shadow_with_shape.setter
    def rotate_shadow_with_shape(self, value: bool):
        ...

    @property
    def scale_horizontal(self) -> float:
        ...

    @scale_horizontal.setter
    def scale_horizontal(self, value: float):
        ...

    @property
    def scale_vertical(self) -> float:
        ...

    @scale_vertical.setter
    def scale_vertical(self, value: float):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class SoftEdge:
    '''Represents a soft edge effect. 
                The edges of the shape are blurred, while the fill is not affected.'''
    def get_effective(self) -> ISoftEdgeEffectiveData:
        '''Gets effective Soft Edge effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.ISoftEdgeEffectiveData`.'''
        ...

    @property
    def radius(self) -> float:
        ...

    @radius.setter
    def radius(self, value: float):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class Tint(ImageTransformOperation):
    '''Represents a Tint effect.
                Shifts effect color values towards/away from hue by the specified amount.'''
    def get_effective(self) -> ITintEffectiveData:
        '''Gets effective Tint effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.ITintEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

