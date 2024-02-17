import generic.lsh.vector
import ghidra.features.bsim.query
import ghidra.features.bsim.query.description
import ghidra.features.bsim.query.protocol
import ghidra.xml
import java.io
import java.lang


class QueryName(ghidra.features.bsim.query.protocol.BSimQuery):
    fillinCallgraph: bool
    fillinCategories: bool
    fillinSigs: bool
    funcname: unicode
    maxfunc: int
    nameresponse: ghidra.features.bsim.query.protocol.ResponseName
    printjustexe: bool
    printselfsig: bool
    spec: ghidra.features.bsim.query.protocol.ExeSpecifier



    def __init__(self): ...



    def buildResponseTemplate(self) -> None: ...

    def clearResponse(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self, __a0: ghidra.features.bsim.query.FunctionDatabase) -> ghidra.features.bsim.query.protocol.QueryResponseRecord: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescriptionManager(self) -> ghidra.features.bsim.query.description.DescriptionManager: ...

    def getLocalStagingCopy(self) -> ghidra.features.bsim.query.protocol.BSimQuery: ...

    def getName(self) -> unicode: ...

    def getResponse(self) -> ghidra.features.bsim.query.protocol.QueryResponseRecord: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def restoreQuery(__a0: ghidra.xml.XmlPullParser, __a1: generic.lsh.vector.LSHVectorFactory) -> ghidra.features.bsim.query.protocol.BSimQuery: ...

    def restoreXml(self, __a0: ghidra.xml.XmlPullParser, __a1: generic.lsh.vector.LSHVectorFactory) -> None: ...

    def saveXml(self, __a0: java.io.Writer) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

