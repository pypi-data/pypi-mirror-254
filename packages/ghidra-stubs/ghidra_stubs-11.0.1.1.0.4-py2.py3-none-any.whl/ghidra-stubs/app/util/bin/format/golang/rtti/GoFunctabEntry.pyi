import ghidra.app.util.bin.format.golang.rtti
import ghidra.program.model.address
import java.lang


class GoFunctabEntry(object):
    """
    A structure that golang generates that maps between a function's entry point and the
     location of the function's GoFuncData structure.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFuncAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address of the function's entry point
        @return address of the function's entry point
        """
        ...

    def getFuncData(self) -> ghidra.app.util.bin.format.golang.rtti.GoFuncData:
        """
        Return the GoFuncData structure that contains metadata about the function.
        @return {@link GoFuncData} structure that contains metadata about the function.
        @throws IOException if error
        """
        ...

    def getFuncoff(self) -> long:
        """
        Returns the offset of the GoFuncData structure.
        @return offset of the GoFuncData structure.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setEntry(self, entry: long) -> None:
        """
        Set the function's entry point using the absolute address.
         <p>
         Called via deserialization for entry fieldmapping annotation.
        @param entry address of the function's entry point
        """
        ...

    def setEntryoff(self, entryoff: long) -> None:
        """
        Set the function's entry point using a relative offset.
         <p>
         Called via deserialization for entryoff fieldmapping annotation.
        @param entryoff relative offset of the function's entry point
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
    def entry(self) -> None: ...  # No getter available.

    @entry.setter
    def entry(self, value: long) -> None: ...

    @property
    def entryoff(self) -> None: ...  # No getter available.

    @entryoff.setter
    def entryoff(self, value: long) -> None: ...

    @property
    def funcAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def funcData(self) -> ghidra.app.util.bin.format.golang.rtti.GoFuncData: ...

    @property
    def funcoff(self) -> long: ...