from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.BinaryReader
import ghidra.app.util.bin.format.golang.rtti
import ghidra.app.util.bin.format.golang.structmapping
import ghidra.program.model.address
import ghidra.program.model.data
import java.lang


class GoSlice(object, ghidra.app.util.bin.format.golang.structmapping.StructureMarkup):
    """
    A structure that represents a golang slice instance (similar to a java ArrayList).  Not to be
     confused with a GoSliceType, which is RTTI info about a slice type.
 
     An initialized static image of a slice found in a go binary will tend to have len==cap (full).
 
     Like java's type erasure for generics, a golang slice instance does not have type information 
     about the elements found in the array blob (nor the size of the blob).
 
    """





    @overload
    def __init__(self): ...

    @overload
    def __init__(self, array: long, len: long, cap: long, programContext: ghidra.app.util.bin.format.golang.rtti.GoRttiMapper):
        """
        Creates an artificial slice instance using the supplied values.
        @param array offset of the slice's data
        @param len number of initialized elements in the slice
        @param cap total number of elements in the data array
        @param programContext the go binary that contains the slice
        """
        ...



    def additionalMarkup(self, __a0: ghidra.app.util.bin.format.golang.structmapping.MarkupSession) -> None: ...

    def containsOffset(self, offset: long, sizeofElement: int) -> bool:
        """
        Returns true if this slice contains the specified offset.
        @param offset memory offset in question
        @param sizeofElement size of elements in this slice
        @return true if this slice contains the specified offset
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getArrayAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address of the array blob
        @return address of the array blob
        """
        ...

    def getArrayEnd(self, elementClass: java.lang.Class) -> long:
        """
        Returns the address of the end of the array.
        @param elementClass structure mapped class
        @return location of the end of the array blob
        """
        ...

    def getArrayOffset(self) -> long:
        """
        Returns address of the array blob.
        @return location of the array blob
        """
        ...

    def getCap(self) -> long:
        """
        Returns the number of elements allocated in the array blob. (capacity)
        @return number of allocated elements in the array blob
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getElementDataType(self) -> ghidra.program.model.data.DataType:
        """
        Returns the {@link DataType} of elements of this slice, as detected by the type information
         contained in the struct field that contains this slice.
         <p>
         Returns null if this slice instance was not nested (contained) in a structure.  If the
         slice data type wasn't a specialized slice data type (it was "runtime.slice" instead of
         "[]element"), void data type will be returned.
        @return data type of the elements of this slice, if possible, or null
        """
        ...

    def getElementOffset(self, elementSize: long, elementIndex: long) -> long:
        """
        Returns the offset of the specified element
        @param elementSize size of elements in this slice
        @param elementIndex index of desired element
        @return offset of element
        """
        ...

    def getElementReader(self, elementSize: int, elementIndex: int) -> ghidra.app.util.bin.BinaryReader:
        """
        Returns a {@link BinaryReader} positioned at the specified slice element.
        @param elementSize size of elements in this slice
        @param elementIndex index of desired element
        @return {@link BinaryReader} positioned at specified element
        """
        ...

    def getExternalInstancesToMarkup(self) -> List[object]: ...

    def getLen(self) -> long:
        """
        Returns the number of initialized elements
        @return number of initialized elements
        """
        ...

    def getStructureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    def getStructureLabel(self) -> unicode: ...

    def getStructureName(self) -> unicode: ...

    def getStructureNamespace(self) -> unicode: ...

    def getSubSlice(self, startElement: long, elementCount: long, elementSize: long) -> ghidra.app.util.bin.format.golang.rtti.GoSlice:
        """
        Return a artificial view of a portion of this slice's contents.
        @param startElement index of element that will be the new sub-slice's starting element
        @param elementCount number of elements to include in new sub-slice
        @param elementSize size of an individual element
        @return new {@link GoSlice} instance that is limited to a portion of this slice
        """
        ...

    def hashCode(self) -> int: ...

    def isFull(self) -> bool:
        """
        Returns true if this slice's element count is equal to the slice's capacity.  This is
         typically true for all slices that are static.
        @return boolean true if this slice's element count is equal to capacity
        """
        ...

    @overload
    def isValid(self) -> bool:
        """
        Returns true if this slice seems valid.
        @return boolean true if array blob is a valid memory location
        """
        ...

    @overload
    def isValid(self, elementSize: int) -> bool:
        """
        Returns true if this slice seems valid.
        @param elementSize size of elements in this slice
        @return boolean true if array blob is a valid memory location
        """
        ...

    @overload
    def markupArray(self, sliceName: unicode, namespaceName: unicode, elementType: ghidra.program.model.data.DataType, ptr: bool, session: ghidra.app.util.bin.format.golang.structmapping.MarkupSession) -> None:
        """
        Marks up the memory occupied by the array elements with a name and a Ghidra ArrayDataType.
        @param sliceName used to label the memory location
        @param namespaceName namespace the label symbol should be placed in
        @param elementType Ghidra datatype of the array elements, null ok if ptr == true
        @param ptr boolean flag, if true the element type is really a pointer to the supplied
         data type
        @param session state and methods to assist marking up the program
        @throws IOException if error
        """
        ...

    @overload
    def markupArray(self, sliceName: unicode, namespaceName: unicode, elementClazz: java.lang.Class, ptr: bool, session: ghidra.app.util.bin.format.golang.structmapping.MarkupSession) -> None:
        """
        Marks up the memory occupied by the array elements with a name and a Ghidra ArrayDataType,
         which has elements who's type is determined by the specified structure class.
        @param sliceName used to label the memory location
        @param namespaceName namespace the label symbol should be placed in
        @param elementClazz structure mapped class of the element of the array
        @param ptr boolean flag, if true the element type is really a pointer to the supplied
         data type
        @param session state and methods to assist marking up the program
        @throws IOException if error
        """
        ...

    def markupArrayElements(self, clazz: java.lang.Class, session: ghidra.app.util.bin.format.golang.structmapping.MarkupSession) -> List[object]:
        """
        Marks up each element of the array, useful when the elements are themselves structures.
        @param <T> element type
        @param clazz structure mapped class of element
        @param session state and methods to assist marking up the program
        @return list of element instances
        @throws IOException if error reading
        @throws CancelledException if cancelled
        """
        ...

    def markupElementReferences(self, __a0: int, __a1: List[object], __a2: ghidra.app.util.bin.format.golang.structmapping.MarkupSession) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def readList(self, readFunc: ghidra.app.util.bin.BinaryReader.ReaderFunction) -> List[object]:
        """
        Reads the contents of the slice, treating each element as an instance of an object that can
         be read using the supplied reading function.
        @param <T> struct mapped type of element
        @param readFunc function that will read an instance from a BinaryReader
        @return list of instances
        @throws IOException if error reading an element
        """
        ...

    @overload
    def readList(self, clazz: java.lang.Class) -> List[object]:
        """
        Reads the content of the slice, treating each element as an instance of the specified
         structure mapped class.
        @param <T> struct mapped type of element
        @param clazz element type
        @return list of instances
        @throws IOException if error reading an element
        """
        ...

    def readUIntElement(self, intSize: int, elementIndex: int) -> long:
        """
        Reads an unsigned int element from this slice.
        @param intSize size of ints
        @param elementIndex index of element
        @return unsigned int value
        @throws IOException if error reading element
        """
        ...

    def readUIntList(self, intSize: int) -> List[long]:
        """
        Treats this slice as a array of unsigned integers, of the specified intSize.
         <p>
        @param intSize size of integer
        @return array of longs, containing the (possibly smaller) integers contained in the slice
        @throws IOException if error reading
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
    def arrayAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def arrayOffset(self) -> long: ...

    @property
    def cap(self) -> long: ...

    @property
    def elementDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def externalInstancesToMarkup(self) -> List[object]: ...

    @property
    def full(self) -> bool: ...

    @property
    def len(self) -> long: ...

    @property
    def structureContext(self) -> ghidra.app.util.bin.format.golang.structmapping.StructureContext: ...

    @property
    def structureLabel(self) -> unicode: ...

    @property
    def structureName(self) -> unicode: ...

    @property
    def structureNamespace(self) -> unicode: ...

    @property
    def valid(self) -> bool: ...