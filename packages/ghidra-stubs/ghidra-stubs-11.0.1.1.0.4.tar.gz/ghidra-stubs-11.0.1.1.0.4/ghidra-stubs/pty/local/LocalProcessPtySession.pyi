import ghidra.pty
import java.lang


class LocalProcessPtySession(object, ghidra.pty.PtySession):
    """
    A pty session consisting of a local process and its descendants
    """





    def __init__(self, process: java.lang.Process, ptyName: unicode): ...



    def description(self) -> unicode: ...

    def destroyForcibly(self) -> None: ...

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

    def waitExited(self) -> int: ...

