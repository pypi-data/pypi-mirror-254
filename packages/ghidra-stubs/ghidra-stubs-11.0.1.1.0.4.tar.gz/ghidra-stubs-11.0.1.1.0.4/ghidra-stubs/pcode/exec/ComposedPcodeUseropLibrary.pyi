import ghidra.app.plugin.processors.sleigh
import ghidra.pcode.exec
import java.lang
import java.lang.reflect
import java.util


class ComposedPcodeUseropLibrary(object, ghidra.pcode.exec.PcodeUseropLibrary):
    """
    A p-code userop library composed of other libraries
    """

    NIL: ghidra.pcode.exec.PcodeUseropLibrary = ghidra.pcode.exec.PcodeUseropLibrary$EmptyPcodeUseropLibrary@6b662a33



    def __init__(self, libraries: java.util.Collection):
        """
        Construct a composed userop library from the given libraries
 
         <p>
         This uses {@link #composeUserops(Collection)}, so its restrictions apply here, too.
        @param libraries the libraries
        """
        ...



    def compose(self, __a0: ghidra.pcode.exec.PcodeUseropLibrary) -> ghidra.pcode.exec.PcodeUseropLibrary: ...

    @staticmethod
    def composeUserops(libraries: java.util.Collection) -> java.util.Map:
        """
        Obtain a map representing the composition of userops from all the given libraries
 
         <p>
         Name collisions are not allowed. If any two libraries export the same symbol, even if the
         definitions happen to do the same thing, it is an error.
        @param <T> the type of values processed by the libraries
        @param libraries the libraries whose userops to collect
        @return the resulting map
        """
        ...

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