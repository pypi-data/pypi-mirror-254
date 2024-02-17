import ghidra.app.decompiler.signature
import ghidra.program.model.listing
import ghidra.program.model.pcode
import java.lang


class SignatureResult(object):
    """
    An unordered list of features describing a single function.
     Each feature represents partial information about the control-flow and/or data-flow
     making up the function. Together the features form an (approximately) complete representation
     of the function. Each feature is represented internally as 32-bit hash.  Details of how the
     feature was formed are not available through this object, but see DebugSignature
     This object may optionally include a list of addresses of functions directly called by
     the function being described.
    """

    calllist: java.util.ArrayList
    features: List[int]
    hasbaddata: bool
    hasunimplemented: bool



    def __init__(self): ...



    @staticmethod
    def decode(decoder: ghidra.program.model.pcode.Decoder, func: ghidra.program.model.listing.Function, keepcalllist: bool) -> ghidra.app.decompiler.signature.SignatureResult:
        """
        Decode a sequence of raw feature hashes associated with a specific function from a stream.
         The stream may optionally include addresses of called functions.
        @param decoder is the stream decoder
        @param func is the specific function being described
        @param keepcalllist is true if call addresses should be stored in the result object
        @return the decoded SignatureResult
        @throws DecoderException for problems reading from the stream
        """
        ...

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

