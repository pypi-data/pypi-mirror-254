from typing import List
import ghidra.app.util.bin
import ghidra.app.util.importer
import ghidra.app.util.opinion
import ghidra.program.database.mem
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class DyldCacheExtractProgramBuilder(ghidra.app.util.opinion.MachoProgramBuilder):








    @staticmethod
    def buildProgram(__a0: ghidra.program.model.listing.Program, __a1: ghidra.app.util.bin.ByteProvider, __a2: ghidra.program.database.mem.FileBytes, __a3: ghidra.app.util.importer.MessageLog, __a4: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processChainedFixups(self, __a0: List[object]) -> List[object]: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

