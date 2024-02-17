from typing import List
import ghidra.bsfv
import java.lang
import java.util


class BSimFeatureType(java.lang.Enum):
    COMBINED: ghidra.bsfv.BSimFeatureType = COMBINED
    CONTROL_FLOW: ghidra.bsfv.BSimFeatureType = CONTROL_FLOW
    COPY_SIG: ghidra.bsfv.BSimFeatureType = COPY_SIG
    DATA_FLOW: ghidra.bsfv.BSimFeatureType = DATA_FLOW
    DUAL_FLOW: ghidra.bsfv.BSimFeatureType = DUAL_FLOW







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
    def valueOf(__a0: unicode) -> ghidra.bsfv.BSimFeatureType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.bsfv.BSimFeatureType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

