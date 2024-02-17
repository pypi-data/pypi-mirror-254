import docking.widgets.values
import java.lang
import javax.swing


class ProjectFileValue(docking.widgets.values.AbstractValue):
    """
    Value class for project files (DomainFile). The editor component consists of a
     JTextField and a browse button for bringing up a DataTreeDialog for picking
     project files from the current project.
 
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
        Constructor for creating a new ProjectFileValue with the given name.
        @param name the name of the value
        """
        ...

    @overload
    def __init__(self, name: unicode, startingPath: unicode):
        """
        Constructor for creating a new ProjectFileValue with the given name and a starting
         folder when using the project file chooser.
        @param name the name of the value
        @param startingPath the path to a starting folder
        """
        ...

    @overload
    def __init__(self, name: unicode, projectFileClass: java.lang.Class):
        """
        Constructor for creating a new ProgramFileValue with the given name and {@link DomainObject}
         class to filter on (All other types will be filtered out in the chooser).
        @param name the name of the value
        @param projectFileClass the DomainObject class to filter
        """
        ...

    @overload
    def __init__(self, name: unicode, project: ghidra.framework.model.Project, startingPath: unicode, projectFileClass: java.lang.Class):
        """
        Constructor for ProgramValue when wanting to pick from a different project than the
         active project, such as a read-only project.
        @param name the name of the value
        @param project The project from which to pick a project.
        @param startingPath the path to a starting folder (Can also be a path to program)
        @param projectFileClass a {@link DomainFile} class to filter on. (Only those types
         will appear in the chooser)
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

    @property
    def component(self) -> javax.swing.JComponent: ...