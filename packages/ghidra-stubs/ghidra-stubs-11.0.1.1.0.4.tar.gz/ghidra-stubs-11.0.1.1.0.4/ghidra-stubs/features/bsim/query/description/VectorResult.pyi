import generic.lsh.vector
import ghidra.xml
import java.io
import java.lang


class VectorResult(object):
    hitcount: int
    signif: float
    sim: float
    vec: generic.lsh.vector.LSHVector
    vectorid: long



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, __a0: long, __a1: int, __a2: float, __a3: float, __a4: generic.lsh.vector.LSHVector): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, __a0: ghidra.xml.XmlPullParser, __a1: generic.lsh.vector.LSHVectorFactory) -> None: ...

    def saveXml(self, __a0: java.io.Writer) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

