# import threading 
# class FooBar:
#     def __init__(self, n):
#         self.n = n
#         self.s1=threading.Semaphore(1)
#         self.s2=threading.Semaphore(0)


#     def foo(self, printFoo: 'Callable[[], None]') -> None:
        
#         for i in range(self.n):
#             print("index:...",i)
#             # printFoo() outputs "foo". Do not change or remove this line.
#             self.s1.acquire()
#             printFoo()
#             self.s2.release()


#     def bar(self, printBar: 'Callable[[], None]') -> None:
        
#         for i in range(self.n):
#             print("index...:",i)
#             # printBar() outputs "bar". Do not change or remove this line.
#             self.s2.acquire()
#             printBar()
#             self.s1.release()

import threading
empty=threading.Semaphore(1) # empty信号量初始值设为1  空缓冲区数量
full=threading.Semaphore(0)  # full 信号量初始值设为0  满缓冲区数量
'''信号量为0时，不可被减，同时信号量不设上限
所以需要两个信号量empty、full共同监测两个边界[0,1]'''

class FooBar:
    def __init__(self, n):
        self.n = n


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            empty.acquire() # empty-1，申请一个空缓冲区，有空位时应执行生产者活动
            printFoo()
            full.release() # full+1，释放一个满缓冲区


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            full.acquire() # full-1, 申请一个满缓冲区，当缓冲区有商品时才能实现消费者行为
            printBar()
            empty.release() # empty+1，释放一个空缓冲区


def printBar():
    print ("Bar")

def printFoo():
    print("Foo")

foobar =FooBar(10)
t1 =threading.Thread(foobar.foo(printFoo))
t2 =threading.Thread(foobar.bar(printBar))
threads = []
t1.start()
t2.start()
threads.append(t1)
threads.append(t2)
for t in threads:
    t.join()
print("exit __main__")


