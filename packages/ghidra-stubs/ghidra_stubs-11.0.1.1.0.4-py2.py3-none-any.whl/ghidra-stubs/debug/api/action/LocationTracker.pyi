import ghidra.debug.api.action
import ghidra.debug.api.tracemgr
import ghidra.framework.plugintool
import ghidra.program.util
import ghidra.trace.model
import ghidra.trace.model.stack
import ghidra.trace.util
import java.lang
import java.util.concurrent


class LocationTracker(object):








    def affectedByBytesChange(self, __a0: ghidra.trace.util.TraceAddressSpace, __a1: ghidra.trace.model.TraceAddressSnapRange, __a2: ghidra.debug.api.tracemgr.DebuggerCoordinates) -> bool: ...

    def affectedByStackChange(self, __a0: ghidra.trace.model.stack.TraceStack, __a1: ghidra.debug.api.tracemgr.DebuggerCoordinates) -> bool: ...

    def computeTraceAddress(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.debug.api.tracemgr.DebuggerCoordinates) -> java.util.concurrent.CompletableFuture: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultGoToInput(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.debug.api.tracemgr.DebuggerCoordinates, __a2: ghidra.program.util.ProgramLocation) -> ghidra.debug.api.action.GoToInput: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def shouldDisassemble(self) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

