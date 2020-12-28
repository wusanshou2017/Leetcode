import threading

from queue import Queue

q = Queue(maxsize=1)


class FooBar:
    def __init__(self, n):
        self.n = n
        self.q1 = Queue(1)
        self.q2 = Queue(1)
        self.q1.put(0)

    def foo(self) -> None:

        for i in range(self.n):

            # printFoo() outputs "foo". Do not change or remove this line.
            self.q1.get()
            # self.printFoo()
            print("foo")
            self.q2.put(0)

    def bar(self) -> None:

        for i in range(self.n):
            self.q2.get()
            # self.printBar()
            print("bar")
            self.q1.put(0)

    def printFoo(self):
        print("foo")

    def printBar(self):
        print("bar")


if __name__ == '__main__':

    foobar = FooBar(10)
    # t1 = threading.Thread(target=foobar.foo(printFoo))
    # t2 = threading.Thread(target=foobar.bar(printBar))
    t1 = threading.Thread(target=foobar.foo)
    t2 = threading.Thread(target=foobar.bar)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("exit main")
