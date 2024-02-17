from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.pcode.emu
import ghidra.pcode.emu.PcodeMachine
import ghidra.pcode.exec
import ghidra.program.model.address
import java.lang
import java.util


class PcodeMachine(object):
    """
    A machine which execute p-code on state of an abstract type
    """






    class AccessKind(java.lang.Enum):
        R: ghidra.pcode.emu.PcodeMachine.AccessKind = R
        RW: ghidra.pcode.emu.PcodeMachine.AccessKind = RW
        W: ghidra.pcode.emu.PcodeMachine.AccessKind = W







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def describeConstable(self) -> java.util.Optional: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        def trapsRead(self) -> bool: ...

        def trapsWrite(self) -> bool: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.pcode.emu.PcodeMachine.AccessKind: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.pcode.emu.PcodeMachine.AccessKind]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class SwiMode(java.lang.Enum):
        ACTIVE: ghidra.pcode.emu.PcodeMachine.SwiMode = ACTIVE
        IGNORE_ALL: ghidra.pcode.emu.PcodeMachine.SwiMode = IGNORE_ALL
        IGNORE_STEP: ghidra.pcode.emu.PcodeMachine.SwiMode = IGNORE_STEP







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def describeConstable(self) -> java.util.Optional: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.pcode.emu.PcodeMachine.SwiMode: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.pcode.emu.PcodeMachine.SwiMode]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    def addAccessBreakpoint(self, range: ghidra.program.model.address.AddressRange, kind: ghidra.pcode.emu.PcodeMachine.AccessKind) -> None:
        """
        Add an access breakpoint over the given range
 
         <p>
         Access breakpoints are implemented out of band, without modification to the emulated image.
         The breakpoints are only effective for p-code {@link PcodeOp#LOAD} and {@link PcodeOp#STORE}
         operations with concrete offsets. Thus, an operation that refers directly to a memory
         address, e.g., a memory-mapped register, will not be trapped. Similarly, access breakpoints
         on registers or unique variables will not work. Access to an abstract offset that cannot be
         made concrete, i.e., via {@link PcodeArithmetic#toConcrete(Object, Purpose)} cannot be
         trapped. To interrupt on direct and/or abstract accesses, consider wrapping the relevant
         state and/or overriding {@link PcodeExecutorStatePiece#getVar(Varnode, Reason)} and related.
         For accesses to abstract offsets, consider overriding
         {@link AbstractPcodeMachine#checkLoad(AddressSpace, Object, int)} and/or
         {@link AbstractPcodeMachine#checkStore(AddressSpace, Object, int)} instead.
 
         <p>
         A breakpoint's range cannot cross more than one page boundary. Pages are 4096 bytes each.
         This allows implementations to optimize checking for breakpoints. If a breakpoint does not
         follow this rule, the behavior is undefined. Breakpoints may overlap, but currently no
         indication is given as to which breakpoint interrupted emulation.
 
         <p>
         No synchronization is provided on the internal breakpoint storage. Clients should ensure the
         machine is not executing when adding breakpoints. Additionally, the client must ensure only
         one thread is adding breakpoints to the machine at a time.
        @param range the address range to trap
        @param kind the kind of access to trap
        """
        ...

    def addBreakpoint(self, address: ghidra.program.model.address.Address, sleighCondition: unicode) -> None:
        """
        Add a conditional execution breakpoint at the given address
 
         <p>
         Breakpoints are implemented at the p-code level using an inject, without modification to the
         emulated image. As such, it cannot coexist with another inject. A client needing to break
         during an inject must use {@link PcodeEmulationLibrary#emu_swi()} in the injected Sleigh.
 
         <p>
         No synchronization is provided on the internal breakpoint storage. Clients should ensure the
         machine is not executing when adding breakpoints. Additionally, the client must ensure only
         one thread is adding breakpoints to the machine at a time.
        @param address the address at which to break
        @param sleighCondition a Sleigh expression which controls the breakpoint
        """
        ...

    def clearAccessBreakpoints(self) -> None:
        """
        Remove all access breakpoints from this machine
        """
        ...

    def clearAllInjects(self) -> None:
        """
        Remove all injects from this machine
 
         <p>
         This will clear execution breakpoints, but not access breakpoints. See
         {@link #clearAccessBreakpoints()}.
        """
        ...

    def clearInject(self, address: ghidra.program.model.address.Address) -> None:
        """
        Remove the inject, if present, at the given address
        @param address the address to clear
        """
        ...

    def compileSleigh(self, sourceName: unicode, source: unicode) -> ghidra.pcode.exec.PcodeProgram:
        """
        Compile the given Sleigh code for execution by a thread of this machine
 
         <p>
         This links in the userop library given at construction time and those defining the emulation
         userops, e.g., {@code emu_swi}.
        @param sourceName a user-defined source name for the resulting "program"
        @param source the Sleigh source
        @return the compiled program
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAllThreads(self) -> java.util.Collection:
        """
        Collect all threads present in the machine
        @return the collection of threads
        """
        ...

    def getArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic:
        """
        Get the arithmetic applied by the machine
        @return the arithmetic
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLanguage(self) -> ghidra.app.plugin.processors.sleigh.SleighLanguage:
        """
        Get the machine's Sleigh language (processor model)
        @return the language
        """
        ...

    def getSharedState(self) -> ghidra.pcode.exec.PcodeExecutorState:
        """
        Get the machine's shared (memory) state
 
         <p>
         The returned state will may throw {@link IllegalArgumentException} if the client requests
         register values of it. This state is shared among all threads in this machine.
        @return the memory state
        """
        ...

    def getSoftwareInterruptMode(self) -> ghidra.pcode.emu.PcodeMachine.SwiMode:
        """
        Get the current software interrupt mode
        @return the mode
        """
        ...

    def getStubUseropLibrary(self) -> ghidra.pcode.exec.PcodeUseropLibrary:
        """
        Get a userop library which at least declares all userops available in each thread userop
         library.
 
         <p>
         Thread userop libraries may have more userops than are defined in the machine's userop
         library. However, to compile Sleigh programs linked to thread libraries, the thread's userops
         must be known to the compiler. The stub library will name all userops common among the
         threads, even if their definitions vary. <b>WARNING:</b> The stub library is not required to
         provide implementations of the userops. Often they will throw exceptions, so do not attempt
         to use the returned library in an executor.
        @return the stub library
        """
        ...

    def getThread(self, name: unicode, createIfAbsent: bool) -> ghidra.pcode.emu.PcodeThread:
        """
        Get the thread, if present, with the given name
        @param name the name
        @param createIfAbsent create a new thread if the thread does not already exist
        @return the thread, or {@code null} if absent and not created
        """
        ...

    def getUseropLibrary(self) -> ghidra.pcode.exec.PcodeUseropLibrary:
        """
        Get the userop library common to all threads in the machine.
 
         <p>
         Note that threads may have larger libraries, but each contains all the userops in this
         library.
        @return the userop library
        """
        ...

    def hashCode(self) -> int: ...

    def inject(self, address: ghidra.program.model.address.Address, source: unicode) -> None:
        """
        Override the p-code at the given address with the given Sleigh source
 
         <p>
         This will attempt to compile the given source against this machine's userop library and then
         inject it at the given address. The resulting p-code <em>replaces</em> that which would be
         executed by decoding the instruction at the given address. The means the machine will not
         decode, nor advance its counter, unless the Sleigh causes it. In most cases, the Sleigh will
         call {@link PcodeEmulationLibrary#emu_exec_decoded()} to cause the machine to decode and
         execute the overridden instruction.
 
         <p>
         Each address can have at most a single inject. If there is already one present, it is
         replaced and the old inject completely forgotten. The injector does not support chaining or
         double-wrapping, etc.
 
         <p>
         No synchronization is provided on the internal injection storage. Clients should ensure the
         machine is not executing when injecting p-code. Additionally, the client must ensure only one
         thread is injecting p-code to the machine at a time.
        @param address the address to inject at
        @param source the Sleigh source to compile and inject
        """
        ...

    def isSuspended(self) -> bool:
        """
        Check the suspension state of the machine
        @see PcodeThread#isSuspended()
        """
        ...

    @overload
    def newThread(self) -> ghidra.pcode.emu.PcodeThread:
        """
        Create a new thread with a default name in this machine
        @return the new thread
        """
        ...

    @overload
    def newThread(self, name: unicode) -> ghidra.pcode.emu.PcodeThread:
        """
        Create a new thread with the given name in this machine
        @param name the name
        @return the new thread
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setSoftwareInterruptMode(self, mode: ghidra.pcode.emu.PcodeMachine.SwiMode) -> None:
        """
        Change the efficacy of p-code breakpoints
 
         <p>
         This is used to prevent breakpoints from interrupting at inappropriate times, e.g., upon
         continuing from a breakpoint.
        @param mode the new mode
        """
        ...

    def setSuspended(self, suspended: bool) -> None:
        """
        Set the suspension state of the machine
        @see PcodeThread#setSuspended(boolean)
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
    def allThreads(self) -> java.util.Collection: ...

    @property
    def arithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    @property
    def language(self) -> ghidra.app.plugin.processors.sleigh.SleighLanguage: ...

    @property
    def sharedState(self) -> ghidra.pcode.exec.PcodeExecutorState: ...

    @property
    def softwareInterruptMode(self) -> ghidra.pcode.emu.PcodeMachine.SwiMode: ...

    @softwareInterruptMode.setter
    def softwareInterruptMode(self, value: ghidra.pcode.emu.PcodeMachine.SwiMode) -> None: ...

    @property
    def stubUseropLibrary(self) -> ghidra.pcode.exec.PcodeUseropLibrary: ...

    @property
    def suspended(self) -> bool: ...

    @suspended.setter
    def suspended(self, value: bool) -> None: ...

    @property
    def useropLibrary(self) -> ghidra.pcode.exec.PcodeUseropLibrary: ...