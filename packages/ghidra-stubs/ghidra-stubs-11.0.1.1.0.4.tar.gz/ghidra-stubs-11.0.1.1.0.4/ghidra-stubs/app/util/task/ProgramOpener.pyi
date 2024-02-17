import ghidra.app.plugin.core.progmgr
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class ProgramOpener(object):
    """
    Helper class that contains the logic for opening program for all the various program locations
     and program states. It handles opening DomainFiles, URLs, versioned DomainFiles, and links
     to DomainFiles. It also handles upgrades and checkouts.
    """





    def __init__(self, consumer: object):
        """
        Constructs this class with a consumer to use when opening a program.
        @param consumer the consumer for opening a program
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openProgram(self, locator: ghidra.app.plugin.core.progmgr.ProgramLocator, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Program:
        """
        Opens the program for the given location
        @param locator the program location to open
        @param monitor the TaskMonitor used for status and cancelling
        @return the opened program or null if the operation failed or was cancelled
        """
        ...

    def setNoCheckout(self) -> None:
        """
        Invoking this method prior to task execution will prevent the use of optional checkout which
         require prompting the user.
        """
        ...

    def setPromptText(self, text: unicode) -> None:
        """
        Sets the text to use for the base action type for various prompts that can appear
         when opening programs. (The default is "Open".) For example, you may want to override
         this so be something like "Open Source", or "Open target".
        @param text the text to use as the base action name.
        """
        ...

    def setSilent(self) -> None:
        """
        Invoking this method prior to task execution will prevent any confirmation interaction with
         the user (e.g., optional checkout, snapshot recovery, etc.).  Errors may still be displayed
         if they occur.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def promptText(self) -> None: ...  # No getter available.

    @promptText.setter
    def promptText(self, value: unicode) -> None: ...