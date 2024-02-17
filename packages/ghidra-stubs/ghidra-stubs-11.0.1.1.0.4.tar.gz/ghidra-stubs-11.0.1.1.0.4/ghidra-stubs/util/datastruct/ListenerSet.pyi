import ghidra.util.datastruct
import java.lang


class ListenerSet(object):
    """
    A data structure meant to be used to hold listeners.  This class has a few benefits:
 
      Clients supply the class of the listeners being stored.  Then, clients make use of a Java
          Proxy object to sends events by calling the desired method directly on the proxy.
  
      This class is thread safe, allowing adding and removing listeners while events are being
          fired.
  
      Weak or strong references may be used seamlessly by passing the correct constructor value.
  
 

 
     Some restrictions:
 
      Exception handling is currently done by storing the first exception encountered while
          processing events.   Any exception encountered while notifying a listener does not stop
          follow-on listeners from getting notified.
  
      Listener classes are restricted to using methods with a void return type, as there is
          currently no way to return values back to the client when notifying.
  
      The insertion order of listeners is not maintained, which means that event notification may
          take place in an arbitrary order.
  
 

 
     An example use of this class to fire events could look like this:
 
         ListenerSetActionListener listeners = new ListenerSet(ActionListener.class);
         ActionEvent event = new ActionEvent(this, 1, "Event");
         listeners.invoke().actionPerformed(event);
 
    """





    def __init__(self, iface: java.lang.Class, isWeak: bool):
        """
        Constructs a listener set that is backed by weak references.
        @param iface the listener class type.
        @param isWeak true signals to use weak storage for the listeners.  If using weak storage,
                clients must keep a reference to the listener or it will eventually be removed from
                this data structure when garbage collected.
        """
        ...



    def add(self, e: object) -> bool: ...

    def clear(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getProxy(self) -> object:
        """
        Returns the proxy used by this class.  Using {@link #invoke()} is preferred for better
         readability.
        @return the proxy
        """
        ...

    def hashCode(self) -> int: ...

    def invoke(self) -> object:
        """
        Returns the proxy object.  Using this is the same as calling {@link #getProxy()}. Use this
         method to make the client call more readable.
        @return the proxy
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, e: object) -> bool: ...

    def setErrorHandler(self, errorHandler: ghidra.util.datastruct.ListenerErrorHandler) -> None: ...

    def size(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def errorHandler(self) -> None: ...  # No getter available.

    @errorHandler.setter
    def errorHandler(self, value: ghidra.util.datastruct.ListenerErrorHandler) -> None: ...

    @property
    def proxy(self) -> object: ...