import java.lang


class RustConstants(object):
    RUST_CATEGORYPATH: ghidra.program.model.data.CategoryPath = /rust
    RUST_COMPILER: unicode = u'rustc'
    RUST_EXTENSIONS_PATH: unicode = u'extensions/rust/'
    RUST_EXTENSIONS_UNIX: unicode = u'unix'
    RUST_EXTENSIONS_WINDOWS: unicode = u'windows'
    RUST_SIGNATURE_1: List[int] = array('b', [82, 85, 83, 84, 95, 66, 65, 67, 75, 84, 82, 65, 67, 69])
    RUST_SIGNATURE_2: List[int] = array('b', [47, 114, 117, 115, 116, 99, 47])



    def __init__(self): ...



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

