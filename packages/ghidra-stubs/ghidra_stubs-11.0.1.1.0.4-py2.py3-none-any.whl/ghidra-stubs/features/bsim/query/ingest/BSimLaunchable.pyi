from typing import List
import ghidra
import ghidra.util.task
import java.lang
import utility.application


class BSimLaunchable(object, ghidra.GhidraLaunchable):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def initializeApplication(__a0: utility.application.ApplicationLayout, __a1: int, __a2: unicode, __a3: unicode) -> None: ...

    def launch(self, __a0: ghidra.GhidraApplicationLayout, __a1: List[unicode]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def run(self, __a0: List[unicode]) -> None: ...

    @overload
    def run(self, __a0: List[unicode], __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

