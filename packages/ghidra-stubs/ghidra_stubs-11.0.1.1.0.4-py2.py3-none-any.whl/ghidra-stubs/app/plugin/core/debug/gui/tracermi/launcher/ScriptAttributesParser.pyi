from typing import List
import ghidra.app.plugin.core.debug.gui.tracermi.launcher
import ghidra.util
import java.io
import java.lang
import java.net
import java.util
import javax.swing


class ScriptAttributesParser(object):
    AT_ARG: unicode = u'@arg'
    AT_ARGS: unicode = u'@args'
    AT_DESC: unicode = u'@desc'
    AT_ENUM: unicode = u'@enum'
    AT_ENV: unicode = u'@env'
    AT_HELP: unicode = u'@help'
    AT_ICON: unicode = u'@icon'
    AT_MENU_GROUP: unicode = u'@menu-group'
    AT_MENU_ORDER: unicode = u'@menu-order'
    AT_MENU_PATH: unicode = u'@menu-path'
    AT_TITLE: unicode = u'@title'
    AT_TTY: unicode = u'@tty'
    KEY_ARGS: unicode = u'args'
    MSGPAT_INVALID_ARGS_SYNTAX: unicode = u'%s: Invalid %s syntax. Use "Display" "Tool Tip"'
    MSGPAT_INVALID_ARG_SYNTAX: unicode = u'%s: Invalid %s syntax. Use :type "Display" "Tool Tip"'
    MSGPAT_INVALID_ENUM_SYNTAX: unicode = u'%s: Invalid %s syntax. Use NAME:type Choice1 [ChoiceN...]'
    MSGPAT_INVALID_ENV_SYNTAX: unicode = u'%s: Invalid %s syntax. Use NAME:type=default "Display" "Tool Tip"'
    MSGPAT_INVALID_HELP_SYNTAX: unicode = u'%s: Invalid %s syntax. Use Topic#anchor'
    PREFIX_ARG: unicode = u'arg:'
    PREFIX_ENV: unicode = u'env:'




    class ScriptAttributes(java.lang.Record):




        def __init__(self, __a0: unicode, __a1: unicode, __a2: List[object], __a3: unicode, __a4: unicode, __a5: javax.swing.Icon, __a6: ghidra.util.HelpLocation, __a7: java.util.Map, __a8: java.util.Collection): ...



        def description(self) -> unicode: ...

        def equals(self, __a0: object) -> bool: ...

        def extraTtys(self) -> java.util.Collection: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def helpLocation(self) -> ghidra.util.HelpLocation: ...

        def icon(self) -> javax.swing.Icon: ...

        def menuGroup(self) -> unicode: ...

        def menuOrder(self) -> unicode: ...

        def menuPath(self) -> List[object]: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def parameters(self) -> java.util.Map: ...

        def title(self) -> unicode: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parseComment(self, __a0: ghidra.app.plugin.core.debug.gui.tracermi.launcher.ScriptAttributesParser.Location, __a1: unicode) -> None: ...

    def parseFile(self, __a0: java.io.File) -> ghidra.app.plugin.core.debug.gui.tracermi.launcher.ScriptAttributesParser.ScriptAttributes: ...

    @staticmethod
    def processArguments(__a0: List[object], __a1: java.util.Map, __a2: java.io.File, __a3: java.util.Map, __a4: java.util.Map, __a5: java.net.SocketAddress) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

