from typing import List
import ghidra.app.decompiler.signature
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.pcode
import java.lang


class DebugSignature(object):
    """
    A feature extracted from a function, with an additional description of what information is
     incorporated into the feature.  The feature may incorporate data-flow and/or control-flow
     information from the function. Internally, the feature is a 32-bit hash of this information, but
     derived classes from this abstract class include more detailed information about how the hash was formed.
    """

    hash: int



    def __init__(self): ...



    def decode(self, decoder: ghidra.program.model.pcode.Decoder) -> None:
        """
        Decode the feature from a stream.
        @param decoder is the stream decoder
        @throws DecoderException for problems reading the stream
        """
        ...

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

    def printRaw(self, language: ghidra.program.model.lang.Language, buf: java.lang.StringBuffer) -> None:
        """
        Write a brief description of this feature to the given StringBuffer.
        @param language is the underlying language of the function
        @param buf is the given StringBuffer
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

