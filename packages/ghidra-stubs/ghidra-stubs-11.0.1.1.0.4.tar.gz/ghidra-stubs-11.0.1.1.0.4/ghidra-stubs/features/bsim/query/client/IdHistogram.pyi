import ghidra.features.bsim.query.client
import ghidra.features.bsim.query.description
import java.lang
import java.util


class IdHistogram(object, java.lang.Comparable):
    count: int
    id: long
    vec: generic.lsh.vector.LSHVector



    def __init__(self): ...



    @staticmethod
    def buildVectorIdHistogram(__a0: java.util.Iterator) -> java.util.TreeSet: ...

    @staticmethod
    def collectVectors(__a0: ghidra.features.bsim.query.description.DescriptionManager, __a1: java.util.Iterator) -> java.util.Set: ...

    @overload
    def compareTo(self, __a0: ghidra.features.bsim.query.client.IdHistogram) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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

