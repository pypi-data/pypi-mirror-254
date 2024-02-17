import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.util.task
import java.lang


class RustUtilities(object):




    def __init__(self): ...



    @staticmethod
    def addExtensions(__a0: ghidra.program.model.listing.Program, __a1: ghidra.util.task.TaskMonitor, __a2: unicode) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isRust(__a0: ghidra.program.model.mem.MemoryBlock) -> bool: ...

    @staticmethod
    def isRustProgram(__a0: ghidra.program.model.listing.Program) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

