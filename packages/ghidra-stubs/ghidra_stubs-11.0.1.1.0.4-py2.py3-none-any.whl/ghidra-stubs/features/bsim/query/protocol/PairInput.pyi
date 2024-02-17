import ghidra.xml
import java.io
import java.lang


class PairInput(object):
    execA: ghidra.features.bsim.query.protocol.ExeSpecifier
    execB: ghidra.features.bsim.query.protocol.ExeSpecifier
    funcA: ghidra.features.bsim.query.protocol.FunctionEntry
    funcB: ghidra.features.bsim.query.protocol.FunctionEntry



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, __a0: ghidra.xml.XmlPullParser) -> None: ...

    def saveXml(self, __a0: java.io.Writer) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

