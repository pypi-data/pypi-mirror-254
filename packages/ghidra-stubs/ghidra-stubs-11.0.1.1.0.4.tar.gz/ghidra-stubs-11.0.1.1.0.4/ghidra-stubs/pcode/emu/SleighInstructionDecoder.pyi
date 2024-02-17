import ghidra.pcode.emu
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang


class SleighInstructionDecoder(object, ghidra.pcode.emu.InstructionDecoder):
    """
    The default instruction decoder, based on Sleigh
 
 
     This simply uses a Disassembler on the machine's memory state.
    """





    def __init__(self, language: ghidra.program.model.lang.Language, state: ghidra.pcode.exec.PcodeExecutorState):
        """
        Construct a Sleigh instruction decoder
        @see {@link DefaultPcodeThread#createInstructionDecoder(PcodeExecutorState)}
        @param language the language to decoder
        @param state the state containing the target program, probably the shared state of the p-code
                    machine. It must be possible to obtain concrete buffers on this state.
        """
        ...



    def branched(self, address: ghidra.program.model.address.Address) -> None: ...

    def decodeInstruction(self, address: ghidra.program.model.address.Address, context: ghidra.program.model.lang.RegisterValue) -> ghidra.program.model.listing.Instruction: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLastInstruction(self) -> ghidra.program.model.listing.Instruction: ...

    def getLastLengthWithDelays(self) -> int: ...

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