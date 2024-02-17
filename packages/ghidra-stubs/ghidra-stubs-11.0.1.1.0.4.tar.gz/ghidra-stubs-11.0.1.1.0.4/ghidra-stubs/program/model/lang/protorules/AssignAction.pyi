from typing import List
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.lang.protorules
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class AssignAction(object):
    """
    An action that assigns an Address to a function prototype parameter
 
     A request for the address of either return storage or an input parameter is made
     through the assignAddress() method, which is given full information about the function prototype.
     Details about how the action performs is configured through the restoreXml() method.
    """

    FAIL: int = 1
    HIDDENRET_PTRPARAM: int = 3
    HIDDENRET_SPECIALREG: int = 4
    HIDDENRET_SPECIALREG_VOID: int = 5
    NO_ASSIGNMENT: int = 2
    SUCCESS: int = 0



    def __init__(self, res: ghidra.program.model.lang.ParamListStandard): ...



    def assignAddress(self, dt: ghidra.program.model.data.DataType, proto: ghidra.program.model.lang.PrototypePieces, pos: int, dtManager: ghidra.program.model.data.DataTypeManager, status: List[int], res: ghidra.program.model.lang.ParameterPieces) -> int:
        """
        Assign an address and other meta-data for a specific parameter or for return storage in context
         The Address is assigned based on the data-type of the parameter, available register
         resources, and other details of the function prototype.  Consumed resources are marked.
         This method returns a response code:
           - SUCCESS            - indicating the Address was successfully assigned
           - FAIL               - if the Address could not be assigned
           - HIDDENRET_PTRPARAM - if an additional hidden return parameter is required
        @param dt is the data-type of the parameter or return value
        @param proto is the high-level description of the function prototype
        @param pos is the position of the parameter (pos>=0) or return storage (pos=-1)
        @param dtManager is a data-type manager for (possibly) transforming the data-type
        @param status is the resource consumption array
        @param res will hold the resulting description of the parameter
        @return the response code
        """
        ...

    def clone(self, newResource: ghidra.program.model.lang.ParamListStandard) -> ghidra.program.model.lang.protorules.AssignAction:
        """
        Make a copy of this action
        @param newResource is the new resource object that will own the clone
        @return the newly allocated copy
        @throws InvalidInputException if required configuration is not present in new resource object
        """
        ...

    def encode(self, encoder: ghidra.program.model.pcode.Encoder) -> None:
        """
        Save this action and its configuration to a stream
        @param encoder is the stream encoder
        @throws IOException for problems writing to the stream
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEquivalent(self, op: ghidra.program.model.lang.protorules.AssignAction) -> bool:
        """
        Test if the given action is configured and performs identically to this
        @param op is the given action
        @return true if the two actions are equivalent
        """
        ...

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

    def restoreXml(self, parser: ghidra.xml.XmlPullParser) -> None:
        """
        Configure any details of how this action should behave from the stream
        @param parser is the given stream decoder
        @throws XmlParseException is there are problems decoding the stream
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

