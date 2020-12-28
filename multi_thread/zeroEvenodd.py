from queue import Queue
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.s0 = threading.Semaphore(1)
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)
    # printNumber(x) outputs "x", where x is an integer.

    def zero(self) -> None:
        for i in range(1, self.n + 1):
            if i % 2 != 0:
                self.s0.acquire()
                self.printNumber(0)
                self.s1.release()
            else:
                self.s0.acquire()
                self.printNumber(0)
                self.s2.release()

    def even(self) -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                self.s2.acquire()
                self.printNumber(i)
                self.s0.release()

    def odd(self) -> None:
        for i in range(1, self.n + 1):
            if i % 2 != 0:
                self.s1.acquire()
                self.printNumber(i)
                self.s0.release()

    def printNumber(self, num: int):
        print(num)


if __name__ == '__main__':

    so = ZeroEvenOdd(10)
    # t1 = threading.Thread(target=foobar.foo(printFoo))
    # t2 = threading.Thread(target=foobar.bar(printBar))
    t1 = threading.Thread(target=so.zero)
    t2 = threading.Thread(target=so.odd)
    t3 = threading.Thread(target=so.even)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("exit main")
