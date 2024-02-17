from typing import List
import ghidra
import java.lang


class BSimControlLaunchable(object, ghidra.GhidraLaunchable):
    AUTH_OPTION: unicode = u'--auth'
    CAFILE_OPTION: unicode = u'--cafile'
    CERT_OPTION: unicode = u'--cert'
    COMMAND_ADDUSER: unicode = u'adduser'
    COMMAND_CHANGEAUTH: unicode = u'changeauth'
    COMMAND_CHANGE_PRIVILEGE: unicode = u'changeprivilege'
    COMMAND_DROPUSER: unicode = u'dropuser'
    COMMAND_RESET_PASSWORD: unicode = u'resetpassword'
    COMMAND_START: unicode = u'start'
    COMMAND_STOP: unicode = u'stop'
    DN_OPTION: unicode = u'--dn'
    FORCE_OPTION: unicode = u'--force'
    NO_LOCAL_AUTH_OPTION: unicode = u'--noLocalAuth'
    PORT_OPTION: unicode = u'--port'
    USER_OPTION: unicode = u'--user'



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def launch(self, __a0: ghidra.GhidraApplicationLayout, __a1: List[unicode]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def run(self, __a0: List[unicode]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

