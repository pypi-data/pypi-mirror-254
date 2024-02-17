import java.lang
import java.time


class GTimerCache(object):
    """
    Class for caching key,value entries for a limited time and cache size. Entries in this cache
     will be removed after the cache duration time has passed. If the cache ever exceeds its capacity,
     the least recently used entry will be removed.
 
     This class uses a LinkedHashMap with it ordering mode set to "access order". This means
     that iterating through keys, values, or entries of the map will be presented oldest first. 
     Inserting or accessing an entry in the map will move the entry to the back of the list, thus
     making it the youngest. This means that entries closest to or past expiration will be presented
     first. 
 
     This class is designed to be subclassed for two specific cases. The first case is for when 
     additional processing is required when an entry is removed from the cache. This typically would
     be for cases where resources need to be released, such as closing a File or disposing the object.
     The second reason to subclass this cache is to get more control of expiring values. Overriding
     #shouldRemoveFromCache(Object, Object), which gets called when an entry's time
     has expired, gives the client a chance to decide if the entry should be removed.
    """





    def __init__(self, lifetime: java.time.Duration, capacity: int):
        """
        Constructs new GTimerCache with a duration for cached entries and a maximum
         number of entries to cache.
        @param lifetime the duration that a key,value will remain in the cache without being
         accessed (accessing a cached entry resets its time)
        @param capacity the maximum number of entries in the cache before least recently used
         entries are removed
        """
        ...



    def clear(self) -> None:
        """
        Clears all the values in the cache. The expired callback will be called for each entry
         that was in the cache.
        """
        ...

    def containsKey(self, __a0: object) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, __a0: object) -> object: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, __a0: object, __a1: object) -> object: ...

    def remove(self, __a0: object) -> object: ...

    def setCapacity(self, capacity: int) -> None:
        """
        Sets the capacity for this cache. If this cache currently has more values than the new
         capacity, oldest values will be removed.
        @param capacity the new capacity for this cache
        """
        ...

    def setDuration(self, duration: java.time.Duration) -> None:
        """
        Sets the duration for keeping cached values.
        @param duration the length of time to keep a cached value
        """
        ...

    def size(self) -> int:
        """
        Returns the number of entries in the cache.
        @return the number of entries in the cache
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
    def capacity(self) -> None: ...  # No getter available.

    @capacity.setter
    def capacity(self, value: int) -> None: ...

    @property
    def duration(self) -> None: ...  # No getter available.

    @duration.setter
    def duration(self, value: java.time.Duration) -> None: ...