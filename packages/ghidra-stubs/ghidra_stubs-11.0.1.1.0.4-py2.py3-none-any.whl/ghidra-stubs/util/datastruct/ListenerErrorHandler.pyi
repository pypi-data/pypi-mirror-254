import java.lang


class ListenerErrorHandler(object):
    """
    A simple interface that allows listener structures to use different error handling
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def handleError(self, listener: object, t: java.lang.Throwable) -> None:
        """
        Handles the given error
        @param listener the listener that generated the error
        @param t the error
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

