import ghidra.program.model.data.ISF
import java.lang


class IsfDataTypeBitField(ghidra.program.model.data.ISF.AbstractIsfObject):
    bit_length: int
    bit_offset: int
    bit_position: int
    kind: unicode
    location: unicode
    name: unicode
    settings: List[object]
    type: ghidra.program.model.data.ISF.IsfObject



    def __init__(self, __a0: ghidra.program.model.data.BitFieldDataType, __a1: int, __a2: ghidra.program.model.data.ISF.IsfObject): ...



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

