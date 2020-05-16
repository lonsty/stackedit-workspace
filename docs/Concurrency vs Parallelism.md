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

#### 同步阻塞she


<!--stackedit_data:
eyJoaXN0b3J5IjpbMzM5OTc2MjQ1LDc5NDcyNTU4NiwtMTU3NT
Y2MTcwOSwtODc1OTMzODk3LC0xMzQxMzk5ODUzLDE1OTk2MTgy
NDldfQ==
-->