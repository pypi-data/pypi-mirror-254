import docking.widgets.values
import java.lang
import javax.swing


class AddressValue(docking.widgets.values.AbstractValue):
    """
    Value class for Address types. In order to parse and create Address types, an 
     AddressFactory is required when defining this type. As a convenience, it can
     be constructed with a Program, in which case it will use the AddressFactory from 
     that program.
 
     This class and other subclasses of AbstractValue are part of a subsystem for easily
     defining a set of values that can be displayed in an input dialog (ValuesMapDialog).
     Typically, these values are created indirectly using a GValuesMap which is then
     given to the constructor of the dialog. However, an alternate approach is to create the
     dialog without a ValuesMap and then use its ValuesMapDialog#addValue(AbstractValue) 
     method directly.
    """





    @overload
    def __init__(self, name: unicode, defaultValue: ghidra.program.model.address.Address, factory: ghidra.program.model.address.AddressFactory):
        """
        Creates an AddressValue with an optional default value.
        @param name the name of this value
        @param defaultValue an optional default value
        @param factory the AddressFactory that will be used to create Addresses.
        """
        ...

    @overload
    def __init__(self, name: unicode, defaultValue: ghidra.program.model.address.Address, program: ghidra.program.model.listing.Program):
        """
        Creates an AddressValue with an optional default value and uses the {@link AddressFactory} 
         from the given program.
        @param name the name of this value
        @param defaultValue an optional default value
        @param program the program whose AddressFactory will be used to create Addresses.
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