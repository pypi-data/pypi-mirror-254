import java.lang


class PrototypePieces(object):
    """
    Raw components of a function prototype (obtained from parsing source code)
    """

    firstVarArgSlot: int
    intypes: java.util.ArrayList
    model: ghidra.program.model.lang.PrototypeModel
    outtype: ghidra.program.model.data.DataType



    @overload
    def __init__(self, model: ghidra.program.model.lang.PrototypeModel, outType: ghidra.program.model.data.DataType):
        """
        Create prototype with output data-type and empty/unspecified input data-types
        @param model is the prototype model
        @param outType is the output data-type
        """
        ...

    @overload
    def __init__(self, model: ghidra.program.model.lang.PrototypeModel, oldList: List[ghidra.program.model.data.DataType], injectedThis: ghidra.program.model.data.DataType):
        """
        Populate pieces from old-style array of DataTypes
        @param model is the prototype model
        @param oldList is the list of output and input data-types
        @param injectedThis if non-null is the data-type of the this pointer to be injected
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

