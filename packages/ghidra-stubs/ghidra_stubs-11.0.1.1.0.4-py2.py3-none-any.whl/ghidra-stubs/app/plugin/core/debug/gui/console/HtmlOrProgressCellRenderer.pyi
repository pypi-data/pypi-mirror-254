from typing import List
import ghidra.app.plugin.core.debug.gui.console
import ghidra.docking.settings
import ghidra.util.exception
import ghidra.util.table.column
import java.awt
import java.lang
import java.util
import javax.swing


class HtmlOrProgressCellRenderer(java.lang.Enum, ghidra.util.table.column.GColumnRenderer):
    INSTANCE: ghidra.app.plugin.core.debug.gui.console.HtmlOrProgressCellRenderer = INSTANCE







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def createWrapperTypeException(self) -> ghidra.util.exception.AssertException: ...

    def describeConstable(self) -> java.util.Optional: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumnConstraintFilterMode(self) -> ghidra.util.table.column.GColumnRenderer.ColumnConstraintFilterMode: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getFilterString(self, __a0: object, __a1: ghidra.docking.settings.Settings) -> unicode: ...

    def getTableCellRendererComponent(self, __a0: javax.swing.JTable, __a1: object, __a2: bool, __a3: bool, __a4: int, __a5: int) -> java.awt.Component: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.plugin.core.debug.gui.console.HtmlOrProgressCellRenderer: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.plugin.core.debug.gui.console.HtmlOrProgressCellRenderer]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

