import ghidra.framework.model
import java.lang


class DomainObjectFileListener(object):
    """
    Listener for when the DomainFile associated with a DomainObject changes, such
     as when a 'Save As' action occurs. Unlike DomainObject events, these callbacks are not buffered
     and happen immediately when the DomainFile is changed.
    """









    def domainFileChanged(self, domainObject: ghidra.framework.model.DomainObject) -> None:
        """
        Notification that the DomainFile for the given DomainObject has changed
        @param domainObject the DomainObject whose DomainFile changed
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

