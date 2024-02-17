import ghidra.program.model.lang
import ghidra.program.model.lang.protorules
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class DatatypeMatchFilter(object, ghidra.program.model.lang.protorules.QualifierFilter):
    """
    Check if the function signature has a specific data-type in a specific position.
     This filter does not match against the data-type in the current position
     being assigned, but against a parameter at a fixed position.
    """





    def __init__(self): ...



    def clone(self) -> ghidra.program.model.lang.protorules.QualifierFilter: ...

    def encode(self, encoder: ghidra.program.model.pcode.Encoder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def filter(self, proto: ghidra.program.model.lang.PrototypePieces, pos: int) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEquivalent(self, op: ghidra.program.model.lang.protorules.QualifierFilter) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def restoreFilterXml(__a0: ghidra.xml.XmlPullParser) -> ghidra.program.model.lang.protorules.QualifierFilter: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

