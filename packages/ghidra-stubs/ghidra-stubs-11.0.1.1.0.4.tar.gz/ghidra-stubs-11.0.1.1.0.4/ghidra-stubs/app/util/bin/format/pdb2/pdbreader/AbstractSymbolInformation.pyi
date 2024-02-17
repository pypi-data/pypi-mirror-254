from typing import List
import java.lang


class AbstractSymbolInformation(object):
    GSI70: int = -248575718
    HASH_70_HEADER_LENGTH: int = 16
    HASH_HEADER_MIN_READ_LENGTH: int = 16
    HASH_PRE70_HEADER_LENGTH: int = 0
    HEADER_SIGNATURE: int = -1



    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: int): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getModifiedHashRecordSymbolOffsets(self) -> List[object]: ...

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

    @property
    def modifiedHashRecordSymbolOffsets(self) -> List[object]: ...