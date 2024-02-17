import ghidra.features.bsim.query.facade
import ghidra.program.model.listing
import java.lang


class DefaultSFQueryServiceFactory(ghidra.features.bsim.query.facade.SFQueryServiceFactory):




    def __init__(self): ...



    def createSFQueryService(self, __a0: ghidra.program.model.listing.Program) -> ghidra.features.bsim.query.facade.SimilarFunctionQueryService: ...

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

