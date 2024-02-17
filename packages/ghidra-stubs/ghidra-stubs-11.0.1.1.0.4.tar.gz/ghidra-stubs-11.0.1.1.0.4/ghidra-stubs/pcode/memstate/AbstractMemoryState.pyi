from typing import List
import ghidra.pcode.memstate
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.pcode
import java.lang


class AbstractMemoryState(object, ghidra.pcode.memstate.MemoryState):




    def __init__(self, language: ghidra.program.model.lang.Language): ...



    def equals(self, __a0: object) -> bool: ...

    @overload
    def getBigInteger(self, nm: unicode) -> long:
        """
        This is a convenience method for reading registers by name. any register name known to the
         language can be used as a read location. The associated address space, offset, and size is
         looked up and automatically passed to the main getValue routine.
        @param nm is the name of the register
        @return the unsigned value associated with that register
        """
        ...

    @overload
    def getBigInteger(self, reg: ghidra.program.model.lang.Register) -> long:
        """
        A convenience method for reading a value directly from a register rather than querying for
         the offset and space
        @param reg the register location to be read
        @return the unsigned value read from the register location
        """
        ...

    @overload
    def getBigInteger(self, vn: ghidra.program.model.pcode.Varnode, signed: bool) -> long:
        """
        A convenience method for reading a value directly from a varnode rather than querying for the
         offset and space
        @param vn the varnode location to be read
        @param signed true if signed value should be returned, false for unsigned value
        @return the unsigned value read from the varnode location
        """
        ...

    @overload
    def getBigInteger(self, spc: ghidra.program.model.address.AddressSpace, off: long, size: int, signed: bool) -> long:
        """
        This is the main interface for reading values from the MemoryState. If there is no registered
         MemoryBank for the desired address space, or if there is some other error, an exception is
         thrown.
        @param spc is the address space being queried
        @param off is the offset of the value being queried
        @param size is the number of bytes to query
        @param signed true if signed value should be returned, false for unsigned value
        @return the queried unsigned value
        """
        ...

    def getChunk(self, __a0: List[int], __a1: ghidra.program.model.address.AddressSpace, __a2: long, __a3: int, __a4: bool) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getMemoryBank(self, __a0: ghidra.program.model.address.AddressSpace) -> ghidra.pcode.memstate.MemoryBank: ...

    @overload
    def getValue(self, nm: unicode) -> long:
        """
        This is a convenience method for reading registers by name. any register name known to the
         language can be used as a read location. The associated address space, offset, and size is
         looked up and automatically passed to the main getValue routine.
        @param nm is the name of the register
        @return the value associated with that register
        """
        ...

    @overload
    def getValue(self, reg: ghidra.program.model.lang.Register) -> long:
        """
        A convenience method for reading a value directly from a register rather than querying for
         the offset and space
        @param reg the register location to be read
        @return the value read from the register location
        """
        ...

    @overload
    def getValue(self, vn: ghidra.program.model.pcode.Varnode) -> long:
        """
        A convenience method for reading a value directly from a varnode rather than querying for the
         offset and space
        @param vn the varnode location to be read
        @return the value read from the varnode location
        """
        ...

    @overload
    def getValue(self, spc: ghidra.program.model.address.AddressSpace, off: long, size: int) -> long:
        """
        This is the main interface for reading values from the MemoryState. If there is no registered
         MemoryBank for the desired address space, or if there is some other error, an exception is
         thrown.
        @param spc is the address space being queried
        @param off is the offset of the value being queried
        @param size is the number of bytes to query
        @return the queried value
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setChunk(self, __a0: List[int], __a1: ghidra.program.model.address.AddressSpace, __a2: long, __a3: int) -> None: ...

    def setInitialized(self, __a0: bool, __a1: ghidra.program.model.address.AddressSpace, __a2: long, __a3: int) -> None: ...

    def setMemoryBank(self, __a0: ghidra.pcode.memstate.MemoryBank) -> None: ...

    @overload
    def setValue(self, nm: unicode, cval: long) -> None:
        """
        This is a convenience method for setting registers by name. Any register name known to the
         language can be used as a write location. The associated address space, offset, and size is
         looked up and automatically passed to the main setValue routine.
        @param nm is the name of the register
        @param cval is the value to write to the register
        """
        ...

    @overload
    def setValue(self, reg: ghidra.program.model.lang.Register, cval: long) -> None:
        """
        A convenience method for setting a value directly on a register rather than breaking out the
         components
        @param reg the register location to be written
        @param cval the value to write into the register location
        """
        ...

    @overload
    def setValue(self, vn: ghidra.program.model.pcode.Varnode, cval: long) -> None:
        """
        A convenience method for setting a value directly on a varnode rather than breaking out the
         components
        @param vn the varnode location to be written
        @param cval the value to write into the varnode location
        """
        ...

    @overload
    def setValue(self, nm: unicode, cval: long) -> None:
        """
        This is a convenience method for setting registers by name. Any register name known to the
         language can be used as a write location. The associated address space, offset, and size is
         looked up and automatically passed to the main setValue routine.
        @param nm is the name of the register
        @param cval is the value to write to the register
        """
        ...

    @overload
    def setValue(self, reg: ghidra.program.model.lang.Register, cval: long) -> None:
        """
        A convenience method for setting a value directly on a register rather than breaking out the
         components
        @param reg the register location to be written
        @param cval the value to write into the register location
        """
        ...

    @overload
    def setValue(self, vn: ghidra.program.model.pcode.Varnode, cval: long) -> None:
        """
        A convenience method for setting a value directly on a varnode rather than breaking out the
         components
        @param vn the varnode location to be written
        @param cval the value to write into the varnode location
        """
        ...

    @overload
    def setValue(self, spc: ghidra.program.model.address.AddressSpace, off: long, size: int, cval: long) -> None:
        """
        This is the main interface for writing values to the MemoryState. If there is no registered
         MemoryBank for the desired address space, or if there is some other error, an exception is
         thrown.
        @param spc is the address space to write to
        @param off is the offset where the value should be written
        @param size is the number of bytes to be written
        @param cval is the value to be written
        """
        ...

    @overload
    def setValue(self, spc: ghidra.program.model.address.AddressSpace, off: long, size: int, cval: long) -> None:
        """
        This is the main interface for writing values to the MemoryState. If there is no registered
         MemoryBank for the desired address space, or if there is some other error, an exception is
         thrown.
        @param spc is the address space to write to
        @param off is the offset where the value should be written
        @param size is the number of bytes to be written
        @param cval is the value to be written
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def memoryBank(self) -> None: ...  # No getter available.

    @memoryBank.setter
    def memoryBank(self, value: ghidra.pcode.memstate.MemoryBank) -> None: ...