import ghidra.app.util.bin.format.golang.rtti
import ghidra.app.util.bin.format.golang.rtti.types
import java.lang


class GoStructField(object):
    """
    Structure used to define a field in a GoStructType.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getGoName(self) -> ghidra.app.util.bin.format.golang.rtti.GoName:
        """
        Returns the name of this field.
        @return name of this field as it's raw GoName value
        @throws IOException if error reading
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this field.
        @return name of this field
        """
        ...

    def getOffset(self) -> long:
        """
        Returns the offset of this field.
        @return offset of this field
        """
        ...

    def getType(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoType:
        """
        Returns the type of this field.
        @return type of this field
        @throws IOException if error reading
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setOffsetAnon(self, offsetAnon: long) -> None:
        """
        Setter called by offsetAnon field's serialization, referred by fieldmapping annotation.
        @param offsetAnon value
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def goName(self) -> ghidra.app.util.bin.format.golang.rtti.GoName: ...

    @property
    def name(self) -> unicode: ...

    @property
    def offset(self) -> long: ...

    @property
    def offsetAnon(self) -> None: ...  # No getter available.

    @offsetAnon.setter
    def offsetAnon(self, value: long) -> None: ...

    @property
    def type(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoType: ...