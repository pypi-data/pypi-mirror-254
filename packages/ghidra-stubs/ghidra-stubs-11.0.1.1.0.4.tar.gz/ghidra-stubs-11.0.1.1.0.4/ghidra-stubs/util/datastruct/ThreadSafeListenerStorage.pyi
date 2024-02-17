import java.lang


class ThreadSafeListenerStorage(object):
    """
    A very specific data structure that provides 'copy on write' behavior while the client is
     iterating the elements.
 
     This class is meant for a very narrow and specific use case that includes: having a relatively
     small number of listeners and the need for only basic adding, removing and iterating.
 
     This class will create a new copy of its internal storage for any write operation, but only if
     that happens while the elements in this class are being iterated.  This avoids unnecessary
     copying.
    """





    def __init__(self): ...



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

