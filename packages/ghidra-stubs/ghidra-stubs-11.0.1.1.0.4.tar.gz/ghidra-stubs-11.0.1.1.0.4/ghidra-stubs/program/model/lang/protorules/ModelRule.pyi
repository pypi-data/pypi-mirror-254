from typing import List
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.lang.protorules
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class ModelRule(object):
    """
    A rule controlling how parameters are assigned addresses
  
      Rules are applied to a parameter in the context of a full function prototype.
      A rule applies only for a specific class of data-type associated with the parameter, as
      determined by its DatatypeFilter, and may have other criteria limiting when it applies
      (via QualifierFilter).
    """





    @overload
    def __init__(self): ...

    @overload
    def __init__(self, op2: ghidra.program.model.lang.protorules.ModelRule, res: ghidra.program.model.lang.ParamListStandard):
        """
        Copy constructor
        @param op2 is the ModelRule to copy from
        @param res is the new resource set to associate with the copy
        @throws InvalidInputException if necessary resources are not present in the resource set
        """
        ...

    @overload
    def __init__(self, typeFilter: ghidra.program.model.lang.protorules.DatatypeFilter, action: ghidra.program.model.lang.protorules.AssignAction, res: ghidra.program.model.lang.ParamListStandard):
        """
        Construct from components
 
         The provided components are cloned into the new object.
        @param typeFilter is the data-type filter the rule applies before performing the action
        @param action is the action that will be applied
        @param res is the resource list to which this rule will be applied
        @throws InvalidInputException if necessary resources are missing from the list
        """
        ...



    def assignAddress(self, dt: ghidra.program.model.data.DataType, proto: ghidra.program.model.lang.PrototypePieces, pos: int, dtManager: ghidra.program.model.data.DataTypeManager, status: List[int], res: ghidra.program.model.lang.ParameterPieces) -> int:
        """
        Assign an address and other details for a specific parameter or for return storage in context
 
         The Address is only assigned if the data-type filter and the optional qualifier filter
         pass, otherwise a FAIL response is returned.
         If the filters pass, the Address is assigned based on the AssignAction specific to
         this rule, and the action's response code is returned.
        @param dt is the data-type of the parameter or return value
        @param proto is the high-level description of the function prototype
        @param pos is the position of the parameter (pos>=0) or return storage (pos=-1)
        @param dtManager is a data-type manager for (possibly) transforming the data-type
        @param status is the resource consumption array
        @param res will hold the resulting description of the parameter
        @return the response code
        """
        ...

    def encode(self, encoder: ghidra.program.model.pcode.Encoder) -> None:
        """
        Encode this rule to a stream
        @param encoder is the stream encode
        @throws IOException for problems with the stream
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEquivalent(self, op: ghidra.program.model.lang.protorules.ModelRule) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, res: ghidra.program.model.lang.ParamListStandard) -> None:
        """
        Decode this rule from stream
        @param parser is the stream decoder
        @param res is the parameter resource list owning this rule
        @throws XmlParseException if there are problems decoding are missing resources
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

