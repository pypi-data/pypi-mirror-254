import ghidra.program.model.address
import ghidra.trace.database.target
import ghidra.trace.model
import ghidra.util.database
import ghidra.util.database.spatial
import ghidra.util.database.spatial.hyper
import java.lang
import java.util


class TraceObjectValueQuery(ghidra.util.database.spatial.hyper.AbstractHyperBoxQuery):




    def __init__(self, __a0: ghidra.trace.database.target.ValueBox, __a1: ghidra.trace.database.target.ValueBox, __a2: ghidra.util.database.spatial.hyper.HyperDirection): ...



    @staticmethod
    def all() -> ghidra.trace.database.target.TraceObjectValueQuery: ...

    def and(self, __a0: ghidra.util.database.spatial.hyper.AbstractHyperBoxQuery) -> ghidra.util.database.spatial.hyper.AbstractHyperBoxQuery: ...

    @staticmethod
    def at(__a0: unicode, __a1: long, __a2: ghidra.program.model.address.Address) -> ghidra.trace.database.target.TraceObjectValueQuery: ...

    @staticmethod
    def canonicalParents(__a0: ghidra.trace.database.target.DBTraceObject, __a1: ghidra.trace.model.Lifespan) -> ghidra.trace.database.target.TraceObjectValueQuery: ...

    def equals(self, __a0: object) -> bool: ...

    def getBoundsComparator(self) -> java.util.Comparator: ...

    def getClass(self) -> java.lang.Class: ...

    def getDirection(self) -> ghidra.util.database.spatial.hyper.HyperDirection: ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def intersecting(__a0: ghidra.trace.model.Lifespan, __a1: ghidra.program.model.address.AddressRange) -> ghidra.trace.database.target.TraceObjectValueQuery: ...

    @overload
    @staticmethod
    def intersecting(__a0: unicode, __a1: unicode, __a2: ghidra.trace.model.Lifespan, __a3: ghidra.program.model.address.AddressRange) -> ghidra.trace.database.target.TraceObjectValueQuery: ...

    @overload
    @staticmethod
    def intersecting(__a0: unicode, __a1: unicode, __a2: ghidra.trace.model.Lifespan, __a3: ghidra.util.database.DBCachedObjectStoreFactory.RecAddress, __a4: ghidra.util.database.DBCachedObjectStoreFactory.RecAddress) -> ghidra.trace.database.target.TraceObjectValueQuery: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parents(__a0: ghidra.trace.database.target.DBTraceObject, __a1: ghidra.trace.model.Lifespan) -> ghidra.trace.database.target.TraceObjectValueQuery: ...

    def starting(self, __a0: ghidra.util.database.spatial.hyper.HyperDirection) -> ghidra.util.database.spatial.hyper.AbstractHyperBoxQuery: ...

    @overload
    def terminateEarlyData(self, __a0: ghidra.util.database.spatial.BoundedShape) -> bool: ...

    @overload
    def terminateEarlyData(self, __a0: object) -> bool: ...

    @overload
    def terminateEarlyNode(self, __a0: ghidra.util.database.spatial.hyper.HyperBox) -> bool: ...

    @overload
    def terminateEarlyNode(self, __a0: object) -> bool: ...

    @overload
    def testData(self, __a0: ghidra.trace.database.target.ValueShape) -> bool: ...

    @overload
    def testData(self, __a0: object) -> bool: ...

    @overload
    def testNode(self, __a0: ghidra.util.database.spatial.hyper.HyperBox) -> ghidra.util.database.spatial.Query.QueryInclusion: ...

    @overload
    def testNode(self, __a0: object) -> ghidra.util.database.spatial.Query.QueryInclusion: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def values(__a0: ghidra.trace.database.target.DBTraceObject, __a1: ghidra.trace.model.Lifespan) -> ghidra.trace.database.target.TraceObjectValueQuery: ...

    @overload
    @staticmethod
    def values(__a0: ghidra.trace.database.target.DBTraceObject, __a1: unicode, __a2: unicode, __a3: ghidra.trace.model.Lifespan) -> ghidra.trace.database.target.TraceObjectValueQuery: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

