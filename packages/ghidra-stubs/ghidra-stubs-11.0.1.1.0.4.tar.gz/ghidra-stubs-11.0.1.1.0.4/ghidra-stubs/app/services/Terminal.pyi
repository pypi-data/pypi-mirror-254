from typing import List
import ghidra.app.plugin.core.terminal
import java.lang
import java.nio


class Terminal(java.lang.AutoCloseable, object):
    """
    A handle to a terminal window in the UI.
    """









    def addTerminalListener(self, listener: ghidra.app.plugin.core.terminal.TerminalListener) -> None:
        """
        Add a listener for terminal events
        @param listener the listener
        """
        ...

    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumns(self) -> int:
        """
        Get the maximum number of characters in each row
        @return the column count
        """
        ...

    def getCursorColumn(self) -> int:
        """
        Get the cursor's current column
        @return the column, 0 up, left to right
        """
        ...

    def getCursorRow(self) -> int:
        """
        Get the cursor's current line
 
         <p>
         Lines are indexed 0 up where the top line of the display is 0. The cursor can never be in the
         scroll-back buffer.
        @return the line, 0 up, top to bottom
        """
        ...

    def getDisplayText(self) -> unicode:
        """
        Get the text in the terminal, excluding the scroll-back buffer
        @return the display text
        """
        ...

    def getFullText(self) -> unicode:
        """
        Get all the text in the terminal, including the scroll-back buffer
        @return the full text
        """
        ...

    def getLineText(self, line: int) -> unicode:
        """
        Get the given line's text
 
         <p>
         The line at the top of the display has index 0. Lines in the scroll-back buffer have negative
         indices.
        @param line the index, 0 up
        @return the text in the line
        """
        ...

    def getRangeText(self, startCol: int, startLine: int, endCol: int, endLine: int) -> unicode:
        """
        Get the text in the given range
 
         <p>
         The line at the top of the display has index 0. Lines in the scroll-back buffer have negative
         indices.
        @param startCol the first column to include in the starting line
        @param startLine the first line to include
        @param endCol the first column to <em>exclude</em> in the ending line
        @param endLine the last line to include
        @return the text in the given range
        """
        ...

    def getRows(self) -> int:
        """
        Get the maximum number of rows in the display (not counting scroll-back)
        @return the row count
        """
        ...

    def getScrollBackRows(self) -> int:
        """
        Get the number of lines in the scroll-back buffer
        @return the size of the buffer in lines
        """
        ...

    def getSubTitle(self) -> unicode:
        """
        Get the pane's current sub title
        @return the sub title
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def injectDisplayOutput(self, arr: List[int]) -> None:
        """
        @see #injectDisplayOutput(ByteBuffer)
        """
        ...

    @overload
    def injectDisplayOutput(self, bb: java.nio.ByteBuffer) -> None:
        """
        Process the given buffer as if it were output by the terminal's application.
 
         <p>
         <b>Warning:</b> While implementations may synchronize to ensure the additional buffer is not
         processed at the same time as actual application input, there may not be any effort to ensure
         that the buffer is not injected in the middle of an escape sequence. Even if the injection is
         outside an escape sequence, this may still lead to unexpected behavior, since the injected
         output may be affected by or otherwise interfere with the application's control of the
         terminal's state. Generally, this should only be used for testing, or other cases when the
         caller knows it has exclusive control of the terminal.
        @param bb the buffer of bytes to inject
        """
        ...

    def isTerminated(self) -> bool:
        """
        Check whether the terminal is terminated or active
        @return true for terminated, false for active
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeTerminalListener(self, listener: ghidra.app.plugin.core.terminal.TerminalListener) -> None:
        """
        Remove a listener for terminal events
        @param listener the listener
        """
        ...

    def setDynamicSize(self) -> None:
        """
        Fit the terminal's dimensions to the containing window.
        """
        ...

    @overload
    def setFixedSize(self, cols: int, rows: int) -> None:
        """
        Set the terminal size to the given dimensions, and do <em>not</em> resize it to the window.
        @param cols the number of columns
        @param rows the number of rows
        """
        ...

    @overload
    def setFixedSize(self, cols: int, rows: int) -> None:
        """
        Set the terminal size to the given dimensions, and do <em>not</em> resize it to the window.
        @param cols the number of columns
        @param rows the number of rows
        """
        ...

    def setMaxScrollBackRows(self, rows: int) -> None:
        """
        Set the maximum size of the scroll-back buffer in lines
 
         <p>
         This only affects the primary buffer. The alternate buffer has no scroll-back.
        """
        ...

    def setSubTitle(self, title: unicode) -> None:
        """
        Set the pane's sub title
 
         <p>
         The application may also set this sub title using an escape sequence.
        @param title the new sub title
        """
        ...

    def setTerminateAction(self, action: java.lang.Runnable) -> None:
        """
        Allow the user to terminate the session forcefully
        @param action the action to terminate the session, or null to remove the action
        """
        ...

    def terminated(self) -> None:
        """
        Notify the terminal that its session has terminated
 
         <p>
         The title and sub title are adjust and all listeners are removed. If/when the terminal is
         closed, it is permanently removed from the tool.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def columns(self) -> int: ...

    @property
    def cursorColumn(self) -> int: ...

    @property
    def cursorRow(self) -> int: ...

    @property
    def displayText(self) -> unicode: ...

    @property
    def fullText(self) -> unicode: ...

    @property
    def maxScrollBackRows(self) -> None: ...  # No getter available.

    @maxScrollBackRows.setter
    def maxScrollBackRows(self, value: int) -> None: ...

    @property
    def rows(self) -> int: ...

    @property
    def scrollBackRows(self) -> int: ...

    @property
    def subTitle(self) -> unicode: ...

    @subTitle.setter
    def subTitle(self, value: unicode) -> None: ...

    @property
    def terminateAction(self) -> None: ...  # No getter available.

    @terminateAction.setter
    def terminateAction(self, value: java.lang.Runnable) -> None: ...