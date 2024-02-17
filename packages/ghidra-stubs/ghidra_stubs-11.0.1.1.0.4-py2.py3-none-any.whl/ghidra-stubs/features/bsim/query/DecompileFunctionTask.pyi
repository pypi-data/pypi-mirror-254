import ghidra.features.bsim.query
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class DecompileFunctionTask(object):








    def clone(self, __a0: int) -> ghidra.features.bsim.query.DecompileFunctionTask: ...

    def decompile(self, __a0: ghidra.program.model.listing.Function, __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def initializeGlobal(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def shutdown(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

