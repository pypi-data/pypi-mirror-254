import ghidra.pty
import java.io
import java.lang


class PtyParent(ghidra.pty.PtyEndpoint, object):
    """
    The parent (UNIX "master") end of a pseudo-terminal
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInputStream(self) -> java.io.InputStream: ...

    def getOutputStream(self) -> java.io.OutputStream: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setWindowSize(self, cols: int, rows: int) -> None:
        """
        Resize the terminal window to the given width and height, in characters
        @param cols the width in characters
        @param rows the height in characters
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
    def inputStream(self) -> java.io.InputStream: ...

    @property
    def outputStream(self) -> java.io.OutputStream: ...