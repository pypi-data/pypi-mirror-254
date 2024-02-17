import java.lang


class Xtensa_ElfRelocationConstants(object):
    EM_XTENSA_OLD: int = 43975
    R_XTENSA_32: int = 1
    R_XTENSA_ASM_EXPAND: int = 11
    R_XTENSA_ASM_SIMPLIFY: int = 12
    R_XTENSA_DIFF16: int = 18
    R_XTENSA_DIFF32: int = 19
    R_XTENSA_DIFF8: int = 17
    R_XTENSA_GLOB_DAT: int = 3
    R_XTENSA_GNU_VTENTRY: int = 16
    R_XTENSA_GNU_VTINHERIT: int = 15
    R_XTENSA_JMP_SLOT: int = 4
    R_XTENSA_NONE: int = 0
    R_XTENSA_OP0: int = 8
    R_XTENSA_OP1: int = 9
    R_XTENSA_OP2: int = 10
    R_XTENSA_PLT: int = 6
    R_XTENSA_RELATIVE: int = 5
    R_XTENSA_RTLD: int = 2
    R_XTENSA_SLOT0_ALT: int = 35
    R_XTENSA_SLOT0_OP: int = 20
    R_XTENSA_SLOT10_ALT: int = 45
    R_XTENSA_SLOT10_OP: int = 30
    R_XTENSA_SLOT11_ALT: int = 46
    R_XTENSA_SLOT11_OP: int = 31
    R_XTENSA_SLOT12_ALT: int = 47
    R_XTENSA_SLOT12_OP: int = 32
    R_XTENSA_SLOT13_ALT: int = 48
    R_XTENSA_SLOT13_OP: int = 33
    R_XTENSA_SLOT14_ALT: int = 49
    R_XTENSA_SLOT14_OP: int = 34
    R_XTENSA_SLOT1_ALT: int = 36
    R_XTENSA_SLOT1_OP: int = 21
    R_XTENSA_SLOT2_ALT: int = 37
    R_XTENSA_SLOT2_OP: int = 22
    R_XTENSA_SLOT3_ALT: int = 38
    R_XTENSA_SLOT3_OP: int = 23
    R_XTENSA_SLOT4_ALT: int = 39
    R_XTENSA_SLOT4_OP: int = 24
    R_XTENSA_SLOT5_ALT: int = 40
    R_XTENSA_SLOT5_OP: int = 25
    R_XTENSA_SLOT6_ALT: int = 41
    R_XTENSA_SLOT6_OP: int = 26
    R_XTENSA_SLOT7_ALT: int = 42
    R_XTENSA_SLOT7_OP: int = 27
    R_XTENSA_SLOT8_ALT: int = 43
    R_XTENSA_SLOT8_OP: int = 28
    R_XTENSA_SLOT9_ALT: int = 44
    R_XTENSA_SLOT9_OP: int = 29



    def __init__(self): ...



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

