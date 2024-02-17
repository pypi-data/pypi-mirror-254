import ghidra.debug.api.emulation
import ghidra.debug.api.target
import ghidra.framework.plugintool
import ghidra.trace.model.guest
import java.lang


class AbstractDebuggerPcodeEmulatorFactory(object, ghidra.debug.api.emulation.DebuggerPcodeEmulatorFactory):




    def __init__(self): ...



    @overload
    def create(self, __a0: ghidra.debug.api.emulation.PcodeDebuggerAccess) -> ghidra.debug.api.emulation.DebuggerPcodeMachine: ...

    @overload
    def create(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.trace.model.guest.TracePlatform, __a2: long, __a3: ghidra.debug.api.target.Target) -> ghidra.debug.api.emulation.DebuggerPcodeMachine: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getTitle(self) -> unicode: ...

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
    def title(self) -> unicode: ...