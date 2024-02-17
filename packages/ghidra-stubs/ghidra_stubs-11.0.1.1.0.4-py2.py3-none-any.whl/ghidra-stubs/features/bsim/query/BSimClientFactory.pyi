import ghidra.features.bsim.query
import java.lang
import java.net


class BSimClientFactory(object):




    def __init__(self): ...



    @overload
    @staticmethod
    def buildClient(__a0: ghidra.features.bsim.query.BSimServerInfo, __a1: bool) -> ghidra.features.bsim.query.FunctionDatabase: ...

    @overload
    @staticmethod
    def buildClient(__a0: java.net.URL, __a1: bool) -> ghidra.features.bsim.query.FunctionDatabase: ...

    @staticmethod
    def buildURL(__a0: unicode) -> java.net.URL: ...

    @staticmethod
    def checkBSimServerURL(__a0: java.net.URL) -> None: ...

    @staticmethod
    def deriveBSimURL(__a0: unicode) -> java.net.URL: ...

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

