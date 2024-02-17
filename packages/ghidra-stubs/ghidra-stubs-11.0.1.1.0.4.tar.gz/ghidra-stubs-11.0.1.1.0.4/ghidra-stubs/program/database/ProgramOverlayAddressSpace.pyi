import ghidra.program.model.address
import java.lang


class ProgramOverlayAddressSpace(ghidra.program.model.address.OverlayAddressSpace):




    def __init__(self, key: long, overlayName: unicode, baseSpace: ghidra.program.model.address.AddressSpace, unique: int, overlayRegionSupplier: ghidra.program.database.OverlayRegionSupplier, factory: ghidra.program.database.ProgramAddressFactory):
        """
        @param key DB record key
        @param overlayName current overlay name
        @param baseSpace base address space (type should be restricted as neccessary by caller)
        @param unique assigned unique ID
        @param overlayRegionSupplier callback handler which supplies the defined address set 
         for a specified overlay address space.
        @param factory used to determine a suitable ordered overlay ordered-key used for
         {@link #equals(Object)} and {@link #compareTo(AddressSpace)}.
        @throws DuplicateNameException if specified name duplicates an existing address space name
        """
        ...



    def add(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    @overload
    def addNoWrap(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    @overload
    def addNoWrap(self, addr: ghidra.program.model.address.GenericAddress, displacement: long) -> ghidra.program.model.address.Address: ...

    def addWrap(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    def addWrapSpace(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    @overload
    def compareTo(self, space: ghidra.program.model.address.AddressSpace) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def contains(self, offset: long) -> bool: ...

    def equals(self, obj: object) -> bool: ...

    @overload
    def getAddress(self, offset: long) -> ghidra.program.model.address.Address: ...

    @overload
    def getAddress(self, addrString: unicode) -> ghidra.program.model.address.Address: ...

    @overload
    def getAddress(self, offset: long, isAddressableWordOffset: bool) -> ghidra.program.model.address.Address: ...

    @overload
    def getAddress(self, addrString: unicode, caseSensitive: bool) -> ghidra.program.model.address.Address: ...

    def getAddressInThisSpaceOnly(self, offset: long) -> ghidra.program.model.address.Address: ...

    def getAddressableUnitSize(self) -> int: ...

    def getAddressableWordOffset(self, byteOffset: long) -> long: ...

    def getBaseSpaceID(self) -> int:
        """
        @return the ID of the address space underlying this space
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getKey(self) -> long:
        """
        Get the DB record key used to store this overlay specification.
         This is intended to be used internally to reconcile address spaces only.
        @return DB record key
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getName(self) -> unicode: ...

    def getOrderedKey(self) -> unicode:
        """
        Get the ordered key assigned to this overlay address space instance  This value is used
         when performing {@link #equals(Object)} and {@link #compareTo(AddressSpace)}
         operations.
         <p>
         If this value does not have its optimal value (i.e., same as address space name), the 
         associated {@link AddressFactory} should report a 
         {@link AddressFactory#hasStaleOverlayCondition() stale overlay condition}.
        @return instance ordered key
        """
        ...

    def getOverlayAddress(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def getOverlayAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    def getOverlayedSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        Get the overlayed (i.e., underlying) base space associated with this overlay space.
        @return overlayed base space.
        """
        ...

    def getPhysicalSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    def getPointerSize(self) -> int: ...

    def getSize(self) -> int: ...

    def getSpaceID(self) -> int: ...

    def getTruncatedAddress(self, offset: long, isAddressableWordOffset: bool) -> ghidra.program.model.address.Address: ...

    def getType(self) -> int: ...

    def getUnique(self) -> int:
        """
        Returns the unique id value for this space.
        """
        ...

    def hasMappedRegisters(self) -> bool: ...

    def hasSignedOffset(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isConstantSpace(self) -> bool: ...

    def isExternalSpace(self) -> bool: ...

    def isHashSpace(self) -> bool: ...

    def isLoadedMemorySpace(self) -> bool: ...

    def isMemorySpace(self) -> bool: ...

    def isNonLoadedMemorySpace(self) -> bool: ...

    def isOverlaySpace(self) -> bool: ...

    def isRegisterSpace(self) -> bool: ...

    def isStackSpace(self) -> bool: ...

    def isSuccessor(self, addr1: ghidra.program.model.address.Address, addr2: ghidra.program.model.address.Address) -> bool: ...

    def isUniqueSpace(self) -> bool: ...

    @staticmethod
    def isValidName(__a0: unicode) -> bool: ...

    def isValidRange(self, byteOffset: long, length: long) -> bool: ...

    def isVariableSpace(self) -> bool: ...

    def makeValidOffset(self, offset: long) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setHasMappedRegisters(self, hasRegisters: bool) -> None:
        """
        Tag this memory space as having memory mapped registers
        @param hasRegisters true if it has registers, false otherwise
        """
        ...

    def setName(self, name: unicode) -> None:
        """
        Method to support renaming an overlay address space instance.  Intended for internal use only.
        @param name new overlay space name
        """
        ...

    def setShowSpaceName(self, b: bool) -> None: ...

    def showSpaceName(self) -> bool: ...

    @overload
    def subtract(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    @overload
    def subtract(self, addr1: ghidra.program.model.address.Address, addr2: ghidra.program.model.address.Address) -> long: ...

    def subtractNoWrap(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    def subtractWrap(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    def subtractWrapSpace(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    def toString(self) -> unicode: ...

    @overload
    def translateAddress(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        If the given address is outside the overlay block, then the address is tranlated to an
         address in the base space with the same offset, otherwise (if the address exists in the
         overlay block), it is returned
        @param addr the address to translate to the base space if it is outside the overlay block
        @return either the given address if it is contained in the overlay memory block or an address
                 in the base space with the same offset as the given address.
        """
        ...

    @overload
    def translateAddress(self, addr: ghidra.program.model.address.Address, forceTranslation: bool) -> ghidra.program.model.address.Address:
        """
        Tranlated an overlay-space address (addr, which may exceed the bounds of the overlay space)
         to an address in the base space with the same offset. If forceTranslation is false and addr
         is contained within the overlay-space the original addr is returned.
        @param addr the address to translate to the base space
        @param forceTranslation if true addr will be translated even if addr falls within the bounds
                    of this overlay-space.
        @return either the given address if it is contained in the overlay memory block or an address
                 in the base space with the same offset as the given address.
        """
        ...

    def truncateAddressableWordOffset(self, wordOffset: long) -> long: ...

    def truncateOffset(self, offset: long) -> long: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def key(self) -> long: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def overlayAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...