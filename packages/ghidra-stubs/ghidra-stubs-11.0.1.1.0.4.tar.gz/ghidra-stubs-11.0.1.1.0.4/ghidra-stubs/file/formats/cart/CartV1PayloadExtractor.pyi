from typing import List
import ghidra.app.util.bin
import ghidra.file.formats.cart
import ghidra.util.task
import java.lang


class CartV1PayloadExtractor(object):




    @overload
    def __init__(self, __a0: ghidra.app.util.bin.BinaryReader, __a1: java.io.OutputStream, __a2: ghidra.file.formats.cart.CartV1File): ...

    @overload
    def __init__(self, __a0: ghidra.app.util.bin.ByteProvider, __a1: java.io.OutputStream, __a2: ghidra.file.formats.cart.CartV1File): ...



    def equals(self, __a0: object) -> bool: ...

    def extract(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def testExtraction(__a0: ghidra.app.util.bin.BinaryReader, __a1: ghidra.file.formats.cart.CartV1File, __a2: List[int]) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

