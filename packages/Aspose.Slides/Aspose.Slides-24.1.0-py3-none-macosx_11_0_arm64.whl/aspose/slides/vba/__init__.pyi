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

class IVbaModule:
    @property
    def name(self) -> string:
        ...

    @property
    def source_code(self) -> string:
        ...

    @source_code.setter
    def source_code(self, value: string):
        ...

    ...

class IVbaModuleCollection:
    def add_empty_module(self, name: string) -> IVbaModule:
        ...

    def remove(self, value: IVbaModule) -> None:
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IVbaModule
        ...

    ...

class IVbaProject:
    def to_binary(self) -> bytes:
        ...

    @property
    def name(self) -> string:
        ...

    @property
    def modules(self) -> IVbaModuleCollection:
        ...

    @property
    def references(self) -> IVbaReferenceCollection:
        ...

    ...

class IVbaProjectFactory:
    def create_vba_project(self) -> IVbaProject:
        ...

    def read_vba_project(self, data: bytes) -> IVbaProject:
        ...

    ...

class IVbaReference:
    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    ...

class IVbaReferenceCollection:
    def add(self, value: IVbaReference) -> None:
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IVbaReference
        ...

    ...

class IVbaReferenceFactory:
    def create_ole_type_lib_reference(self, name: string, libid: string) -> IVbaReferenceOleTypeLib:
        ...

    ...

class IVbaReferenceOleTwiddledTypeLib:
    @property
    def as_i_vba_reference(self) -> IVbaReference:
        ...

    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    ...

class IVbaReferenceOleTypeLib:
    @property
    def libid(self) -> string:
        ...

    @libid.setter
    def libid(self, value: string):
        ...

    @property
    def as_i_vba_reference(self) -> IVbaReference:
        ...

    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    ...

class IVbaReferenceProject:
    @property
    def as_i_vba_reference(self) -> IVbaReference:
        ...

    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    ...

class VbaModule:
    '''Represents module that is contained in VBA project.'''
    @property
    def name(self) -> string:
        ...

    @property
    def source_code(self) -> string:
        ...

    @source_code.setter
    def source_code(self, value: string):
        ...

    ...

class VbaModuleCollection:
    '''Represents a collection of a VBA Project modules.'''
    def remove(self, value: IVbaModule) -> None:
        '''Removes the first occurrence of a specific object from the collection.
        :param value: The module to remove from the collection.'''
        ...

    def add_empty_module(self, name: string) -> IVbaModule:
        '''Adds a new empty module to the VBA Project.
        :param name: Name of the module
        :returns: Added module.'''
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IVbaModule
        '''Gets the element at the specified index.'''
        ...

    ...

class VbaProject:
    '''Represents VBA project with presentation macros.'''
    def __init__(self):
        '''This constructor creates new VBA project from scratch.
                    Project will be created in 1252 Windows Latin 1 (ANSI) codepage'''
        ...

    def __init__(self, data: bytes):
        '''This constructor loads VBA project from binary representation of OLE container.'''
        ...

    def to_binary(self) -> bytes:
        '''Returns the binary representation of the VBA project as OLE container
        :returns: Binary representation of the VBA project as OLE container'''
        ...

    @property
    def name(self) -> string:
        ...

    @property
    def modules(self) -> IVbaModuleCollection:
        ...

    @property
    def references(self) -> IVbaReferenceCollection:
        ...

    ...

class VbaProjectFactory:
    '''Allows to create VBA project via COM interface'''
    def __init__(self):
        ...

    def create_vba_project(self) -> IVbaProject:
        '''Creates new VBA project.
        :returns: New VBA project'''
        ...

    def read_vba_project(self, data: bytes) -> IVbaProject:
        '''Reads VBA project from OLE container.
        :returns: Read VBA project'''
        ...

    @classmethod
    @property
    def instance(cls) -> VbaProjectFactory:
        ...

    ...

class VbaReferenceCollection:
    '''Represents a collection of a VBA Project references.'''
    def add(self, value: IVbaReference) -> None:
        '''Adds the new reference to references collection'''
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IVbaReference
        '''Gets the element at the specified index.'''
        ...

    ...

class VbaReferenceFactory:
    '''Allows to create VBA project references via COM interface'''
    def __init__(self):
        ...

    def create_ole_type_lib_reference(self, name: string, libid: string) -> IVbaReferenceOleTypeLib:
        '''Creates new OLE Automation type library reference.
        :returns: New OLE Automation type library reference'''
        ...

    @classmethod
    @property
    def instance(cls) -> VbaReferenceFactory:
        ...

    ...

class VbaReferenceOleTypeLib:
    '''Represents OLE Automation type library reference.'''
    def __init__(self, name: string, libid: string):
        '''This constructor creates new OLE Automation type library reference.'''
        ...

    @property
    def name(self) -> string:
        ...

    @name.setter
    def name(self, value: string):
        ...

    @property
    def libid(self) -> string:
        ...

    @libid.setter
    def libid(self, value: string):
        ...

    @property
    def as_i_vba_reference(self) -> IVbaReference:
        ...

    ...

