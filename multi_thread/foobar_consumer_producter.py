import threading

from queue import Queue

q = Queue(maxsize=1)


class FooBar:
    def __init__(self, n):
        self.n = n
        self.q = Queue(1)

    def foo(self) -> None:

        for i in range(self.n):

            # printFoo() outputs "foo". Do not change or remove this line.
            self.q.put(1)
            # self.printFoo()
            print("foo")

    def bar(self) -> None:

        for i in range(self.n):
            self.q.get()
            # self.printBar()
            print("bar")
           

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
