from typing import List
import ghidra.app.plugin.core.analysis
import ghidra.program.model.listing
import java.lang
import java.util


class TransientProgramProperties(object):





    class SCOPE(java.lang.Enum):
        ANALYSIS_SESSION: ghidra.app.plugin.core.analysis.TransientProgramProperties.SCOPE = ANALYSIS_SESSION
        PROGRAM: ghidra.app.plugin.core.analysis.TransientProgramProperties.SCOPE = PROGRAM







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
        def valueOf(__a0: unicode) -> ghidra.app.plugin.core.analysis.TransientProgramProperties.SCOPE: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.plugin.core.analysis.TransientProgramProperties.SCOPE]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class PropertyValueSupplier(object):








        def equals(self, __a0: object) -> bool: ...

        def get(self) -> object: ...

        def getClass(self) -> java.lang.Class: ...

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



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getProperty(__a0: ghidra.program.model.listing.Program, __a1: object, __a2: ghidra.app.plugin.core.analysis.TransientProgramProperties.SCOPE, __a3: java.lang.Class, __a4: ghidra.app.plugin.core.analysis.TransientProgramProperties.PropertyValueSupplier) -> object: ...

    @staticmethod
    def hasProperty(__a0: ghidra.program.model.listing.Program, __a1: object) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removeProgramProperties(__a0: ghidra.program.model.listing.Program) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

