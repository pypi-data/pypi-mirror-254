import ghidra.feature.vt.api
import java.lang


class NeighborGenerator(object):
    RELATIVE_COMPARES: int = 25




    class GrandParents(ghidra.feature.vt.api.NeighborGenerator):




        def __init__(self, __a0: generic.lsh.vector.LSHVectorFactory, __a1: float): ...



        def equals(self, __a0: object) -> bool: ...

        def generate(self, __a0: ghidra.feature.vt.api.FunctionNode, __a1: ghidra.feature.vt.api.FunctionNode) -> ghidra.feature.vt.api.NeighborGenerator.NeighborhoodPair: ...

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






    class Parents(ghidra.feature.vt.api.NeighborGenerator):




        def __init__(self, __a0: generic.lsh.vector.LSHVectorFactory, __a1: float): ...



        def equals(self, __a0: object) -> bool: ...

        def generate(self, __a0: ghidra.feature.vt.api.FunctionNode, __a1: ghidra.feature.vt.api.FunctionNode) -> ghidra.feature.vt.api.NeighborGenerator.NeighborhoodPair: ...

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






    class Spouses(ghidra.feature.vt.api.NeighborGenerator):




        def __init__(self, __a0: generic.lsh.vector.LSHVectorFactory, __a1: float): ...



        def equals(self, __a0: object) -> bool: ...

        def generate(self, __a0: ghidra.feature.vt.api.FunctionNode, __a1: ghidra.feature.vt.api.FunctionNode) -> ghidra.feature.vt.api.NeighborGenerator.NeighborhoodPair: ...

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






    class Children(ghidra.feature.vt.api.NeighborGenerator):




        def __init__(self, __a0: generic.lsh.vector.LSHVectorFactory, __a1: float): ...



        def equals(self, __a0: object) -> bool: ...

        def generate(self, __a0: ghidra.feature.vt.api.FunctionNode, __a1: ghidra.feature.vt.api.FunctionNode) -> ghidra.feature.vt.api.NeighborGenerator.NeighborhoodPair: ...

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






    class Siblings(ghidra.feature.vt.api.NeighborGenerator):




        def __init__(self, __a0: generic.lsh.vector.LSHVectorFactory, __a1: float): ...



        def equals(self, __a0: object) -> bool: ...

        def generate(self, __a0: ghidra.feature.vt.api.FunctionNode, __a1: ghidra.feature.vt.api.FunctionNode) -> ghidra.feature.vt.api.NeighborGenerator.NeighborhoodPair: ...

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






    class GrandChildren(ghidra.feature.vt.api.NeighborGenerator):




        def __init__(self, __a0: generic.lsh.vector.LSHVectorFactory, __a1: float): ...



        def equals(self, __a0: object) -> bool: ...

        def generate(self, __a0: ghidra.feature.vt.api.FunctionNode, __a1: ghidra.feature.vt.api.FunctionNode) -> ghidra.feature.vt.api.NeighborGenerator.NeighborhoodPair: ...

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






    class NeighborhoodPair(object):
        destNeighbors: java.util.Set
        isFilledOut: bool
        srcNeighbors: java.util.Set



        def __init__(self): ...



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



    def __init__(self, __a0: generic.lsh.vector.LSHVectorFactory, __a1: float): ...



    def equals(self, __a0: object) -> bool: ...

    def generate(self, __a0: ghidra.feature.vt.api.FunctionNode, __a1: ghidra.feature.vt.api.FunctionNode) -> ghidra.feature.vt.api.NeighborGenerator.NeighborhoodPair: ...

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

