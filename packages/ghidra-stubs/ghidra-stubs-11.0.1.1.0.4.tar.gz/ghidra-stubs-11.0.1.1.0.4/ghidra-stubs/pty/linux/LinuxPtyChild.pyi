from typing import List
import ghidra.pty
import ghidra.pty.linux
import java.io
import java.lang
import java.util


class LinuxPtyChild(ghidra.pty.linux.LinuxPtyEndpoint, ghidra.pty.PtyChild):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInputStream(self) -> java.io.InputStream: ...

    def getOutputStream(self) -> java.io.OutputStream: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def nullSession(self, __a0: List[ghidra.pty.PtyChild.TermMode]) -> unicode: ...

    @overload
    def nullSession(self, mode: java.util.Collection) -> unicode: ...

    @overload
    def session(self, __a0: List[unicode], __a1: java.util.Map, __a2: List[ghidra.pty.PtyChild.TermMode]) -> ghidra.pty.PtySession: ...

    @overload
    def session(self, __a0: List[unicode], __a1: java.util.Map, __a2: java.io.File, __a3: List[ghidra.pty.PtyChild.TermMode]) -> ghidra.pty.PtySession: ...

    @overload
    def session(self, args: List[unicode], env: java.util.Map, workingDirectory: java.io.File, mode: java.util.Collection) -> ghidra.pty.PtySession:
        """
        {@inheritDoc}
        @implNote This uses {@link ProcessBuilder} to launch the subprocess. See its documentation
                   for more details of the parameters of this method.
        @implNote This actually launches a special "leader" subprocess, which sets up the session and
                   then executes the requested program. The requested program image replaces the
                   leader so that the returned process is indeed a handle to the requested program.
                   Ordinarily, this does not matter, but it may be useful to know when debugging.
                   Furthermore, if special characters are sent on the parent before the image is
                   replaced, they may be received by the leader instead. For example, Ctrl-C might be
                   received by the leader by mistake if sent immediately upon spawning a new session.
                   Users should send a simple command, e.g., "echo", to confirm that the requested
                   program is active before sending special characters.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

