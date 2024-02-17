import ghidra.pcode.exec
import ghidra.pcode.exec.PcodeArithmetic
import ghidra.pcode.exec.PcodeExecutorStatePiece
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.mem
import ghidra.program.model.pcode
import java.lang
import java.util
import org.apache.commons.lang3.tuple


class PairedPcodeExecutorState(object, ghidra.pcode.exec.PcodeExecutorState):
    """
    A paired executor state
 
 
     This composes a delegate state and piece "left" and "write" creating a single state which instead
     stores pairs of values, where the left component has the value type of the left state, and the
     right component has the value type of the right state. Note that both states are addressed using
     only the left "control" component. Otherwise, every operation on this state is decomposed into
     operations upon the delegate states, and the final result composed from the results of those
     operations.
 
 
     Where a response cannot be composed of both states, the paired state defers to the left. In this
     way, the left state controls the machine, while the right is computed in tandem. The right never
     directly controls the machine
 
 
     See PairedPcodeExecutorStatePiece regarding the composition of three or more pieces.
    """





    @overload
    def __init__(self, piece: ghidra.pcode.exec.PairedPcodeExecutorStatePiece): ...

    @overload
    def __init__(self, left: ghidra.pcode.exec.PcodeExecutorState, right: ghidra.pcode.exec.PcodeExecutorStatePiece): ...

    @overload
    def __init__(self, left: ghidra.pcode.exec.PcodeExecutorState, right: ghidra.pcode.exec.PcodeExecutorStatePiece, arithmetic: ghidra.pcode.exec.PcodeArithmetic):
        """
        Compose a paired state from the given left and right states
        @param left the state backing the left side of paired values ("control")
        @param right the state backing the right side of paired values ("auxiliary")
        """
        ...



    def checkRange(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long, __a2: int) -> None: ...

    def clear(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fork(self) -> ghidra.pcode.exec.PairedPcodeExecutorState: ...

    def getAddressArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    def getArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    def getClass(self) -> java.lang.Class: ...

    def getConcreteBuffer(self, address: ghidra.program.model.address.Address, purpose: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> ghidra.program.model.mem.MemBuffer: ...

    def getLanguage(self) -> ghidra.program.model.lang.Language: ...

    def getLeft(self) -> ghidra.pcode.exec.PcodeExecutorStatePiece:
        """
        Get the delegate backing the left side of paired values
        @return the left state
        """
        ...

    def getRegisterValues(self) -> java.util.Map: ...

    def getRight(self) -> ghidra.pcode.exec.PcodeExecutorStatePiece:
        """
        Get the delegate backing the right side of paired values
        @return the right state
        """
        ...

    @overload
    def getVar(self, __a0: ghidra.program.model.lang.Register, __a1: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.pcode.Varnode, __a1: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.address.Address, __a1: int, __a2: bool, __a3: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long, __a2: int, __a3: bool, __a4: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    @overload
    def getVar(self, space: ghidra.program.model.address.AddressSpace, offset: org.apache.commons.lang3.tuple.Pair, size: int, quantize: bool, reason: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> org.apache.commons.lang3.tuple.Pair: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: object, __a2: int, __a3: bool, __a4: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paired(self, __a0: ghidra.pcode.exec.PcodeExecutorStatePiece) -> ghidra.pcode.exec.PcodeExecutorState: ...

    def quantizeOffset(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long) -> long: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.lang.Register, __a1: object) -> None: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.pcode.Varnode, __a1: object) -> None: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.address.Address, __a1: int, __a2: bool, __a3: object) -> None: ...

    @overload
    def setVar(self, space: ghidra.program.model.address.AddressSpace, offset: org.apache.commons.lang3.tuple.Pair, size: int, quantize: bool, val: org.apache.commons.lang3.tuple.Pair) -> None: ...

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
    def left(self) -> ghidra.pcode.exec.PcodeExecutorStatePiece: ...

    @property
    def registerValues(self) -> java.util.Map: ...

    @property
    def right(self) -> ghidra.pcode.exec.PcodeExecutorStatePiece: ...