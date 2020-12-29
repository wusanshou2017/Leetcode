import threading

from queue import Queue

# using the queue put to join the thread ...
class H2O:
    def __init__(self):
        self._que_h = Queue(2)
        self._que_o = Queue(1)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self._que_h.put(1)
        releaseHydrogen()
        if self._que_h.full() and self._que_o.full():
            self._que_o.get()
            self._que_h.get()
            self._que_h.get()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:

        # releaseOxygen() outputs "O". Do not change or remove this line.
        self._que_o.put(1)
        releaseOxygen()
        if self._que_h.full() and self._que_o.full():
            self._que_o.get()
            self._que_h.get()
            self._que_h.get()
