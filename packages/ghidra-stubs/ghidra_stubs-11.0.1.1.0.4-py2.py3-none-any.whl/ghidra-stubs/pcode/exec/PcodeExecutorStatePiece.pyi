from typing import List
import ghidra.pcode.exec
import ghidra.pcode.exec.PcodeArithmetic
import ghidra.pcode.exec.PcodeExecutorStatePiece
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.mem
import ghidra.program.model.pcode
import java.lang
import java.util


class PcodeExecutorStatePiece(object):
    """
    An interface that provides storage for values of type , addressed by offsets of type
 
 
 
     The typical pattern for implementing a state is to compose it from one or more state pieces. Each
     piece must use the same address type and arithmetic. If more than one piece is needed, they are
     composed using PairedPcodeExecutorStatePiece. Once all the pieces are composed, the root
     piece can be wrapped to make a state using DefaultPcodeExecutorState or
     PairedPcodeExecutorState. The latter corrects the address type to be a pair so it matches
     the type of values.
    """






    class Reason(java.lang.Enum):
        EXECUTE_DECODE: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason = EXECUTE_DECODE
        EXECUTE_READ: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason = EXECUTE_READ
        INSPECT: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason = INSPECT
        RE_INIT: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason = RE_INIT







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
        def valueOf(__a0: unicode) -> ghidra.pcode.exec.PcodeExecutorStatePiece.Reason: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.pcode.exec.PcodeExecutorStatePiece.Reason]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    def checkRange(self, space: ghidra.program.model.address.AddressSpace, offset: long, size: int) -> None:
        """
        Construct a range, if only to verify the range is valid
        @param space the address space
        @param offset the starting offset
        @param size the length (in bytes) of the range
        """
        ...

    def clear(self) -> None:
        """
        Erase the entire state or piece
 
         <p>
         This is generally only useful when the state is itself a cache to another object. This will
         ensure the state is reading from that object rather than a stale cache. If this is not a
         cache, this could in fact clear the whole state, and the machine using it will be left in the
         dark.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def fork(self) -> ghidra.pcode.exec.PcodeExecutorStatePiece:
        """
        Create a deep copy of this state
        @return the copy
        """
        ...

    def getAddressArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic:
        """
        Get the arithmetic used to manipulate addresses of the type used by this state
        @return the address (or offset) arithmetic
        """
        ...

    def getArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic:
        """
        Get the arithmetic used to manipulate values of the type stored by this state
        @return the arithmetic
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getConcreteBuffer(self, address: ghidra.program.model.address.Address, purpose: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> ghidra.program.model.mem.MemBuffer:
        """
        Bind a buffer of concrete bytes at the given start address
        @param address the start address
        @param purpose the reason why the emulator needs a concrete value
        @return a buffer
        """
        ...

    def getLanguage(self) -> ghidra.program.model.lang.Language:
        """
        Get the language defining the address spaces of this state piece
        @return the language
        """
        ...

    def getRegisterValues(self) -> java.util.Map:
        """
        Get all register values known to this state
 
         <p>
         When the state acts as a cache, it should only return those cached.
        @return a map of registers and their values
        """
        ...

    @overload
    def getVar(self, reg: ghidra.program.model.lang.Register, reason: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object:
        """
        Get the value of a register variable
        @param reg the register
        @param reason the reason for reading the register
        @return the value
        """
        ...

    @overload
    def getVar(self, var: ghidra.program.model.pcode.Varnode, reason: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object:
        """
        Get the value of a variable
        @param var the variable
        @param reason the reason for reading the variable
        @return the value
        """
        ...

    @overload
    def getVar(self, address: ghidra.program.model.address.Address, size: int, quantize: bool, reason: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object:
        """
        Get the value of a variable
 
         <p>
         This method is typically used for reading memory variables.
        @param address the address of the variable
        @param size the size of the variable
        @param quantize true to quantize to the language's "addressable unit"
        @param reason the reason for reading the variable
        @return the value
        """
        ...

    @overload
    def getVar(self, space: ghidra.program.model.address.AddressSpace, offset: long, size: int, quantize: bool, reason: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object:
        """
        Get the value of a variable
 
         <p>
         This method is typically used for reading memory variables.
        @param space the address space
        @param offset the offset within the space
        @param size the size of the variable
        @param quantize true to quantize to the language's "addressable unit"
        @param reason the reason for reading the variable
        @return the value
        """
        ...

    @overload
    def getVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: object, __a2: int, __a3: bool, __a4: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def quantizeOffset(self, space: ghidra.program.model.address.AddressSpace, offset: long) -> long:
        """
        Quantize the given offset to the language's "addressable unit"
        @param space the space where the offset applies
        @param offset the offset
        @return the quantized offset
        """
        ...

    @overload
    def setVar(self, reg: ghidra.program.model.lang.Register, val: object) -> None:
        """
        Set the value of a register variable
        @param reg the register
        @param val the value
        """
        ...

    @overload
    def setVar(self, var: ghidra.program.model.pcode.Varnode, val: object) -> None:
        """
        Set the value of a variable
        @param var the variable
        @param val the value
        """
        ...

    @overload
    def setVar(self, address: ghidra.program.model.address.Address, size: int, quantize: bool, val: object) -> None:
        """
        Set the value of a variable
        @param address the address in memory
        @param size the size of the variable
        @param quantize true to quantize to the language's "addressable unit"
        @param val the value
        """
        ...

    @overload
    def setVar(self, space: ghidra.program.model.address.AddressSpace, offset: long, size: int, quantize: bool, val: object) -> None:
        """
        Set the value of a variable
        @param space the address space
        @param offset the offset within the space
        @param size the size of the variable
        @param quantize true to quantize to the language's "addressable unit"
        @param val the value
        """
        ...

    @overload
    def setVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: object, __a2: int, __a3: bool, __a4: object) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    @property
    def arithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    @property
    def language(self) -> ghidra.program.model.lang.Language: ...

    @property
    def registerValues(self) -> java.util.Map: ...