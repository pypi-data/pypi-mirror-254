import java.io
import java.lang


class PtyEndpoint(object):
    """
    One end of a pseudo-terminal
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInputStream(self) -> java.io.InputStream:
        """
        Get the input stream for this end of the pty
 
         <p>
         Writes to the output stream of the opposite end arrive here, subject to the terminal's line
         discipline.
        @return the input stream
        @throws UnsupportedOperationException if this end is not local
        """
        ...

    def getOutputStream(self) -> java.io.OutputStream:
        """
        Get the output stream for this end of the pty
 
         <p>
         Writes to this stream arrive on the input stream for the opposite end, subject to the
         terminal's line discipline.
        @return the output stream
        @throws UnsupportedOperationException if this end is not local
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

    @property
    def inputStream(self) -> java.io.InputStream: ...

    @property
    def outputStream(self) -> java.io.OutputStream: ...