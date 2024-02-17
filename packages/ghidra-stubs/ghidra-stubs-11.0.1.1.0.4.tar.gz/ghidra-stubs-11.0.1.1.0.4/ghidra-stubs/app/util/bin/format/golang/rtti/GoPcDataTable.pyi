from typing import List
import ghidra.app.util.bin.format.golang.rtti
import java.lang
import java.util


class GoPcDataTable(java.lang.Enum):
    PCDATA_ArgLiveIndex: ghidra.app.util.bin.format.golang.rtti.GoPcDataTable = PCDATA_ArgLiveIndex
    PCDATA_InlTreeIndex: ghidra.app.util.bin.format.golang.rtti.GoPcDataTable = PCDATA_InlTreeIndex
    PCDATA_StackMapIndex: ghidra.app.util.bin.format.golang.rtti.GoPcDataTable = PCDATA_StackMapIndex
    PCDATA_UnsafePoint: ghidra.app.util.bin.format.golang.rtti.GoPcDataTable = PCDATA_UnsafePoint







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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.golang.rtti.GoPcDataTable: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.golang.rtti.GoPcDataTable]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

