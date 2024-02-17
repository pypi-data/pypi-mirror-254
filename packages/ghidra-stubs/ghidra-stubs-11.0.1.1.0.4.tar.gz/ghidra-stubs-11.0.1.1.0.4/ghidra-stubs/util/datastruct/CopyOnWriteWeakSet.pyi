from typing import Iterator
from typing import List
import ghidra.util.datastruct
import java.lang
import java.util
import java.util.function
import java.util.stream


class CopyOnWriteWeakSet(ghidra.util.datastruct.WeakSet):
    """
    A set that avoids ConcurrentModificationExceptions by copying the internal storage
     for every mutation operation.  Thus, this data structure is only efficient when the
     number of event notification operations significantly out numbers mutations to this structure
     (e.g., adding and removing items.
 
     An example use case where using this class is a good fit would be a listener list where
     listeners are added during initialization, but not after that.   Further, this hypothetical
     list is used to fire a large number of events.
 
     A bad use of this class would be as a container to store widgets where the container the
     contents are changed often, but iterated very little.
 
     Finally, if this structure is only ever used from a single thread, like the Swing thread, then
     you do not need the overhead of this class, as the Swing thread synchronous access guarantees
     that the structure cannot be mutated while it is being iterated.  See
     WeakDataStructureFactory#createSingleThreadAccessWeakSet().
    """





    def __init__(self): ...

    def __iter__(self): ...

    def add(self, t: object) -> bool: ...

    def addAll(self, c: java.util.Collection) -> bool:
        """
        Adds all items to this set.
         <p>
         Note: calling this method will only result in one copy operation.  If {@link #add(Object)}
         were called instead for each item of the iterator, then each call would copy this set.
        @param c the items
        """
        ...

    def clear(self) -> None: ...

    def contains(self, t: object) -> bool: ...

    def containsAll(self, c: java.util.Collection) -> bool: ...

    @staticmethod
    def copyOf(__a0: java.util.Collection) -> java.util.Set: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool: ...

    def iterator(self) -> Iterator[object]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def of() -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: List[object]) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object) -> java.util.Set: ...

    def parallelStream(self) -> java.util.stream.Stream: ...

    def remove(self, t: object) -> bool: ...

    def removeAll(self, c: java.util.Collection) -> bool: ...

    def removeIf(self, __a0: java.util.function.Predicate) -> bool: ...

    def retainAll(self, c: java.util.Collection) -> bool: ...

    def size(self) -> int: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def stream(self) -> java.util.stream.Stream: ...

    @overload
    def toArray(self) -> List[object]: ...

    @overload
    def toArray(self, a: List[object]) -> List[object]: ...

    @overload
    def toArray(self, __a0: java.util.function.IntFunction) -> List[object]: ...

    def toString(self) -> unicode: ...

    def values(self) -> java.util.Collection: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

