import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang


class ParameterPieces(object):
    """
    Basic elements of a parameter: address, data-type, properties
    """

    address: ghidra.program.model.address.Address
    hiddenReturnPtr: bool
    isIndirect: bool
    isThisPointer: bool
    joinPieces: List[ghidra.program.model.pcode.Varnode]
    type: ghidra.program.model.data.DataType



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getVariableStorage(self, program: ghidra.program.model.listing.Program) -> ghidra.program.model.listing.VariableStorage: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def swapMarkup(self, op: ghidra.program.model.lang.ParameterPieces) -> None:
        """
        Swap data-type markup between this and another parameter
 
         Swap any data-type and flags, but leave the storage address intact.
         This assumes the two parameters are the same size.
        @param op is the other parameter to swap with this.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

