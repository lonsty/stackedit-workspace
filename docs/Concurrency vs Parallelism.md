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

关注的是调用者在等待调用结果时的状态。非阻塞调用是指调用结果返回之前，当前线程会被挂起。

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNjg0MTIzNDAsLTQzNDMzNTkwLDc5ND
cyNTU4NiwtMTU3NTY2MTcwOSwtODc1OTMzODk3LC0xMzQxMzk5
ODUzLDE1OTk2MTgyNDldfQ==
-->