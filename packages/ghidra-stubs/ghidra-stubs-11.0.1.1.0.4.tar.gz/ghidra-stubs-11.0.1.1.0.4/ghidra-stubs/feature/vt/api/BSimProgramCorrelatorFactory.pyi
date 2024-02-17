import ghidra.feature.vt.api.main
import ghidra.feature.vt.api.util
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class BSimProgramCorrelatorFactory(ghidra.feature.vt.api.util.VTAbstractProgramCorrelatorFactory):
    DESC: unicode = u'Finds function matches by using data flow and call graph similarities between the source and destination programs.'
    IMPLICATION_THRESHOLD: unicode = u'Confidence Threshold for a Match'
    IMPLICATION_THRESHOLD_DEFAULT: float = 0.0
    IMPLICATION_THRESHOLD_DESC: unicode = u'For threshold N, the probability that a match is incorrect is approximately 1/2^(N/5+9).'
    MEMORY_MODEL: unicode = u'Memory Model'
    MEMORY_MODEL_DEFAULT: generic.lsh.LSHMemoryModel = Large (faster)
    MEMORY_MODEL_DESC: unicode = u'Amount of memory used to compute matches. Smaller models are slightly less accurate.'
    NAME: unicode = u'BSim Function Matching'
    SEED_CONF_THRESHOLD: unicode = u'Confidence Threshold for a Seed'
    SEED_CONF_THRESHOLD_DEFAULT: float = 10.0
    SEED_CONF_THRESHOLD_DESC: unicode = u'For threshold N, the probability that a seed is incorrect is approximately 1/2^(N/5+9).'
    USE_ACCEPTED_MATCHES_AS_SEEDS: unicode = u'Use Accepted Matches as Seeds'
    USE_ACCEPTED_MATCHES_AS_SEEDS_DEFAULT: bool = True
    USE_ACCEPTED_MATCHES_AS_SEEDS_DESC: unicode = u'Already accepted matches will also be used as seeds.'



    def __init__(self): ...



    @overload
    def createCorrelator(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressSetView, __a2: ghidra.program.model.listing.Program, __a3: ghidra.program.model.address.AddressSetView, __a4: ghidra.feature.vt.api.util.VTOptions) -> ghidra.feature.vt.api.main.VTProgramCorrelator: ...

    @overload
    def createCorrelator(self, __a0: ghidra.framework.plugintool.ServiceProvider, __a1: ghidra.program.model.listing.Program, __a2: ghidra.program.model.address.AddressSetView, __a3: ghidra.program.model.listing.Program, __a4: ghidra.program.model.address.AddressSetView, __a5: ghidra.feature.vt.api.util.VTOptions) -> ghidra.feature.vt.api.main.VTProgramCorrelator: ...

    def createDefaultOptions(self) -> ghidra.feature.vt.api.util.VTOptions: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressRestrictionPreference(self) -> ghidra.feature.vt.api.main.VTProgramCorrelatorAddressRestrictionPreference: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getPriority(self) -> int: ...

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

    @property
    def addressRestrictionPreference(self) -> ghidra.feature.vt.api.main.VTProgramCorrelatorAddressRestrictionPreference: ...

    @property
    def description(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def priority(self) -> int: ...