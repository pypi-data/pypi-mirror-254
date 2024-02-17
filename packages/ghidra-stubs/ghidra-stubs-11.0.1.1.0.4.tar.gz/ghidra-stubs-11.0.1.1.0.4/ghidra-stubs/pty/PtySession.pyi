import java.lang


class PtySession(object):
    """
    A session led by the child pty
 
 
     This is typically a handle to the (local or remote) process designated as the "session leader"
    """









    def description(self) -> unicode:
        """
        Get a human-readable description of the session
        @return the description
        """
        ...

    def destroyForcibly(self) -> None:
        """
        Take the greatest efforts to terminate the session (leader and descendants)
 
         <p>
         If this represents a remote session, this should strive to release the remote resources
         consumed by this session. If that is not possible, this should at the very least release
         whatever local resources are used in maintaining and controlling the remote session.
        """
        ...

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

    def waitExited(self) -> int:
        """
        Wait for the session leader to exit, returning its optional exit status code
        @return the status code, if applicable and implemented
        @throws InterruptedException if the wait is interrupted
        """
        ...

