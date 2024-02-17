from typing import List
import ghidra.app.decompiler
import ghidra.codecompare.graphanalysis
import ghidra.program.model.pcode
import ghidra.util.task
import java.io
import java.lang
import java.util


class Pinning(object):





    class Side(java.lang.Enum):
        LEFT: ghidra.codecompare.graphanalysis.Pinning.Side = LEFT
        RIGHT: ghidra.codecompare.graphanalysis.Pinning.Side = RIGHT







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def describeConstable(self) -> java.util.Optional: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def getValue(self) -> int: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.codecompare.graphanalysis.Pinning.Side: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.codecompare.graphanalysis.Pinning.Side]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @property
        def value(self) -> int: ...




    class DataCtrl(object):




        def __init__(self, __a0: ghidra.codecompare.graphanalysis.DataVertex, __a1: ghidra.codecompare.graphanalysis.CtrlNGram): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, __a0: ghidra.program.model.pcode.HighFunction, __a1: ghidra.program.model.pcode.HighFunction, __a2: int, __a3: bool, __a4: bool, __a5: bool, __a6: bool, __a7: bool, __a8: ghidra.util.task.TaskMonitor): ...



    def buildTokenMap(self, __a0: ghidra.app.decompiler.ClangTokenGroup, __a1: ghidra.app.decompiler.ClangTokenGroup) -> java.util.ArrayList: ...

    def dump(self, __a0: java.io.Writer) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def findMatch(self, __a0: ghidra.program.model.pcode.PcodeOp) -> ghidra.program.model.pcode.PcodeOpAST: ...

    @overload
    def findMatch(self, __a0: ghidra.program.model.pcode.Varnode) -> ghidra.program.model.pcode.VarnodeAST: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def makePinning(__a0: ghidra.program.model.pcode.HighFunction, __a1: ghidra.program.model.pcode.HighFunction, __a2: bool, __a3: bool, __a4: bool, __a5: ghidra.util.task.TaskMonitor) -> ghidra.codecompare.graphanalysis.Pinning: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

