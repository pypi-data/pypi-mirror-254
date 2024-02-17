import ghidra.pcode.emu
import ghidra.pcode.emu.DefaultPcodeThread
import ghidra.pcode.emu.auxiliary
import ghidra.pcode.exec
import ghidra.program.model.lang
import java.lang


class AuxEmulatorPartsFactory(object):
    """
    An auxiliary emulator parts factory for stand-alone emulation

 
     This can manufacture all the parts needed for a stand-alone emulator with concrete and some
     implementation-defined auxiliary state. More capable emulators may also use many of these parts.
     Usually, the additional capabilities deal with how state is loaded and stored or otherwise made
     available to the user. The pattern of use for a stand-alone emulator is usually in a script:
     Create an emulator, initialize its state, write instructions to its memory, create and initialize
     a thread, point its counter at the instructions, instrument, step/run, inspect, and finally
     terminate.
 
 
     This "parts factory" pattern aims to flatten the extension points of the
     AbstractPcodeMachine and its components into a single class. Its use is not required, but
     may make things easier. It also encapsulates some "special knowledge," that might not otherwise
     be obvious to a developer, e.g., it creates the concrete state pieces, so the developer need not
     guess (or keep up to date) the concrete state piece classes to instantiate.
 
 
     The factory itself should be a singleton object. See the Taint Analyzer for a complete example
     solution using this interface.
    """









    def createExecutor(self, emulator: ghidra.pcode.emu.auxiliary.AuxPcodeEmulator, thread: ghidra.pcode.emu.DefaultPcodeThread) -> ghidra.pcode.emu.DefaultPcodeThread.PcodeThreadExecutor:
        """
        Create an executor for the given thread
 
         <p>
         This allows the implementor to override or intercept the logic for individual p-code
         operations that would not otherwise be possible in the arithmetic, e.g., to print diagnostics
         on a conditional branch.
        @param emulator the emulator
        @param thread the thread
        @return the executor
        """
        ...

    def createLocalState(self, emulator: ghidra.pcode.emu.auxiliary.AuxPcodeEmulator, thread: ghidra.pcode.emu.PcodeThread, concrete: ghidra.pcode.exec.BytesPcodeExecutorStatePiece) -> ghidra.pcode.exec.PcodeExecutorState:
        """
        Create the local (register) state of a new stand-alone emulator
 
         <p>
         This is usually composed of pieces using {@link PairedPcodeExecutorStatePiece}, but it does
         not have to be. It must incorporate the concrete piece provided. It should be self contained
         and relatively fast.
        @param emulator the emulator
        @param thread the thread
        @param concrete the concrete piece
        @return the composed state
        """
        ...

    def createLocalUseropLibrary(self, emulator: ghidra.pcode.emu.auxiliary.AuxPcodeEmulator, thread: ghidra.pcode.emu.PcodeThread) -> ghidra.pcode.exec.PcodeUseropLibrary:
        """
        Create a userop library for a given thread
        @param emulator the emulator
        @param thread the thread
        @return the userop library
        """
        ...

    def createLocalUseropStub(self, emulator: ghidra.pcode.emu.auxiliary.AuxPcodeEmulator) -> ghidra.pcode.exec.PcodeUseropLibrary:
        """
        Create a stub userop library for the emulator's threads
        @param emulator the emulator
        @return the library of stubs
        """
        ...

    def createSharedState(self, emulator: ghidra.pcode.emu.auxiliary.AuxPcodeEmulator, concrete: ghidra.pcode.exec.BytesPcodeExecutorStatePiece) -> ghidra.pcode.exec.PcodeExecutorState:
        """
        Create the shared (memory) state of a new stand-alone emulator
 
         <p>
         This is usually composed of pieces using {@link PairedPcodeExecutorStatePiece}, but it does
         not have to be. It must incorporate the concrete piece provided. It should be self contained
         and relatively fast.
        @param emulator the emulator
        @param concrete the concrete piece
        @return the composed state
        """
        ...

    def createSharedUseropLibrary(self, emulator: ghidra.pcode.emu.auxiliary.AuxPcodeEmulator) -> ghidra.pcode.exec.PcodeUseropLibrary:
        """
        Create the userop library for the emulator (used by all threads)
        @param emulator the emulator
        @return the userop library
        """
        ...

    def createThread(self, emulator: ghidra.pcode.emu.auxiliary.AuxPcodeEmulator, name: unicode) -> ghidra.pcode.emu.PcodeThread:
        """
        Create a thread with the given name
        @param emulator the emulator
        @param name the thread's name
        @return the thread
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getArithmetic(self, language: ghidra.program.model.lang.Language) -> ghidra.pcode.exec.PcodeArithmetic:
        """
        Get the arithmetic for the emulator given a target langauge
        @param language the language
        @return the arithmetic
        """
        ...

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

