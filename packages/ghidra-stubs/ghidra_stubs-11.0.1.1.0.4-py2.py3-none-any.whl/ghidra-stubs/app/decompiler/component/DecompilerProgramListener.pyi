import ghidra.framework.model
import java.lang


class DecompilerProgramListener(object, ghidra.framework.model.DomainObjectListener):
    """
    Listener of Program events for decompiler panels. Program events are buffered using 
     a SwingUpdateManager before triggering a new decompile process.
    """





    @overload
    def __init__(self, controller: ghidra.app.decompiler.component.DecompilerController, updater: ghidra.util.task.SwingUpdateManager):
        """
        Construct a listener with a SwingUpdateManger that should be kicked for every
         program change.
        @param controller the DecompilerController
        @param updater A SwingUpdateManger to be kicked as program events are received which will
         eventually trigger a decompile refresh.
        """
        ...

    @overload
    def __init__(self, controller: ghidra.app.decompiler.component.DecompilerController, callback: java.lang.Runnable):
        """
        Construct a listener with a callback to be called when a decompile should occur. Program
         events are buffered using SwingUpdateManager before the callback is called.
        @param controller the DecompilerController
        @param callback the callback for when the decompile should be refreshed.
        """
        ...



    def dispose(self) -> None: ...

    def domainObjectChanged(self, ev: ghidra.framework.model.DomainObjectChangedEvent) -> None: ...

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

