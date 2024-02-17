from typing import List
import ghidra.app.services
import ghidra.framework.plugintool
import java.lang


class StringValidatorService(object):
    """
    A service that judges the validity of a string
    """

    DUMMY: ghidra.app.services.StringValidatorService = ghidra.app.services.StringValidatorService$DummyStringValidator@53f25c21




    class DummyStringValidator(object, ghidra.app.services.StringValidatorService):
        DUMMY: ghidra.app.services.StringValidatorService = ghidra.app.services.StringValidatorService$DummyStringValidator@53f25c21



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        @staticmethod
        def getCurrentStringValidatorServices(__a0: ghidra.framework.plugintool.PluginTool) -> List[object]: ...

        def getStringValidityScore(self, __a0: ghidra.app.services.StringValidatorQuery) -> ghidra.app.services.StringValidityScore: ...

        def getValidatorServiceName(self) -> unicode: ...

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

        @property
        def validatorServiceName(self) -> unicode: ...





    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getCurrentStringValidatorServices(tool: ghidra.framework.plugintool.PluginTool) -> List[ghidra.app.services.StringValidatorService]:
        """
        Returns a list of string validator services
        @param tool {@link PluginTool}
        @return list of services
        """
        ...

    def getStringValidityScore(self, query: ghidra.app.services.StringValidatorQuery) -> ghidra.app.services.StringValidityScore:
        """
        Judges a string (specified in the query instance).
        @param query {@link StringValidatorQuery}
        @return {@link StringValidityScore}
        """
        ...

    def getValidatorServiceName(self) -> unicode:
        """
        Returns the name of the service
        @return 
        """
        ...

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

    @property
    def validatorServiceName(self) -> unicode: ...