import ghidra.app.emulator
import ghidra.pcode.emulate
import ghidra.pcode.memstate
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.util.task
import java.lang


class Emulator(object):
    """
    The emulator interface
 
 
     This interface may soon be deprecated. It was extracted from what has now been renamed
     DefaultEmulator. Please consider using PcodeEmulator instead.
    """









    def addMemoryAccessFilter(self, filter: ghidra.app.emulator.MemoryAccessFilter) -> None:
        """
        Add a filter on memory access
        @param filter the filter
        """
        ...

    def dispose(self) -> None:
        """
        Clean up resources used by the emulator
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def executeInstruction(self, stopAtBreakpoint: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Execute instruction at current address
        @param stopAtBreakpoint if true and breakpoint hits at current execution address execution
                    will halt without executing instruction.
        @throws CancelledException if execution was cancelled
        """
        ...

    def getBreakTable(self) -> ghidra.pcode.emulate.BreakTableCallBack:
        """
        Get the breakpoint table
        @return the breakpoint table
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getContextRegisterValue(self) -> ghidra.program.model.lang.RegisterValue:
        """
        Returns the current context register value.
 
         <p>
         The context value returned reflects its state when the previously executed instruction was
         parsed/executed. The context value returned will feed into the next instruction to be parsed
         with its non-flowing bits cleared and any future context state merged in.
        @return context as a RegisterValue object
        """
        ...

    def getEmulateExecutionState(self) -> ghidra.pcode.emulate.EmulateExecutionState:
        """
        Get the low-level execution state
 
         <p>
         This can be useful within a memory fault handler to determine if a memory read was associated
         with instruction parsing (i.e., {@link EmulateExecutionState#INSTRUCTION_DECODE}) or an
         actual emulated read (i.e., {@link EmulateExecutionState#EXECUTE}).
        @return emulator execution state.
        """
        ...

    def getExecuteAddress(self) -> ghidra.program.model.address.Address:
        """
        Get current execution address (or the address of the next instruction to be executed)
        @return current execution address
        """
        ...

    def getFilteredMemState(self) -> ghidra.app.emulator.FilteredMemoryState:
        """
        Get the memory state, modified by all installed access filters
        @return the state
        """
        ...

    def getHalt(self) -> bool:
        """
        Check if the emulator has been halted
        @return true if halted
        """
        ...

    def getLastExecuteAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the address of the last instruction executed (or the instructed currently being executed)
        @return the address
        """
        ...

    def getMemState(self) -> ghidra.pcode.memstate.MemoryState:
        """
        Get the memory state
        @return the state
        """
        ...

    def getPC(self) -> long:
        """
        Get the value of the program counter
        @return the value, i.e., offset in code space
        """
        ...

    def getPCRegisterName(self) -> unicode:
        """
        Get the name of the program counter register
        @return the name
        """
        ...

    def hashCode(self) -> int: ...

    def isAtBreakpoint(self) -> bool:
        """
        @return true if halted at a breakpoint
        """
        ...

    def isExecuting(self) -> bool:
        """
        @return true if emulator is busy executing an instruction
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setContextRegisterValue(self, regValue: ghidra.program.model.lang.RegisterValue) -> None:
        """
        Sets the context register value at the current execute address.
 
         <p>
         The Emulator should not be running when this method is invoked. Only flowing context bits
         should be set, as non-flowing bits will be cleared prior to parsing on instruction. In
         addition, any future context state set by the pcode emitter will take precedence over context
         set using this method. This method is primarily intended to be used to establish the initial
         context state.
        @param regValue is the value to set context to
        """
        ...

    def setExecuteAddress(self, addressableWordOffset: long) -> None:
        """
        Set the value of the program counter
        @param addressableWordOffset the <em>word</em> offset of the instruction to execute next.
        """
        ...

    def setHalt(self, halt: bool) -> None:
        """
        Halt or un-halt the emulator
        @param halt true to halt
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
    def PC(self) -> long: ...

    @property
    def PCRegisterName(self) -> unicode: ...

    @property
    def atBreakpoint(self) -> bool: ...

    @property
    def breakTable(self) -> ghidra.pcode.emulate.BreakTableCallBack: ...

    @property
    def contextRegisterValue(self) -> ghidra.program.model.lang.RegisterValue: ...

    @contextRegisterValue.setter
    def contextRegisterValue(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @property
    def emulateExecutionState(self) -> ghidra.pcode.emulate.EmulateExecutionState: ...

    @property
    def executeAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def executing(self) -> bool: ...

    @property
    def filteredMemState(self) -> ghidra.app.emulator.FilteredMemoryState: ...

    @property
    def halt(self) -> bool: ...

    @halt.setter
    def halt(self, value: bool) -> None: ...

    @property
    def lastExecuteAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def memState(self) -> ghidra.pcode.memstate.MemoryState: ...