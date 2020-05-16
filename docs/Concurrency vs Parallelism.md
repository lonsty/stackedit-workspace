## 并发 Concurrency
> Concurrency is about dealing with lot of things at once.

操作系统处理任务的方式。（宏观上）CPU 在一段时间内，处理了多个任务。

## 并行 Parallelism
> Parallelism is about doing lot of things at once.

操作系统处理任务的方式。CPU 在某一个时间点，同时处理多个任务。（并行的数量取决于 CPU 的核心数，一个核心在一个时间点只能处理一个任务。）

## 同步 Synchronous

关注的是消息通信机制。同步描述的是调用 IO 操作时，需一直等到结果出来才返回。

## 异步 Asynchronous

关注的是消息通信机制。异步描述的是调用 IO 操作时，不等待结果出来而立即返回，此时还没有返回结果。

#### 异步阻塞式 IO

#### 异步非阻塞式 IO

## 阻塞 Blocked

关注的是调用者在等待调用结果时的状态。阻塞调用是指调用结果返回之前，当前线程会被挂起（不能做其他事）。

## 非阻塞 Unblocked

关注的是调用者在等待调用结果时的状态。非阻塞调用是指调用在不能立即得到结果之前，该调用不会阻塞当前线程，线程不会挂起（仍可处理其他事）。

## 多线程和多进程

### 线程

* 线程是 CPU 调度分配的最小单位
* 实际可以并行的线程数量是物理核数的两倍。但在 Python 中由于 GIL 的存在，单核多线程在同一时刻实际上

### 进程

* 进程是操作系统资源分配（内存、显卡、磁盘）的最小单位
* CPU 看到的都是线程而非进程
* 一个进程可以有一个或多个线程，线程之共享进程的资源，通过这样的方式，不断地调度线程可以减少进程的创建和销毁带来的代价
* 

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAzNjI1MTUzOSwtNjc0NjI2MzgzLC0yMD
Y4NDEyMzQwLC00MzQzMzU5MCw3OTQ3MjU1ODYsLTE1NzU2NjE3
MDksLTg3NTkzMzg5NywtMTM0MTM5OTg1MywxNTk5NjE4MjQ5XX
0=
-->