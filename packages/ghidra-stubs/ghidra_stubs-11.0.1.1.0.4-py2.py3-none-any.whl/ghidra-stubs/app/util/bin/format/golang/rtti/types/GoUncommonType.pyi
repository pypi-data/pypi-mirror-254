from typing import List
import ghidra.app.util.bin.format.golang.rtti
import ghidra.app.util.bin.format.golang.rtti.types
import java.lang


class GoUncommonType(object):
    """
    Structure found immediately after a GoType structure, if it has the uncommon flag
     set.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEndOfTypeInfo(self) -> long:
        """
        Returns the location of where this object, and any known associated optional
         structures ends.
        @return index location of end of this type object
        """
        ...

    def getMethods(self) -> List[ghidra.app.util.bin.format.golang.rtti.types.GoMethod]:
        """
        Returns a list of the methods defined by the type.
        @return list of the methods defined by the type
        @throws IOException if error reading data
        """
        ...

    def getMethodsSlice(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice:
        """
        Returns a slice containing the methods defined by the type.
        @return slice containing the methods defined by the type
        """
        ...

    def getPackagePathString(self) -> unicode:
        """
        Returns the package path of the type.
        @return package path of the type, as a string
        @throws IOException if error reading data
        """
        ...

    def getPkgPath(self) -> ghidra.app.util.bin.format.golang.rtti.GoName:
        """
        Returns the package path of the type.
        @return package path of the type
        @throws IOException if error reading data
        """
        ...

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
    def endOfTypeInfo(self) -> long: ...

    @property
    def methods(self) -> List[object]: ...

    @property
    def methodsSlice(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice: ...

    @property
    def packagePathString(self) -> unicode: ...

    @property
    def pkgPath(self) -> ghidra.app.util.bin.format.golang.rtti.GoName: ...