import ghidra.pty
import java.lang


class PtyFactory(object):
    """
    A mechanism for opening pseudo-terminals
    """

    DEFAULT_COLS: int = 80
    DEFAULT_ROWS: int = 25







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Get a human-readable description of the factory
        @return the description
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def local() -> ghidra.pty.PtyFactory:
        """
        Choose a factory of local pty's for the host operating system
        @return the factory
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def openpty(self) -> ghidra.pty.Pty:
        """
        Open a new pseudo-terminal of the default size ({@value #DEFAULT_COLS} x
         {@value #DEFAULT_ROWS})
        @return new new Pty
        @throws IOException for an I/O error, including cancellation
        """
        ...

    @overload
    def openpty(self, cols: int, rows: int) -> ghidra.pty.Pty:
        """
        Open a new pseudo-terminal
        @param cols the initial width in characters, or 0 to let the system decide both dimensions
        @param rows the initial height in characters, or 0 to let the system decide both dimensions
        @return new new Pty
        @throws IOException for an I/O error, including cancellation
        """
        ...

    @overload
    def openpty(self, cols: int, rows: int) -> ghidra.pty.Pty:
        """
        Open a new pseudo-terminal
        @param cols the initial width in characters, or 0 to let the system decide both dimensions
        @param rows the initial height in characters, or 0 to let the system decide both dimensions
        @return new new Pty
        @throws IOException for an I/O error, including cancellation
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def description(self) -> unicode: ...