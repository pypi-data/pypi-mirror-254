from typing import List
import ghidra.app.util.bin.format.golang.rtti
import ghidra.app.util.bin.format.golang.rtti.types
import ghidra.app.util.bin.format.golang.rtti.types.GoMethod
import ghidra.app.util.bin.format.golang.structmapping
import ghidra.program.model.data
import java.lang
import java.util


class GoPointerType(ghidra.app.util.bin.format.golang.rtti.types.GoType):
    """
    GoType structure that defines a pointer.
    """





    def __init__(self): ...



    def additionalMarkup(self, session: ghidra.app.util.bin.format.golang.structmapping.MarkupSession) -> None: ...

    def discoverGoTypes(self, discoveredTypes: java.util.Set) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDebugId(self) -> unicode: ...

    def getElement(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoType:
        """
        Returns a reference to the element's type.
        @return reference to the element's type
        @throws IOException if error reading data
        """
        ...

    def getEndOfTypeInfo(self) -> long:
        """
        Returns the location of where this type object, and any known associated optional
         structures ends.
        @return index location of end of this type object
        @throws IOException if error reading
        """
        ...

    def getExternalInstancesToMarkup(self) -> List[object]: ...

    def getMethodInfoList(self) -> List[ghidra.app.util.bin.format.golang.rtti.types.GoMethod.GoMethodInfo]:
        """
        Returns a list of all methods defined on this type.  Methods that specify both a
         "tfn" address as well as a "ifn" address will be represented twice.
        @return list of MethodInfo's
        @throws IOException if error reading
        """
        ...

    def getMethodSignature(self, method: ghidra.app.util.bin.format.golang.rtti.types.GoMethod, allowPartial: bool) -> ghidra.program.model.data.FunctionDefinition:
        """
        Return a funcdef signature for a method that is attached to this type.
        @param method {@link GoMethod}
        @param allowPartial boolean flag, if true, allow returning a partially defined signature
         when the method's funcdef type is not specified
        @return {@link FunctionDefinition} (that contains a receiver parameter), or null if
         the method's funcdef type was not specified and allowPartial was not true
        @throws IOException if error reading type info
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this type.
        @return name of this type
        """
        ...

    def getNameWithPackageString(self) -> unicode: ...

    def getPackagePathString(self) -> unicode:
        """
        Returns the package path of this type.
        @return package path of this type
        """
        ...

    @staticmethod
    def getSpecializedTypeClass(programContext: ghidra.app.util.bin.format.golang.rtti.GoRttiMapper, offset: long) -> java.lang.Class:
        """
        Returns the specific GoType derived class that will handle the go type located at the
         specified offset.
        @param programContext program-level mapper context
        @param offset absolute location of go type struct
        @return GoType class that will best handle the type struct
        @throws IOException if error reading
        """
        ...

    def getStructureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    def getStructureLabel(self) -> unicode: ...

    def getStructureName(self) -> unicode: ...

    def getStructureNamespace(self) -> unicode: ...

    def getTypeOffset(self) -> long:
        """
        Returns the starting offset of this type, used as an identifier.
        @return starting offset of this type
        """
        ...

    def getUncommonType(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoUncommonType: ...

    def getUniqueTypename(self) -> unicode:
        """
        Returns the name of this type, after being uniqified against all other types defined in the
         program.
         <p>
         See {@link GoRttiMapper#getUniqueGoTypename(GoType)}.
        @return name of this type
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def recoverDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def element(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoType: ...

    @property
    def structureNamespace(self) -> unicode: ...