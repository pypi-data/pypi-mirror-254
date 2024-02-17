import com.google.common.collect
import ghidra.app.util.bin
import ghidra.app.util.bin.format.macho.dyld
import ghidra.app.util.opinion
import ghidra.file.formats.ios.dyldcache
import ghidra.formats.gfilesystem
import ghidra.util.task
import java.lang
import java.util


class DyldCacheExtractor(object):
    FOOTER_V1: List[int] = array('b', [71, 104, 105, 100, 114, 97, 32, 68, 89, 76, 68, 32, 101, 120, 116, 114, 97, 99, 116, 105, 111, 110, 32, 118, 49])




    class MappingRange(java.lang.Record):




        def __init__(self, __a0: ghidra.app.util.bin.format.macho.dyld.DyldCacheMappingAndSlideInfo, __a1: com.google.common.collect.RangeSet): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def mappingInfo(self) -> ghidra.app.util.bin.format.macho.dyld.DyldCacheMappingAndSlideInfo: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def rangeSet(self) -> com.google.common.collect.RangeSet: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def extractDylib(__a0: long, __a1: ghidra.app.util.opinion.DyldCacheUtils.SplitDyldCache, __a2: int, __a3: java.util.Map, __a4: ghidra.formats.gfilesystem.FSRL, __a5: ghidra.util.task.TaskMonitor) -> ghidra.app.util.bin.ByteProvider: ...

    @staticmethod
    def extractMapping(__a0: ghidra.file.formats.ios.dyldcache.DyldCacheExtractor.MappingRange, __a1: unicode, __a2: ghidra.app.util.opinion.DyldCacheUtils.SplitDyldCache, __a3: int, __a4: java.util.Map, __a5: ghidra.formats.gfilesystem.FSRL, __a6: ghidra.util.task.TaskMonitor) -> ghidra.app.util.bin.ByteProvider: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getSlideFixups(__a0: ghidra.app.util.opinion.DyldCacheUtils.SplitDyldCache, __a1: ghidra.util.task.TaskMonitor) -> java.util.Map: ...

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

