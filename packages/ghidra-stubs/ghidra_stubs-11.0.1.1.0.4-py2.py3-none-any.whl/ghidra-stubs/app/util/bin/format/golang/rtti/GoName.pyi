from typing import List
import ghidra.app.util.bin.format.golang.rtti
import ghidra.app.util.bin.format.golang.structmapping
import ghidra.program.model.data
import java.lang
import java.util


class GoName(object, ghidra.app.util.bin.format.golang.structmapping.StructureReader, ghidra.app.util.bin.format.golang.structmapping.StructureMarkup):
    """
    Represents a golang "name" construct, which isn't represented in go as a normal structure
     since it is full of variable length and optional fields.
 
     struct {
     	byte flag;
     	varint strlen;
     	char[strlen] chars; 
     	(optional: varint tag_strlen; char [tag_strlen];)
     	(optional: int32 pkgpath)
     }
 
     Because this type has variable length fields (@FieldOutput(isVariableLength=true)), there will
     be unique structure data types produced for each size combination of a GoName structure, and
     will be named "GoName_N_M", where N and M are the lengths of the variable fields [name, tag]
    """






    class Flag(java.lang.Enum):
        EMBEDDED: ghidra.app.util.bin.format.golang.rtti.GoName.Flag = EMBEDDED
        EXPORTED: ghidra.app.util.bin.format.golang.rtti.GoName.Flag = EXPORTED
        HAS_PKGPATH: ghidra.app.util.bin.format.golang.rtti.GoName.Flag = HAS_PKGPATH
        HAS_TAG: ghidra.app.util.bin.format.golang.rtti.GoName.Flag = HAS_TAG







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def describeConstable(self) -> java.util.Optional: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def isSet(self, __a0: int) -> bool: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        @staticmethod
        def parseFlags(__a0: int) -> java.util.Set: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.golang.rtti.GoName.Flag: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.golang.rtti.GoName.Flag]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self): ...



    def additionalMarkup(self, __a0: ghidra.app.util.bin.format.golang.structmapping.MarkupSession) -> None: ...

    @staticmethod
    def createFakeInstance(fakeName: unicode) -> ghidra.app.util.bin.format.golang.rtti.GoName:
        """
        Create a GoName instance that supplies a specified name.
        @param fakeName string name to return from the GoName's getName()
        @return new GoName instance that can only be used to call getName()
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExternalInstancesToMarkup(self) -> List[object]: ...

    def getFlags(self) -> int:
        """
        Returns the flags found in this structure.
        @return flags, as an int
        """
        ...

    def getFlagsSet(self) -> java.util.Set:
        """
        Returns the flags found in this structure.
        @return flags, as a set of {@link Flag} enum values
        """
        ...

    def getFullNameString(self) -> unicode:
        """
        Returns a descriptive string containing the full name value.
        @return descriptive string
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name value.
        @return name string
        """
        ...

    def getPkgPath(self) -> ghidra.app.util.bin.format.golang.rtti.GoName:
        """
        Returns the package path string, or null if not present.
        @return package path string, or null if not present
        @throws IOException if error reading data
        """
        ...

    def getPkgPathDataType(self) -> ghidra.program.model.data.DataType:
        """
        Returns the data type needed to store the pkg path offset field, called by serialization
         from the fieldoutput annotation.
        @return Ghidra data type needed to store the pkg path offset field, or null if not present
        """
        ...

    def getStructureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    def getStructureLabel(self) -> unicode: ...

    def getStructureName(self) -> unicode: ...

    def getStructureNamespace(self) -> unicode: ...

    def getTag(self) -> unicode:
        """
        Returns the tag string.
        @return tag string
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readStructure(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def externalInstancesToMarkup(self) -> List[object]: ...

    @property
    def flags(self) -> int: ...

    @property
    def flagsSet(self) -> java.util.Set: ...

    @property
    def fullNameString(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def pkgPath(self) -> ghidra.app.util.bin.format.golang.rtti.GoName: ...

    @property
    def pkgPathDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def structureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    @property
    def structureLabel(self) -> unicode: ...

    @property
    def structureName(self) -> unicode: ...

    @property
    def structureNamespace(self) -> unicode: ...

    @property
    def tag(self) -> unicode: ...