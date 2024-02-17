import java.lang
import java.nio.file
import java.util.function


class GhidraGoIPC(object):








    def dispose(self) -> None: ...

    @staticmethod
    def doLockedAction(__a0: java.nio.file.Path, __a1: bool, __a2: java.util.function.Supplier) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isGhidraListening(self) -> bool: ...

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
    def ghidraListening(self) -> bool: ...