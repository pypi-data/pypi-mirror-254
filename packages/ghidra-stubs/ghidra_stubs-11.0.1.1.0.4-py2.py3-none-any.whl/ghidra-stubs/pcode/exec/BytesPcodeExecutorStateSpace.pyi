from typing import List
import ghidra.pcode.exec
import ghidra.pcode.exec.PcodeExecutorStatePiece
import java.lang
import java.util


class BytesPcodeExecutorStateSpace(object):
    """
    A p-code executor state space for storing and retrieving bytes as arrays
    """





    def __init__(self, __a0: ghidra.program.model.lang.Language, __a1: ghidra.program.model.address.AddressSpace, __a2: object): ...



    def clear(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fork(self) -> ghidra.pcode.exec.BytesPcodeExecutorStateSpace: ...

    def getClass(self) -> java.lang.Class: ...

    def getRegisterValues(self, __a0: List[object]) -> java.util.Map: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def read(self, offset: long, size: int, reason: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> List[int]:
        """
        Read a value from the space at the given offset
 
         <p>
         If this space is not acting as a cache, this simply delegates to
         {@link #readBytes(long, int, Reason)}. Otherwise, it will first ensure the cache covers the
         requested value.
        @param offset the offset
        @param size the number of bytes to read (the size of the value)
        @param reason the reason for reading state
        @return the bytes read
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def write(self, offset: long, val: List[int], srcOffset: int, length: int) -> None:
        """
        Write a value at the given offset
        @param offset the offset
        @param val the value
        """
        ...

