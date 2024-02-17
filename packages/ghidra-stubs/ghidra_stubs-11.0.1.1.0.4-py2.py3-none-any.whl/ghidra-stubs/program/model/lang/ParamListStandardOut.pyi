from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.lang.ParamList
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.xml
import java.lang
import java.util


class ParamListStandardOut(ghidra.program.model.lang.ParamListStandard):
    """
    A list of resources describing possible storage locations for a function's return value,
     and a strategy for selecting a storage location based on data-types in a function signature.
 
     Similar to the parent class, when assigning storage, the first entry that matches the data-type
     is chosen.  But if this instance fails to find a match (because the return value data-type is too
     big) the data-type is converted to a pointer and storage is assigned based on that pointer.
     Additionally, if configured, this instance will signal that a hidden input parameter is required
     to fully model where the large return value is stored.
 
     The resource list is checked to ensure entries are distinguishable.
    """





    def __init__(self): ...



    def assignAddress(self, dt: ghidra.program.model.data.DataType, proto: ghidra.program.model.lang.PrototypePieces, pos: int, dtManager: ghidra.program.model.data.DataTypeManager, status: List[int], res: ghidra.program.model.lang.ParameterPieces) -> int:
        """
        Fill in the Address and other details for the given parameter
 
         Attempt to apply a ModelRule first. If these do not succeed, use the fallback assignment algorithm.
        @param dt is the data-type assigned to the parameter
        @param proto is the description of the function prototype
        @param pos is the position of the parameter to assign (pos=-1 for output, pos >=0 for input)
        @param dtManager is the data-type manager for (possibly) transforming the parameter's data-type
        @param status is the consumed resource status array
        @param res is parameter description to be filled in
        @return the response code
        """
        ...

    def assignAddressFallback(self, resource: ghidra.program.model.lang.StorageClass, tp: ghidra.program.model.data.DataType, matchExact: bool, status: List[int], param: ghidra.program.model.lang.ParameterPieces) -> int:
        """
        Assign storage for given parameter class, using the fallback assignment algorithm
 
         Given a resource list, a data-type, and the status of previously allocated slots,
         select the storage location for the parameter.  The status array is
         indexed by group: a positive value indicates how many slots have been allocated
         from that group, and a -1 indicates the group/resource is fully consumed.
         If an Address can be assigned to the parameter, it and other details are passed back in the
         ParameterPieces object and the SUCCESS code is returned.  Otherwise, the FAIL code is returned.
        @param resource is the resource list to allocate from
        @param tp is the data-type of the parameter
        @param matchExact is false if TYPECLASS_GENERAL is considered a match for any storage class
        @param status is an array marking how many slots have already been consumed in a group
        @param param will hold the address and other details of the assigned parameter
        @return either SUCCESS or FAIL
        """
        ...

    def assignMap(self, __a0: ghidra.program.model.lang.PrototypePieces, __a1: ghidra.program.model.data.DataTypeManager, __a2: java.util.ArrayList, __a3: bool) -> None: ...

    def encode(self, encoder: ghidra.program.model.pcode.Encoder, isInput: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEntry(self, index: int) -> ghidra.program.model.lang.ParamEntry:
        """
        Within this list, get the ParamEntry at the given index
        @param index is the given index
        @return the selected ParamEntry
        """
        ...

    def getNumParamEntry(self) -> int:
        """
        @return the number of ParamEntry objets in this list
        """
        ...

    def getPotentialRegisterStorage(self, prog: ghidra.program.model.listing.Program) -> List[ghidra.program.model.listing.VariableStorage]: ...

    def getSpacebase(self) -> ghidra.program.model.address.AddressSpace: ...

    def getStackParameterAlignment(self) -> int: ...

    def getStackParameterOffset(self) -> long: ...

    def hashCode(self) -> int: ...

    def isEquivalent(self, obj: ghidra.program.model.lang.ParamList) -> bool: ...

    def isThisBeforeRetPointer(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def possibleParamWithSlot(self, loc: ghidra.program.model.address.Address, size: int, res: ghidra.program.model.lang.ParamList.WithSlotRec) -> bool: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, cspec: ghidra.program.model.lang.CompilerSpec) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

