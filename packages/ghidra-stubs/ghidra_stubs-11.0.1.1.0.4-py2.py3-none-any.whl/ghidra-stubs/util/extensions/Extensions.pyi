from typing import List
import ghidra.util.extensions
import java.lang


class Extensions(object):
    """
    A collection of all extensions found.  This class provides methods processing duplicates and
     managing extensions marked for removal.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMatchingExtensions(self, e: ghidra.util.extensions.ExtensionDetails) -> List[ghidra.util.extensions.ExtensionDetails]:
        """
        Returns all extensions matching the given details
        @param e the extension details to match
        @return all matching extensions
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

