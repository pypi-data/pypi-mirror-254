import ghidra.program.model.lang
import ghidra.program.model.lang.protorules
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class AndFilter(object, ghidra.program.model.lang.protorules.QualifierFilter):
    """
    Logically AND multiple QualifierFilters together into a single filter.
     An instances contains some number of other arbitrary filters.  In order for this filter to
     pass, all these contained filters must pass.
    """





    @overload
    def __init__(self, op: ghidra.program.model.lang.protorules.AndFilter): ...

    @overload
    def __init__(self, __a0: java.util.ArrayList): ...



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

