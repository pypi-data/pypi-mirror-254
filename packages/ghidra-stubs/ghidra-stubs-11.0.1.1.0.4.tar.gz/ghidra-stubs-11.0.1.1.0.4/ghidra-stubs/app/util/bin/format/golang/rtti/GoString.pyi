from typing import List
import ghidra.app.util.bin.format.golang.rtti
import ghidra.app.util.bin.format.golang.structmapping
import ghidra.program.model.address
import java.lang
import java.util.function


class GoString(object, ghidra.app.util.bin.format.golang.structmapping.StructureMarkup):
    """
    A structure that represents a golang string instance.
    """

    MAX_SANE_STR_LEN: int = 1048576



    def __init__(self): ...



    def additionalMarkup(self, session: ghidra.app.util.bin.format.golang.structmapping.MarkupSession) -> None: ...

    @staticmethod
    def createInlineString(goBinary: ghidra.app.util.bin.format.golang.rtti.GoRttiMapper, stringData: ghidra.program.model.address.Address, len: long) -> ghidra.app.util.bin.format.golang.rtti.GoString:
        """
        Creates a artificial gostring instance that was not read from a memory location.
         <p>
        @param goBinary {@link GoRttiMapper}
        @param stringData location of char array
        @param len length of char array
        @return new GoString instance
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExternalInstancesToMarkup(self) -> List[object]: ...

    def getLength(self) -> long:
        """
        Returns the length of the string data
        @return length of the string data
        """
        ...

    def getStringAddr(self) -> ghidra.program.model.address.Address:
        """
        Returns the address of the char data, referenced via the str field's markup annotation
        @return address of the char data
        """
        ...

    def getStringDataRange(self) -> ghidra.program.model.address.AddressRange:
        """
        Returns an AddressRange that encompasses the string char data.
        @return AddressRange that encompasses the string char data
        """
        ...

    def getStringValue(self) -> unicode:
        """
        Returns the string value.
        @return string value
        @throws IOException if error reading char data
        """
        ...

    def getStructureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    def getStructureLabel(self) -> unicode: ...

    def getStructureName(self) -> unicode: ...

    def getStructureNamespace(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isValid(self, charValidRange: ghidra.program.model.address.AddressSetView, stringContentValidator: java.util.function.Predicate) -> bool:
        """
        Returns true if this string instance is valid and probably contains a go string.
        @param charValidRange addresses that are valid locations for a string's char[] data
        @param stringContentValidator a callback that will test a recovered string for validity
        @return boolean true if valid string, false if not valid string
        @throws IOException if error reading data
        """
        ...

    def isValidInlineString(self, charValidRange: ghidra.program.model.address.AddressSetView, stringContentValidator: java.util.function.Predicate) -> bool:
        """
        Returns true if this string instance points to valid char[] data.
        @param charValidRange addresses that are valid locations for a string's char[] data
        @param stringContentValidator a callback that will test a recovered string for validity
        @return boolean true if valid string, false if not valid string
        @throws IOException if error reading data
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

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
    def length(self) -> long: ...

    @property
    def stringAddr(self) -> ghidra.program.model.address.Address: ...

    @property
    def stringDataRange(self) -> ghidra.program.model.address.AddressRange: ...

    @property
    def stringValue(self) -> unicode: ...

    @property
    def structureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    @property
    def structureLabel(self) -> unicode: ...

    @property
    def structureName(self) -> unicode: ...

    @property
    def structureNamespace(self) -> unicode: ...