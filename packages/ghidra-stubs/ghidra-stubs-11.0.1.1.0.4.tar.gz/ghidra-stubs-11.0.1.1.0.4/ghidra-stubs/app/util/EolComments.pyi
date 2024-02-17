from typing import List
import docking.widgets.fieldpanel.support
import ghidra.app.util
import ghidra.program.util
import java.lang


class EolComments(object):
    """
    Utility class with methods to get comment information that can be displayed in the end of line
     comment field. Each instance of this class is associated with a code unit.  This class uses the
     provided options to decide how to load and filter existing comments.

     Comment types that can be shown include the End of Line comment for the code unit, the
     Repeatable comment for the code unit, any repeatable comments for the code units that this code
     unit has references to, and possibly a comment indicating the data at a code unit that is
     referenced by this code unit.
    """





    def __init__(self, cu: ghidra.program.model.listing.CodeUnit, operandsShowReferences: bool, maxDisplayComments: int, extraCommentsOption: ghidra.app.util.viewer.field.EolExtraCommentsOption): ...



    def equals(self, __a0: object) -> bool: ...

    def getAutomaticComment(self) -> List[unicode]:
        """
        Gets the automatic comments
        @return the comments
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComments(self) -> List[unicode]:
        """
        Return all comments loaded by this class
        @return the comments
        """
        ...

    def getEOLComments(self) -> List[unicode]:
        """
        Gets the End of Line comments
        @return the comments
        """
        ...

    def getLocation(self, eolRow: int, eolColumn: int) -> ghidra.program.util.ProgramLocation: ...

    def getReferencedRepeatableComments(self) -> List[ghidra.app.util.RefRepeatComment]:
        """
        Gets the repeatable comments at the "to reference"s
        @return the comments
        """
        ...

    def getRepeatableComments(self) -> List[unicode]:
        """
        Gets the repeatable comments
        @return the comments
        """
        ...

    def getRowCol(self, cloc: ghidra.program.util.CommentFieldLocation) -> docking.widgets.fieldpanel.support.RowColLocation: ...

    def hashCode(self) -> int: ...

    def isShowingAutoComments(self) -> bool: ...

    def isShowingRefRepeatables(self) -> bool: ...

    def isShowingRepeatables(self) -> bool: ...

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
    def EOLComments(self) -> List[object]: ...

    @property
    def automaticComment(self) -> List[object]: ...

    @property
    def comments(self) -> List[object]: ...

    @property
    def referencedRepeatableComments(self) -> List[object]: ...

    @property
    def repeatableComments(self) -> List[object]: ...

    @property
    def showingAutoComments(self) -> bool: ...

    @property
    def showingRefRepeatables(self) -> bool: ...

    @property
    def showingRepeatables(self) -> bool: ...