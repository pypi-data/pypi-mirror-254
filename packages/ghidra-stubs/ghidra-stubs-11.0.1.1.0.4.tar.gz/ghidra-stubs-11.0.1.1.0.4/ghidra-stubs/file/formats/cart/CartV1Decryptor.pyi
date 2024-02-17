from typing import List
import ghidra.util.task
import java.lang


class CartV1Decryptor(object):




    def __init__(self, __a0: List[int]): ...



    @overload
    def decrypt(self, __a0: List[int]) -> List[int]: ...

    @overload
    def decrypt(self, __a0: List[int], __a1: ghidra.util.task.TaskMonitor) -> List[int]: ...

    @overload
    @staticmethod
    def decrypt(__a0: List[int], __a1: List[int]) -> List[int]: ...

    @overload
    @staticmethod
    def decrypt(__a0: List[int], __a1: List[int], __a2: ghidra.util.task.TaskMonitor) -> List[int]: ...

    @overload
    def decryptToString(self, __a0: List[int]) -> unicode: ...

    @overload
    def decryptToString(self, __a0: List[int], __a1: ghidra.util.task.TaskMonitor) -> unicode: ...

    @overload
    @staticmethod
    def decryptToString(__a0: List[int], __a1: List[int]) -> unicode: ...

    @overload
    @staticmethod
    def decryptToString(__a0: List[int], __a1: List[int], __a2: ghidra.util.task.TaskMonitor) -> unicode: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setKey(self, __a0: List[int]) -> None: ...

    @overload
    def throwIfInvalid(self) -> None: ...

    @overload
    def throwIfInvalid(self, __a0: List[int]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def key(self) -> None: ...  # No getter available.

    @key.setter
    def key(self, value: List[int]) -> None: ...