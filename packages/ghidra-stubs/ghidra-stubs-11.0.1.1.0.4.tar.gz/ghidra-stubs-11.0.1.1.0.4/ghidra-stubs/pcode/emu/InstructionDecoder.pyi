import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang


class InstructionDecoder(object):
    """
    A means of decoding machine instructions from the bytes contained in the machine state
    """









    def branched(self, address: ghidra.program.model.address.Address) -> None:
        """
        Inform the decoder that the emulator thread just branched
        @param address
        """
        ...

    def decodeInstruction(self, address: ghidra.program.model.address.Address, context: ghidra.program.model.lang.RegisterValue) -> ghidra.program.model.listing.Instruction:
        """
        Decode the instruction starting at the given address using the given context
 
         <p>
         This method cannot return null. If a decode error occurs, it must throw an exception.
        @param address the address to start decoding
        @param context the disassembler/decode context
        @return the instruction
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLastInstruction(self) -> ghidra.program.model.listing.Instruction:
        """
        Get the last instruction decoded
        @return the instruction
        """
        ...

    def getLastLengthWithDelays(self) -> int:
        """
        Get the length of the last decoded instruction, including delay slots
        @return the length
        """
        ...

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

    @property
    def lastInstruction(self) -> ghidra.program.model.listing.Instruction: ...

    @property
    def lastLengthWithDelays(self) -> int: ...