from typing import Iterator
from typing import List
import java.lang
import java.util
import java.util.function
import java.util.stream


class WeakSet(object, java.util.Set):




    def __init__(self): ...

    def __iter__(self): ...

    def add(self, t: object) -> bool:
        """
        Add the given object to the set
        @param t the object to add
        """
        ...

    def addAll(self, c: java.util.Collection) -> bool: ...

    def clear(self) -> None:
        """
        Remove all elements from this data structure
        """
        ...

    def contains(self, t: object) -> bool:
        """
        Returns true if the given object is in this data structure
        @param t the object
        @return true if the given object is in this data structure
        """
        ...

    def containsAll(self, c: java.util.Collection) -> bool: ...

    @staticmethod
    def copyOf(__a0: java.util.Collection) -> java.util.Set: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Return whether this data structure is empty
        @return whether this data structure is empty
        """
        ...

    def iterator(self) -> java.util.Iterator: ...

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

    def removeAll(self, c: java.util.Collection) -> bool: ...

    def removeIf(self, __a0: java.util.function.Predicate) -> bool: ...

    def retainAll(self, c: java.util.Collection) -> bool: ...

    def size(self) -> int:
        """
        Return the number of objects contained within this data structure
        @return the size
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def stream(self) -> java.util.stream.Stream:
        """
        Returns a stream of the values of this collection.
        @return a stream of the values of this collection.
        """
        ...

    @overload
    def toArray(self) -> List[object]: ...

    @overload
    def toArray(self, a: List[object]) -> List[object]: ...

    @overload
    def toArray(self, __a0: java.util.function.IntFunction) -> List[object]: ...

    def toString(self) -> unicode: ...

    def values(self) -> java.util.Collection:
        """
        Returns a Collection view of this set.  The returned Collection is backed by this set.
        @return a Collection view of this set.  The returned Collection is backed by this set.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def empty(self) -> bool: ...