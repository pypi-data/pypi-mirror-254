import ghidra.xml
import java.io
import java.lang


class DatabaseInformation(object):
    databasename: unicode
    dateColumnName: unicode
    description: unicode
    execats: List[object]
    functionTags: List[object]
    layout_version: int
    major: int
    minor: int
    owner: unicode
    readonly: bool
    settings: int
    trackcallgraph: bool



    def __init__(self): ...



    def checkSignatureSettings(self, __a0: int, __a1: int, __a2: int) -> int: ...

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

