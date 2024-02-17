from typing import List
import docking
import docking.widgets.values
import ghidra.features.base.values
import ghidra.framework.model
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.util
import ghidra.util.task
import java.io
import java.lang
import java.util


class GhidraValuesMap(docking.widgets.values.GValuesMap):
    """
    Extends GValuesMap to add Ghidra specific types such as Address and Program
    """





    def __init__(self): ...



    def addValue(self, value: docking.widgets.values.AbstractValue) -> docking.widgets.values.AbstractValue:
        """
        Adds an AbstractValue to this ValuesMap. This is a way to add a custom AbstractValue that
         doesn't have a convenience method for a predefine value type.
        @param value the AbstractValue to add to this ValuesMap
        @return returns the added value
        """
        ...

    def copyValues(self, otherMap: docking.widgets.values.GValuesMap) -> None:
        """
        Copies the values (not the AbstractValues objects, but the T values of each AbstractValue)
         from the given map into this map. The given map must have exactly the same name and
         AbstractValue types as this map.
        @param otherMap The GValuesMap to copy values from
        @throws IllegalArgumentException if the given map does not have exactly the same set of
         names and types as this this map
        """
        ...

    @overload
    def defineAddress(self, name: unicode, program: ghidra.program.model.listing.Program) -> ghidra.features.base.values.AddressValue:
        """
        Defines a value of type {@link Address} with no default value.
        @param name the name for this value
        @param program the program used to get an {@link AddressFactory} for parsing addresses
        @return the new AddressValue that was defined.
        """
        ...

    @overload
    def defineAddress(self, name: unicode, defaultValue: ghidra.program.model.address.Address, factory: ghidra.program.model.address.AddressFactory) -> ghidra.features.base.values.AddressValue:
        """
        Defines a value of type {@link Address}
        @param name the name for this value
        @param defaultValue an option default value
        @param factory the {@link AddressFactory} used to parse addresses
        @return the new AddressValue that was defined.
        """
        ...

    @overload
    def defineAddress(self, name: unicode, defaultValue: ghidra.program.model.address.Address, program: ghidra.program.model.listing.Program) -> ghidra.features.base.values.AddressValue:
        """
        Defines a value of type {@link Address}
        @param name the name for this value
        @param defaultValue an option default value
        @param program the program used to get an {@link AddressFactory} for parsing addresses
        @return the new AddressValue that was defined.
        """
        ...

    def defineBoolean(self, name: unicode, defaultValue: bool) -> docking.widgets.values.BooleanValue:
        """
        Defines a value of type Boolean.
        @param name the name for this value
        @param defaultValue the default value for this boolean value.
        @return the new BooleanValue that was defined.
        """
        ...

    def defineChoice(self, name: unicode, defaultValue: unicode, choices: List[unicode]) -> docking.widgets.values.ChoiceValue:
        """
        Defines a value of type String, but with a restricted set of valid string values.
        @param name the name for this value.
        @param defaultValue an optional (can be null) initial value
        @param choices varargs list of valid string choices
        @return the new ChoiceValue that was defined
        """
        ...

    def defineDirectory(self, name: unicode, defaultValue: java.io.File) -> docking.widgets.values.FileValue:
        """
        Defines a value of type File, but is restricted to directories.
        @param name the name for this value
        @param defaultValue an optional initial value
        @return the new FileValue that was defined
        """
        ...

    @overload
    def defineDouble(self, name: unicode) -> docking.widgets.values.DoubleValue:
        """
        Defines a value of type Double with no initial default value.
        @param name the name for this value
        @return the new DoubleValue that was defined
        """
        ...

    @overload
    def defineDouble(self, name: unicode, defaultValue: float) -> docking.widgets.values.DoubleValue:
        """
        Defines a value of type Double with an initial value
        @param name the name for this value
        @param defaultValue the initial value
        @return the new DoubleValue that was defined
        """
        ...

    @overload
    def defineFile(self, name: unicode, defaultValue: java.io.File) -> docking.widgets.values.FileValue:
        """
        Defines a value of type File
        @param name the name for this value
        @param defaultValue an optional initial value
        @return the new FileValue that was defined
        """
        ...

    @overload
    def defineFile(self, name: unicode, defaultValue: java.io.File, startingDir: java.io.File) -> docking.widgets.values.FileValue:
        """
        Defines a value of type File
        @param name the name for this value
        @param defaultValue an optional initial value
        @param startingDir specifies the starting directory when the FileChooser is invoked
        @return the new FileValue that was defined
        """
        ...

    @overload
    def defineHexInt(self, name: unicode) -> docking.widgets.values.IntValue:
        """
        Defines a value of type Integer that displays as a hex value.
        @param name the name for this value
        @return the new IntValue that was defined
        """
        ...

    @overload
    def defineHexInt(self, name: unicode, defaultValue: int) -> docking.widgets.values.IntValue:
        """
        Defines a value of type Integer with an initial value and displays as a hex value.
        @param name the name for this value
        @param defaultValue the initial value
        @return the new IntValue that was defined
        """
        ...

    @overload
    def defineHexLong(self, name: unicode) -> docking.widgets.values.LongValue:
        """
        Defines a value of type Long that displays as a hex value.
        @param name the name for this value
        @return the new LongValue that was defined
        """
        ...

    @overload
    def defineHexLong(self, name: unicode, defaultValue: long) -> docking.widgets.values.LongValue:
        """
        Defines a value of type Long with an initial value and displays as a hex value.
        @param name the name for this value
        @param defaultValue the initial value
        @return the new LongValue that was defined
        """
        ...

    @overload
    def defineInt(self, name: unicode) -> docking.widgets.values.IntValue:
        """
        Defines a value of type Integer with no initial value.
        @param name the name for this value
        @return the new IntValue that was defined
        """
        ...

    @overload
    def defineInt(self, name: unicode, defaultValue: int) -> docking.widgets.values.IntValue:
        """
        Defines a value of type Integer with an initial value.
        @param name the name for this value
        @param defaultValue the initial value
        @return the new IntValue that was defined
        """
        ...

    def defineLanguage(self, name: unicode, defaultValue: ghidra.program.model.lang.LanguageCompilerSpecPair) -> ghidra.features.base.values.LanguageValue:
        """
        Defines a value of type LanguageCompilerSpecPair (folders in a Ghidra project).
        @param name the name for this value
        @param defaultValue the initial value (can be null)
        @return the new ProjectFolderValue that was defined
        """
        ...

    @overload
    def defineLong(self, name: unicode) -> docking.widgets.values.LongValue:
        """
        Defines a value of type Long with an initial value.
        @param name the name for this value
        @return the new LongValue that was defined
        """
        ...

    @overload
    def defineLong(self, name: unicode, defaultValue: long) -> docking.widgets.values.LongValue:
        """
        Defines a value of type Long with an initial value.
        @param name the name for this value
        @param defaultValue the initial value
        @return the new LongValue that was defined
        """
        ...

    @overload
    def defineProgram(self, name: unicode) -> ghidra.features.base.values.ProgramFileValue:
        """
        Defines a value of type Program file.
        @param name the name for this value
        @return the new ProgramFileValue defined
        """
        ...

    @overload
    def defineProgram(self, name: unicode, startPath: unicode) -> ghidra.features.base.values.ProgramFileValue:
        """
        Defines a value of type Program file.
        @param name the name for this value
        @param startPath the starting folder to display when picking programs from the chooser
        @return the new ProgramFileValue that was defined
        """
        ...

    @overload
    def defineProjectFile(self, name: unicode) -> ghidra.features.base.values.ProjectFileValue:
        """
        Defines a value of type DomainFile (files in a Ghidra project).
        @param name the name for this value
        @return the new ProjectFileValue that was defined
        """
        ...

    @overload
    def defineProjectFile(self, name: unicode, startingPath: unicode) -> ghidra.features.base.values.ProjectFileValue:
        """
        Defines a value of type DomainFile (files in a Ghidra project).
        @param name the name for this value
        @param startingPath the initial folder path for the chooser widget
        @return the new ProjectFileValue that was defined
        """
        ...

    @overload
    def defineProjectFolder(self, name: unicode) -> ghidra.features.base.values.ProjectFolderValue:
        """
        Defines a value of type DomainFolder (folders in a Ghidra project).
        @param name the name for this value
        @return the new ProjectFolderValue that was defined
        """
        ...

    @overload
    def defineProjectFolder(self, name: unicode, defaultValuePath: unicode) -> ghidra.features.base.values.ProjectFolderValue:
        """
        Defines a value of type DomainFolder (files in a Ghidra project).
        @param name the name for this value
        @param defaultValuePath the path for the initial value (can be null)
        @return the new ProjectFolderValue that was defined
        """
        ...

    @overload
    def defineString(self, name: unicode) -> docking.widgets.values.StringValue:
        """
        Defines a value of type String.
        @param name the name for this value
        @return the new StringValue that was defined
        """
        ...

    @overload
    def defineString(self, name: unicode, defaultValue: unicode) -> docking.widgets.values.StringValue:
        """
        Defines a value of type String with an optional initial value
        @param name the name for this value
        @param defaultValue the initial value (can be null)
        @return the new StringValue that was defined
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAbstractValue(self, name: unicode) -> docking.widgets.values.AbstractValue:
        """
        Returns the AbstractValue for the given value name.
        @param name the name for which to get the AbstractValue
        @return the AbstractValue for the given value name.
        """
        ...

    def getAddress(self, name: unicode) -> ghidra.program.model.address.Address:
        """
        Gets the {@link Address} value for the given name.
        @param name the name of a previously defined Address value
        @return the Address
        @throws IllegalArgumentException if the name hasn't been defined as an Address type
        """
        ...

    def getBoolean(self, name: unicode) -> bool:
        """
        Gets the boolean value for the given name.
        @param name the name of a previously defined boolean value
        @return the boolean value
        @throws IllegalArgumentException if the name hasn't been defined as a boolean type
        """
        ...

    def getChoice(self, name: unicode) -> unicode:
        """
        Gets the Choice (String) value for the given name. The value will be either null or one of
         the strings that were defined as valid choices.
        @param name the name of a previously defined Choice value
        @return the Choice value
        @throws IllegalArgumentException if the name hasn't been defined as a Choice type
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDouble(self, name: unicode) -> float:
        """
        Gets the double value for the given name.
        @param name the name of a previously defined double value
        @return the double value
        @throws IllegalArgumentException if the name hasn't been defined as a double type
        """
        ...

    def getFile(self, name: unicode) -> java.io.File:
        """
        Gets the {@link File} value for the given name.
        @param name the name of a previously defined File value
        @return the File value
        @throws IllegalArgumentException if the name hasn't been defined as a File type
        """
        ...

    def getInt(self, name: unicode) -> int:
        """
        Gets the int value for the given name.
        @param name the name of a previously defined int value
        @return the int value
        @throws IllegalArgumentException if the name hasn't been defined as a int type
        """
        ...

    def getLanguage(self, name: unicode) -> ghidra.program.model.lang.LanguageCompilerSpecPair:
        """
        Gets the Language ({@link LanguageCompilerSpecPair}) value for the given name.
        @param name the name of a previously defined language value
        @return the language value
        @throws IllegalArgumentException if the name hasn't been defined as a language type
        """
        ...

    def getLong(self, name: unicode) -> long:
        """
        Gets the long value for the given name.
        @param name the name of a previously defined long value
        @return the long value
        @throws IllegalArgumentException if the name hasn't been defined as a long type
        """
        ...

    def getProgram(self, name: unicode, consumer: object, tool: docking.Tool, upgradeIfNeeded: bool) -> ghidra.program.model.listing.Program:
        """
        Gets (opens) the {@link Program} value for the given name. If the program is already open,
         then the consumer will be added to the program. The caller of this method is responsible
         for calling {@link Program#release(Object)} with the same consumer when it is done using this
         program. Program are only closed after all consumers are released. If multiple calls
         are made to this method, then the consumer will be added multiple times and must be released
         multiple times.
         <P>
         The consumer can be any object, but since the consumer's purpose is to keep the program open 
         while some object is using it, the object itself is typically passed in as
         the consumer. For example, when used in a script, passing in the java keyword "this" as the
         consumer will make the script itself the consumer.
         <P>
        @param name the name of a previously defined program value
        @param consumer the consumer to be used to open the program
        @param tool if non-null, the program will also be opened in the given tool. Note: the
         program will only be added to the tool once even if this method is called multiple times.
        @param upgradeIfNeeded if true, program will be upgraded if needed and possible. If false,
         the program will only be upgraded after first prompting the user. In headless mode, it will
         attempt to upgrade only if the parameter is true.
        @return an opened program with the given consumer for the selected domain file or null if
         no program was selected.
        @throws VersionException if the Program is out-of-date from the version of GHIDRA and an 
         upgrade was not been performed. In non-headless mode, the user will have already been
         notified via a popup dialog.
         current Ghidra Program version.
        @throws IOException if there is an error accessing the Program's DomainObject
        @throws CancelledException if the operation is cancelled
        @throws IllegalArgumentException if the name hasn't been defined as a project folder type
        """
        ...

    def getProjectFile(self, name: unicode) -> ghidra.framework.model.DomainFile:
        """
        Gets the project file ({@link DomainFile}) value for the given name.
        @param name the name of a previously defined project file value
        @return the project file value
        @throws IllegalArgumentException if the name hasn't been defined as a project file type
        """
        ...

    def getProjectFolder(self, name: unicode) -> ghidra.framework.model.DomainFolder:
        """
        Gets the project folder ({@link DomainFolder}) value for the given name.
        @param name the name of a previously defined project folder value
        @return the project folder value
        @throws IllegalArgumentException if the name hasn't been defined as a project folder type
        """
        ...

    def getString(self, name: unicode) -> unicode:
        """
        Gets the String value for the given name.
        @param name the name of a previously defined String value
        @return the String value
        @throws IllegalArgumentException if the name hasn't been defined as a String type
        """
        ...

    def getValues(self) -> java.util.Collection:
        """
        Returns a collection of the AbstractValues defined in this ValuesMap.
        @return a collection of the AbstractValues defined in this ValuesMap.
        """
        ...

    def hasValue(self, name: unicode) -> bool:
        """
        Returns true if the value defined for the given name has a non-null value.
        @param name the name of the value
        @return true if the value defined for the given name has a non-null value.
        """
        ...

    def hashCode(self) -> int: ...

    def isDefined(self, name: unicode) -> bool:
        """
        Returns true if there is a defined value for the given name.
        @param name the name of the value to check for
        @return true if there is a defined value for the given name.
        """
        ...

    def isValid(self, listener: ghidra.util.StatusListener) -> bool:
        """
        The call to validate the data using the {@link ValuesMapValidator} set in the
         {@link #setValidator(ValuesMapValidator)} method. If no validator has been set,
         this method will return true.
        @param listener The {@link StatusListener} for reporting an error message.
        @return true if the validator passes or no validator has been set.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAddress(self, name: unicode, address: ghidra.program.model.address.Address) -> None:
        """
        Sets the address value for the given name.
        @param name the name of the Address value that was previously defined
        @param address the address to set as the value
        @throws IllegalArgumentException if the name hasn't been defined as an Address type
        """
        ...

    def setBoolean(self, name: unicode, value: bool) -> None:
        """
        Sets the boolean value for the given name.
        @param name the name of the boolean value that was previously defined
        @param value the boolean to set as the value
        @throws IllegalArgumentException if the name hasn't been defined as a boolean type
        """
        ...

    def setChoice(self, name: unicode, choice: unicode) -> None:
        """
        Sets the Choice (String) value for the given name.
        @param name the name of the Choice value that was previously defined
        @param choice the string to set as the value. This String must be one of the defined choices
        @throws IllegalArgumentException if the name hasn't been defined as a choice type
        """
        ...

    def setDouble(self, name: unicode, value: float) -> None:
        """
        Sets the double value for the given name.
        @param name the name of the double value that was previously defined
        @param value the double to set as the value
        @throws IllegalArgumentException if the name hasn't been defined as a double type
        """
        ...

    def setFile(self, name: unicode, value: java.io.File) -> None:
        """
        Sets the {@link File} value for the given name.
        @param name the name of the File value that was previously defined
        @param value the File to set as the value
        @throws IllegalArgumentException if the name hasn't been defined as a File type
        """
        ...

    def setInt(self, name: unicode, value: int) -> None:
        """
        Sets the int value for the given name.
        @param name the name of the int value that was previously defined
        @param value the int to set as the value
        @throws IllegalArgumentException if the name hasn't been defined as a int type
        """
        ...

    def setLanguage(self, name: unicode, value: ghidra.program.model.lang.LanguageCompilerSpecPair) -> None:
        """
        Sets the Language ({@link LanguageCompilerSpecPair}) value for the given name.
        @param name the name of the Language value that was previously defined
        @param value the Language to set as the value
        @throws IllegalArgumentException if the name hasn't been defined as a Language type
        """
        ...

    def setLong(self, name: unicode, value: long) -> None:
        """
        Sets the long value for the given name.
        @param name the name of the long value that was previously defined
        @param value the long to set as the value
        @throws IllegalArgumentException if the name hasn't been defined as a long type
        """
        ...

    def setProgram(self, name: unicode, program: ghidra.program.model.listing.Program) -> None:
        """
        Sets the {@link Program} value for the given name.
        @param name the name of the Program value that was previously defined
        @param program the Program to set as the value
        @throws IllegalArgumentException if the name hasn't been defined as a Program type
        """
        ...

    def setProjectFile(self, name: unicode, file: ghidra.framework.model.DomainFile) -> None:
        """
        Sets the project file {@link DomainFile} value for the given name.
        @param name the name of the project file value that was previously defined
        @param file the project file to set as the value
        @throws IllegalArgumentException if the name hasn't been defined as a project file type
        """
        ...

    def setProjectFolder(self, name: unicode, folder: ghidra.framework.model.DomainFolder) -> None:
        """
        Sets the project folder {@link DomainFolder} value for the given name.
        @param name the name of the project folder value that was previously defined
        @param folder the project folder to set as the value
        @throws IllegalArgumentException if the name hasn't been defined as a project folder type
        """
        ...

    def setString(self, name: unicode, value: unicode) -> None:
        """
        Sets the String value for the given name.
        @param name the name of the String value that was previously defined
        @param value the String to set as the value
        @throws IllegalArgumentException if the name hasn't been defined as a String type
        """
        ...

    def setTaskMonitor(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Sets a task monitor to be used when opening programs. Otherwise, {@link TaskMonitor#DUMMY} is
         used.
        @param monitor the TaskMonitor to use for opening programs
        """
        ...

    def setValidator(self, validator: docking.widgets.values.ValuesMapValidator) -> None:
        """
        Sets a {@link ValuesMapValidator}. If set, this will be called when the user presses the 
         "Ok" button on the {@link ValuesMapDialog}. If the validator passes (returns true), then 
         the dialog will close and return the user values. Otherwise, the dialog will display the
         error message (via the {@link StatusListener} in the 
         {@link ValuesMapValidator#validate(GValuesMap, StatusListener)} call) and remain open.
        @param validator the validator to be called before returning from the dialog
        """
        ...

    def toString(self) -> unicode: ...

    def updateFromComponents(self) -> None:
        """
        Updates each value in this ValuesMap from its corresponding JComponent.
        @throws ValuesMapParseException if any value encountered an error trying to update its
         value from the editor component.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def taskMonitor(self) -> None: ...  # No getter available.

    @taskMonitor.setter
    def taskMonitor(self, value: ghidra.util.task.TaskMonitor) -> None: ...