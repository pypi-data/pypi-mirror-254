from typing import List
import java.lang


class GoPcValueEvaluator(object):
    """
    Evaluates a sequence of (value_delta,pc_delta) leb128 pairs to calculate a value for a certain 
     PC location.
    """





    def __init__(self, func: ghidra.app.util.bin.format.golang.rtti.GoFuncData, offset: long):
        """
        Creates a {@link GoPcValueEvaluator} instance, tied to the specified GoFuncData, starting
         at the specified offset in the moduledata's pctab.
        @param func {@link GoFuncData}
        @param offset offset in moduledata's pctab
        @throws IOException if error reading pctab
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def eval(self, targetPC: long) -> int:
        """
        Returns the value encoded into the table at the specified pc.
        @param targetPC pc
        @return value at specified pc, or -1 if error evaluating table
        @throws IOException if error reading data
        """
        ...

    def evalAll(self, targetPC: long) -> List[int]:
        """
        Returns the set of all values for each unique pc section.
        @param targetPC max pc to advance the sequence to when evaluating the table
        @return list of integer values
        @throws IOException if error reading data
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getMaxPC(self) -> long:
        """
        Returns the largest PC value calculated when evaluating the result of the table's sequence.
        @return largest PC value encountered
        @throws IOException if error evaluating result
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
    def maxPC(self) -> long: ...