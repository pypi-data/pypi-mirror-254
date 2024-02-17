from typing import List
import ghidra.program.model.lang
import java.lang
import java.util


class StorageClass(java.lang.Enum):
    CLASS1: ghidra.program.model.lang.StorageClass = class1
    CLASS2: ghidra.program.model.lang.StorageClass = class2
    CLASS3: ghidra.program.model.lang.StorageClass = class3
    CLASS4: ghidra.program.model.lang.StorageClass = class4
    FLOAT: ghidra.program.model.lang.StorageClass = float
    GENERAL: ghidra.program.model.lang.StorageClass = general
    HIDDENRET: ghidra.program.model.lang.StorageClass = hiddenret
    PTR: ghidra.program.model.lang.StorageClass = ptr
    VECTOR: ghidra.program.model.lang.StorageClass = vector







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def describeConstable(self) -> java.util.Optional: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getClass(__a0: unicode) -> ghidra.program.model.lang.StorageClass: ...

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
    def valueOf(__a0: unicode) -> ghidra.program.model.lang.StorageClass: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.program.model.lang.StorageClass]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def value(self) -> int: ...