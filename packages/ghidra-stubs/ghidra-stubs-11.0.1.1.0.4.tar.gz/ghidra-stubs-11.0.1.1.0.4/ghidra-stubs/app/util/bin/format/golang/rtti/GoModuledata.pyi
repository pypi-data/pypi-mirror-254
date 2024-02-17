from typing import Iterator
from typing import List
import ghidra.app.util.bin.format.golang.rtti
import ghidra.app.util.bin.format.golang.rtti.types
import ghidra.app.util.bin.format.golang.structmapping
import ghidra.program.model.address
import java.lang


class GoModuledata(object, ghidra.app.util.bin.format.golang.structmapping.StructureMarkup):
    """
    Represents a golang moduledata structure, which contains a lot of valuable bootstrapping
     data for RTTI and function data.
    """





    def __init__(self): ...



    def additionalMarkup(self, session: ghidra.app.util.bin.format.golang.structmapping.MarkupSession) -> None: ...

    def containsFuncDataInstance(self, offset: long) -> bool:
        """
        Returns true if this GoModuleData is the module data that contains the specified
         GoFuncData structure.
        @param offset offset of a GoFuncData structure
        @return true if this GoModuleData is the module data that contains the specified GoFuncData
         structure
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAllFunctionData(self) -> List[ghidra.app.util.bin.format.golang.rtti.GoFuncData]:
        """
        Returns a list of all functions contained in this module.
        @return list of all functions contained in this module
        @throws IOException if error reading data
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCutab(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice:
        """
        Returns the cutab slice.
        @return cutab slice
        """
        ...

    def getExternalInstancesToMarkup(self) -> List[object]: ...

    def getFilename(self, fileoff: long) -> unicode:
        """
        Returns the filename at the specified offset.
        @param fileoff offset in the filetab of the filename
        @return filename
        @throws IOException if error reading
        """
        ...

    def getFiletab(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice:
        """
        Returns the filetab slice.
        @return filetab slice
        """
        ...

    def getFuncDataInstance(self, offset: long) -> ghidra.app.util.bin.format.golang.rtti.GoFuncData:
        """
        Reads a {@link GoFuncData} structure from the pclntable.
        @param offset relative to the pclntable
        @return {@link GoFuncData}
        @throws IOException if error reading data
        """
        ...

    def getFuncnametab(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice:
        """
        Returns a slice that contains all the function names.
        @return slice that contains all the function names
        """
        ...

    def getFunctabEntriesSlice(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice:
        """
        Returns an artificial slice of the functab entries that are valid.
        @return artificial slice of the functab entries that are valid
        """
        ...

    def getGoBinary(self) -> ghidra.app.util.bin.format.golang.rtti.GoRttiMapper:
        """
        Returns a reference to the controlling {@link GoRttiMapper go binary} context.
        @return reference to the controlling {@link GoRttiMapper go binary} context
        """
        ...

    def getGofunc(self) -> long:
        """
        Return the offset of the gofunc location
        @return offset of the gofunc location
        """
        ...

    def getItabs(self) -> List[ghidra.app.util.bin.format.golang.rtti.GoItab]:
        """
        Returns a list of the GoItabs present in this module.
        @return list of the GoItabs present in this module
        @throws IOException if error reading data
        """
        ...

    def getPcHeader(self) -> ghidra.app.util.bin.format.golang.rtti.GoPcHeader: ...

    def getPctab(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice:
        """
        Returns the pctab slice.
        @return pctab slice
        """
        ...

    def getStructureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    def getStructureLabel(self) -> unicode: ...

    def getStructureName(self) -> unicode: ...

    def getStructureNamespace(self) -> unicode: ...

    def getText(self) -> ghidra.program.model.address.Address:
        """
        Returns the address of the beginning of the text section.
        @return address of the beginning of the text section
        """
        ...

    def getTypeList(self) -> List[ghidra.program.model.address.Address]:
        """
        Returns a list of locations of the types contained in this module.
        @return list of addresses of GoType structures
        @throws IOException if error reading data
        """
        ...

    def getTypesEndOffset(self) -> long:
        """
        Returns the ending offset of type info
        @return ending offset of type info
        """
        ...

    def getTypesOffset(self) -> long:
        """
        Returns the starting offset of type info
        @return starting offset of type info
        """
        ...

    def hashCode(self) -> int: ...

    def isValid(self) -> bool:
        """
        Returns true if this module data structure contains sane values.
        @return true if this module data structure contains sane values
        """
        ...

    def iterateTypes(self) -> Iterator[ghidra.app.util.bin.format.golang.rtti.types.GoType]:
        """
        Returns an iterator that walks all the types contained in this module
        @return iterator that walks all the types contained in this module
        @throws IOException if error reading data
        """
        ...

    def matchesPclntab(self, pclntab: ghidra.app.util.bin.format.golang.rtti.GoPcHeader) -> bool:
        """
        Compares the data in this structure to fields in a GoPcHeader and returns true if they
         match.
        @param pclntab GoPcHeader instance
        @return boolean true if match, false if no match
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
    def allFunctionData(self) -> List[object]: ...

    @property
    def cutab(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice: ...

    @property
    def externalInstancesToMarkup(self) -> List[object]: ...

    @property
    def filetab(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice: ...

    @property
    def funcnametab(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice: ...

    @property
    def functabEntriesSlice(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice: ...

    @property
    def goBinary(self) -> ghidra.app.util.bin.format.golang.rtti.GoRttiMapper: ...

    @property
    def gofunc(self) -> long: ...

    @property
    def itabs(self) -> List[object]: ...

    @property
    def pcHeader(self) -> ghidra.app.util.bin.format.golang.rtti.GoPcHeader: ...

    @property
    def pctab(self) -> ghidra.app.util.bin.format.golang.rtti.GoSlice: ...

    @property
    def structureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    @property
    def structureLabel(self) -> unicode: ...

    @property
    def structureName(self) -> unicode: ...

    @property
    def structureNamespace(self) -> unicode: ...

    @property
    def text(self) -> ghidra.program.model.address.Address: ...

    @property
    def typeList(self) -> List[object]: ...

    @property
    def typesEndOffset(self) -> long: ...

    @property
    def typesOffset(self) -> long: ...

    @property
    def valid(self) -> bool: ...