from typing import List
import ghidra.app.plugin.core.debug.disassemble
import java.lang
import java.lang.annotation


class DisassemblyInjectInfo(java.lang.annotation.Annotation, object):





    class CompilerInfo(java.lang.annotation.Annotation, object):








        def annotationType(self) -> java.lang.Class: ...

        def compilerID(self) -> unicode: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def langID(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    def annotationType(self) -> java.lang.Class: ...

    def compilers(self) -> List[ghidra.app.plugin.core.debug.disassemble.DisassemblyInjectInfo.CompilerInfo]: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def priority(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

