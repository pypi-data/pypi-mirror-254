import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.util.task
import java.lang


class ApplyFunctionSignatureCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    Command to create apply a function signature at an address.
    """





    @overload
    def __init__(self, entry: ghidra.program.model.address.Address, signature: ghidra.program.model.listing.FunctionSignature, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for applying a signature to an existing function.
         <br>
         Only a function with a default name will be renamed to the function signature's name
         (see {@link FunctionRenameOption#RENAME_IF_DEFAULT}).
         <br>
         All datatypes will be resolved using the 
         {@link DataTypeConflictHandler#DEFAULT_HANDLER default conflict handler}.
        @param entry entry point address for the function to be created.
        @param signature function signature to apply
        @param source the source of this function signature
        """
        ...

    @overload
    def __init__(self, entry: ghidra.program.model.address.Address, signature: ghidra.program.model.listing.FunctionSignature, source: ghidra.program.model.symbol.SourceType, preserveCallingConvention: bool, forceSetName: bool):
        """
        Constructs a new command for applying a signature to an existing function.
         <br>
         All datatypes will be resolved using the 
         {@link DataTypeConflictHandler#DEFAULT_HANDLER default conflict handler}.
        @param entry entry point address for the function to be created.
        @param signature function signature to apply
        @param source the source of this function signature
        @param preserveCallingConvention if true the function calling convention will not be changed
        @param forceSetName true if name of the function should be set to the name, otherwise name
                             will only be set name if currently default (e.g., FUN_1234). A value of 
                             true is equivalent to {@link FunctionRenameOption#RENAME}, while a value
                             of false is equivalent to {@link FunctionRenameOption#RENAME_IF_DEFAULT}.
        """
        ...

    @overload
    def __init__(self, entry: ghidra.program.model.address.Address, signature: ghidra.program.model.listing.FunctionSignature, source: ghidra.program.model.symbol.SourceType, preserveCallingConvention: bool, functionRenameOption: ghidra.app.cmd.function.FunctionRenameOption):
        """
        Constructs a new command for applying a signature to an existing function.
         <br>
         All datatypes will be resolved using the 
         {@link DataTypeConflictHandler#DEFAULT_HANDLER default conflict handler}.
        @param entry entry point address for the function to be created.
        @param signature function signature to apply
        @param source the source of this function signature
        @param preserveCallingConvention if true the function calling convention will not be changed
        @param functionRenameOption controls renaming of the function using the name from the 
                               specified function signature.
        """
        ...

    @overload
    def __init__(self, entry: ghidra.program.model.address.Address, signature: ghidra.program.model.listing.FunctionSignature, source: ghidra.program.model.symbol.SourceType, preserveCallingConvention: bool, applyEmptyComposites: bool, conflictHandler: ghidra.program.model.data.DataTypeConflictHandler, functionRenameOption: ghidra.app.cmd.function.FunctionRenameOption):
        """
        Constructs a new command for applying a signature to an existing function.
        @param entry entry point address for the function to be created.
        @param signature function signature to apply
        @param source the source of this function signature
        @param preserveCallingConvention if true the function calling convention will not be changed
        @param applyEmptyComposites If true, applied composites will be resolved without their
                                respective components if the type does not already exist in the 
                                destination datatype manager.  If false, normal type resolution 
                                will occur.
        @param conflictHandler conflict handler to be used when applying datatypes to the
                                destination program.  If this value is not null or 
                                {@link DataTypeConflictHandler#DEFAULT_HANDLER} the datatypes will be 
                                resolved prior to updating the destinationFunction.  This handler
                                will provide some control over how applied datatype are handled when 
                                they conflict with existing datatypes. 
                                See {@link DataTypeConflictHandler} which provides some predefined
                                handlers.
        @param functionRenameOption controls renaming of the function using the name from the 
                                specified function signature.
        """
        ...



    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    def canCancel(self) -> bool:
        """
        Check if the command can be canceled.
        @return true if this command can be canceled
        """
        ...

    def dispose(self) -> None:
        """
        Called when this command is going to be removed/canceled without
         running it.  This gives the command the opportunity to free any
         temporary resources it has hold of.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getStatusMsg(self) -> unicode: ...

    def hasProgress(self) -> bool:
        """
        Check if the command provides progress information.
        @return true if the command shows progress information
        """
        ...

    def hashCode(self) -> int: ...

    def isModal(self) -> bool:
        """
        Check if the command requires the monitor to be modal.  No other
         command should be allowed, and the GUI will be locked.
        @return true if no other operation should be going on while this
         command is in progress.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def taskCompleted(self) -> None:
        """
        Called when the task monitor is completely done with indicating progress.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

