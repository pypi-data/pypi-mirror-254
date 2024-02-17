import ghidra.features.bsim.query.client
import ghidra.features.bsim.query.description
import java.lang


class IDSQLResolution(object):
    id1: long
    id2: long




    class Compiler(ghidra.features.bsim.query.client.IDSQLResolution):
        id1: long
        id2: long



        def __init__(self, __a0: unicode): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def resolve(self, __a0: ghidra.features.bsim.query.client.AbstractSQLFunctionDatabase, __a1: ghidra.features.bsim.query.description.ExecutableRecord) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class Architecture(ghidra.features.bsim.query.client.IDSQLResolution):
        id1: long
        id2: long



        def __init__(self, __a0: unicode): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def resolve(self, __a0: ghidra.features.bsim.query.client.AbstractSQLFunctionDatabase, __a1: ghidra.features.bsim.query.description.ExecutableRecord) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class ExternalFunction(ghidra.features.bsim.query.client.IDSQLResolution):
        id1: long
        id2: long



        def __init__(self, __a0: unicode, __a1: unicode): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def resolve(self, __a0: ghidra.features.bsim.query.client.AbstractSQLFunctionDatabase, __a1: ghidra.features.bsim.query.description.ExecutableRecord) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class ExeCategory(ghidra.features.bsim.query.client.IDSQLResolution):
        id1: long
        id2: long



        def __init__(self, __a0: unicode, __a1: unicode): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def resolve(self, __a0: ghidra.features.bsim.query.client.AbstractSQLFunctionDatabase, __a1: ghidra.features.bsim.query.description.ExecutableRecord) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resolve(self, __a0: ghidra.features.bsim.query.client.AbstractSQLFunctionDatabase, __a1: ghidra.features.bsim.query.description.ExecutableRecord) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

