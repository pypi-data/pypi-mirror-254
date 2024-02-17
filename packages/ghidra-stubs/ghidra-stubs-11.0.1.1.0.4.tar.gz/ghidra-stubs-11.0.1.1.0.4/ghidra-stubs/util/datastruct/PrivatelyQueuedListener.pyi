import ghidra.util.datastruct
import java.lang


class PrivatelyQueuedListener(object):
    in: object



    @overload
    def __init__(self, __a0: java.lang.Class, __a1: unicode, __a2: object): ...

    @overload
    def __init__(self, __a0: java.lang.Class, __a1: java.util.concurrent.Executor, __a2: object): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setErrorHandler(self, __a0: ghidra.util.datastruct.ListenerErrorHandler) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def errorHandler(self) -> None: ...  # No getter available.

    @errorHandler.setter
    def errorHandler(self, value: ghidra.util.datastruct.ListenerErrorHandler) -> None: ...