from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.pcode.exec
import ghidra.program.model.pcode
import java.lang
import java.lang.reflect
import java.util


class PcodeUseropLibrary(object):
    """
    A "library" of p-code userops available to a p-code executor

 
     The library can provide definitions of p-code userops already declared by the executor's language
     as well as completely new userops accessible to Sleigh/p-code later compiled for the executor.
     The recommended way to implement a library is to extend AnnotatedPcodeUseropLibrary.
    """

    NIL: ghidra.pcode.exec.PcodeUseropLibrary = ghidra.pcode.exec.PcodeUseropLibrary$EmptyPcodeUseropLibrary@6b662a33




    class PcodeUseropDefinition(object):








        def equals(self, __a0: object) -> bool: ...

        def execute(self, __a0: ghidra.pcode.exec.PcodeExecutor, __a1: ghidra.pcode.exec.PcodeUseropLibrary, __a2: ghidra.program.model.pcode.Varnode, __a3: List[object]) -> None: ...

        def getClass(self) -> java.lang.Class: ...

        def getInputCount(self) -> int: ...

        def getName(self) -> unicode: ...

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

        @property
        def inputCount(self) -> int: ...

        @property
        def name(self) -> unicode: ...




    class EmptyPcodeUseropLibrary(object, ghidra.pcode.exec.PcodeUseropLibrary):
        NIL: ghidra.pcode.exec.PcodeUseropLibrary = ghidra.pcode.exec.PcodeUseropLibrary$EmptyPcodeUseropLibrary@6b662a33



        def __init__(self): ...



        def compose(self, __a0: ghidra.pcode.exec.PcodeUseropLibrary) -> ghidra.pcode.exec.PcodeUseropLibrary: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        @staticmethod
        def getOperandType(__a0: java.lang.Class) -> java.lang.reflect.Type: ...

        def getSymbols(self, __a0: ghidra.app.plugin.processors.sleigh.SleighLanguage) -> java.util.Map: ...

        def getUserops(self) -> java.util.Map: ...

        def hashCode(self) -> int: ...

        @staticmethod
        def nil() -> ghidra.pcode.exec.PcodeUseropLibrary: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @property
        def userops(self) -> java.util.Map: ...





    def compose(self, lib: ghidra.pcode.exec.PcodeUseropLibrary) -> ghidra.pcode.exec.PcodeUseropLibrary:
        """
        Compose this and the given library into a new library.
        @param lib the other library
        @return a new library having all userops defined between the two
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getOperandType(cls: java.lang.Class) -> java.lang.reflect.Type:
        """
        Get the type {@code T} for the given class
 
         <p>
         If the class does not implement {@link PcodeUseropLibrary}, this returns null. If it does,
         but no arguments are given (i.e., it implements the raw type), this return {@link Object}.
        @param cls the class
        @return the type, or null
        """
        ...

    def getSymbols(self, language: ghidra.app.plugin.processors.sleigh.SleighLanguage) -> java.util.Map:
        """
        Get named symbols defined by this library that are not already declared in the language
        @param language the language whose existing symbols to consider
        @return a map of new userop indices to extra userop symbols
        """
        ...

    def getUserops(self) -> java.util.Map:
        """
        Get all the userops defined in this library, keyed by (symbol) name.
        @return the map of names to defined userops
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def nil() -> ghidra.pcode.exec.PcodeUseropLibrary:
        """
        The empty userop library, cast to match parameter types.
        @param <T> the type required by the executor
        @return the empty userop library
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def userops(self) -> java.util.Map: ...