from typing import List
import generic.ULongSpan
import ghidra.generic.util.datastruct
import java.lang


class SemisparseByteArray(object):
    """
    A sparse byte array characterized by contiguous dense regions
 
 
     Notionally, the array is 2 to the power 64 bytes in size. Only the initialized values are
     actually stored. Uninitialized indices are assumed to have the value 0. Naturally, this
     implementation works best when the array is largely uninitialized. For efficient use, isolated
     initialized values should be avoided. Rather, an entire range should be initialized at the same
     time.
 
 
     On a number line, the initialized indices of a semisparse array might be depicted:
 
 
     -----   --------- - ------         ---
 
 
 
     In contrast, the same for a sparse array might be depicted:
 
 
     -    --  -  - -    ---     --     -         -
 
 
 
     This implementation is well-suited for memory caches where the memory is accessed by reading
     ranges instead of individual bytes. Because consecutive reads and writes tend to occur in a
     common locality, caches using a semisparse array may perform well.
 
 
     This implementation is also thread-safe. Any thread needing exclusive access for multiple reads
     and/or writes, e.g., to implement a compare-and-set operation, must apply additional
     synchronization.
    """

    BLOCK_SIZE: int = 4096



    def __init__(self): ...



    def clear(self) -> None:
        """
        Clear the array
 
         <p>
         All indices will be uninitialized after this call, just as it was immediately after
         construction
        """
        ...

    def contiguousAvailableAfter(self, loc: long) -> int:
        """
        Check how many contiguous bytes are available starting at the given address
        @param loc the starting offset
        @return the number of contiguous defined bytes following
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def fork(self) -> ghidra.generic.util.datastruct.SemisparseByteArray: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getData(self, loc: long, data: List[int]) -> None:
        """
        Copy a range of data from the semisparse array into the given byte array
        @see #getData(long, byte[], int, int)
        @param loc the index to begin copying data out
        @param data the array to copy data into
        """
        ...

    @overload
    def getData(self, loc: long, data: List[int], offset: int, length: int) -> None:
        """
        Copy a range of data from the semisparse array into a portion of the given byte array
 
         <p>
         Copies {@code length} bytes of data from the semisparse array starting at index {@code loc}
         into {@code data} starting at index {@code offset}. All initialized portions within the
         requested region are copied. The uninitialized portions may be treated as zeroes or not
         copied at all. Typically, the destination array has been initialized to zero by the caller,
         such that all uninitialized portions are zero. To avoid fetching uninitialized data, use
         {@link #contiguousAvailableAfter(long)} as an upper bound on the length.
        @param loc the index to begin copying data out
        @param data the array to copy data into
        @param offset the offset into the destination array
        @param length the length of data to read
        """
        ...

    def getInitialized(self, a: long, b: long) -> generic.ULongSpan.ULongSpanSet:
        """
        Enumerate the initialized ranges within the given range
 
         <p>
         The given range is interpreted as closed, i.e., [a, b].
        @param a the lower-bound, inclusive, of the range
        @param b the upper-bound, inclusive, of the range
        @return the set of initialized ranges
        """
        ...

    def getUninitialized(self, a: long, b: long) -> generic.ULongSpan.ULongSpanSet:
        """
        Enumerate the uninitialized ranges within the given range
 
         <p>
         The given range is interpreted as closed, i.e., [a, b].
        @param a the lower-bound, inclusive, of the range
        @param b the upper-bound, inclusive, of the range
        @return the set of uninitialized ranges
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def isInitialized(self, a: long) -> bool:
        """
        Check if an index is initialized
        @param a the index to check
        @return true if the index is initialized, false otherwise
        """
        ...

    @overload
    def isInitialized(self, a: long, b: long) -> bool:
        """
        Check if a range is completely initialized
 
         <p>
         The given range is interpreted as closed, i.e., [a, b].
        @param a the lower-bound, inclusive, of the range
        @param b the upper-bound, inclusive, of the range
        @return true if all indices in the range are initialized, false otherwise
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def putAll(self, from_: ghidra.generic.util.datastruct.SemisparseByteArray) -> None:
        """
        Copy the contents on another semisparse array into this one
        @param from the source array
        """
        ...

    @overload
    def putData(self, loc: long, data: List[int]) -> None:
        """
        Initialize or modify a range of the array by copying from a given array
        @see #putData(long, byte[], int, int)
        @param loc the index of the semisparse array to begin copying into
        @param data the data to copy
        """
        ...

    @overload
    def putData(self, loc: long, data: List[int], offset: int, length: int) -> None:
        """
        Initialize or modify a range of the array by copying a portion from a given array
        @param loc the index of the semisparse array to begin copying into
        @param data the source array to copy from
        @param offset the offset of the source array to begin copying from
        @param length the length of data to copy
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

