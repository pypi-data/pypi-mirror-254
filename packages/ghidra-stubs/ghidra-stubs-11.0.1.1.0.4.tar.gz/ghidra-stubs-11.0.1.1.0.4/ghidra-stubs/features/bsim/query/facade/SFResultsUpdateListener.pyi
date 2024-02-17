import ghidra.features.bsim.query.protocol
import java.lang


class SFResultsUpdateListener(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resultAdded(self, __a0: ghidra.features.bsim.query.protocol.QueryResponseRecord) -> None: ...

    def setFinalResult(self, __a0: object) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def finalResult(self) -> None: ...  # No getter available.

    @finalResult.setter
    def finalResult(self, value: object) -> None: ...