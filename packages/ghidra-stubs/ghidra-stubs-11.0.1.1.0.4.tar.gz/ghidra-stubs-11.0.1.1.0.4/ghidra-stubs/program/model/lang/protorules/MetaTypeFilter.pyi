import ghidra.program.model.data
import ghidra.program.model.lang.protorules
import ghidra.program.model.pcode
import ghidra.xml
import java.lang
import java.util


class MetaTypeFilter(ghidra.program.model.lang.protorules.SizeRestrictedFilter):
    """
    Filter on a single meta data-type. Filters on TYPE_STRUCT or TYPE_FLOAT etc.
     Additional filtering on size of the data-type can be configured.
    """





    @overload
    def __init__(self, meta: int):
        """
        Constructor for use with decode().
        @param meta is the data-type metatype to filter on
        """
        ...

    @overload
    def __init__(self, meta: int, min: int, max: int):
        """
        Constructor
        @param meta is the data-type metatype to filter on
        @param min is the minimum size in bytes
        @param max is the maximum size in bytes
        """
        ...



    def clone(self) -> ghidra.program.model.lang.protorules.DatatypeFilter: ...

    def encode(self, encoder: ghidra.program.model.pcode.Encoder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def extractPrimitives(__a0: ghidra.program.model.data.DataType, __a1: int, __a2: java.util.ArrayList) -> bool: ...

    def filter(self, dt: ghidra.program.model.data.DataType) -> bool: ...

    def filterOnSize(self, dt: ghidra.program.model.data.DataType) -> bool:
        """
        Enforce any size bounds on a given data-type.
         If \b maxSize is not zero, the data-type is checked to see if its size in bytes
         falls between \b minSize and \b maxSize inclusive.
        @param dt is the data-type to test
        @return true if the data-type meets the size restrictions
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEquivalent(self, op: ghidra.program.model.lang.protorules.DatatypeFilter) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def restoreFilterXml(__a0: ghidra.xml.XmlPullParser) -> ghidra.program.model.lang.protorules.DatatypeFilter: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

