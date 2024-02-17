import ghidra.debug.api.tracermi
import java.lang
import java.net


class TraceRmiAcceptor(object):








    def accept(self) -> ghidra.debug.api.tracermi.TraceRmiConnection: ...

    def cancel(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> java.net.SocketAddress: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setTimeout(self, __a0: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def address(self) -> java.net.SocketAddress: ...

    @property
    def timeout(self) -> None: ...  # No getter available.

    @timeout.setter
    def timeout(self, value: int) -> None: ...