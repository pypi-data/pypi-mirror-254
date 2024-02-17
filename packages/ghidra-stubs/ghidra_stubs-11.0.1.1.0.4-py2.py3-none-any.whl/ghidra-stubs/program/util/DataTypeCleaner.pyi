import ghidra.program.model.data
import java.io
import java.lang


class DataTypeCleaner(object, java.io.Closeable):
    """
    DataTypeCleaner provides a convenient way to clean composite definitions which may be
     included within a complex datatype which was derived from an source unrelated to a target
     DataTypeManager.  The cleaning process entails clearing all details associated with
     all composites other than their description which may be present.  There is also an option
     to retain those composites which are already defined within the target.
 
     All datatypes and their referenced datatypes will be accumulated and possibly re-used across
     multiple invocations of the #clean(DataType) method.  It is important that this instance 
     be #close() when instance and any resulting DataType is no longer in use.
    """





    def __init__(self, targetDtm: ghidra.program.model.data.DataTypeManager, retainExistingComposites: bool):
        """
        Consruct a {@link DataTypeCleaner} instance.  The caller must ensure that this instance
         is {@link #close() closed} when instance and any resulting {@link DataType} is no longer in
         use.
        @param targetDtm target datatype manager
        @param retainExistingComposites if true all composites will be checked against the 
         {@code targetDtm} and retained if it already exists, otherwise all composites will be
         cleaned.
        """
        ...



    def clean(self, dt: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType:
        """
        Clean the specified datatype
        @param dt datatype
        @return clean datatype
        """
        ...

    def close(self) -> None: ...

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

