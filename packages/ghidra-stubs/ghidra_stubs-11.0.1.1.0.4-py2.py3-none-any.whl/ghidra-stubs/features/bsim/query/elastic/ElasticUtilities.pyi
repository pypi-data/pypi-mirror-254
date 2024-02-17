import java.lang


class ElasticUtilities(object):
    IDF_CONFIG: unicode = u'idf_config'
    K_SETTING: unicode = u'k_setting'
    LSH_WEIGHTS: unicode = u'lsh_weights'
    L_SETTING: unicode = u'l_setting'



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

