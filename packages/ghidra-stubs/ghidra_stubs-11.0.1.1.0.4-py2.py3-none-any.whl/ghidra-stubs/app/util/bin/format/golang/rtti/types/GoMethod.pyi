from typing import List
import ghidra.app.util.bin.format.golang.rtti
import ghidra.app.util.bin.format.golang.rtti.types
import ghidra.app.util.bin.format.golang.rtti.types.GoMethod
import ghidra.app.util.bin.format.golang.structmapping
import ghidra.program.model.address
import ghidra.program.model.data
import java.lang


class GoMethod(object, ghidra.app.util.bin.format.golang.structmapping.StructureMarkup):
    """
    Structure that defines a method for a GoType, found in the type's GoUncommonType struct.
    """






    class GoMethodInfo(ghidra.app.util.bin.format.golang.rtti.MethodInfo):




        def __init__(self, __a0: ghidra.app.util.bin.format.golang.rtti.types.GoMethod, __a1: ghidra.app.util.bin.format.golang.rtti.types.GoType, __a2: ghidra.app.util.bin.format.golang.rtti.types.GoMethod, __a3: ghidra.program.model.address.Address): ...



        def equals(self, __a0: object) -> bool: ...

        def getAddress(self) -> ghidra.program.model.address.Address: ...

        def getClass(self) -> java.lang.Class: ...

        def getMethod(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoMethod: ...

        def getPartialSignature(self) -> ghidra.program.model.data.FunctionDefinition: ...

        def getSignature(self) -> ghidra.program.model.data.FunctionDefinition: ...

        def getType(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoType: ...

        def hashCode(self) -> int: ...

        def isIfn(self, __a0: ghidra.program.model.address.Address) -> bool: ...

        def isTfn(self, __a0: ghidra.program.model.address.Address) -> bool: ...

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
        def method(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoMethod: ...

        @property
        def partialSignature(self) -> ghidra.program.model.data.FunctionDefinition: ...

        @property
        def signature(self) -> ghidra.program.model.data.FunctionDefinition: ...

        @property
        def type(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoType: ...

    def __init__(self): ...



    def additionalMarkup(self, __a0: ghidra.app.util.bin.format.golang.structmapping.MarkupSession) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExternalInstancesToMarkup(self) -> List[object]: ...

    def getGoName(self) -> ghidra.app.util.bin.format.golang.rtti.GoName:
        """
        Returns the name of this method.
        @return name of this method as a raw GoName value
        @throws IOException if error reading
        """
        ...

    def getIfn(self) -> ghidra.program.model.address.Address:
        """
        Returns the address of the version of the function that is called via the interface.
        @return address of the version of the function that is called via the interface
        """
        ...

    def getMethodInfos(self, containingType: ghidra.app.util.bin.format.golang.rtti.types.GoType) -> List[ghidra.app.util.bin.format.golang.rtti.types.GoMethod.GoMethodInfo]:
        """
        Returns a list of {@link GoMethodInfo}s containing the ifn and tfn values (if present).
        @param containingType {@link GoType} that contains this method
        @return list of {@link GoMethodInfo} instances representing the ifn and tfn values if present
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this method.
        @return name of this method
        """
        ...

    def getStructureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    def getStructureLabel(self) -> unicode: ...

    def getStructureName(self) -> unicode: ...

    def getStructureNamespace(self) -> unicode: ...

    def getTfn(self) -> ghidra.program.model.address.Address:
        """
        Returns the address of the version of the function that is called normally.
        @return address of the version of the function that is called normally
        """
        ...

    def getType(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoType:
        """
        Return the {@link GoType} that defines the funcdef / func signature.
        @return {@link GoType} that defines the funcdef / func signature
        @throws IOException if error reading data
        """
        ...

    def hashCode(self) -> int: ...

    def isSignatureMissing(self) -> bool:
        """
        Returns true if the funcdef is missing for this method.
        @return true if the funcdef is missing for this method
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
    def externalInstancesToMarkup(self) -> List[object]: ...

    @property
    def goName(self) -> ghidra.app.util.bin.format.golang.rtti.GoName: ...

    @property
    def ifn(self) -> ghidra.program.model.address.Address: ...

    @property
    def name(self) -> unicode: ...

    @property
    def signatureMissing(self) -> bool: ...

    @property
    def structureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    @property
    def structureLabel(self) -> unicode: ...

    @property
    def structureName(self) -> unicode: ...

    @property
    def structureNamespace(self) -> unicode: ...

    @property
    def tfn(self) -> ghidra.program.model.address.Address: ...

    @property
    def type(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoType: ...