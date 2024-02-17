import ghidra.program.model.data
import ghidra.program.model.lang.protorules
import ghidra.program.model.pcode
import ghidra.xml
import java.lang
import java.util


class DatatypeFilter(object):
    """
    A filter selecting a specific class of data-type.
     A test of whether  data-type belongs to its class can be performed by calling
     the filter() method.
    """









    def clone(self) -> ghidra.program.model.lang.protorules.DatatypeFilter:
        """
        Make a copy of this filter
        @return the new copy
        """
        ...

    def encode(self, encoder: ghidra.program.model.pcode.Encoder) -> None:
        """
        Encode this filter and its configuration to a stream
        @param encoder is the stream encoder
        @throws IOException for problems writing to the stream
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def extractPrimitives(__a0: ghidra.program.model.data.DataType, __a1: int, __a2: java.util.ArrayList) -> bool: ...

    def filter(self, dt: ghidra.program.model.data.DataType) -> bool:
        """
        Test whether the given data-type belongs to this filter's data-type class
        @param dt is the given data-type to test
        @return true if the data-type is in the class, false otherwise
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEquivalent(self, op: ghidra.program.model.lang.protorules.DatatypeFilter) -> bool:
        """
        Test if the given filter is configured and performs identically to this
        @param op is the given filter
        @return true if the two filters are equivalent
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def restoreFilterXml(parser: ghidra.xml.XmlPullParser) -> ghidra.program.model.lang.protorules.DatatypeFilter:
        """
        Instantiate a filter from the given stream.
        @param parser is the given stream decoder
        @return the new data-type filter instance
        @throws XmlParseException for problems reading the stream
        """
        ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser) -> None:
        """
        Configure details of the data-type class being filtered from the given stream
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

