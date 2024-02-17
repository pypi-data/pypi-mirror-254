from typing import List
import ghidra.service.graph
import java.lang


class BSimFeatureGraphType(ghidra.service.graph.GraphType):
    BASE_BLOCK_VERTEX: unicode = u'Base Block'
    BASE_VARNODE_VERTEX: unicode = u'Base Varnode'
    BLOCK_START: unicode = u'Block Start'
    BLOCK_STOP: unicode = u'Block Stop'
    BSIM_NEIGHBOR_VERTEX: unicode = u'BSim Neighbor Block'
    CALL_STRING: unicode = u'Call String'
    CHILD_BLOCK_VERTEX: unicode = u'Child Block'
    COLLAPSED_IN: unicode = u'Collapsed Input'
    COLLAPSED_OP: unicode = u'Collapsed Op'
    COLLAPSED_OUT: unicode = u'Collapsed Output'
    COLLAPSED_VARNODE: unicode = u'Collapsed Varnode'
    CONSTANT_FUNCTION_INPUT: unicode = u'Constant Function Input'
    CONSTANT_VERTEX: unicode = u'Constant'
    CONTROL_FLOW_DEFAULT_EDGE: unicode = u'Default'
    CONTROL_FLOW_PREFIX: unicode = u'cf'
    COPY_PREFIX: unicode = u'copy'
    COPY_SIGNATURE: unicode = u'Copy Signature'
    DATAFLOW_IN: unicode = u'Input'
    DATAFLOW_OUT: unicode = u'Output'
    DATAFLOW_PREFIX: unicode = u'df'
    DATAFLOW_WINDOW_SIZE: int
    DEFAULT_VERTEX: unicode = u'Default'
    EMPTY_CALL_STRING: unicode = u'(empty)'
    FALSE_EDGE: unicode = u'False'
    FUNCTION_INPUT: unicode = u'Function Input'
    GRANDPARENT_BLOCK_VERTEX: unicode = u'Grandparent Block'
    NULL_BLOCK_VERTEX: unicode = u'Null Block'
    OPTIONS_NAME: unicode = u'BSim Feature Graph'
    OP_ADDRESS: unicode = u'Address'
    PARENT_BLOCK_VERTEX: unicode = u'Parent Block'
    PCODE_OP_VERTEX: unicode = u'Pcode Op'
    PCODE_OUTPUT: unicode = u'Pcode Output'
    SECONDARY_BASE_VARNODE_VERTEX: unicode = u'Secondary Base Varnode'
    SIBLING_BLOCK_VERTEX: unicode = u'Sibling Block'
    SIZE: unicode = u'Size'
    TRUE_EDGE: unicode = u'True'
    VARNODE_ADDRESS: unicode = u'Address Varnode'
    VOID_BASE: unicode = u'void'



    def __init__(self): ...



    def containsEdgeType(self, __a0: unicode) -> bool: ...

    def containsVertexType(self, __a0: unicode) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getEdgeTypes(self) -> List[object]: ...

    def getName(self) -> unicode: ...

    def getOptionsName(self) -> unicode: ...

    def getVertexTypes(self) -> List[object]: ...

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
    def optionsName(self) -> unicode: ...