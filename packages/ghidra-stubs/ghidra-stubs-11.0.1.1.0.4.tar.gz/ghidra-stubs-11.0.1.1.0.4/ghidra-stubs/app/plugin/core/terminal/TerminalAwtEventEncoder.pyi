from typing import List
import ghidra.app.plugin.core.terminal.vt
import java.awt.event
import java.lang


class TerminalAwtEventEncoder(object):
    CODE_DELETE: List[int] = array('b', [27, 91, 51, 126])
    CODE_DOWN_APPLICATION: List[int] = array('b', [27, 79, 66])
    CODE_DOWN_NORMAL: List[int] = array('b', [27, 91, 66])
    CODE_END_APPLICATION: List[int] = array('b', [27, 79, 70])
    CODE_END_NORMAL: List[int] = array('b', [27, 91, 70])
    CODE_ENTER: List[int] = array('b', [13])
    CODE_F1: List[int] = array('b', [27, 91, 49, 80])
    CODE_F10: List[int] = array('b', [27, 91, 50, 49, 126])
    CODE_F11: List[int] = array('b', [27, 91, 50, 51, 126])
    CODE_F12: List[int] = array('b', [27, 91, 50, 52, 126])
    CODE_F13: List[int] = array('b', [27, 91, 50, 53, 126])
    CODE_F14: List[int] = array('b', [27, 91, 50, 54, 126])
    CODE_F15: List[int] = array('b', [27, 91, 50, 56, 126])
    CODE_F16: List[int] = array('b', [27, 91, 50, 57, 126])
    CODE_F17: List[int] = array('b', [27, 91, 51, 49, 126])
    CODE_F18: List[int] = array('b', [27, 91, 51, 50, 126])
    CODE_F19: List[int] = array('b', [27, 91, 51, 51, 126])
    CODE_F2: List[int] = array('b', [27, 91, 49, 81])
    CODE_F20: List[int] = array('b', [27, 91, 51, 52, 126])
    CODE_F3: List[int] = array('b', [27, 91, 49, 82])
    CODE_F4: List[int] = array('b', [27, 91, 49, 83])
    CODE_F5: List[int] = array('b', [27, 91, 49, 53, 126])
    CODE_F6: List[int] = array('b', [27, 91, 49, 55, 126])
    CODE_F7: List[int] = array('b', [27, 91, 49, 56, 126])
    CODE_F8: List[int] = array('b', [27, 91, 49, 57, 126])
    CODE_F9: List[int] = array('b', [27, 91, 50, 48, 126])
    CODE_FOCUS_GAINED: List[int] = array('b', [27, 91, 73])
    CODE_FOCUS_LOST: List[int] = array('b', [27, 91, 79])
    CODE_HOME_APPLICATION: List[int] = array('b', [27, 79, 72])
    CODE_HOME_NORMAL: List[int] = array('b', [27, 91, 72])
    CODE_INSERT: List[int] = array('b', [27, 91, 50, 126])
    CODE_LEFT_APPLICATION: List[int] = array('b', [27, 79, 68])
    CODE_LEFT_NORMAL: List[int] = array('b', [27, 91, 68])
    CODE_NONE: List[int] = array('b')
    CODE_NUMPAD5: List[int] = array('b', [27, 91, 69])
    CODE_PAGE_DOWN: List[int] = array('b', [27, 91, 54, 126])
    CODE_PAGE_UP: List[int] = array('b', [27, 91, 53, 126])
    CODE_RIGHT_APPLICATION: List[int] = array('b', [27, 79, 67])
    CODE_RIGHT_NORMAL: List[int] = array('b', [27, 91, 67])
    CODE_UP_APPLICATION: List[int] = array('b', [27, 79, 65])
    CODE_UP_NORMAL: List[int] = array('b', [27, 91, 65])
    ESC: int = 27



    @overload
    def __init__(self, __a0: unicode): ...

    @overload
    def __init__(self, __a0: java.nio.charset.Charset): ...



    def equals(self, __a0: object) -> bool: ...

    def focusGained(self) -> None: ...

    def focusLost(self) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def keyPressed(self, __a0: java.awt.event.KeyEvent, __a1: ghidra.app.plugin.core.terminal.vt.VtHandler.KeyMode, __a2: ghidra.app.plugin.core.terminal.vt.VtHandler.KeyMode) -> None: ...

    def keyTyped(self, __a0: java.awt.event.KeyEvent) -> None: ...

    def mousePressed(self, __a0: java.awt.event.MouseEvent, __a1: int, __a2: int) -> None: ...

    def mouseReleased(self, __a0: java.awt.event.MouseEvent, __a1: int, __a2: int) -> None: ...

    def mouseWheelMoved(self, __a0: java.awt.event.MouseWheelEvent, __a1: int, __a2: int) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def sendChar(self, __a0: int) -> None: ...

    def sendText(self, __a0: java.lang.CharSequence) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def vtseq(__a0: int) -> List[int]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

