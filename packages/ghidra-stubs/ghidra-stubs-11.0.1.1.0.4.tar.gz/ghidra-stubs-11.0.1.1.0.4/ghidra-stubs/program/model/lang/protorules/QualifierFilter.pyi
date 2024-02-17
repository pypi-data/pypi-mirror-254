import ghidra.program.model.lang
import ghidra.program.model.lang.protorules
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class QualifierFilter(object):
    """
    A filter on some aspect of a specific function prototype.
     An instance is configured via the restoreXml() method, then a test of whether
     a function prototype meets its criteria can be performed by calling its filter() method.
    """









    def clone(self) -> ghidra.program.model.lang.protorules.QualifierFilter:
        """
        Make a copy of this qualifier
        @return the copy
        """
        ...

    def encode(self, encoder: ghidra.program.model.pcode.Encoder) -> None:
        """
        Save this filter and its configuration to a stream
        @param encoder is the stream encoder
        @throws IOException for problems writing to the stream
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def filter(self, proto: ghidra.program.model.lang.PrototypePieces, pos: int) -> bool:
        """
        Test whether the given function prototype meets this filter's criteria
        @param proto is the high-level description of the function prototype to test
        @param pos is the position of a specific output (pos=-1) or input (pos >=0) in context
        @return true if the prototype meets the criteria, false otherwise
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEquivalent(self, op: ghidra.program.model.lang.protorules.QualifierFilter) -> bool:
        """
        Test if the given filter is configured and performs identically to this
        @param op is the given filter
        @return true if the two filters are equivalent
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def restoreFilterXml(parser: ghidra.xml.XmlPullParser) -> ghidra.program.model.lang.protorules.QualifierFilter:
        """
        Instantiate a qualifier from the stream. If the next element is not a qualifier,
         return null.
        @param parser is the given stream decoder
        @return the new qualifier instance or null
        @throws XmlParseException for problems decoding the stream
        """
        ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser) -> None:
        """
        Configure details of the criteria being filtered from the given stream
        @param parser is the given stream decoder
        @throws XmlParseException if there are problems with the stream
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

