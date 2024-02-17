from typing import Iterator
import ghidra.app.decompiler
import java.lang
import java.util
import java.util.function


class TokenIterator(object, java.util.Iterator):
    """
    An iterator over ClangToken objects.  The iterator walks a tree of ClangNode objects based on
     the Parent() and Child() methods, returning successive ClangNode leaf objects that are also
     ClangToken objects.  The iterator can run either forward or backward over the tokens.
 
     The constructor TokenIterator(ClangToken,int) initializes the iterator to start at the given
     token, which can be in the middle of the sequence.
    """





    @overload
    def __init__(self, token: ghidra.app.decompiler.ClangToken, forward: bool):
        """
        Initialize an iterator to a point to a specific ClangToken, which may be anywhere in the sequence.
        @param token is the specific ClangToken
        @param forward is true for a forward iterator, false for a backward iterator
        """
        ...

    @overload
    def __init__(self, group: ghidra.app.decompiler.ClangTokenGroup, forward: bool):
        """
        Create iterator across all tokens under the given ClangTokenGroup.  The iterator will walk the
         entire tree of token groups under the given group.  The iterator will run over tokens in display
         order (forward=true) or in reverse of display order (forward=false)
        @param group is the given ClangTokenGroup
        @param forward is true for a forward iterator, false for a backward iterator
        """
        ...

    def __iter__(self) -> Iterator[ghidra.app.decompiler.ClangToken]: ...

    def equals(self, __a0: object) -> bool: ...

    def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool: ...

    def hashCode(self) -> int: ...

    def next(self) -> ghidra.app.decompiler.ClangToken: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

