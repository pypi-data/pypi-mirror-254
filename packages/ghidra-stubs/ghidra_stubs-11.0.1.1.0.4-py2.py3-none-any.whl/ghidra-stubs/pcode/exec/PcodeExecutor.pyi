from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.pcode.exec
import ghidra.pcode.exec.PcodeExecutorStatePiece
import ghidra.pcode.opbehavior
import ghidra.program.model.pcode
import java.lang
import java.util


class PcodeExecutor(object):
    """
    An executor of p-code programs
 
 
     This is the kernel of Sleigh expression evaluation and p-code emulation. For a complete example
     of a p-code emulator, see PcodeEmulator.
    """





    def __init__(self, language: ghidra.app.plugin.processors.sleigh.SleighLanguage, arithmetic: ghidra.pcode.exec.PcodeArithmetic, state: ghidra.pcode.exec.PcodeExecutorState, reason: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason):
        """
        Construct an executor with the given bindings
        @param language the processor language
        @param arithmetic an implementation of arithmetic p-code ops
        @param state an implementation of load/store p-code ops
        @param reason a reason for reading the state with this executor
        """
        ...



    @overload
    def begin(self, program: ghidra.pcode.exec.PcodeProgram) -> ghidra.pcode.exec.PcodeFrame:
        """
        Begin execution of the given program
        @param program the program, e.g., from an injection, or a decoded instruction
        @return the frame
        """
        ...

    @overload
    def begin(self, __a0: List[object], __a1: java.util.Map) -> ghidra.pcode.exec.PcodeFrame: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def execute(self, program: ghidra.pcode.exec.PcodeProgram, library: ghidra.pcode.exec.PcodeUseropLibrary) -> ghidra.pcode.exec.PcodeFrame:
        """
        Execute a program using the given library
        @param program the program, e.g., from an injection, or a decoded instruction
        @param library the library
        @return the frame
        """
        ...

    @overload
    def execute(self, __a0: List[object], __a1: java.util.Map, __a2: ghidra.pcode.exec.PcodeUseropLibrary) -> ghidra.pcode.exec.PcodeFrame: ...

    def executeBinaryOp(self, op: ghidra.program.model.pcode.PcodeOp, b: ghidra.pcode.opbehavior.BinaryOpBehavior) -> None:
        """
        Execute the given binary op
        @param op the op
        @param b the op behavior
        """
        ...

    def executeBranch(self, op: ghidra.program.model.pcode.PcodeOp, frame: ghidra.pcode.exec.PcodeFrame) -> None:
        """
        Execute a branch
 
         <p>
         This merely defers to {@link #doExecuteBranch(PcodeOp, PcodeFrame)}. To instrument the
         operation, override this. To modify or instrument branching in general, override
         {@link #doExecuteBranch(PcodeOp, PcodeFrame)}, {@link #branchToOffset(Object, PcodeFrame)},
         and/or {@link #branchToAddress(Address)}.
        @param op the op
        @param frame the frame
        """
        ...

    def executeCall(self, op: ghidra.program.model.pcode.PcodeOp, frame: ghidra.pcode.exec.PcodeFrame, library: ghidra.pcode.exec.PcodeUseropLibrary) -> None:
        """
        Execute a call
        @param op the op
        @param frame the frame
        """
        ...

    def executeCallother(self, op: ghidra.program.model.pcode.PcodeOp, frame: ghidra.pcode.exec.PcodeFrame, library: ghidra.pcode.exec.PcodeUseropLibrary) -> None:
        """
        Execute a userop call
        @param op the op
        @param frame the frame
        @param library the library of userops
        """
        ...

    def executeConditionalBranch(self, op: ghidra.program.model.pcode.PcodeOp, frame: ghidra.pcode.exec.PcodeFrame) -> None:
        """
        Execute a conditional branch
        @param op the op
        @param frame the frame
        """
        ...

    def executeIndirectBranch(self, op: ghidra.program.model.pcode.PcodeOp, frame: ghidra.pcode.exec.PcodeFrame) -> None:
        """
        Execute an indirect branch
 
         <p>
         This merely defers to {@link #doExecuteIndirectBranch(PcodeOp, PcodeFrame)}. To instrument
         the operation, override this. To modify or instrument indirect branching in general, override
         {@link #doExecuteIndirectBranch(PcodeOp, PcodeFrame)}.
        @param op the op
        @param frame the frame
        """
        ...

    def executeIndirectCall(self, op: ghidra.program.model.pcode.PcodeOp, frame: ghidra.pcode.exec.PcodeFrame) -> None:
        """
        Execute an indirect call
        @param op the op
        @param frame the frame
        """
        ...

    def executeLoad(self, op: ghidra.program.model.pcode.PcodeOp) -> None:
        """
        Execute a load
        @param op the op
        """
        ...

    def executeReturn(self, op: ghidra.program.model.pcode.PcodeOp, frame: ghidra.pcode.exec.PcodeFrame) -> None:
        """
        Execute a return
        @param op the op
        @param frame the frame
        """
        ...

    def executeSleigh(self, source: unicode) -> None:
        """
        Compile and execute a block of Sleigh
        @param source the Sleigh source
        """
        ...

    def executeStore(self, op: ghidra.program.model.pcode.PcodeOp) -> None:
        """
        Execute a store
        @param op the op
        """
        ...

    def executeUnaryOp(self, op: ghidra.program.model.pcode.PcodeOp, b: ghidra.pcode.opbehavior.UnaryOpBehavior) -> None:
        """
        Execute the given unary op
        @param op the op
        @param b the op behavior
        """
        ...

    def finish(self, frame: ghidra.pcode.exec.PcodeFrame, library: ghidra.pcode.exec.PcodeUseropLibrary) -> None:
        """
        Finish execution of a frame
 
         <p>
         TODO: This is not really sufficient for continuation after a break, esp. if that break occurs
         within a nested call back into the executor. This would likely become common when using pCode
         injection.
        @param frame the incomplete frame
        @param library the library of userops to use
        """
        ...

    def getArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic:
        """
        Get the arithmetic applied by the executor
        @return the arithmetic
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLanguage(self) -> ghidra.app.plugin.processors.sleigh.SleighLanguage:
        """
        Get the executor's Sleigh language (processor model)
        @return the language
        """
        ...

    def getReason(self) -> ghidra.pcode.exec.PcodeExecutorStatePiece.Reason:
        """
        Get the reason for reading state with this executor
        @return the reason
        """
        ...

    def getState(self) -> ghidra.pcode.exec.PcodeExecutorState:
        """
        Get the state bound to this executor
        @return the state
        """
        ...

    def getUseropName(self, opNo: int, frame: ghidra.pcode.exec.PcodeFrame) -> unicode:
        """
        Get the name of a userop
        @param opNo the userop number
        @param frame the frame
        @return the name, or null if it is not defined
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def skip(self, frame: ghidra.pcode.exec.PcodeFrame) -> None:
        """
        Skip a single p-code op
        @param frame the frame whose next op to skip
        """
        ...

    def step(self, frame: ghidra.pcode.exec.PcodeFrame, library: ghidra.pcode.exec.PcodeUseropLibrary) -> None:
        """
        Step a single p-code op
        @param frame the frame whose next op to execute
        @param library the userop library
        """
        ...

    def stepOp(self, op: ghidra.program.model.pcode.PcodeOp, frame: ghidra.pcode.exec.PcodeFrame, library: ghidra.pcode.exec.PcodeUseropLibrary) -> None:
        """
        Step on p-code op
        @param op the op
        @param frame the current frame
        @param library the library, invoked in case of {@link PcodeOp#CALLOTHER}
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
    def arithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    @property
    def language(self) -> ghidra.app.plugin.processors.sleigh.SleighLanguage: ...

    @property
    def reason(self) -> ghidra.pcode.exec.PcodeExecutorStatePiece.Reason: ...

    @property
    def state(self) -> ghidra.pcode.exec.PcodeExecutorState: ...