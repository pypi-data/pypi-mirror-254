from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.pcode.exec
import ghidra.program.model.listing
import ghidra.program.model.pcode
import java.lang


class PcodeProgram(object):
    """
    A p-code program to be executed by a PcodeExecutor
 
 
     This is a list of p-code operations together with a map of expected userops.
    """









    def equals(self, __a0: object) -> bool: ...

    def execute(self, executor: ghidra.pcode.exec.PcodeExecutor, library: ghidra.pcode.exec.PcodeUseropLibrary) -> None:
        """
        Execute this program using the given executor and library
        @param <T> the type of values to be operated on
        @param executor the executor
        @param library the library
        """
        ...

    @staticmethod
    def fromInject(program: ghidra.program.model.listing.Program, name: unicode, type: int) -> ghidra.pcode.exec.PcodeProgram:
        """
        Generate a p-code program from a given program's inject library
        @param program the program
        @param name the name of the snippet
        @param type the type of the snippet
        @return the p-code program
        @throws MemoryAccessException for problems establishing the injection context
        @throws IOException for problems while emitting the injection p-code
        @throws UnknownInstructionException if there is no underlying instruction being injected
        @throws NotFoundException if an expected aspect of the injection is not present in context
        """
        ...

    @overload
    @staticmethod
    def fromInstruction(instruction: ghidra.program.model.listing.Instruction) -> ghidra.pcode.exec.PcodeProgram:
        """
        Generate a p-code program from the given instruction, without overrides
        @param instruction the instruction
        @return the p-code program
        """
        ...

    @overload
    @staticmethod
    def fromInstruction(instruction: ghidra.program.model.listing.Instruction, includeOverrides: bool) -> ghidra.pcode.exec.PcodeProgram:
        """
        Generate a p-code program from the given instruction
        @param instruction the instruction
        @param includeOverrides as in {@link Instruction#getPcode(boolean)}
        @return the p-code program
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCode(self) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    def getLanguage(self) -> ghidra.app.plugin.processors.sleigh.SleighLanguage:
        """
        Get the language generating this program
        @return the language
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
    def code(self) -> List[object]: ...

    @property
    def language(self) -> ghidra.app.plugin.processors.sleigh.SleighLanguage: ...