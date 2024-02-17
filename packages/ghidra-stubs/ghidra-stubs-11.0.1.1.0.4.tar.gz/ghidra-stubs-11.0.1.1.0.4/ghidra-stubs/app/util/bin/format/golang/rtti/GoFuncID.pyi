from typing import List
import ghidra.app.util.bin.format.golang.rtti
import java.lang
import java.util


class GoFuncID(java.lang.Enum):
    ABORT: ghidra.app.util.bin.format.golang.rtti.GoFuncID = ABORT
    ASMCGOCALL: ghidra.app.util.bin.format.golang.rtti.GoFuncID = ASMCGOCALL
    ASYNCPREEMPT: ghidra.app.util.bin.format.golang.rtti.GoFuncID = ASYNCPREEMPT
    CGOCALLBACK: ghidra.app.util.bin.format.golang.rtti.GoFuncID = CGOCALLBACK
    DEBUGCALLV2: ghidra.app.util.bin.format.golang.rtti.GoFuncID = DEBUGCALLV2
    GCBGMARKWORKER: ghidra.app.util.bin.format.golang.rtti.GoFuncID = GCBGMARKWORKER
    GOEXIT: ghidra.app.util.bin.format.golang.rtti.GoFuncID = GOEXIT
    GOGO: ghidra.app.util.bin.format.golang.rtti.GoFuncID = GOGO
    GOPANIC: ghidra.app.util.bin.format.golang.rtti.GoFuncID = GOPANIC
    HANDLEASYNCEVENT: ghidra.app.util.bin.format.golang.rtti.GoFuncID = HANDLEASYNCEVENT
    MCALL: ghidra.app.util.bin.format.golang.rtti.GoFuncID = MCALL
    MORESTACK: ghidra.app.util.bin.format.golang.rtti.GoFuncID = MORESTACK
    MSTART: ghidra.app.util.bin.format.golang.rtti.GoFuncID = MSTART
    NORMAL: ghidra.app.util.bin.format.golang.rtti.GoFuncID = NORMAL
    PANICWRAP: ghidra.app.util.bin.format.golang.rtti.GoFuncID = PANICWRAP
    RT0_GO: ghidra.app.util.bin.format.golang.rtti.GoFuncID = RT0_GO
    RUNFINQ: ghidra.app.util.bin.format.golang.rtti.GoFuncID = RUNFINQ
    RUNTIME_MAIN: ghidra.app.util.bin.format.golang.rtti.GoFuncID = RUNTIME_MAIN
    SIGPANIC: ghidra.app.util.bin.format.golang.rtti.GoFuncID = SIGPANIC
    SYSTEMSTACK: ghidra.app.util.bin.format.golang.rtti.GoFuncID = SYSTEMSTACK
    SYSTEMSTACK_SWITCH: ghidra.app.util.bin.format.golang.rtti.GoFuncID = SYSTEMSTACK_SWITCH
    WRAPPER: ghidra.app.util.bin.format.golang.rtti.GoFuncID = WRAPPER







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def describeConstable(self) -> java.util.Optional: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    @staticmethod
    def parseIDByte(__a0: int) -> ghidra.app.util.bin.format.golang.rtti.GoFuncID: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.golang.rtti.GoFuncID: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.golang.rtti.GoFuncID]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

