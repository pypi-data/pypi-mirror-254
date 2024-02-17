from typing import List
import ghidra.app.decompiler.signature
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.pcode
import java.lang


class BlockSignature(ghidra.app.decompiler.signature.DebugSignature):
    """
    A feature rooted in a basic block.  There are two forms of a block feature.
     Form 1 contains only local control-flow information about the basic block.
     Form 2 is a feature that combines two operations that occur in sequence within the block.
     This form incorporates info about the operations and data-flow info about their inputs.
    """

    blockSeq: ghidra.program.model.address.Address
    hash: int
    index: int
    opSeq: ghidra.program.model.pcode.SequenceNumber
    opcode: unicode
    previousOpSeq: ghidra.program.model.pcode.SequenceNumber
    previousOpcode: unicode



    def __init__(self): ...



    def decode(self, decoder: ghidra.program.model.pcode.Decoder) -> None: ...

    @staticmethod
    def decodeSignatures(decoder: ghidra.program.model.pcode.Decoder, func: ghidra.program.model.listing.Function) -> List[ghidra.app.decompiler.signature.DebugSignature]:
        """
        Decode an array of features from the stream. Collectively, the features make up
         a "feature vector" for a specific function.  Each feature is returned as a separate descriptive object.
        @param decoder is the stream decoder
        @param func is the specific function whose feature vector is being decoded
        @return the array of feature objects
        @throws DecoderException for problems reading from the stream
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def printRaw(self, language: ghidra.program.model.lang.Language, buf: java.lang.StringBuffer) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

