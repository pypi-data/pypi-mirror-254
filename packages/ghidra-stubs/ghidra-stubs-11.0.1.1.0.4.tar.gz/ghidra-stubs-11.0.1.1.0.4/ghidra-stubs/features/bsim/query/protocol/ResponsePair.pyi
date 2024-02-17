import generic.lsh.vector
import ghidra.features.bsim.query.description
import ghidra.features.bsim.query.protocol
import ghidra.xml
import java.io
import java.lang


class ResponsePair(ghidra.features.bsim.query.protocol.QueryResponseRecord):
    averageSig: float
    averageSim: float
    missedExe: int
    missedFunc: int
    missedVector: int
    notes: List[object]
    pairCount: int
    scale: float
    sigStdDev: float
    simStdDev: float




    class Accumulator(object):
        missedExe: int
        missedFunc: int
        missedVector: int
        pairCount: int
        sumSig: float
        sumSigSquare: float
        sumSim: float
        sumSimSquare: float



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def merge(self, __a0: ghidra.features.bsim.query.protocol.ResponsePair) -> None: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def fillOutStatistics(self, __a0: ghidra.features.bsim.query.protocol.ResponsePair.Accumulator) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescriptionManager(self) -> ghidra.features.bsim.query.description.DescriptionManager: ...

    def getLocalStagingCopy(self) -> ghidra.features.bsim.query.protocol.QueryResponseRecord: ...

    def getName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def mergeResults(self, __a0: ghidra.features.bsim.query.protocol.QueryResponseRecord) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, __a0: ghidra.xml.XmlPullParser, __a1: generic.lsh.vector.LSHVectorFactory) -> None: ...

    def saveXml(self, __a0: java.io.Writer) -> None: ...

    def saveXmlTail(self, __a0: java.io.Writer) -> None: ...

    def sort(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

