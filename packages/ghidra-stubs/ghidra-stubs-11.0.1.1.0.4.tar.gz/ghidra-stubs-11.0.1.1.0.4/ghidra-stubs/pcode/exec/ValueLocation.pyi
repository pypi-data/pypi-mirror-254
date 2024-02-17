import ghidra.pcode.exec
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.pcode
import java.lang


class ValueLocation(object):
    """
    The location of a value
 
 
     This is an analog to VariableStorage, except that this records the actual storage
     location of the evaluated variable or expression. This does not incorporate storage of
     intermediate dereferenced values. For example, suppose , and we want to
     evaluate . The storage would be , not
     .
    """





    @overload
    def __init__(self, nodes: List[ghidra.program.model.pcode.Varnode]):
        """
        Construct a location from a list of varnodes
 
         <p>
         Any leading varnodes which are constant 0s are removed.
        @param nodes the varnodes
        """
        ...

    @overload
    def __init__(self, __a0: List[object]): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fromConst(value: long, size: int) -> ghidra.pcode.exec.ValueLocation:
        """
        Generate the "location" of a constant
        @param value the value
        @param size the size of the constant in bytes
        @return the "location"
        """
        ...

    @staticmethod
    def fromVarnode(address: ghidra.program.model.address.Address, size: int) -> ghidra.pcode.exec.ValueLocation:
        """
        Generate a location from a varnode
        @param address the dynamic address of the variable
        @param size the size of the variable in bytes
        @return the location
        """
        ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the address of the first varnode
        @return the address, or null if this location has no varnodes
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getConst(self) -> long:
        """
        If the location represents a constant, get its value
        @return the constant value
        """
        ...

    def hashCode(self) -> int: ...

    def intOr(self, that: ghidra.pcode.exec.ValueLocation) -> ghidra.pcode.exec.ValueLocation:
        """
        Apply a {@link PcodeOp#INT_OR} operator
 
         <p>
         There is a very restrictive set of constraints for which this yields a non-null location. If
         either this or that is empty, the other is returned. Otherwise, the varnodes are arranged in
         pairs by taking one from each storage starting at the right, or least-significant varnode.
         Each pair must match in length, and one of the pair must be a constant zero. The non-zero
         varnode is taken. The unpaired varnodes to the left, if any, are all taken. If any pair does
         not match in length, or if neither is zero, the resulting location is null. This logic is to
         ensure location information is accrued during concatenation.
        @param that the other location
        @return the location
        """
        ...

    def isEmpty(self) -> bool:
        """
        Check if this location includes any varnodes
 
         <p>
         Note that a location cannot consist entirely of constant zeros and be non-empty. The
         constructor will have removed them all.
        @return true if empty
        """
        ...

    def nodeCount(self) -> int:
        """
        Get the number of varnodes for this location
        @return the count
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def shiftLeft(self, amount: int) -> ghidra.pcode.exec.ValueLocation:
        """
        Apply a {@link PcodeOp#INT_LEFT} operator
 
         <p>
         This requires the shift amount to represent an integral number of bytes. Otherwise, the
         result is null. This simply inserts a constant zero to the right, having the number of bytes
         indicated by the shift amount. This logic is to ensure location information is accrued during
         concatenation.
        @param amount the number of bits to shift
        @return the location.
        """
        ...

    def size(self) -> int:
        """
        Get the total size of this location in bytes
        @return the size in bytes
        """
        ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    def toString(self, language: ghidra.program.model.lang.Language) -> unicode:
        """
        Render this location as a string, substituting registers where applicable
        @param language the optional language for register substitution
        @return the string
        """
        ...

    @staticmethod
    def vnToString(vn: ghidra.program.model.pcode.Varnode, language: ghidra.program.model.lang.Language) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def const(self) -> long: ...

    @property
    def empty(self) -> bool: ...