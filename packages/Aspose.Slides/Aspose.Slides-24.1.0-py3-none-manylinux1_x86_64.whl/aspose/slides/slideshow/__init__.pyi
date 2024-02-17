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

class CornerDirectionTransition(TransitionValueBase):
    '''Corner direction slide transition effect.'''
    @property
    def direction(self) -> TransitionCornerDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionCornerDirectionType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class EightDirectionTransition(TransitionValueBase):
    '''Eight direction slide transition effect.'''
    @property
    def direction(self) -> TransitionEightDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionEightDirectionType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class EmptyTransition(TransitionValueBase):
    '''Empty slide transition effect.'''
    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class FlyThroughTransition(TransitionValueBase):
    '''Fly-through slide transition effect.'''
    @property
    def direction(self) -> TransitionInOutDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        ...

    @property
    def has_bounce(self) -> bool:
        ...

    @has_bounce.setter
    def has_bounce(self, value: bool):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class GlitterTransition(TransitionValueBase):
    '''Glitter slide transition effect.'''
    @property
    def direction(self) -> TransitionSideDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionSideDirectionType):
        ...

    @property
    def pattern(self) -> TransitionPattern:
        ...

    @pattern.setter
    def pattern(self, value: TransitionPattern):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class ICornerDirectionTransition:
    @property
    def direction(self) -> TransitionCornerDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionCornerDirectionType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IEightDirectionTransition:
    @property
    def direction(self) -> TransitionEightDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionEightDirectionType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IEmptyTransition:
    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IFlyThroughTransition:
    @property
    def direction(self) -> TransitionInOutDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        ...

    @property
    def has_bounce(self) -> bool:
        ...

    @has_bounce.setter
    def has_bounce(self, value: bool):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IGlitterTransition:
    @property
    def direction(self) -> TransitionSideDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionSideDirectionType):
        ...

    @property
    def pattern(self) -> TransitionPattern:
        ...

    @pattern.setter
    def pattern(self, value: TransitionPattern):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IInOutTransition:
    @property
    def direction(self) -> TransitionInOutDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class ILeftRightDirectionTransition:
    @property
    def direction(self) -> TransitionLeftRightDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionLeftRightDirectionType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IMorphTransition:
    @property
    def morph_type(self) -> TransitionMorphType:
        ...

    @morph_type.setter
    def morph_type(self, value: TransitionMorphType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IOptionalBlackTransition:
    @property
    def from_black(self) -> bool:
        ...

    @from_black.setter
    def from_black(self, value: bool):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IOrientationTransition:
    @property
    def direction(self) -> Orientation:
        ...

    @direction.setter
    def direction(self, value: Orientation):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IRevealTransition:
    @property
    def direction(self) -> TransitionLeftRightDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionLeftRightDirectionType):
        ...

    @property
    def through_black(self) -> bool:
        ...

    @through_black.setter
    def through_black(self, value: bool):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IRippleTransition:
    @property
    def direction(self) -> TransitionCornerAndCenterDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionCornerAndCenterDirectionType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IShredTransition:
    @property
    def direction(self) -> TransitionInOutDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        ...

    @property
    def pattern(self) -> TransitionShredPattern:
        ...

    @pattern.setter
    def pattern(self, value: TransitionShredPattern):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class ISideDirectionTransition:
    @property
    def direction(self) -> TransitionSideDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionSideDirectionType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class ISplitTransition:
    @property
    def direction(self) -> TransitionInOutDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        ...

    @property
    def orientation(self) -> Orientation:
        ...

    @orientation.setter
    def orientation(self, value: Orientation):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class ITransitionValueBase:
    ...

class IWheelTransition:
    @property
    def spokes(self) -> int:
        ...

    @spokes.setter
    def spokes(self, value: int):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class InOutTransition(TransitionValueBase):
    '''In-Out slide transition effect.'''
    @property
    def direction(self) -> TransitionInOutDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class LeftRightDirectionTransition(TransitionValueBase):
    '''Left-right direction slide transition effect.'''
    @property
    def direction(self) -> TransitionLeftRightDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionLeftRightDirectionType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class MorphTransition(TransitionValueBase):
    '''Ripple slide transition effect.'''
    @property
    def morph_type(self) -> TransitionMorphType:
        ...

    @morph_type.setter
    def morph_type(self, value: TransitionMorphType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class OptionalBlackTransition(TransitionValueBase):
    '''Optional black slide transition effect.'''
    @property
    def from_black(self) -> bool:
        ...

    @from_black.setter
    def from_black(self, value: bool):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class OrientationTransition(TransitionValueBase):
    '''Orientation slide transition effect.'''
    @property
    def direction(self) -> Orientation:
        ...

    @direction.setter
    def direction(self, value: Orientation):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class RevealTransition(TransitionValueBase):
    '''Reveal slide transition effect.'''
    @property
    def direction(self) -> TransitionLeftRightDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionLeftRightDirectionType):
        ...

    @property
    def through_black(self) -> bool:
        ...

    @through_black.setter
    def through_black(self, value: bool):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class RippleTransition(TransitionValueBase):
    '''Ripple slide transition effect.'''
    @property
    def direction(self) -> TransitionCornerAndCenterDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionCornerAndCenterDirectionType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class ShredTransition(TransitionValueBase):
    '''Shred slide transition effect.'''
    @property
    def direction(self) -> TransitionInOutDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        ...

    @property
    def pattern(self) -> TransitionShredPattern:
        ...

    @pattern.setter
    def pattern(self, value: TransitionShredPattern):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class SideDirectionTransition(TransitionValueBase):
    '''Side direction slide transition effect.'''
    @property
    def direction(self) -> TransitionSideDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionSideDirectionType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class SlideShowTransition:
    '''Represents slide show transition.'''
    @property
    def sound(self) -> IAudio:
        ...

    @sound.setter
    def sound(self, value: IAudio):
        ...

    @property
    def sound_mode(self) -> TransitionSoundMode:
        ...

    @sound_mode.setter
    def sound_mode(self, value: TransitionSoundMode):
        ...

    @property
    def sound_loop(self) -> bool:
        ...

    @sound_loop.setter
    def sound_loop(self, value: bool):
        ...

    @property
    def advance_on_click(self) -> bool:
        ...

    @advance_on_click.setter
    def advance_on_click(self, value: bool):
        ...

    @property
    def advance_after(self) -> bool:
        ...

    @advance_after.setter
    def advance_after(self, value: bool):
        ...

    @property
    def advance_after_time(self) -> int:
        ...

    @advance_after_time.setter
    def advance_after_time(self, value: int):
        ...

    @property
    def speed(self) -> TransitionSpeed:
        ...

    @speed.setter
    def speed(self, value: TransitionSpeed):
        ...

    @property
    def value(self) -> ITransitionValueBase:
        ...

    @property
    def type(self) -> TransitionType:
        ...

    @type.setter
    def type(self, value: TransitionType):
        ...

    @property
    def sound_is_built_in(self) -> bool:
        ...

    @sound_is_built_in.setter
    def sound_is_built_in(self, value: bool):
        ...

    @property
    def sound_name(self) -> string:
        ...

    @sound_name.setter
    def sound_name(self, value: string):
        ...

    ...

class SplitTransition(TransitionValueBase):
    '''Split slide transition effect.'''
    @property
    def direction(self) -> TransitionInOutDirectionType:
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        ...

    @property
    def orientation(self) -> Orientation:
        ...

    @orientation.setter
    def orientation(self, value: Orientation):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class TransitionValueBase:
    '''Base class for slide transition effects.'''
    ...

class WheelTransition(TransitionValueBase):
    '''Wheel slide transition effect.'''
    @property
    def spokes(self) -> int:
        ...

    @spokes.setter
    def spokes(self, value: int):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class TransitionCornerAndCenterDirectionType:
    @classmethod
    @property
    def LEFT_DOWN(cls) -> TransitionCornerAndCenterDirectionType:
        ...

    @classmethod
    @property
    def LEFT_UP(cls) -> TransitionCornerAndCenterDirectionType:
        ...

    @classmethod
    @property
    def RIGHT_DOWN(cls) -> TransitionCornerAndCenterDirectionType:
        ...

    @classmethod
    @property
    def RIGHT_UP(cls) -> TransitionCornerAndCenterDirectionType:
        ...

    @classmethod
    @property
    def CENTER(cls) -> TransitionCornerAndCenterDirectionType:
        ...

    ...

class TransitionCornerDirectionType:
    @classmethod
    @property
    def LEFT_DOWN(cls) -> TransitionCornerDirectionType:
        ...

    @classmethod
    @property
    def LEFT_UP(cls) -> TransitionCornerDirectionType:
        ...

    @classmethod
    @property
    def RIGHT_DOWN(cls) -> TransitionCornerDirectionType:
        ...

    @classmethod
    @property
    def RIGHT_UP(cls) -> TransitionCornerDirectionType:
        ...

    ...

class TransitionEightDirectionType:
    @classmethod
    @property
    def LEFT_DOWN(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def LEFT_UP(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def RIGHT_DOWN(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def RIGHT_UP(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def LEFT(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def UP(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def DOWN(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def RIGHT(cls) -> TransitionEightDirectionType:
        ...

    ...

class TransitionInOutDirectionType:
    @classmethod
    @property
    def IN(cls) -> TransitionInOutDirectionType:
        ...

    @classmethod
    @property
    def OUT(cls) -> TransitionInOutDirectionType:
        ...

    ...

class TransitionLeftRightDirectionType:
    @classmethod
    @property
    def LEFT(cls) -> TransitionLeftRightDirectionType:
        ...

    @classmethod
    @property
    def RIGHT(cls) -> TransitionLeftRightDirectionType:
        ...

    ...

class TransitionMorphType:
    @classmethod
    @property
    def BY_OBJECT(cls) -> TransitionMorphType:
        ...

    @classmethod
    @property
    def BY_WORD(cls) -> TransitionMorphType:
        ...

    @classmethod
    @property
    def BY_CHAR(cls) -> TransitionMorphType:
        ...

    ...

class TransitionPattern:
    @classmethod
    @property
    def DIAMOND(cls) -> TransitionPattern:
        ...

    @classmethod
    @property
    def HEXAGON(cls) -> TransitionPattern:
        ...

    ...

class TransitionShredPattern:
    @classmethod
    @property
    def STRIP(cls) -> TransitionShredPattern:
        ...

    @classmethod
    @property
    def RECTANGLE(cls) -> TransitionShredPattern:
        ...

    ...

class TransitionSideDirectionType:
    @classmethod
    @property
    def LEFT(cls) -> TransitionSideDirectionType:
        ...

    @classmethod
    @property
    def UP(cls) -> TransitionSideDirectionType:
        ...

    @classmethod
    @property
    def DOWN(cls) -> TransitionSideDirectionType:
        ...

    @classmethod
    @property
    def RIGHT(cls) -> TransitionSideDirectionType:
        ...

    ...

class TransitionSoundMode:
    @classmethod
    @property
    def NOT_DEFINED(cls) -> TransitionSoundMode:
        ...

    @classmethod
    @property
    def START_SOUND(cls) -> TransitionSoundMode:
        ...

    @classmethod
    @property
    def STOP_PREVOIUS_SOUND(cls) -> TransitionSoundMode:
        ...

    ...

class TransitionSpeed:
    @classmethod
    @property
    def FAST(cls) -> TransitionSpeed:
        ...

    @classmethod
    @property
    def MEDIUM(cls) -> TransitionSpeed:
        ...

    @classmethod
    @property
    def SLOW(cls) -> TransitionSpeed:
        ...

    ...

class TransitionType:
    @classmethod
    @property
    def NONE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def BLINDS(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def CHECKER(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def CIRCLE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def COMB(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def COVER(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def CUT(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def DIAMOND(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def DISSOLVE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def FADE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def NEWSFLASH(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def PLUS(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def PULL(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def PUSH(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def RANDOM(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def RANDOM_BAR(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def SPLIT(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def STRIPS(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def WEDGE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def WHEEL(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def WIPE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def ZOOM(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def VORTEX(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def SWITCH(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def FLIP(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def RIPPLE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def HONEYCOMB(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def CUBE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def BOX(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def ROTATE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def ORBIT(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def DOORS(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def WINDOW(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def FERRIS(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def GALLERY(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def CONVEYOR(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def PAN(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def GLITTER(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def WARP(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def FLYTHROUGH(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def FLASH(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def SHRED(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def REVEAL(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def WHEEL_REVERSE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def FALL_OVER(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def DRAPE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def CURTAINS(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def WIND(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def PRESTIGE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def FRACTURE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def CRUSH(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def PEEL_OFF(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def PAGE_CURL_DOUBLE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def PAGE_CURL_SINGLE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def AIRPLANE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def ORIGAMI(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def MORPH(cls) -> TransitionType:
        ...

    ...

