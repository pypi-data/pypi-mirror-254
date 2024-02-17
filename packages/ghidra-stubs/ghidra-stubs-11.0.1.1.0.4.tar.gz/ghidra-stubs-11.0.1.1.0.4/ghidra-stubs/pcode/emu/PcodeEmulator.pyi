import ghidra.app.plugin.processors.sleigh
import ghidra.pcode.emu
import ghidra.pcode.emu.PcodeMachine
import ghidra.pcode.exec
import ghidra.program.model.address
import java.lang
import java.util


class PcodeEmulator(ghidra.pcode.emu.AbstractPcodeMachine):
    """
    A p-code machine which executes on concrete bytes and incorporates per-architecture state
     modifiers
 
 
     This is a simple concrete bytes emulator suitable for unit testing and scripting. More complex
     use cases likely benefit by extending this or one of its super types. Likewise, the factory
     methods will likely instantiate classes which extend the default or one of its super types. When
     creating such an extension, it helps to refer to this default implementation to understand the
     overall architecture of an emulator. The emulator was designed using hierarchies of abstract
     classes each extension incorporating more complexity (and restrictions) finally culminating here.
     Every class should be extensible and have overridable factory methods so that those extensions
     can be incorporated into even more capable emulators. Furthermore, many components, e.g.,
     PcodeExecutorState were designed with composition in mind. Referring to examples, it is
     straightforward to extend the emulator via composition. Consider using AuxPcodeEmulator
     or one of its derivatives to create a concrete-plus-auxiliary style emulator.
 
 
     emulator      : PcodeMachine
      - language     : SleighLanguage
      - arithmetic   : PcodeArithmetic
      - sharedState  : PcodeExecutorState
      - library      : PcodeUseropLibrary
      - injects      : PcodeProgram
      - threads      : PcodeThread
        - [0]          : PcodeThread
          - decoder      : InstructionDecoder
          - executor     : PcodeExecutor
          - frame        : PcodeFrame
          - localState   : PcodeExecutorState
          - library      : PcodeUseropLibrary
          - injects      : PcodeProgram
        - [1] ...
 
 
 
     The root object of an emulator is the PcodeEmulator, usually ascribed the type
     PcodeMachine. At the very least, it must know the language of the processor it emulates.
     It then derives appropriate arithmetic definitions, a shared (memory) state, and a shared userop
     library. Initially, the machine has no threads. For many use cases creating a single
     PcodeThread suffices; however, this default implementation models multi-threaded
     execution "out of the box." Upon creation, each thread is assigned a local (register) state, and
     a userop library for controlling that particular thread. The thread's full state and userop
     library are composed from the machine's shared components and that thread's particular
     components. For state, the composition directs memory accesses to the machine's state and
     register accesses to the thread's state. (Accesses to the "unique" space are also directed to the
     thread's state.) This properly emulates the thread semantics of most platforms. For the userop
     library, composition is achieved via PcodeUseropLibrary#compose(PcodeUseropLibrary).
     Thus, each invocation is directed to the library that exports the invoked userop.
 
 
     Each thread creates an InstructionDecoder and a PcodeExecutor, providing the
     kernel of p-code emulation for that thread. That executor is bound to the thread's composed
     state, and to the machine's arithmetic. Together, the state and the arithmetic "define" all the
     p-code ops that the executor can invoke. Unsurprisingly, arithmetic operations are delegated to
     the PcodeArithmetic, and state operations (including memory operations and temporary
     variable access) are delegated to the PcodeExecutorState. The core execution loop easily
     follows: 1) decode the current instruction, 2) generate that instruction's p-code, 3) feed the
     code to the executor, 4) resolve the outcome and advance the program counter, then 5) repeat. So
     long as the arithmetic and state objects agree in type, a p-code machine can be readily
     implemented to manipulate values of that type.
 
 
     This concrete emulator chooses a BytesPcodeArithmetic based on the endianness of the
     target language. Its threads are BytesPcodeThread. The shared and thread-local states are
     all BytesPcodeExecutorState. That pieces of that state can be extended to read through to
     some other backing object. For example, the memory state could read through to an imported
     program image, which allows the emulator's memory to be loaded lazily.
 
 
     The default userop library is empty. For many use cases, it will be necessary to override
     #createUseropLibrary() if only to implement the language-defined userops. If needed,
     simulation of the host operating system is typically achieved by implementing the 
     userop. The fidelity of that simulation depends on the use case. See the SystemEmulation module
     to see what simulators are available "out of the box."
 
 
     Alternatively, if the target program never invokes system calls directly, but rather via
     system-provided APIs, then it may suffice to stub out those imports. Typically, Ghidra will place
     a "thunk" at each import address with the name of the import. Stubbing an import is accomplished
     by injecting p-code at the import address. See PcodeMachine#inject(Address, String). The
     inject will need to replicate the semantics of that call to the desired fidelity.
     IMPORTANT: The inject must also return control to the calling function, usually by
     replicating the conventions of the target platform.
    """





    def __init__(self, language: ghidra.program.model.lang.Language):
        """
        Construct a new concrete emulator
 
         <p>
         Yes, it is customary to invoke this constructor directly.
        @param language the language of the target processor
        """
        ...



    def addAccessBreakpoint(self, range: ghidra.program.model.address.AddressRange, kind: ghidra.pcode.emu.PcodeMachine.AccessKind) -> None: ...

    def addBreakpoint(self, address: ghidra.program.model.address.Address, sleighCondition: unicode) -> None: ...

    def clearAccessBreakpoints(self) -> None: ...

    def clearAllInjects(self) -> None: ...

    def clearInject(self, address: ghidra.program.model.address.Address) -> None: ...

    def compileSleigh(self, sourceName: unicode, source: unicode) -> ghidra.pcode.exec.PcodeProgram: ...

    def equals(self, __a0: object) -> bool: ...

    def getAllThreads(self) -> java.util.Collection: ...

    def getArithmetic(self) -> ghidra.pcode.exec.PcodeArithmetic: ...

    def getClass(self) -> java.lang.Class: ...

    def getLanguage(self) -> ghidra.app.plugin.processors.sleigh.SleighLanguage: ...

    def getSharedState(self) -> ghidra.pcode.exec.PcodeExecutorState: ...

    def getSoftwareInterruptMode(self) -> ghidra.pcode.emu.PcodeMachine.SwiMode: ...

    def getStubUseropLibrary(self) -> ghidra.pcode.exec.PcodeUseropLibrary: ...

    def getThread(self, name: unicode, createIfAbsent: bool) -> ghidra.pcode.emu.PcodeThread: ...

    def getUseropLibrary(self) -> ghidra.pcode.exec.PcodeUseropLibrary: ...

    def hashCode(self) -> int: ...

    def inject(self, address: ghidra.program.model.address.Address, source: unicode) -> None: ...

    def isSuspended(self) -> bool: ...

    @overload
    def newThread(self) -> ghidra.pcode.emu.PcodeThread: ...

    @overload
    def newThread(self, name: unicode) -> ghidra.pcode.emu.PcodeThread: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setSoftwareInterruptMode(self, mode: ghidra.pcode.emu.PcodeMachine.SwiMode) -> None: ...

    def setSuspended(self, suspended: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

