import ghidra.app.util.bin.format.golang.rtti
import ghidra.app.util.bin.format.golang.rtti.types
import java.lang
import java.util


class GoBaseType(object):
    """
    Represents the fundamental golang rtti type information.
 
     The in-memory instance will typically be part of a specialized type structure, depending
     on the 'kind' of this type.
 
     Additionally, there can be an GoUncommonType structure immediately after this type, if
     the uncommon bit is set in tflag.
 
 
     struct specialized_type { basetype_struct; (various_fields)* } struct uncommon; 
 
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFlags(self) -> java.util.Set:
        """
        Returns the {@link GoTypeFlag}s assigned to this type definition.
        @return {@link GoTypeFlag}s assigned to this type definition
        """
        ...

    def getGoName(self) -> ghidra.app.util.bin.format.golang.rtti.GoName:
        """
        Returns the name of this type.
        @return name of this type, as a {@link GoName}
        @throws IOException if error reading data
        """
        ...

    def getKind(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoKind:
        """
        Returns the {@link GoKind} enum assigned to this type definition.
        @return {@link GoKind} enum assigned to this type definition
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this type.
        @return String name of this type
        """
        ...

    def getPtrToThis(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoType:
        """
        Returns a reference to the {@link GoType} that represents a pointer to this type.
        @return reference to the {@link GoType} that represents a pointer to this type
        @throws IOException if error reading
        """
        ...

    def getSize(self) -> long:
        """
        Returns the size of the type being defined by this structure.
        @return size of the type being defined
        """
        ...

    def getTflag(self) -> int:
        """
        Returns the raw flag value.
        @return raw flag value
        """
        ...

    def hasUncommonType(self) -> bool:
        """
        Returns true if this type definition's flags indicate there is a following GoUncommon
         structure.
        @return true if this type definition's flags indicate there is a following GoUncommon struct
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
    def flags(self) -> java.util.Set: ...

    @property
    def goName(self) -> ghidra.app.util.bin.format.golang.rtti.GoName: ...

    @property
    def kind(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoKind: ...

    @property
    def name(self) -> unicode: ...

    @property
    def ptrToThis(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoType: ...

    @property
    def size(self) -> long: ...

    @property
    def tflag(self) -> int: ...