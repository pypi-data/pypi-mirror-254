import java.lang


class Permissions(object):
    ALL: ghidra.app.util.Permissions = ghidra.app.util.Permissions@552caec5
    READ_EXECUTE: ghidra.app.util.Permissions = ghidra.app.util.Permissions@5453dde2
    READ_ONLY: ghidra.app.util.Permissions = ghidra.app.util.Permissions@6d632f6
    execute: bool
    read: bool
    write: bool



    def __init__(self, read: bool, write: bool, execute: bool): ...



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

