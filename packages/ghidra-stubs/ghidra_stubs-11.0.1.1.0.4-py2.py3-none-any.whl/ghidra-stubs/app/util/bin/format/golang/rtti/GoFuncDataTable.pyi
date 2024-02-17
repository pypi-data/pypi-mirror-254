from typing import List
import ghidra.app.util.bin.format.golang.rtti
import java.lang
import java.util


class GoFuncDataTable(java.lang.Enum):
    FUNCDATA_ArgInfo: ghidra.app.util.bin.format.golang.rtti.GoFuncDataTable = FUNCDATA_ArgInfo
    FUNCDATA_ArgLiveInfo: ghidra.app.util.bin.format.golang.rtti.GoFuncDataTable = FUNCDATA_ArgLiveInfo
    FUNCDATA_ArgsPointerMaps: ghidra.app.util.bin.format.golang.rtti.GoFuncDataTable = FUNCDATA_ArgsPointerMaps
    FUNCDATA_InlTree: ghidra.app.util.bin.format.golang.rtti.GoFuncDataTable = FUNCDATA_InlTree
    FUNCDATA_LocalsPointerMaps: ghidra.app.util.bin.format.golang.rtti.GoFuncDataTable = FUNCDATA_LocalsPointerMaps
    FUNCDATA_OpenCodedDeferInfo: ghidra.app.util.bin.format.golang.rtti.GoFuncDataTable = FUNCDATA_OpenCodedDeferInfo
    FUNCDATA_StackObjects: ghidra.app.util.bin.format.golang.rtti.GoFuncDataTable = FUNCDATA_StackObjects
    FUNCDATA_WrapInfo: ghidra.app.util.bin.format.golang.rtti.GoFuncDataTable = FUNCDATA_WrapInfo







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

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.golang.rtti.GoFuncDataTable: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.golang.rtti.GoFuncDataTable]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

