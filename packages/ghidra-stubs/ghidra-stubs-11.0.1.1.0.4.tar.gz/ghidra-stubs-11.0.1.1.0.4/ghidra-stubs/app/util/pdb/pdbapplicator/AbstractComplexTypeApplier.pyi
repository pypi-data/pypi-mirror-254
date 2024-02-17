import ghidra.app.util.bin.format.pdb2.pdbreader.type
import ghidra.app.util.pdb.pdbapplicator
import java.lang


class AbstractComplexTypeApplier(ghidra.app.util.pdb.pdbapplicator.MsTypeApplier):




    def __init__(self, __a0: ghidra.app.util.pdb.pdbapplicator.DefaultPdbApplicator): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefinitionType(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractComplexMsType, __a1: java.lang.Class) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractComplexMsType: ...

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

