from typing import List
import ghidra.app.util.bin.format.golang.structmapping
import ghidra.program.model.data
import java.lang


class GoVarlenString(object, ghidra.app.util.bin.format.golang.structmapping.StructureReader):
    """
    A pascal-ish string, using a LEB128 value as the length of the following bytes.
 
     Used mainly in lower-level RTTI structures, this class is a ghidra'ism used to parse the
     golang rtti data and does not have a counterpart in the golang src.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getBytes(self) -> List[int]:
        """
        Returns the raw bytes of the string
        @return raw bytes of the string
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getString(self) -> unicode:
        """
        Returns the string value.
        @return string value
        """
        ...

    def getStrlen(self) -> int:
        """
        Returns the string's length
        @return string's length
        """
        ...

    def getStrlenDataType(self) -> ghidra.program.model.data.DataTypeInstance:
        """
        Returns the data type that is needed to hold the string length field.
        @return data type needed to hold the string length field
        """
        ...

    def getStrlenLen(self) -> int:
        """
        Returns the string length's length (length of the leb128 number)
        @return string length's length
        """
        ...

    def getValueDataType(self) -> ghidra.program.model.data.DataType:
        """
        Returns the data type that holds the raw string value.
        @return data type that holds the raw string value.
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
    def bytes(self) -> List[int]: ...

    @property
    def string(self) -> unicode: ...

    @property
    def strlen(self) -> int: ...

    @property
    def strlenDataType(self) -> ghidra.program.model.data.DataTypeInstance: ...

    @property
    def strlenLen(self) -> int: ...

    @property
    def valueDataType(self) -> ghidra.program.model.data.DataType: ...