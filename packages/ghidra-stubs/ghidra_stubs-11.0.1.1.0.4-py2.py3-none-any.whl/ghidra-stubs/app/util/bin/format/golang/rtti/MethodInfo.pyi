import ghidra.program.model.address
import ghidra.program.model.data
import java.lang


class MethodInfo(object):
    """
    Abstract base for information about type methods and interface methods
    """





    def __init__(self, address: ghidra.program.model.address.Address): ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Entry point of the method
        @return {@link Address}
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getSignature(self) -> ghidra.program.model.data.FunctionDefinition:
        """
        Function signature of the method.
        @return {@link FunctionDefinition}
        @throws IOException if error reading method information
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def signature(self) -> ghidra.program.model.data.FunctionDefinition: ...