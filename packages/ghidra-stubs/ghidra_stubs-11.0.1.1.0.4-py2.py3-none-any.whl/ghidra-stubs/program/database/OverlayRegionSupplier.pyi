import ghidra.program.model.address
import java.lang


class OverlayRegionSupplier(object):
    """
    OverlayRegionSupplier provides a callback mechanism which allows a
     ProgramOverlayAddressSpace to identify defined memory regions within its
     space so that it may properly implement the OverlayAddressSpace#contains(long)
     method.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOverlayAddressSet(self, overlaySpace: ghidra.program.model.address.OverlayAddressSpace) -> ghidra.program.model.address.AddressSetView:
        """
        Get the set of memory address defined within the specified overlay space.
        @param overlaySpace overlay address space
        @return set of memory address defined within the specified overlay space or null
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

