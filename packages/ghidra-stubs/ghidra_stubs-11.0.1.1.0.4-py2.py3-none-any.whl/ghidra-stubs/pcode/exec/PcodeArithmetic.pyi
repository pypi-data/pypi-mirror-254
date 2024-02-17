from typing import List
import ghidra.pcode.exec
import ghidra.pcode.exec.PcodeArithmetic
import ghidra.program.model.lang
import ghidra.program.model.pcode
import java.lang
import java.util


class PcodeArithmetic(object):
    """
    An interface that defines arithmetic p-code operations on values of type .

 
     See BytesPcodeArithmetic for the typical pattern when implementing an arithmetic. There
     are generally two cases: 1) Where endianness matters, 2) Where endianness does not matter. The
     first is typical. The implementation should be an Enum with two constants, one for the
     big endian implementation, and one for the little endian implementation. The class should also
     provide static methods:  for getting the correct one based
     on endianness, and  for getting the correct one given a
     language. If endianness does not matter, then the implementation should follow a singleton
     pattern. See notes on #getEndian() for the endian-agnostic case.
    """

    SIZEOF_SIZEOF: int = 8




    class Purpose(java.lang.Enum):
        BRANCH: ghidra.pcode.exec.PcodeArithmetic.Purpose = BRANCH
        CONDITION: ghidra.pcode.exec.PcodeArithmetic.Purpose = CONDITION
        CONTEXT: ghidra.pcode.exec.PcodeArithmetic.Purpose = CONTEXT
        DECODE: ghidra.pcode.exec.PcodeArithmetic.Purpose = DECODE
        INSPECT: ghidra.pcode.exec.PcodeArithmetic.Purpose = INSPECT
        LOAD: ghidra.pcode.exec.PcodeArithmetic.Purpose = LOAD
        OTHER: ghidra.pcode.exec.PcodeArithmetic.Purpose = OTHER
        STORE: ghidra.pcode.exec.PcodeArithmetic.Purpose = STORE







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

        def reason(self) -> ghidra.pcode.exec.PcodeExecutorStatePiece.Reason: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.pcode.exec.PcodeArithmetic.Purpose: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.pcode.exec.PcodeArithmetic.Purpose]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    @overload
    def binaryOp(self, op: ghidra.program.model.pcode.PcodeOp, in1: object, in2: object) -> object:
        """
        Apply a binary operator to the given input
 
         <p>
         This provides the full p-code op, allowing deeper inspection of the code. For example, an
         arithmetic may wish to distinguish immediate (constant) values from variables. By default,
         this unpacks the details and defers to {@link #binaryOp(int, int, int, Object, int, Object)}.
        @implNote {@link OpBehaviorFactory#getOpBehavior(int)} for the given opcode is guaranteed to
                   return a derivative of {@link BinaryOpBehavior}.
        @param op the operation
        @param in1 the first (left) input value
        @param in2 the second (right) input value
        @return the output value
        """
        ...

    @overload
    def binaryOp(self, opcode: int, sizeout: int, sizein1: int, in1: object, sizein2: int, in2: object) -> object:
        """
        Apply a binary operator to the given inputs
 
         <p>
         Note the sizes of variables are given, because values don't necessarily have an intrinsic
         size. For example, a {@link BigInteger} may have a minimum encoding size, but that does not
         necessarily reflect the size of the variable from which is was read.
        @implNote {@link OpBehaviorFactory#getOpBehavior(int)} for the given opcode is guaranteed to
                   return a derivative of {@link BinaryOpBehavior}.
        @param opcode the operation's opcode. See {@link PcodeOp}.
        @param sizeout the size (in bytes) of the output variable
        @param sizein1 the size (in bytes) of the first (left) input variable
        @param in1 the first (left) input value
        @param sizein2 the size (in bytes) of the second (right) input variable
        @param in2 the second (right) input value
        @return the output value
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def fromConst(self, value: List[int]) -> object:
        """
        Convert the given constant concrete value to type {@code T} having the same size.
        @param value the constant value
        @return the value as a {@code T}
        """
        ...

    @overload
    def fromConst(self, value: long, size: int) -> object:
        """
        Convert the given constant concrete value to type {@code T} having the given size.
 
         <p>
         Note that the size may not be applicable to {@code T}. It is given to ensure the value can be
         held in a variable of that size when passed to downstream operators or stored in the executor
         state.
        @param value the constant value
        @param size the size (in bytes) of the variable into which the value is to be stored
        @return the value as a {@code T}
        """
        ...

    @overload
    def fromConst(self, value: long, size: int) -> object:
        """
        Convert the given constant concrete value to type {@code T} having the given size.
 
         <p>
         Note that the size may not be applicable to {@code T}. It is given to ensure the value can be
         held in a variable of that size when passed to downstream operators or stored in the executor
         state.
        @param value the constant value
        @param size the size (in bytes) of the variable into which the value is to be stored
        @return the value as a {@code T}
        """
        ...

    @overload
    def fromConst(self, value: long, size: int, isContextreg: bool) -> object:
        """
        Convert the given constant concrete value to type {@code T} having the given size.
 
         <p>
         Note that the size may not be applicable to {@code T}. It is given to ensure the value can be
         held in a variable of that size when passed to downstream operators or stored in the executor
         state.
        @param value the constant value
        @param size the size (in bytes) of the variable into which the value is to be stored
        @param isContextreg true to indicate the value is from the disassembly context register. If
                    {@code T} represents bytes, and the value is the contextreg, then the bytes are in
                    big endian, no matter the machine language's endianness.
        @return the value as a {@code T}
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEndian(self) -> ghidra.program.model.lang.Endian:
        """
        Get the endianness of this arithmetic
 
         <p>
         Often T is a byte array, or at least represents one abstractly. Ideally, it is an array where
         each element is an abstraction of a byte. If that is the case, then the arithmetic likely has
         to interpret those bytes as integral values according to an endianness. This should return
         that endianness.
 
         <p>
         If the abstraction has no notion of endianness, return null. In that case, the both
         {@link #fromConst(BigInteger, int, boolean)} and {@link #fromConst(long, int)} must be
         overridden. Furthermore, unless {@link #toConcrete(Object, Purpose)} is guaranteed to throw
         an exception, then {@link #toBigInteger(Object, Purpose)} and
         {@link #toLong(Object, Purpose)} must also be overridden.
        @return the endianness or null
        """
        ...

    def hashCode(self) -> int: ...

    def isTrue(self, cond: object, purpose: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> bool:
        """
        Convert, if possible, the given abstract condition to a concrete boolean value
        @param cond the abstract condition
        @param purpose probably {@link Purpose#CONDITION}
        @return the boolean value
        """
        ...

    def modAfterLoad(self, sizeout: int, sizeinAddress: int, inAddress: object, sizeinValue: int, inValue: object) -> object:
        """
        Apply any modifications after a value is loaded
 
         <p>
         This implements any abstractions associated with {@link PcodeOp#LOAD}. This is called on the
         address/offset and the value after the value is actually loaded from the state.
        @param sizeout the size (in bytes) of the output variable
        @param sizeinAddress the size (in bytes) of the variable used for indirection
        @param inAddress the value used as the address (or offset)
        @param sizeinValue the size (in bytes) of the variable loaded
        @param inValue the value loaded
        @return the modified value loaded
        """
        ...

    def modBeforeStore(self, sizeout: int, sizeinAddress: int, inAddress: object, sizeinValue: int, inValue: object) -> object:
        """
        Apply any modifications before a value is stored
 
         <p>
         This implements any abstractions associated with {@link PcodeOp#STORE}. This is called on the
         address/offset and the value before the value is actually stored into the state.
        @param sizeout the size (in bytes) of the output variable
        @param sizeinAddress the size (in bytes) of the variable used for indirection
        @param inAddress the value used as the address (or offset)
        @param sizeinValue the size (in bytes) of the variable to store
        @param inValue the value to store
        @return the modified value to store
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ptrAdd(self, sizeout: int, sizeinBase: int, inBase: object, sizeinIndex: int, inIndex: object, inSize: int) -> object:
        """
        Apply the {@link PcodeOp#PTRADD} operator to the given inputs
 
         <p>
         The "pointer add" op takes three operands: base, index, size; and is used as a more compact
         representation of array index address computation. The {@code size} operand must be constant.
         Suppose {@code arr} is an array whose elements are {@code size} bytes each, and the address
         of its first element is {@code base}. The decompiler would likely render the
         {@link PcodeOp#PTRADD} op as {@code &arr[index]}. An equivalent SLEIGH expression is
         {@code base + index*size}.
 
         <p>
         NOTE: This op is always a result of decompiler simplification, not low p-code generation, and
         so are not ordinarily used by a {@link PcodeExecutor}.
        @param sizeout the size (in bytes) of the output variable
        @param sizeinBase the size (in bytes) of the variable used for the array's base address
        @param inBase the value used as the array's base address
        @param sizeinIndex the size (in bytes) of the variable used for the index
        @param inIndex the value used as the index
        @param inSize the size of each array element in bytes
        @return the output value
        """
        ...

    def ptrSub(self, sizeout: int, sizeinBase: int, inBase: object, sizeinOffset: int, inOffset: object) -> object:
        """
        Apply the {@link PcodeOp#PTRSUB} operator to the given inputs
 
         <p>
         The "pointer subfield" op takes two operands: base, offset; and is used as a more specific
         representation of structure field address computation. Its behavior is exactly equivalent to
         {@link PcodeOp#INT_ADD}. Suppose {@code st} is a structure pointer with a field {@code f}
         located {@code inOffset} bytes into the structure, and {@code st} has the value {@code base}.
         The decompiler would likely render the {@link PcodeOp#PTRSUB} op as {@code &st->f}. An
         equivalent SLEIGH expression is {@code base + offset}.
 
         <p>
         NOTE: This op is always a result of decompiler simplification, not low p-code generation, and
         so are not ordinarily used by a {@link PcodeExecutor}.
        @param sizeout the size (in bytes) of the output variable
        @param sizeinBase the size (in bytes) of the variable used for the structure's base address
        @param inBase the value used as the structure's base address
        @param sizeinOffset the size (in bytes) of the variable used for the offset
        @param inOffset the value used as the offset
        @return the output value
        """
        ...

    def sizeOf(self, value: object) -> long:
        """
        Get the size in bytes, if possible, of the given abstract value
 
         <p>
         If the abstract value does not conceptually have a size, throw an exception.
        @param value the abstract value
        @return the size in bytes
        """
        ...

    def sizeOfAbstract(self, value: object) -> object:
        """
        Get the size in bytes, if possible, of the given abstract value, as an abstract value
 
         <p>
         The returned size should itself has a size of {@link #SIZEOF_SIZEOF}.
        @param value the abstract value
        @return the size in bytes, as an abstract value
        """
        ...

    def toBigInteger(self, value: object, purpose: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> long:
        """
        Convert, if possible, the given abstract value to a concrete big integer
 
         <p>
         If the conversion is not possible, throw an exception.
        @param value the abstract value
        @param purpose the reason why the emulator needs a concrete value
        @return the concrete value
        @throws ConcretionError if the value cannot be made concrete
        """
        ...

    def toConcrete(self, value: object, purpose: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> List[int]:
        """
        Convert, if possible, the given abstract value to a concrete byte array
        @param value the abstract value
        @param purpose the purpose for which the emulator needs a concrete value
        @return the array
        @throws ConcretionError if the value cannot be made concrete
        """
        ...

    def toLong(self, value: object, purpose: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> long:
        """
        Convert, if possible, the given abstract value to a concrete long
 
         <p>
         If the conversion is not possible, throw an exception.
        @param value the abstract value
        @param purpose the reason why the emulator needs a concrete value
        @return the concrete value
        @throws ConcretionError if the value cannot be made concrete
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def unaryOp(self, op: ghidra.program.model.pcode.PcodeOp, in1: object) -> object:
        """
        Apply a unary operator to the given input
 
         <p>
         This provides the full p-code op, allowing deeper inspection of the code. For example, an
         arithmetic may wish to distinguish immediate (constant) values from variables. By default,
         this unpacks the details and defers to {@link #unaryOp(int, int, int, Object)}.
        @implNote {@link OpBehaviorFactory#getOpBehavior(int)} for the given opcode is guaranteed to
                   return a derivative of {@link UnaryOpBehavior}.
        @param op the operation
        @param in1 the input value
        @return the output value
        """
        ...

    @overload
    def unaryOp(self, opcode: int, sizeout: int, sizein1: int, in1: object) -> object:
        """
        Apply a unary operator to the given input
 
         <p>
         Note the sizes of variables are given, because values don't necessarily have an intrinsic
         size. For example, a {@link BigInteger} may have a minimum encoding size, but that does not
         necessarily reflect the size of the variable from which is was read.
        @implNote {@link OpBehaviorFactory#getOpBehavior(int)} for the given opcode is guaranteed to
                   return a derivative of {@link UnaryOpBehavior}.
        @param opcode the p-code opcode
        @param sizeout the size (in bytes) of the output variable
        @param sizein1 the size (in bytes) of the input variable
        @param in1 the input value
        @return the output value
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def endian(self) -> ghidra.program.model.lang.Endian: ...