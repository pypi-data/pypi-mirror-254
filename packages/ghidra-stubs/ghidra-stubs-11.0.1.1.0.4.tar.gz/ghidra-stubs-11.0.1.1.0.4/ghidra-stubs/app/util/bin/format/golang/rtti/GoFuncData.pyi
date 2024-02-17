from typing import List
import ghidra.app.util.bin.format.golang.rtti
import ghidra.app.util.bin.format.golang.rtti.types.GoMethod
import ghidra.app.util.bin.format.golang.structmapping
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import java.lang
import java.util


class GoFuncData(object, ghidra.app.util.bin.format.golang.structmapping.StructureMarkup):
    """
    A structure that golang generates that contains metadata about a function.
    """





    def __init__(self): ...



    def additionalMarkup(self, session: ghidra.app.util.bin.format.golang.structmapping.MarkupSession) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def findMethodInfo(self) -> ghidra.app.util.bin.format.golang.rtti.types.GoMethod.GoMethodInfo:
        """
        Attempts to return a {@link GoMethodInfo} for this function, based on this
         function's inclusion in a golang interface as a method.
        @return {@link GoMethodInfo}
        """
        ...

    def findMethodSignature(self) -> ghidra.program.model.data.FunctionDefinition:
        """
        Attempts to return a {@link FunctionDefinition} for this function, based on this
         function's inclusion in a golang interface as a method.
        @return {@link FunctionDefinition}
        @throws IOException if error
        """
        ...

    def getBody(self) -> ghidra.program.model.address.AddressRange:
        """
        Returns the address range of this function's body, recovered by examining addresses in the
         function's pc-to-filename translation table, or if not present, a single address range
         that contains the function's entry point.
        @return {@link AddressRange} representing the function's known footprint
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns a descriptive string.
         <p>
         Referenced from the entry, entryoff field's markup annotation
        @return String description
        """
        ...

    def getExternalInstancesToMarkup(self) -> List[object]: ...

    def getFlags(self) -> java.util.Set:
        """
        Returns the func flags for this function.
        @return {@link GoFuncFlag}s
        """
        ...

    def getFuncAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address of this function.
        @return the address of this function
        """
        ...

    def getFuncDataValue(self, tableIndex: ghidra.app.util.bin.format.golang.rtti.GoFuncDataTable) -> long:
        """
        Returns a value associated with this function.
        @param tableIndex {@link GoFuncDataTable} enum
        @return requested value, or -1 if the requested table index is not present for this function
        @throws IOException if error reading lookup data
        """
        ...

    def getFuncIDEnum(self) -> ghidra.app.util.bin.format.golang.rtti.GoFuncID:
        """
        Returns the {@link GoFuncID} enum that categorizes this function
        @return the {@link GoFuncID} enum that categorizes this function
        """
        ...

    def getFunction(self) -> ghidra.program.model.listing.Function:
        """
        Returns the Ghidra function that corresponds to this go function.
        @return Ghidra {@link Function}, or null if there is no Ghidra function at the address
        """
        ...

    def getModuledata(self) -> ghidra.app.util.bin.format.golang.rtti.GoModuledata:
        """
        Returns a reference to the {@link GoModuledata} that contains this function.
        @return {@link GoModuledata} that contains this function
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this function.
        @return String name of this function
        """
        ...

    def getNameAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address of this function's name string.
         <p>
         Referenced from nameoff's markup annotation
        @return {@link Address}
        """
        ...

    def getPcDataValue(self, tableIndex: ghidra.app.util.bin.format.golang.rtti.GoPcDataTable, targetPC: long) -> int:
        """
        Returns a value from the specified pc->value lookup table, for a specific 
         address (that should be within the function's footprint).
        @param tableIndex {@link GoPcDataTable} enum
        @param targetPC address (inside the function) to determine the value of
        @return int value, will be specific to the {@link GoPcDataTable table} it comes from, or
         -1 if the requested table index is not present for this function
        @throws IOException if error reading lookup data
        """
        ...

    def getPcDataValues(self, tableIndex: ghidra.app.util.bin.format.golang.rtti.GoPcDataTable) -> List[int]:
        """
        Returns all values for the specified pc->value lookup table for the entire range of the
         function's footprint.
        @param tableIndex {@link GoPcDataTable} enum
        @return list of int values, will be specific to the {@link GoPcDataTable table} it comes 
         from, or an empty list if the requested table index is not present for this function
        @throws IOException if error reading lookup data
        """
        ...

    def getSourceFileInfo(self) -> ghidra.app.util.bin.format.golang.rtti.GoSourceFileInfo:
        """
        Returns information about the source file that this function was defined in.
        @return {@link GoSourceFileInfo}, or null if no source file info present
        @throws IOException if error reading lookup data
        """
        ...

    def getStructureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    def getStructureLabel(self) -> unicode: ...

    def getStructureName(self) -> unicode: ...

    def getStructureNamespace(self) -> unicode: ...

    def getSymbolName(self) -> ghidra.app.util.bin.format.golang.rtti.GoSymbolName:
        """
        Returns the name of this function, as a parsed symbol object.
        @return {@link GoSymbolName} containing this function's name
        """
        ...

    def hashCode(self) -> int: ...

    def isAsmFunction(self) -> bool:
        """
        Returns true if this function is an ASM function
        @return true if this function is an ASM function
        """
        ...

    def isInline(self) -> bool:
        """
        Returns true if this function is inline
        @return true if this function is inline
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def recoverFunctionSignature(self) -> unicode:
        """
        Attempts to build a 'function signature' string representing the known information about
         this function's arguments, using go's built-in stack trace metadata.
         <p>
         The information that can be recovered about arguments is limited to:
         <ul>
         	<li>the size of the argument
         	<li>general grouping (eg. grouping of arg values as a structure or array)
         </ul>
         Return value information is unknown and always represented as an "undefined" data type.
        @return pseduo-function signature string, such as "undefined foo( 8, 8 )" which would
         indicate the function had 2 8-byte arguments
        @throws IOException if error reading lookup data
        """
        ...

    def setEntry(self, entry: long) -> None:
        """
        Sets the absolute entry address.
         <p>
         Called via deserialization for entry fieldmapping annotation
        @param entry absolute value.
        """
        ...

    def setEntryoff(self, entryoff: long) -> None:
        """
        Sets the function's entry point via a relative offset value
         <p>
         Called via deserialization for entryoff fieldmapping annotation
        @param entryoff relative offset to function
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
    def asmFunction(self) -> bool: ...

    @property
    def body(self) -> ghidra.program.model.address.AddressRange: ...

    @property
    def description(self) -> unicode: ...

    @property
    def entry(self) -> None: ...  # No getter available.

    @entry.setter
    def entry(self, value: long) -> None: ...

    @property
    def entryoff(self) -> None: ...  # No getter available.

    @entryoff.setter
    def entryoff(self, value: long) -> None: ...

    @property
    def externalInstancesToMarkup(self) -> List[object]: ...

    @property
    def flags(self) -> java.util.Set: ...

    @property
    def funcAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def funcIDEnum(self) -> ghidra.app.util.bin.format.golang.rtti.GoFuncID: ...

    @property
    def function(self) -> ghidra.program.model.listing.Function: ...

    @property
    def inline(self) -> bool: ...

    @property
    def moduledata(self) -> ghidra.app.util.bin.format.golang.rtti.GoModuledata: ...

    @property
    def name(self) -> unicode: ...

    @property
    def nameAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def sourceFileInfo(self) -> ghidra.app.util.bin.format.golang.rtti.GoSourceFileInfo: ...

    @property
    def structureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    @property
    def structureLabel(self) -> unicode: ...

    @property
    def structureName(self) -> unicode: ...

    @property
    def structureNamespace(self) -> unicode: ...

    @property
    def symbolName(self) -> ghidra.app.util.bin.format.golang.rtti.GoSymbolName: ...