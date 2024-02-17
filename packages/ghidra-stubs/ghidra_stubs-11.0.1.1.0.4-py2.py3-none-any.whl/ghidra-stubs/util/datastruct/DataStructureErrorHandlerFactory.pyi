import ghidra.util.datastruct
import java.lang


class DataStructureErrorHandlerFactory(object):
    """
    A class data structures can use to delegate error handling responsibilities to system-level
     decision making.  This allows for specialized error handling in testing mode.
    """





    def __init__(self): ...



    @staticmethod
    def createListenerErrorHandler() -> ghidra.util.datastruct.ListenerErrorHandler:
        """
        Creates a {@link ListenerErrorHandler}
        @return the error handler
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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

