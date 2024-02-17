import java.awt
import java.lang
import java.util


class CharacterScriptUtils(object):
    ANY_SCRIPT_ALIAS: java.lang.Character.UnicodeScript = UNKNOWN
    IGNORED_SCRIPTS: List[object] = [INHERITED, UNKNOWN]



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDisplayableScriptExamples(__a0: java.awt.Font, __a1: int) -> java.util.Map: ...

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

