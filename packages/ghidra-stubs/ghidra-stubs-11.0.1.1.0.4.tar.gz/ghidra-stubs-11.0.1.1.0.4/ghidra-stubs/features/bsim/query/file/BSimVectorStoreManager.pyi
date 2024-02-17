import ghidra.features.bsim.query
import ghidra.features.bsim.query.file
import java.lang


class BSimVectorStoreManager(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getVectorStore(__a0: ghidra.features.bsim.query.BSimServerInfo) -> ghidra.features.bsim.query.file.VectorStore: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def remove(__a0: ghidra.features.bsim.query.BSimServerInfo) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

