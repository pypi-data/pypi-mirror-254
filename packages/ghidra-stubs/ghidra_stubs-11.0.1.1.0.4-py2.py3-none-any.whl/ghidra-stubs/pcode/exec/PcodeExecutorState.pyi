import ghidra.pcode.exec
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.mem
import ghidra.program.model.pcode
import java.lang
import java.util


class PcodeExecutorState(ghidra.pcode.exec.PcodeExecutorStatePiece, object):
    """
    An interface that provides storage for values of type 
 
 
     This is not much more than a stricter form of PcodeExecutorStatePiece, in that it
     requires the value and address offset types to agree, so that a p-code executor or emulator can
     perform loads and stores using indirect addresses. The typical pattern for implementing a state
     is to compose it from pieces. See PcodeExecutorStatePiece.
    """









    def checkRange(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long, __a2: int) -> None: ...

    def clear(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fork(self) -> ghidra.pcode.exec.PcodeExecutorState: ...

    def getAddressArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    def getArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    def getClass(self) -> java.lang.Class: ...

    def getConcreteBuffer(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> ghidra.program.model.mem.MemBuffer: ...

    def getLanguage(self) -> ghidra.program.model.lang.Language: ...

    def getRegisterValues(self) -> java.util.Map: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.lang.Register, __a1: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.pcode.Varnode, __a1: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.address.Address, __a1: int, __a2: bool, __a3: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long, __a2: int, __a3: bool, __a4: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: object, __a2: int, __a3: bool, __a4: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paired(self, right: ghidra.pcode.exec.PcodeExecutorStatePiece) -> ghidra.pcode.exec.PcodeExecutorState:
        """
        Use this state as the control, paired with the given auxiliary state.
 
         <p>
         <b>CAUTION:</b> Often, the default paired state is not quite sufficient. Consider
         {@link #getVar(AddressSpace, Object, int, boolean, Reason)}. The rider on the offset may
         offer information that must be incorporated into the rider of the value just read. This is
         the case, for example, with taint propagation. In those cases, an anonymous inner class
         extending {@link PairedPcodeExecutorState} is sufficient.
        @param <U> the type of values and offsets stored by the rider
        @param right the rider state
        @return the paired state
        """
        ...

    def quantizeOffset(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long) -> long: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.lang.Register, __a1: object) -> None: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.pcode.Varnode, __a1: object) -> None: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.address.Address, __a1: int, __a2: bool, __a3: object) -> None: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long, __a2: int, __a3: bool, __a4: object) -> None: ...

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