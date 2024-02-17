import docking.widgets.fieldpanel.support
import ghidra.app.plugin.core.terminal
import java.lang


class TerminalFinder(object):





    class TextTerminalFinder(ghidra.app.plugin.core.terminal.TerminalFinder):




        def __init__(self, __a0: ghidra.app.plugin.core.terminal.TerminalLayoutModel, __a1: docking.widgets.fieldpanel.support.FieldLocation, __a2: bool, __a3: unicode, __a4: java.util.Set): ...



        def equals(self, __a0: object) -> bool: ...

        def find(self) -> docking.widgets.fieldpanel.support.FieldRange: ...

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






    class RegexTerminalFinder(ghidra.app.plugin.core.terminal.TerminalFinder):




        def __init__(self, __a0: ghidra.app.plugin.core.terminal.TerminalLayoutModel, __a1: docking.widgets.fieldpanel.support.FieldLocation, __a2: bool, __a3: unicode, __a4: java.util.Set): ...



        def equals(self, __a0: object) -> bool: ...

        def find(self) -> docking.widgets.fieldpanel.support.FieldRange: ...

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







    def equals(self, __a0: object) -> bool: ...

    def find(self) -> docking.widgets.fieldpanel.support.FieldRange: ...

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

