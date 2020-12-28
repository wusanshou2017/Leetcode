import threading

# 两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。

# 请设计修改程序，以确保 "foobar" 被输出 n 次。


s1 = threading.Semaphore(1)
s2 = threading.Semaphore(0)


def printFoo():
    for _ in range(10):
        s1.acquire()
        print("foo")
        s2.release()


def printBar():
    for _ in range(10):
        s2.acquire()
        print("bar")
        s1.release()


class FooBar:
    def __init__(self, n):
        self.n = n
        self.s1 = threading.Semaphore(1)
        self.s2 = threading.Semaphore(0)

    def foo(self) -> None:

        for i in range(self.n):

            # printFoo() outputs "foo". Do not change or remove this line.
            self.s1.acquire()
            # s1.acquire()
            self.printFoo()
            # s2.release()
            self.s2.release()

    def bar(self) -> None:

        for i in range(self.n):

            # printBar() outputs "bar". Do not change or remove this line.
            self.s2.acquire()
            # s2.acquire()
            self.printBar()
            # s1.release()
            self.s1.release()

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

# unit_test
# class DemoThread1(Thread):
#     def __init__(self):
#         Thread.__init__(self)

#     def run(self):
#         pass


# if __name__ == '__main__':
#     foobar = FooBar(10)
#     t1 = threading.Thread(target=printFoo)
#     t2 = threading.Thread(target=printBar)
#     t1.start()
#     t2.start()
