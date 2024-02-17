from typing import List
import ghidra.app.plugin.core.terminal.vt
import java.awt
import java.lang
import java.util


class AnsiColorResolver(object):





    class WhichGround(java.lang.Enum):
        BACKGROUND: ghidra.app.plugin.core.terminal.vt.AnsiColorResolver.WhichGround = BACKGROUND
        FOREGROUND: ghidra.app.plugin.core.terminal.vt.AnsiColorResolver.WhichGround = FOREGROUND







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def describeConstable(self) -> java.util.Optional: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.plugin.core.terminal.vt.AnsiColorResolver.WhichGround: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.plugin.core.terminal.vt.AnsiColorResolver.WhichGround]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resolveColor(self, __a0: ghidra.app.plugin.core.terminal.vt.VtHandler.AnsiColor, __a1: ghidra.app.plugin.core.terminal.vt.AnsiColorResolver.WhichGround, __a2: ghidra.app.plugin.core.terminal.vt.VtHandler.Intensity, __a3: bool) -> java.awt.Color: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

