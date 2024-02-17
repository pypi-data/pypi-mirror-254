from typing import List
import java.io
import java.lang


class Unfinished(object):
    """
    This serves both as a marker interface for classes missing important methods and as container for
     the #TODO(String, Object...) method.
 
 
     TODO: It'd be nice to optionally ignore TODO exceptions, but this seems to require a dependency
     on JUnit, which is a no-no within . Maybe there's a way via the abstract test
     case, or an interface mixin....
    """






    class TODOException(java.lang.UnsupportedOperationException):




        @overload
        def __init__(self): ...

        @overload
        def __init__(self, __a0: unicode): ...



        def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

        def equals(self, __a0: object) -> bool: ...

        def fillInStackTrace(self) -> java.lang.Throwable: ...

        def getCause(self) -> java.lang.Throwable: ...

        def getClass(self) -> java.lang.Class: ...

        def getLocalizedMessage(self) -> unicode: ...

        def getMessage(self) -> unicode: ...

        def getStackTrace(self) -> List[java.lang.StackTraceElement]: ...

        def getSuppressed(self) -> List[java.lang.Throwable]: ...

        def hashCode(self) -> int: ...

        def initCause(self, __a0: java.lang.Throwable) -> java.lang.Throwable: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        @overload
        def printStackTrace(self) -> None: ...

        @overload
        def printStackTrace(self, __a0: java.io.PrintStream) -> None: ...

        @overload
        def printStackTrace(self, __a0: java.io.PrintWriter) -> None: ...

        def setStackTrace(self, __a0: List[java.lang.StackTraceElement]) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    @overload
    @staticmethod
    def TODO() -> object:
        """
        Perhaps a little better than returning {@code null} or throwing
         {@link UnsupportedOperationException} yourself, as references can be found in most IDEs.
        """
        ...

    @overload
    @staticmethod
    def TODO(message: unicode, ignore: List[object]) -> object:
        """
        Perhaps a little better than returning {@code null} or throwing
         {@link UnsupportedOperationException} yourself, as references can be found in most IDEs.
        @param message A message describing the task that is yet to be done
        @param ignore variables involved in the implementation so far
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

