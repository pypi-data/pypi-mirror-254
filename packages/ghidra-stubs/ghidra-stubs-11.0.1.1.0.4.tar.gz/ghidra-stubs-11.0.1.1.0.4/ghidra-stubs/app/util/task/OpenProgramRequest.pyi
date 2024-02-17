import ghidra.app.plugin.core.progmgr
import ghidra.program.model.listing
import java.lang


class OpenProgramRequest(object):




    def __init__(self, program: ghidra.program.model.listing.Program, locator: ghidra.app.plugin.core.progmgr.ProgramLocator, consumer: object): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLocator(self) -> ghidra.app.plugin.core.progmgr.ProgramLocator: ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Get the open Program instance which corresponds to this open request.
        @return program instance or null if never opened.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def release(self) -> None:
        """
        Release opened program.  This must be done once, and only once, on a successful 
         open request.  If handing ownership off to another consumer, they should be added
         as a program consumer prior to invoking this method.  Releasing the last consumer
         will close the program instance.
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
    def locator(self) -> ghidra.app.plugin.core.progmgr.ProgramLocator: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...