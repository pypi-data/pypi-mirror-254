from typing import List
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.lang.protorules
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class HiddenReturnAssign(ghidra.program.model.lang.protorules.AssignAction):
    """
    Allocate the return value as an input parameter
 
     A pointer to where the return value is to be stored is passed in as an input parameter.
     This action signals this by returning one of
       - HIDDENRET_PTRPARAM         - indicating the pointer is allocated as a normal input parameter
       - HIDDENRET_SPECIALREG       - indicating the pointer is passed in a dedicated register
       - HIDDENRET_SPECIALREG_VOID
 
     Usually, if a hidden return input is present, the normal register used for return
     will also hold the pointer at the point(s) where the function returns.  A signal of
     HIDDENRET_SPECIALREG_VOID indicates the normal return register is not used to pass back
     the pointer.
    """

    STRATEGY_NORMAL: unicode = u'normalparam'
    STRATEGY_SPECIAL: unicode = u'special'



    def __init__(self, res: ghidra.program.model.lang.ParamListStandard, code: int): ...



    def assignAddress(self, dt: ghidra.program.model.data.DataType, proto: ghidra.program.model.lang.PrototypePieces, pos: int, dtManager: ghidra.program.model.data.DataTypeManager, status: List[int], res: ghidra.program.model.lang.ParameterPieces) -> int: ...

    def clone(self, newResource: ghidra.program.model.lang.ParamListStandard) -> ghidra.program.model.lang.protorules.AssignAction: ...

    def encode(self, encoder: ghidra.program.model.pcode.Encoder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEquivalent(self, op: ghidra.program.model.lang.protorules.AssignAction) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def restoreActionXml(parser: ghidra.xml.XmlPullParser, res: ghidra.program.model.lang.ParamListStandard) -> ghidra.program.model.lang.protorules.AssignAction:
        """
        Read the next action element from the stream and return the new configured
         AssignAction object.  If the next element is not an action, throw an exception.
        @param parser is the stream parser
        @param res is the resource set for the new action
        @return the new action
        @throws XmlParseException for problems parsing the stream
        """
        ...

    @staticmethod
    def restoreSideeffectXml(parser: ghidra.xml.XmlPullParser, res: ghidra.program.model.lang.ParamListStandard) -> ghidra.program.model.lang.protorules.AssignAction:
        """
        Read the next sideeffect element from the stream and return the new configured
         AssignAction object.  If the next element is not a sideeffect, throw an exception.
        @param parser is the stream parser
        @param res is the resource set for the new sideeffect
        @return the new sideeffect
        @throws XmlParseException for problems parsing the stream
        """
        ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

