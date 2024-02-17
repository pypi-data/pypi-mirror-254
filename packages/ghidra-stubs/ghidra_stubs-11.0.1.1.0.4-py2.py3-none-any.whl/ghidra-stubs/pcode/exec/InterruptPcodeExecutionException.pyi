from typing import List
import ghidra.pcode.exec
import java.io
import java.lang


class InterruptPcodeExecutionException(ghidra.pcode.exec.PcodeExecutionException):
    """
    Exception thrown by PcodeEmulationLibrary#emu_swi(), a p-code userop exported by
     emulators for implementing breakpoints.
    """





    def __init__(self, frame: ghidra.pcode.exec.PcodeFrame, cause: java.lang.Throwable): ...



    def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fillInStackTrace(self) -> java.lang.Throwable: ...

    def getCause(self) -> java.lang.Throwable: ...

    def getClass(self) -> java.lang.Class: ...

    def getFrame(self) -> ghidra.pcode.exec.PcodeFrame:
        """
        Get the frame at the time of the exception
 
         <p>
         Note that the frame counter is advanced <em>before</em> execution of the p-code op. Thus, the
         counter often points to the op following the one which caused the exception. For a frame to
         be present and meaningful, the executor must intervene between the throw and the catch. In
         other words, if you're invoking the executor, you should always expect to see a frame. If you
         are implementing, e.g., a userop, then it is possible to catch an exception without frame
         information populated. You might instead retrieve the frame from the executor, if you have a
         handle to it.
        @return the frame, possibly {@code null}
        """
        ...

    def getLocalizedMessage(self) -> unicode: ...

    def getMessage(self) -> unicode: ...

    def getStackTrace(self) -> List[java.lang.StackTraceElement]: ...

    def getSuppressed(self) -> List[java.lang.Throwable]: ...

    def hashCode(self) -> int: ...

    def initCause(self, __a0: java.lang.Throwable) -> java.lang.Throwable: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def printStackTrace(self) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintStream) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintWriter) -> None: ...

    def setStackTrace(self, __a0: List[java.lang.StackTraceElement]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

