import ghidra.pcode.emu
import ghidra.program.model.lang
import ghidra.util.classfinder
import java.lang


class PcodeStateInitializer(ghidra.util.classfinder.ExtensionPoint, object):
    """
    An extension for preparing execution state for sleigh emulation
 
 
     As much as possible, it's highly-recommended to use Sleigh execution to perform any
     modifications. This will help it remain agnostic to various state types.
 
 
     TODO: Implement annotation-based #isApplicable(Language)?
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def initializeMachine(self, machine: ghidra.pcode.emu.PcodeMachine) -> None:
        """
        The machine's memory state has just been initialized, and additional initialization is needed
         for Sleigh execution
 
         <p>
         There's probably not much preparation of memory
        @param <T> the type of values in the machine state
        @param machine the newly-initialized machine
        """
        ...

    def initializeThread(self, thread: ghidra.pcode.emu.PcodeThread) -> None:
        """
        The thread's register state has just been initialized, and additional initialization is
         needed for Sleigh execution
 
         <p>
         Initialization generally consists of setting "virtual" registers using data from the real
         ones. Virtual registers are those specified in the Sleigh, but which don't actually exist on
         the target processor. Often, they exist to simplify static analysis, but unfortunately cause
         a minor headache for dynamic execution.
        @param <T> the type of values in the machine state
        @param thread the newly-initialized thread
        """
        ...

    def isApplicable(self, language: ghidra.program.model.lang.Language) -> bool:
        """
        Check if this initializer applies to the given language
        @param language the language to check
        @return true if it applies, false otherwise
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

