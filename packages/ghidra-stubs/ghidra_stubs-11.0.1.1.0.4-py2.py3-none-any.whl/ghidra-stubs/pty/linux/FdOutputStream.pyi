from typing import List
import java.io
import java.lang


class FdOutputStream(java.io.OutputStream):
    """
    An output stream that wraps a native POSIX file descriptor
 
 
     WARNING: This class makes use of jnr-ffi to invoke native functions. An invalid file
     descriptor is generally detected, but an incorrect, but valid file descriptor may cause undefined
     behavior.
    """









    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def flush(self) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def nullOutputStream() -> java.io.OutputStream: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @overload
    def write(self, b: int) -> None: ...

    @overload
    def write(self, b: List[int]) -> None: ...

    @overload
    def write(self, b: List[int], off: int, len: int) -> None: ...

