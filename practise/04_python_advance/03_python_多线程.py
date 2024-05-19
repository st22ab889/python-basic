"""
进程、线程:
    进程： 就是一个程序，运行在系统之上，那么便称之这个程序为一个运行进程，并分配进程ID方便系统管理。
    线程：线程是归属于进程的，一个进程可以开启多个线程，执行不同的工作，是进程的实际工作最小单位。 所以进程是一个逻辑概念, 由一个或多个线程构成一个进程
    注意点：
        进程之间是内存隔离的， 即不同的进程拥有各自的内存空间。
        线程之间是内存共享的，线程是属于进程的，一个进程内的多个线程之间是共享这个进程所拥有的内存空间的。


现代操作系统比如Mac OS X，UNIX，Linux，Windows等，都是支持“多任务”的操作系统。
    操作系统中可以运行多个进程，即多任务运行
    一个进程内可以运行多个线程，即多线程运行


并行执行：
    并行执行的意思指的是同一时间做不同的工作。
    进程之间就是并行执行的，操作系统可以同时运行好多程序，这些程序都是在并行执行。

    除了进程外，线程其实也是可以并行执行的。也就是比如一个Python程序，其实是完全可以做到：
        一个线程在输出：你好
        一个线程在输出：Hello
    像这样一个程序在同一时间做两件乃至多件不同的事情， 我们就称之为：多线程并行执行

Python的多线程可以通过threading模块来实现。
    threading_obj = threading.Thread([group [, target [, name [,args [, kwargs [, daemon]]]]]])
    参数解释：
        - group : 暂时无用,未来功能的预留参数
        - target : 运行的目标任务名
        - name : 线程名, 一般不用设置
        - args : 以元组的方式给运行任务传参
        - kwargs : 以字典的方式给运行任务传参
        - daemon : 当其他线程都结束了，被设置成“daemon=True”的线程也跟着一起结束
"""


import time
import threading


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # 注意: 如果元组只有一个元素, 元素后面要跟上一个逗号, 表示这是个元组. 不加上逗号就只是一个普通的括号,并不表示元组
    sing_thread = threading.Thread(target=sing, args=('sing......',))
    # 注意: 字典的key和"运行的目标任务名"的参数名要一致
    dance_thread = threading.Thread(target=dance, kwargs={"msg": "dance......"})
    sing_thread.start()
    dance_thread.start()

