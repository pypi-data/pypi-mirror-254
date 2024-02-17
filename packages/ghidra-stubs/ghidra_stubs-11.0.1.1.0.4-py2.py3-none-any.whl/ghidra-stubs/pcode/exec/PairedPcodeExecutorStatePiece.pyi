import ghidra.pcode.exec
import ghidra.pcode.exec.PcodeArithmetic
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.mem
import ghidra.program.model.pcode
import java.lang
import java.util
import org.apache.commons.lang3.tuple


class PairedPcodeExecutorStatePiece(object, ghidra.pcode.exec.PcodeExecutorStatePiece):
    """
    A paired executor state piece
 
 
     This composes two delegate pieces "left" and "right" creating a single piece which stores pairs
     of values, where the left component has the value type of the left piece, and the right component
     has the value type of the right piece. Both pieces must have the same address type. Every
     operation on this piece is decomposed into operations upon the delegate pieces, and the final
     result composed from the results of those operations.
 
 
     To compose three or more states, first ask if it is really necessary. Second, consider
     implementing the PcodeExecutorStatePiece interface for a record type. Third, use the
     Church-style triple. In that third case, it is recommended to compose the nested pair on the
     right of the top pair: Compose the two right pieces into a single piece, then use
     PairedPcodeExecutorState to compose a concrete state with the composed piece, yielding a
     state of triples. This can be applied ad nauseam to compose arbitrarily large tuples; however, at
     a certain point clients should consider creating a record and implementing the state piece and/or
     state interface. It's helpful to use this implementation as a reference. Alternatively, the
      module has a  which follows this
     recommendation.
    """





    @overload
    def __init__(self, left: ghidra.pcode.exec.PcodeExecutorStatePiece, right: ghidra.pcode.exec.PcodeExecutorStatePiece): ...

    @overload
    def __init__(self, left: ghidra.pcode.exec.PcodeExecutorStatePiece, right: ghidra.pcode.exec.PcodeExecutorStatePiece, addressArithmetic: ghidra.pcode.exec.PcodeArithmetic, arithmetic: ghidra.pcode.exec.PcodeArithmetic): ...



    def checkRange(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long, __a2: int) -> None: ...

    def clear(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fork(self) -> ghidra.pcode.exec.PairedPcodeExecutorStatePiece: ...

    def getAddressArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    def getArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    def getClass(self) -> java.lang.Class: ...

    def getConcreteBuffer(self, address: ghidra.program.model.address.Address, purpose: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> ghidra.program.model.mem.MemBuffer: ...

    def getLanguage(self) -> ghidra.program.model.lang.Language: ...

    def getLeft(self) -> ghidra.pcode.exec.PcodeExecutorStatePiece:
        """
        Get the delegate backing the left side of paired values
        @return the left piece
        """
        ...

    def getRegisterValues(self) -> java.util.Map: ...

    def getRight(self) -> ghidra.pcode.exec.PcodeExecutorStatePiece:
        """
        Get the delegate backing the right side of paired values
        @return the right piece
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
    def getVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: object, __a2: int, __a3: bool, __a4: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> org.apache.commons.lang3.tuple.Pair: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def quantizeOffset(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long) -> long: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.lang.Register, __a1: object) -> None: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.pcode.Varnode, __a1: object) -> None: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.address.Address, __a1: int, __a2: bool, __a3: object) -> None: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: object, __a2: int, __a3: bool, __a4: org.apache.commons.lang3.tuple.Pair) -> None: ...

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