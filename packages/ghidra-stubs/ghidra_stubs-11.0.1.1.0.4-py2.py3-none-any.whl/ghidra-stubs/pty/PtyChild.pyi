from typing import List
import ghidra.pty
import ghidra.pty.PtyChild
import java.io
import java.lang
import java.util


class PtyChild(ghidra.pty.PtyEndpoint, object):
    """
    The child (UNIX "slave") end of a pseudo-terminal
    """






    class Echo(java.lang.Enum, ghidra.pty.PtyChild.TermMode):
        OFF: ghidra.pty.PtyChild.Echo = OFF
        ON: ghidra.pty.PtyChild.Echo = ON







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def describeConstable(self) -> java.util.Optional: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.pty.PtyChild.Echo: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.pty.PtyChild.Echo]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class TermMode(object):








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







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInputStream(self) -> java.io.InputStream: ...

    def getOutputStream(self) -> java.io.OutputStream: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def nullSession(self, mode: List[ghidra.pty.PtyChild.TermMode]) -> unicode:
        """
        @see #nullSession(Collection)
        """
        ...

    @overload
    def nullSession(self, mode: java.util.Collection) -> unicode:
        """
        Start a session without a real leader, instead obtaining the pty's name
 
         <p>
         This method or any other {@code session} method can only be invoked once per pty. It must be
         called before anyone reads the parent's output stream, since obtaining the filename may be
         implemented by the parent sending commands to its child.
 
         <p>
         If the child end of the pty is on a remote system, this should be the file (or other
         resource) name as it would be accessed on that remote system.
        @param mode the terminal mode. If a mode is not implemented, it may be silently ignored.
        @return the file name
        @throws IOException if the session could not be started or the pty name could not be
                     determined
        """
        ...

    @overload
    def session(self, args: List[unicode], env: java.util.Map, mode: List[ghidra.pty.PtyChild.TermMode]) -> ghidra.pty.PtySession:
        """
        @see #session(String[], Map, File, Collection)
        """
        ...

    @overload
    def session(self, args: List[unicode], env: java.util.Map, workingDirectory: java.io.File, mode: List[ghidra.pty.PtyChild.TermMode]) -> ghidra.pty.PtySession:
        """
        @see #session(String[], Map, File, Collection)
        """
        ...

    @overload
    def session(self, args: List[unicode], env: java.util.Map, workingDirectory: java.io.File, mode: java.util.Collection) -> ghidra.pty.PtySession:
        """
        Spawn a subprocess in a new session whose controlling tty is this pseudo-terminal
 
         <p>
         This method or {@link #nullSession(Collection)} can only be invoked once per pty.
        @param args the image path and arguments
        @param env the environment
        @param workingDirectory the working directory
        @param mode the terminal mode. If a mode is not implemented, it may be silently ignored.
        @return a handle to the subprocess
        @throws IOException if the session could not be started
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