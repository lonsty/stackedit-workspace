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
* 实际可以并行的线程数量是物理核数的两倍。但在 Python 中由于 GIL 的存在，单核多线程在同一时刻实际上并行数为 1，即只有一个线程可以获得操作系统资源的权限。
* IO 密集型任务，使用多个（需要远多于核心数）线程，，才能最大的提高 CPU 的使用率
* 线程可以共享同一进程的资源，因此在线程创建和销毁上开销较进程小，使用会更加轻便

### 进程

* 进程是操作系统资源分配（内存、显卡、磁盘）的最小单位
* CPU 看到的都是线程而非进程
* 一个进程可以有一个或多个线程，线程之共享进程的资源，通过这样的方式，不断地调度线程可以减少进程的创建和销毁带来的代价
* 计算密集型任务，使用核心数个进程，可以充分利用 CPU 计算资源
* 因为每个进程之间的资源是独立的（地址空间和数据空间），若要通信，则需要在操作系统层面进行通信，如管道、队列、信号等

### 封装

### 继承

### 多态
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MjAxNDc0OTYsMTU4NTgyNzMwOCwtNj
c0NjI2MzgzLC0yMDY4NDEyMzQwLC00MzQzMzU5MCw3OTQ3MjU1
ODYsLTE1NzU2NjE3MDksLTg3NTkzMzg5NywtMTM0MTM5OTg1My
wxNTk5NjE4MjQ5XX0=
-->