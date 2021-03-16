# [Concurrent](https://docs.python.org/3/library/concurrency.html) Execution

## What 

The modules described in this chapter provide support for **concurrent execution** of code. The appropriate choice of tool will depend on the task to be executed (CPU bound vs IO bound) and preferred style of development (event driven cooperative multitasking vs preemptive multitasking). Here’s an overview:


* **threading** — Thread-based parallelism
* **multiprocessing** — Process-based parallelism
* **multiprocessing.shared_memory** — Provides shared memory for direct access across processes
* The **concurrent** package
* **concurrent.futures** — Launching parallel tasks
* **subprocess** — Subprocess management
* **sched** — Event scheduler
* **queue** — A synchronized queue class
* **_thread** — Low-level threading API


## How 

* [playground](https://repl.it/@WillWang42/threading-test)