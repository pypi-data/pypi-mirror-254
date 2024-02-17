import java.lang


class MemoryAccessFilter(object):
    """
    A means of intercepting and/or modifying the emulator's memory access.
 
 
     Several of these filters may be chained together, each being invoked in the reverse of the order
     added. In this way, the first added gets the "final say," but it also is farthest from the
     original request.
    """





    def __init__(self): ...



    def dispose(self) -> None:
        """
        Dispose this filter which will cause it to be removed from the memory state.
 
         <p>
         If overriden, be sure to invoke {@code super.dispose()}.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def filterOnExecutionOnly(self) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setFilterOnExecutionOnly(self, filterOnExecutionOnly: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

