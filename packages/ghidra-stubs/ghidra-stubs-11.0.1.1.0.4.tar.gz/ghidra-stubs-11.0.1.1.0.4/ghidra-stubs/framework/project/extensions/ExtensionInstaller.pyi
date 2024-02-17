import ghidra.util.extensions
import java.io
import java.lang


class ExtensionInstaller(object):
    """
    Utility class for managing Ghidra Extensions.
 
     Extensions are defined as any archive or folder that contains an extension.properties
     file. This properties file can contain the following attributes:
 
     name (required)
     description
     author
     createdOn (format: MM/dd/yyyy)
     version
 

 
     Extensions may be installed/uninstalled by users at runtime, using the
     ExtensionTableProvider. Installation consists of unzipping the extension archive to an
     installation folder, currently {ghidra user settings dir}/Extensions. To uninstall,
     the unpacked folder is simply removed.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def install(file: java.io.File) -> bool:
        """
        Installs the given extension file. This can be either an archive (zip) or a directory that
         contains an extension.properties file.
        @param file the extension to install
        @return true if the extension was successfully installed
        """
        ...

    @staticmethod
    def installExtensionFromArchive(extension: ghidra.util.extensions.ExtensionDetails) -> bool:
        """
        Installs the given extension from its declared archive path
        @param extension the extension
        @return true if successful
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

