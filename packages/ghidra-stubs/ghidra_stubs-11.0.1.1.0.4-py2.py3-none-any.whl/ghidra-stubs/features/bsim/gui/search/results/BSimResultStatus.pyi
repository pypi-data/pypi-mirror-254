from typing import List
import ghidra.features.bsim.gui.search.results
import java.lang
import java.util


class BSimResultStatus(java.lang.Enum):
    APPLIED_NO_LONGER_MATCHES: ghidra.features.bsim.gui.search.results.BSimResultStatus = APPLIED_NO_LONGER_MATCHES
    ERROR: ghidra.features.bsim.gui.search.results.BSimResultStatus = ERROR
    IGNORED: ghidra.features.bsim.gui.search.results.BSimResultStatus = IGNORED
    MATCHES: ghidra.features.bsim.gui.search.results.BSimResultStatus = MATCHES
    NAME_APPLIED: ghidra.features.bsim.gui.search.results.BSimResultStatus = NAME_APPLIED
    NOT_APPLIED: ghidra.features.bsim.gui.search.results.BSimResultStatus = NOT_APPLIED
    NO_FUNCTION: ghidra.features.bsim.gui.search.results.BSimResultStatus = NO_FUNCTION
    SIGNATURE_APPLIED: ghidra.features.bsim.gui.search.results.BSimResultStatus = SIGNATURE_APPLIED







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def describeConstable(self) -> java.util.Optional: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.features.bsim.gui.search.results.BSimResultStatus: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.features.bsim.gui.search.results.BSimResultStatus]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def description(self) -> unicode: ...