from typing import List
import ghidra.pcode.exec
import ghidra.pcode.exec.PcodeArithmetic
import ghidra.program.model.lang
import ghidra.program.model.pcode
import java.lang
import org.apache.commons.lang3.tuple


class PairedPcodeArithmetic(object, ghidra.pcode.exec.PcodeArithmetic):
    """
    An arithmetic composed from two.
 
 
     The new arithmetic operates on tuples where each is subject to its respective arithmetic. One
     exception is #toConcrete(Pair, Purpose). This arithmetic defers to left ("control")
     arithmetic. Thus, conventionally, when part of the pair represents the concrete value, it should
     be the left.
 
 
     See PairedPcodeExecutorStatePiece regarding composing three or more elements. Generally,
     it's recommended the client provide its own "record" type and the corresponding arithmetic and
     state piece to manipulate it. Nesting pairs would work, but is not recommended.
    """

    SIZEOF_SIZEOF: int = 8



    def __init__(self, leftArith: ghidra.pcode.exec.PcodeArithmetic, rightArith: ghidra.pcode.exec.PcodeArithmetic):
        """
        Construct a composed arithmetic from the given two
        @param leftArith the left ("control") arithmetic
        @param rightArith the right ("rider") arithmetic
        """
        ...



    @overload
    def binaryOp(self, op: ghidra.program.model.pcode.PcodeOp, in1: org.apache.commons.lang3.tuple.Pair, in2: org.apache.commons.lang3.tuple.Pair) -> org.apache.commons.lang3.tuple.Pair: ...

    @overload
    def binaryOp(self, __a0: ghidra.program.model.pcode.PcodeOp, __a1: object, __a2: object) -> object: ...

    @overload
    def binaryOp(self, opcode: int, sizeout: int, sizein1: int, in1: org.apache.commons.lang3.tuple.Pair, sizein2: int, in2: org.apache.commons.lang3.tuple.Pair) -> org.apache.commons.lang3.tuple.Pair: ...

    @overload
    def binaryOp(self, __a0: int, __a1: int, __a2: int, __a3: object, __a4: int, __a5: object) -> object: ...

    def equals(self, obj: object) -> bool: ...

    @overload
    def fromConst(self, value: List[int]) -> org.apache.commons.lang3.tuple.Pair: ...

    @overload
    def fromConst(self, __a0: long, __a1: int) -> object: ...

    @overload
    def fromConst(self, __a0: long, __a1: int) -> object: ...

    @overload
    def fromConst(self, __a0: long, __a1: int, __a2: bool) -> object: ...

    def getClass(self) -> java.lang.Class: ...

    def getEndian(self) -> ghidra.program.model.lang.Endian: ...

    def getLeft(self) -> ghidra.pcode.exec.PcodeArithmetic:
        """
        Get the left ("control") arithmetic
        @return the arithmetic
        """
        ...

    def getRight(self) -> ghidra.pcode.exec.PcodeArithmetic:
        """
        Get the right ("rider") arithmetic
        @return the arithmetic
        """
        ...

    def hashCode(self) -> int: ...

    def isTrue(self, __a0: object, __a1: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> bool: ...

    @overload
    def modAfterLoad(self, sizeout: int, sizeinAddress: int, inAddress: org.apache.commons.lang3.tuple.Pair, sizeinValue: int, inValue: org.apache.commons.lang3.tuple.Pair) -> org.apache.commons.lang3.tuple.Pair: ...

    @overload
    def modAfterLoad(self, __a0: int, __a1: int, __a2: object, __a3: int, __a4: object) -> object: ...

    @overload
    def modBeforeStore(self, sizeout: int, sizeinAddress: int, inAddress: org.apache.commons.lang3.tuple.Pair, sizeinValue: int, inValue: org.apache.commons.lang3.tuple.Pair) -> org.apache.commons.lang3.tuple.Pair: ...

    @overload
    def modBeforeStore(self, __a0: int, __a1: int, __a2: object, __a3: int, __a4: object) -> object: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ptrAdd(self, __a0: int, __a1: int, __a2: object, __a3: int, __a4: object, __a5: int) -> object: ...

    def ptrSub(self, __a0: int, __a1: int, __a2: object, __a3: int, __a4: object) -> object: ...

    @overload
    def sizeOf(self, value: org.apache.commons.lang3.tuple.Pair) -> long: ...

    @overload
    def sizeOf(self, __a0: object) -> long: ...

    def sizeOfAbstract(self, __a0: object) -> object: ...

    def toBigInteger(self, __a0: object, __a1: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> long: ...

    @overload
    def toConcrete(self, value: org.apache.commons.lang3.tuple.Pair, purpose: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> List[int]: ...

    @overload
    def toConcrete(self, __a0: object, __a1: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> List[int]: ...

    def toLong(self, __a0: object, __a1: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> long: ...

    def toString(self) -> unicode: ...

    @overload
    def unaryOp(self, op: ghidra.program.model.pcode.PcodeOp, in1: org.apache.commons.lang3.tuple.Pair) -> org.apache.commons.lang3.tuple.Pair: ...

    @overload
    def unaryOp(self, __a0: ghidra.program.model.pcode.PcodeOp, __a1: object) -> object: ...

    @overload
    def unaryOp(self, opcode: int, sizeout: int, sizein1: int, in1: org.apache.commons.lang3.tuple.Pair) -> org.apache.commons.lang3.tuple.Pair: ...

    @overload
    def unaryOp(self, __a0: int, __a1: int, __a2: int, __a3: object) -> object: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def endian(self) -> ghidra.program.model.lang.Endian: ...

    @property
    def left(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    @property
    def right(self) -> ghidra.pcode.exec.PcodeArithmetic: ...