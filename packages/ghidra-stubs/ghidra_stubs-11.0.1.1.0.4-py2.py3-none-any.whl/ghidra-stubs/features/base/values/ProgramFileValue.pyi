import docking
import docking.widgets.values
import ghidra.features.base.values
import ghidra.program.model.listing
import ghidra.util.task
import java.lang
import javax.swing


class ProgramFileValue(ghidra.features.base.values.ProjectFileValue):
    """
    Value class for Program files. The editor component consists of the JTextField 
     and a browse button for bringing up a DataTreeDialog for picking programs from the 
     current project. This class also provides a convenience method for opening a program.
 
     This class and other subclasses of AbstractValue are part of a subsystem for easily
     defining a set of values that can be displayed in an input dialog (ValuesMapDialog).
     Typically, these values are created indirectly using a GValuesMap which is then
     given to the constructor of the dialog. However, an alternate approach is to create the
     dialog without a ValuesMap and then use its ValuesMapDialog#addValue(AbstractValue) 
     method directly.
    """





    @overload
    def __init__(self, name: unicode):
        """
        Constructor for creating a new ProgramFileValue with the given name.
        @param name the name of the value
        """
        ...

    @overload
    def __init__(self, name: unicode, startingPath: unicode):
        """
        Constructor for creating a new ProgramFileValue with the given name and a starting
         folder when using the project file chooser.
        @param name the name of the value
        @param startingPath the path to a starting folder
        """
        ...

    @overload
    def __init__(self, name: unicode, project: ghidra.framework.model.Project, startingPath: unicode):
        """
        Constructor for ProgramValue when wanting to pick from a different project than the
         active project, such as a read-only project.
        @param name the name of the value
        @param project The project from which to pick a project.
        @param startingPath the path to a starting folder (Can also be a path to program)
        """
        ...



    def copyValue(self, other: docking.widgets.values.AbstractValue) -> None:
        """
        Copies the T value from the given AbstractValue to this AbstractValue.
        @param other the AbstractValue to copy from
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAsText(self) -> unicode:
        """
        Returns a string representation for the value. It is expected that the string returned
         from this method can be parsed by the corresponding {@link #setAsText(String)} method. If the
         value of this object is null, null will be returned.
        @return a string representation for the value or null if the value is null
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent: ...

    def getName(self) -> unicode:
        """
        Returns the name of this value object.
        @return the name of this value object
        """
        ...

    def getValue(self) -> object:
        """
        Returns the value currently assigned to this object.
        @return the value currently assigned to this object (may be null)
        """
        ...

    def hasValue(self) -> bool:
        """
        Returns true if the value is non-null.
        @return true if the value is non-null
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openProgram(self, consumer: object, tool: docking.Tool, upgradeIfNeeded: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Program:
        """
        Convenience method for opening the program for the current program file value. If the program
         is already open, then the consumer will be added to the program. The caller of this method is
         responsible for calling {@link Program#release(Object)} with the same consumer when it is
         done using this program. Program are only closed after all consumers are released. If
         multiple calls are made to this method, then the consumer will be added multiple times
         and must be released multiple times.
         <P>
         The consumer can be any object, but since the consumer's purpose is to keep the program open 
         while some object is using it, the object itself is typically passed in as
         the consumer. For example, when used in a script, passing in the java keyword "this" as the
         consumer will make the script itself the consumer.
         <P>
        @param consumer the consumer to be used to open the program
        @param tool optional tool that if non-null, the program will also be opened in the tool
        @param upgradeIfNeeded if true, program will be upgraded if needed and possible. If false,
         the program will only be upgraded after first prompting the user. In headless mode, it will
         attempt to upgrade only if the parameter is true.
        @param monitor task monitor for cancelling the open program.
        @return a program for the currently selected program file. If no file chosen, returns null
        @throws VersionException if the Program is out-of-date from the version of GHIDRA and an 
         upgrade was not been performed. In non-headless mode, the user will have already been
         notified via a popup dialog.
         current Ghidra Program version.
        @throws IOException if there is an error accessing the Program's DomainObject
        @throws CancelledException if the operation is cancelled
        """
        ...

    def setAsText(self, valueString: unicode) -> object:
        """
        Sets the value for this object from the given string. If this object can not succesfully
         parse the string, an exception will be thrown.
        @param valueString the string to be parsed into the type for this object
        @return The value resulting from parsing the string value
        @throws IllegalArgumentException if the string can not be parsed into a value of type T
        """
        ...

    def setValue(self, value: object) -> None:
        """
        Sets the value for this object.
        @param value the value to set for this object (may be null)
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

