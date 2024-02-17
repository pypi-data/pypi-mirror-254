import ghidra.features.bsim.query.protocol
import ghidra.xml
import java.io
import java.lang


class FunctionEntry(object):
    address: long
    funcName: unicode



    def __init__(self, __a0: ghidra.features.bsim.query.description.FunctionDescription): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def restoreXml(__a0: ghidra.xml.XmlPullParser) -> ghidra.features.bsim.query.protocol.FunctionEntry: ...

    def saveXml(self, __a0: java.io.Writer) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

