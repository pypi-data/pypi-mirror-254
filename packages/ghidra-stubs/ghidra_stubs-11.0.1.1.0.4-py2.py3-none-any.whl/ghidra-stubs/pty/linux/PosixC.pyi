from typing import List
import com.sun.jna
import ghidra.pty.linux.PosixC.Termios
import java.lang


class PosixC(com.sun.jna.Library, object):
    """
    Interface for POSIX functions in libc
 
 
     The functions are not documented here. Instead see the POSIX manual pages.
    """

    BARE: ghidra.pty.linux.PosixC = Proxy interface to Native Library <null@140374673838480>
    INSTANCE: ghidra.pty.linux.PosixC = ghidra.pty.linux.PosixC$1@6ef36c2b
    OPTION_ALLOW_OBJECTS: unicode = u'allow-objects'
    OPTION_CALLING_CONVENTION: unicode = u'calling-convention'
    OPTION_CLASSLOADER: unicode = u'classloader'
    OPTION_FUNCTION_MAPPER: unicode = u'function-mapper'
    OPTION_INVOCATION_MAPPER: unicode = u'invocation-mapper'
    OPTION_OPEN_FLAGS: unicode = u'open-flags'
    OPTION_STRING_ENCODING: unicode = u'string-encoding'
    OPTION_STRUCTURE_ALIGNMENT: unicode = u'structure-alignment'
    OPTION_TYPE_MAPPER: unicode = u'type-mapper'




    class Winsize(com.sun.jna.Structure):
        TIOCSWINSZ: int = 21524
        ws_col: int
        ws_row: int
        ws_xpixel: int
        ws_ypixel: int



        def __init__(self): ...



        @overload
        def autoRead(self) -> None: ...

        @overload
        @staticmethod
        def autoRead(__a0: List[com.sun.jna.Structure]) -> None: ...

        @overload
        def autoWrite(self) -> None: ...

        @overload
        @staticmethod
        def autoWrite(__a0: List[com.sun.jna.Structure]) -> None: ...

        def clear(self) -> None: ...

        @overload
        @staticmethod
        def createFieldsOrder(__a0: unicode) -> List[object]: ...

        @overload
        @staticmethod
        def createFieldsOrder(__a0: List[unicode]) -> List[object]: ...

        @overload
        @staticmethod
        def createFieldsOrder(__a0: List[object], __a1: List[unicode]) -> List[object]: ...

        @overload
        @staticmethod
        def createFieldsOrder(__a0: List[object], __a1: List[object]) -> List[object]: ...

        @overload
        def dataEquals(self, __a0: com.sun.jna.Structure) -> bool: ...

        @overload
        def dataEquals(self, __a0: com.sun.jna.Structure, __a1: bool) -> bool: ...

        def equals(self, __a0: object) -> bool: ...

        def getAutoRead(self) -> bool: ...

        def getAutoWrite(self) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getPointer(self) -> com.sun.jna.Pointer: ...

        def hashCode(self) -> int: ...

        @overload
        @staticmethod
        def newInstance(__a0: java.lang.Class) -> com.sun.jna.Structure: ...

        @overload
        @staticmethod
        def newInstance(__a0: java.lang.Class, __a1: com.sun.jna.Pointer) -> com.sun.jna.Structure: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def read(self) -> None: ...

        def readField(self, __a0: unicode) -> object: ...

        def setAutoRead(self, __a0: bool) -> None: ...

        def setAutoSynch(self, __a0: bool) -> None: ...

        def setAutoWrite(self, __a0: bool) -> None: ...

        def size(self) -> int: ...

        @overload
        def toArray(self, __a0: int) -> List[com.sun.jna.Structure]: ...

        @overload
        def toArray(self, __a0: List[com.sun.jna.Structure]) -> List[com.sun.jna.Structure]: ...

        @overload
        def toString(self) -> unicode: ...

        @overload
        def toString(self, __a0: bool) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        def write(self) -> None: ...

        @overload
        def writeField(self, __a0: unicode) -> None: ...

        @overload
        def writeField(self, __a0: unicode, __a1: object) -> None: ...






    class Termios(com.sun.jna.Structure):
        ECHO: int = 8
        TCSANOW: int = 0
        c_cc: List[int]
        c_cflag: int
        c_iflag: int
        c_ispeed: int
        c_lflag: int
        c_line: int
        c_oflag: int
        c_ospeed: int



        def __init__(self): ...



        @overload
        def autoRead(self) -> None: ...

        @overload
        @staticmethod
        def autoRead(__a0: List[com.sun.jna.Structure]) -> None: ...

        @overload
        def autoWrite(self) -> None: ...

        @overload
        @staticmethod
        def autoWrite(__a0: List[com.sun.jna.Structure]) -> None: ...

        def clear(self) -> None: ...

        @overload
        @staticmethod
        def createFieldsOrder(__a0: unicode) -> List[object]: ...

        @overload
        @staticmethod
        def createFieldsOrder(__a0: List[unicode]) -> List[object]: ...

        @overload
        @staticmethod
        def createFieldsOrder(__a0: List[object], __a1: List[unicode]) -> List[object]: ...

        @overload
        @staticmethod
        def createFieldsOrder(__a0: List[object], __a1: List[object]) -> List[object]: ...

        @overload
        def dataEquals(self, __a0: com.sun.jna.Structure) -> bool: ...

        @overload
        def dataEquals(self, __a0: com.sun.jna.Structure, __a1: bool) -> bool: ...

        def equals(self, __a0: object) -> bool: ...

        def getAutoRead(self) -> bool: ...

        def getAutoWrite(self) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getPointer(self) -> com.sun.jna.Pointer: ...

        def hashCode(self) -> int: ...

        @overload
        @staticmethod
        def newInstance(__a0: java.lang.Class) -> com.sun.jna.Structure: ...

        @overload
        @staticmethod
        def newInstance(__a0: java.lang.Class, __a1: com.sun.jna.Pointer) -> com.sun.jna.Structure: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def read(self) -> None: ...

        def readField(self, __a0: unicode) -> object: ...

        def setAutoRead(self, __a0: bool) -> None: ...

        def setAutoSynch(self, __a0: bool) -> None: ...

        def setAutoWrite(self, __a0: bool) -> None: ...

        def size(self) -> int: ...

        @overload
        def toArray(self, __a0: int) -> List[com.sun.jna.Structure]: ...

        @overload
        def toArray(self, __a0: List[com.sun.jna.Structure]) -> List[com.sun.jna.Structure]: ...

        @overload
        def toString(self) -> unicode: ...

        @overload
        def toString(self, __a0: bool) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        def write(self) -> None: ...

        @overload
        def writeField(self, __a0: unicode) -> None: ...

        @overload
        def writeField(self, __a0: unicode, __a1: object) -> None: ...







    def close(self, fd: int) -> int: ...

    def dup2(self, oldfd: int, newfd: int) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def execv(self, path: unicode, argv: List[unicode]) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def ioctl(self, fd: int, cmd: int, args: List[com.sun.jna.Pointer]) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def open(self, path: unicode, mode: int, flags: int) -> int: ...

    def read(self, fd: int, buf: com.sun.jna.Pointer, len: int) -> int: ...

    def setsid(self) -> int: ...

    def strerror(self, errnum: int) -> unicode: ...

    def tcgetattr(self, fd: int, termios_p: ghidra.pty.linux.PosixC.Termios.ByReference) -> int: ...

    def tcsetattr(self, fd: int, optional_actions: int, termios_p: ghidra.pty.linux.PosixC.Termios.ByReference) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def write(self, fd: int, buf: com.sun.jna.Pointer, i: int) -> int: ...

