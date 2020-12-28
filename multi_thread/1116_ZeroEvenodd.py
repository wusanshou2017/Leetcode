from queue import Queue
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.q0 = Queue(1)
        self.q1 = Queue(1)
        self.q2 = Queue(1)
        self.q0.put(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self) -> None:
        for i in range(1, self.n + 1):
            if i % 2 != 0:
                self.q0.get()
                self.printNumber(0)
                self.q1.put(1)
            else:
                self.q0.get()
                self.printNumber(0)
                self.q2.put(1)

    def even(self) -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                self.q2.get()
                self.printNumber(i)
                self.q0.put(1)

    def odd(self) -> None:
        for i in range(1, self.n + 1):
            if i % 2 != 0:
                self.q1.get()
                self.printNumber(i)
                self.q0.put(1)

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
