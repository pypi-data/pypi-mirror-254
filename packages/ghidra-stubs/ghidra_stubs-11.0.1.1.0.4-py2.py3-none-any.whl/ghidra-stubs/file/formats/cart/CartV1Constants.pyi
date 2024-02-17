import java.lang


class CartV1Constants(object):
    ARC4_KEY_LENGTH: int = 16
    BLOCK_SIZE: int = 65536
    DEFAULT_ARC4_KEY: List[int] = array('b', [3, 1, 4, 1, 5, 9, 2, 6, 3, 1, 4, 1, 5, 9, 2, 6])
    EXPECTED_HASHES: java.util.Map = {u'md5': u'MD5', u'sha1': u'SHA1', u'sha256': u'SHA-256'}
    FOOTER_LENGTH: int = 28
    FOOTER_MAGIC: unicode = u'TRAC'
    FOOTER_ONLY_KEYS: java.util.Set = [sha1, sha256, length, md5]
    FOOTER_RESERVED: long = 0x0L
    HEADER_LENGTH: int = 38
    HEADER_MAGIC: unicode = u'CART'
    HEADER_RESERVED: long = 0x0L
    HEADER_VERSION: int = 1
    MINIMUM_LENGTH: int = 66
    PRIVATE_ARC4_KEY_PLACEHOLDER: List[int] = array('b', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    ZLIB_HEADER_BYTES: List[object] = [[B@4c0d6cd, [B@32b0dbd8, [B@3142cdfc]



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

