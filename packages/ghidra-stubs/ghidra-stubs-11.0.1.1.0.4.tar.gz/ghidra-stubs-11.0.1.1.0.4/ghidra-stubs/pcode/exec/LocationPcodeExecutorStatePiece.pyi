from typing import List
import ghidra.pcode.exec
import ghidra.pcode.exec.PcodeArithmetic
import ghidra.pcode.exec.PcodeExecutorStatePiece
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.mem
import ghidra.program.model.pcode
import java.lang
import java.util


class LocationPcodeExecutorStatePiece(object, ghidra.pcode.exec.PcodeExecutorStatePiece):
    """
    An auxiliary state piece that reports the location of the control value
 
 
     This is intended for use as the right side of a PairedPcodeExecutorState or
     PairedPcodeExecutorStatePiece. Except for unique spaces, sets are ignored, and gets
     simply echo back the location of the requested read. In unique spaces, the "location" is treated
     as the value, so that values transiting unique space can correctly have their source locations
     reported.
    """





    def __init__(self, language: ghidra.program.model.lang.Language):
        """
        Construct a "location" state piece
        @param language the language of the machine
        """
        ...



    def checkRange(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long, __a2: int) -> None: ...

    def clear(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fork(self) -> ghidra.pcode.exec.LocationPcodeExecutorStatePiece: ...

    def getAddressArithmetic(self) -> List[ghidra.pcode.exec.PcodeArithmetic]: ...

    def getArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    def getClass(self) -> java.lang.Class: ...

    def getConcreteBuffer(self, address: ghidra.program.model.address.Address, purpose: ghidra.pcode.exec.PcodeArithmetic.Purpose) -> ghidra.program.model.mem.MemBuffer: ...

    def getLanguage(self) -> ghidra.program.model.lang.Language: ...

    def getRegisterValues(self) -> java.util.Map: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.lang.Register, __a1: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.pcode.Varnode, __a1: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.address.Address, __a1: int, __a2: bool, __a3: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long, __a2: int, __a3: bool, __a4: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    @overload
    def getVar(self, space: ghidra.program.model.address.AddressSpace, offset: List[int], size: int, quantize: bool, reason: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> ghidra.pcode.exec.ValueLocation: ...

    @overload
    def getVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: object, __a2: int, __a3: bool, __a4: ghidra.pcode.exec.PcodeExecutorStatePiece.Reason) -> object: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def quantizeOffset(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long) -> long: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.lang.Register, __a1: object) -> None: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.pcode.Varnode, __a1: object) -> None: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.address.Address, __a1: int, __a2: bool, __a3: object) -> None: ...

    @overload
    def setVar(self, space: ghidra.program.model.address.AddressSpace, offset: List[int], size: int, quantize: bool, val: ghidra.pcode.exec.ValueLocation) -> None: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: long, __a2: int, __a3: bool, __a4: object) -> None: ...

    @overload
    def setVar(self, __a0: ghidra.program.model.address.AddressSpace, __a1: object, __a2: int, __a3: bool, __a4: object) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    @property
    def arithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    @property
    def language(self) -> ghidra.program.model.lang.Language: ...

    @property
    def registerValues(self) -> java.util.Map: ...