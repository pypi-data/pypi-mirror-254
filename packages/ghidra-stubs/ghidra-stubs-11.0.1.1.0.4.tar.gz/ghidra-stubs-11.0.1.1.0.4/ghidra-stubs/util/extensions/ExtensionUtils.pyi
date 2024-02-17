import generic.jar
import ghidra.util.extensions
import ghidra.util.task
import java.io
import java.lang
import java.util


class ExtensionUtils(object):
    """
    Utilities for finding extensions.
 
     Extension searching is cached.  Use #reload() to update the cache.
    """

    PROPERTIES_FILE_NAME: unicode
    PROPERTIES_FILE_NAME_UNINSTALLED: unicode



    def __init__(self): ...



    @staticmethod
    def clearCache() -> None:
        """
        Clears any cached extensions.
        """
        ...

    @staticmethod
    def createExtensionDetailsFromArchive(resourceFile: generic.jar.ResourceFile) -> ghidra.util.extensions.ExtensionDetails: ...

    @staticmethod
    def createExtensionFromProperties(file: java.io.File) -> ghidra.util.extensions.ExtensionDetails: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getActiveInstalledExtensions() -> java.util.Set: ...

    @staticmethod
    def getAllInstalledExtensions() -> ghidra.util.extensions.Extensions: ...

    @staticmethod
    def getArchiveExtensions() -> java.util.Set:
        """
        Returns all archive extensions. These are all the extensions found in
         {@link ApplicationLayout#getExtensionArchiveDir}.   This are added to an installation as
         part of the build processes.
         <p>
         Archived extensions may be zip files and directories.
        @return set of archive extensions
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getExtension(path: unicode) -> ghidra.util.extensions.ExtensionDetails: ...

    @overload
    @staticmethod
    def getExtension(file: java.io.File, quiet: bool) -> ghidra.util.extensions.ExtensionDetails: ...

    @staticmethod
    def getInstalledExtensions() -> java.util.Set:
        """
        Returns all installed extensions. These are all the extensions found in
         {@link ApplicationLayout#getExtensionInstallationDirs}.
        @return set of installed extensions
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def initializeExtensions() -> None:
        """
        Performs extension maintenance.  This should be called at startup, before any plugins or
         extension points are loaded.
        """
        ...

    @staticmethod
    def install(extension: ghidra.util.extensions.ExtensionDetails, file: java.io.File, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    @staticmethod
    def isExtension(file: java.io.File) -> bool:
        """
        Returns true if the given file or directory is a valid ghidra extension.
         <p>
         Note: This means that the zip or directory contains an extension.properties file.
        @param file the zip or directory to inspect
        @return true if the given file represents a valid extension
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def reload() -> None:
        """
        Clears any cached extensions and searches for extensions.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

