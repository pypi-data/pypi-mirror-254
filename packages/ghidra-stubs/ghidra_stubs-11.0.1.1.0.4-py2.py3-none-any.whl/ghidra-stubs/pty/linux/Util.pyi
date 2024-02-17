import com.sun.jna
import com.sun.jna.ptr
import java.lang


class Util(com.sun.jna.Library, object):
    """
    The interface for linking to  via jna
 
 
     See the UNIX manual pages
    """

    BARE: ghidra.pty.linux.Util = Proxy interface to Native Library <libutil.so@140372627862144>
    INSTANCE: ghidra.pty.linux.Util = ghidra.pty.linux.Util$1@1b46355f
    OPTION_ALLOW_OBJECTS: unicode = u'allow-objects'
    OPTION_CALLING_CONVENTION: unicode = u'calling-convention'
    OPTION_CLASSLOADER: unicode = u'classloader'
    OPTION_FUNCTION_MAPPER: unicode = u'function-mapper'
    OPTION_INVOCATION_MAPPER: unicode = u'invocation-mapper'
    OPTION_OPEN_FLAGS: unicode = u'open-flags'
    OPTION_STRING_ENCODING: unicode = u'string-encoding'
    OPTION_STRUCTURE_ALIGNMENT: unicode = u'structure-alignment'
    OPTION_TYPE_MAPPER: unicode = u'type-mapper'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openpty(self, amaster: com.sun.jna.ptr.IntByReference, aslave: com.sun.jna.ptr.IntByReference, name: com.sun.jna.Pointer, termp: com.sun.jna.Pointer, winp: com.sun.jna.Pointer) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

