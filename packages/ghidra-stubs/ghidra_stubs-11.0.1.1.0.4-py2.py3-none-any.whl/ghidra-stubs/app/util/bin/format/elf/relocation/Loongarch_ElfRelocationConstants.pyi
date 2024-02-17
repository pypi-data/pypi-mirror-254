import java.lang


class Loongarch_ElfRelocationConstants(object):
    R_LARCH_32: int = 1
    R_LARCH_32_PCREL: int = 99
    R_LARCH_64: int = 2
    R_LARCH_64_PCREL: int = 109
    R_LARCH_ABS64_HI12: int = 70
    R_LARCH_ABS64_LO20: int = 69
    R_LARCH_ABS_HI20: int = 67
    R_LARCH_ABS_LO12: int = 68
    R_LARCH_ADD16: int = 48
    R_LARCH_ADD24: int = 49
    R_LARCH_ADD32: int = 50
    R_LARCH_ADD6: int = 105
    R_LARCH_ADD64: int = 51
    R_LARCH_ADD8: int = 47
    R_LARCH_ADD_ULEB128: int = 107
    R_LARCH_ALIGN: int = 102
    R_LARCH_B16: int = 64
    R_LARCH_B21: int = 65
    R_LARCH_B26: int = 66
    R_LARCH_CFA: int = 104
    R_LARCH_COPY: int = 4
    R_LARCH_DELETE: int = 101
    R_LARCH_GNU_VTENTRY: int = 58
    R_LARCH_GNU_VTINHERIT: int = 57
    R_LARCH_GOT64_HI12: int = 82
    R_LARCH_GOT64_LO20: int = 81
    R_LARCH_GOT64_PC_HI12: int = 78
    R_LARCH_GOT64_PC_LO20: int = 77
    R_LARCH_GOT_HI20: int = 79
    R_LARCH_GOT_LO12: int = 80
    R_LARCH_GOT_PC_HI20: int = 75
    R_LARCH_GOT_PC_LO12: int = 76
    R_LARCH_IRELATIVE: int = 12
    R_LARCH_JUMP_SLOT: int = 5
    R_LARCH_MARK_LA: int = 20
    R_LARCH_MARK_PCREL: int = 21
    R_LARCH_NONE: int = 0
    R_LARCH_PCALA64_HI12: int = 74
    R_LARCH_PCALA64_LO20: int = 73
    R_LARCH_PCALA_HI20: int = 71
    R_LARCH_PCALA_LO12: int = 72
    R_LARCH_PCREL20_S2: int = 103
    R_LARCH_RELATIVE: int = 3
    R_LARCH_RELAX: int = 100
    R_LARCH_SOP_ADD: int = 35
    R_LARCH_SOP_AND: int = 36
    R_LARCH_SOP_ASSERT: int = 30
    R_LARCH_SOP_IF_ELSE: int = 37
    R_LARCH_SOP_NOT: int = 31
    R_LARCH_SOP_POP_32_S_0_10_10_16_S2: int = 45
    R_LARCH_SOP_POP_32_S_0_5_10_16_S2: int = 44
    R_LARCH_SOP_POP_32_S_10_12: int = 40
    R_LARCH_SOP_POP_32_S_10_16: int = 41
    R_LARCH_SOP_POP_32_S_10_16_S2: int = 42
    R_LARCH_SOP_POP_32_S_10_5: int = 38
    R_LARCH_SOP_POP_32_S_5_20: int = 43
    R_LARCH_SOP_POP_32_U: int = 46
    R_LARCH_SOP_POP_32_U_10_12: int = 39
    R_LARCH_SOP_PUSH_ABSOLUTE: int = 23
    R_LARCH_SOP_PUSH_DUP: int = 24
    R_LARCH_SOP_PUSH_GPREL: int = 25
    R_LARCH_SOP_PUSH_PCREL: int = 22
    R_LARCH_SOP_PUSH_PLT_PCREL: int = 29
    R_LARCH_SOP_PUSH_TLS_GD: int = 28
    R_LARCH_SOP_PUSH_TLS_GOT: int = 27
    R_LARCH_SOP_PUSH_TLS_TPREL: int = 26
    R_LARCH_SOP_SL: int = 33
    R_LARCH_SOP_SR: int = 34
    R_LARCH_SOP_SUB: int = 32
    R_LARCH_SUB16: int = 53
    R_LARCH_SUB24: int = 54
    R_LARCH_SUB32: int = 55
    R_LARCH_SUB6: int = 106
    R_LARCH_SUB64: int = 56
    R_LARCH_SUB8: int = 52
    R_LARCH_SUB_ULEB128: int = 108
    R_LARCH_TLS_DTPMOD32: int = 6
    R_LARCH_TLS_DTPMOD64: int = 7
    R_LARCH_TLS_DTPREL32: int = 8
    R_LARCH_TLS_DTPREL64: int = 9
    R_LARCH_TLS_GD_HI20: int = 98
    R_LARCH_TLS_GD_PC_HI20: int = 97
    R_LARCH_TLS_IE64_HI12: int = 94
    R_LARCH_TLS_IE64_LO20: int = 93
    R_LARCH_TLS_IE64_PC_HI12: int = 90
    R_LARCH_TLS_IE64_PC_LO20: int = 89
    R_LARCH_TLS_IE_HI20: int = 91
    R_LARCH_TLS_IE_LO12: int = 92
    R_LARCH_TLS_IE_PC_HI20: int = 87
    R_LARCH_TLS_IE_PC_LO12: int = 88
    R_LARCH_TLS_LD_HI20: int = 96
    R_LARCH_TLS_LD_PC_HI20: int = 95
    R_LARCH_TLS_LE64_HI12: int = 86
    R_LARCH_TLS_LE64_LO20: int = 85
    R_LARCH_TLS_LE_HI20: int = 83
    R_LARCH_TLS_LE_LO12: int = 84
    R_LARCH_TLS_TPREL32: int = 10
    R_LARCH_TLS_TPREL64: int = 11







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

