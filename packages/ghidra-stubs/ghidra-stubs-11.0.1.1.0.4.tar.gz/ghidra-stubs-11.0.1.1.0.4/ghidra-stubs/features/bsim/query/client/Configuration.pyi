import generic.jar
import ghidra.xml
import java.io
import java.lang


class Configuration(object):
    L: int
    idflookup: generic.lsh.vector.IDFLookup
    info: ghidra.features.bsim.query.description.DatabaseInformation
    k: int
    weightfactory: generic.lsh.vector.WeightFactory



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def loadTemplate(self, __a0: generic.jar.ResourceFile, __a1: unicode) -> None: ...

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

