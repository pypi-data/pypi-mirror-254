import ghidra.app.plugin.core.debug.gui.action
import ghidra.app.services
import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.trace.model
import ghidra.util.classfinder
import ghidra.util.task
import java.lang
import java.util
import javax.swing


class AutoMapSpec(ghidra.util.classfinder.ExtensionPoint, object):
    PRIVATE: ghidra.app.plugin.core.debug.gui.action.AutoMapSpec.Private = ghidra.app.plugin.core.debug.gui.action.AutoMapSpec$Private@207c8909




    class Private(object):








        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

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






    class AutoMapSpecConfigFieldCodec(object, ghidra.framework.plugintool.AutoConfigState.ConfigFieldCodec):




        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        @overload
        def read(self, __a0: ghidra.framework.options.SaveState, __a1: unicode, __a2: ghidra.app.plugin.core.debug.gui.action.AutoMapSpec) -> ghidra.app.plugin.core.debug.gui.action.AutoMapSpec: ...

        @overload
        def read(self, __a0: ghidra.framework.options.SaveState, __a1: unicode, __a2: object) -> object: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @overload
        def write(self, __a0: ghidra.framework.options.SaveState, __a1: unicode, __a2: ghidra.app.plugin.core.debug.gui.action.AutoMapSpec) -> None: ...

        @overload
        def write(self, __a0: ghidra.framework.options.SaveState, __a1: unicode, __a2: object) -> None: ...







    @staticmethod
    def allSpecs() -> java.util.Map: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fromConfigName(__a0: unicode) -> ghidra.app.plugin.core.debug.gui.action.AutoMapSpec: ...

    def getChangeTypes(self) -> java.util.Collection: ...

    def getClass(self) -> java.lang.Class: ...

    def getConfigName(self) -> unicode: ...

    def getMenuIcon(self) -> javax.swing.Icon: ...

    def getMenuName(self) -> unicode: ...

    def getTaskTitle(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def performMapping(self, __a0: ghidra.app.services.DebuggerStaticMappingService, __a1: ghidra.trace.model.Trace, __a2: ghidra.app.services.ProgramManager, __a3: ghidra.util.task.TaskMonitor) -> None: ...

    def runTask(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.trace.model.Trace) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def changeTypes(self) -> java.util.Collection: ...

    @property
    def configName(self) -> unicode: ...

    @property
    def menuIcon(self) -> javax.swing.Icon: ...

    @property
    def menuName(self) -> unicode: ...

    @property
    def taskTitle(self) -> unicode: ...