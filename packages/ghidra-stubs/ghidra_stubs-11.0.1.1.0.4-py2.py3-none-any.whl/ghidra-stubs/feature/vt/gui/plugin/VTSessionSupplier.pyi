import ghidra.feature.vt.api.main
import java.lang


class VTSessionSupplier(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSession(self) -> ghidra.feature.vt.api.main.VTSession: ...

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

    @property
    def session(self) -> ghidra.feature.vt.api.main.VTSession: ...