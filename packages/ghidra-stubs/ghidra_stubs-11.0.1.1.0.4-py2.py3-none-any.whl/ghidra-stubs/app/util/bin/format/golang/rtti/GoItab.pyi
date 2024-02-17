from typing import List
import ghidra.app.util.bin.format.golang.rtti
import ghidra.app.util.bin.format.golang.rtti.types
import ghidra.app.util.bin.format.golang.rtti.types.GoIMethod
import ghidra.app.util.bin.format.golang.structmapping
import ghidra.program.model.data
import java.lang


class GoItab(object, ghidra.app.util.bin.format.golang.structmapping.StructureMarkup):
    """
    Represents a mapping between a golang interface and a type that implements the methods of
     the interface.
    """





    def __init__(self): ...



    def additionalMarkup(self, session: ghidra.app.util.bin.format.golang.structmapping.MarkupSession) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExternalInstancesToMarkup(self) -> List[object]: ...

    def getFunSlice(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice:
        """
        Returns an artificial slice that contains the address of the functions that implement
         the interface methods.
        @return artificial slice that contains the address of the functions that implement
         the interface methods
        @throws IOException if error reading method info
        """
        ...

    def getFuncCount(self) -> long:
        """
        Return the number of methods implemented.
        @return number of methods implemented
        @throws IOException if error reading interface structure
        """
        ...

    def getInterfaceType(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoInterfaceType:
        """
        Returns the interface implemented by the specified type.
        @return interface implemented by the specified type
        @throws IOException if error reading ref'd interface structure
        """
        ...

    def getMethodInfoList(self) -> List[ghidra.app.util.bin.format.golang.rtti.types.GoIMethod.GoIMethodInfo]:
        """
        Returns list of {@link GoIMethodInfo} instances, that represent the methods implemented by
         the specified type / interface.
        @return list of {@link GoIMethodInfo} instances
        @throws IOException if error reading interface method list
        """
        ...

    def getSignatureFor(self, imethod: ghidra.app.util.bin.format.golang.rtti.types.GoIMethod) -> ghidra.program.model.data.FunctionDefinition:
        """
        Returns a {@link FunctionDefinition} for the specified method of this itab.
        @param imethod info about an interface method
        @return {@link FunctionDefinition} for the specified method of this itab
        @throws IOException if error reading required info
        """
        ...

    def getStructureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    def getStructureLabel(self) -> unicode: ...

    def getStructureName(self) -> unicode: ...

    def getStructureNamespace(self) -> unicode: ...

    def getType(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoType:
        """
        Returns the type that implements the specified interface.
        @return type that implements the specified interface
        @throws IOException if error reading the ref'd type structure
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
    def externalInstancesToMarkup(self) -> List[object]: ...

    @property
    def funSlice(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice: ...

    @property
    def funcCount(self) -> long: ...

    @property
    def interfaceType(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoInterfaceType: ...

    @property
    def methodInfoList(self) -> List[object]: ...

    @property
    def structureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    @property
    def structureLabel(self) -> unicode: ...

    @property
    def structureName(self) -> unicode: ...

    @property
    def structureNamespace(self) -> unicode: ...

    @property
    def type(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoType: ...