# Concurrency 

<center><img src="https://i.imgur.com/oAPBEFi.jpg" alt="Inside the Linux Kernel" width="200"/></center>


> In computer science, concurrency is the ability of **different** parts or units of a program, algorithm, or problem to **be executed out-of-order or in partial order**, without **affecting the final outcome**. 
> 
> This allows for **parallel execution** of the **concurrent** units, which can significantly improve overall **speed** of the execution in multi-processor and multi-core systems. 
> 
> 
> [[wiki](https://www.wikiwand.com/en/Concurrency_(computer_science))]


## Why 

The modern world is parallel. Multicore. Networks. Clouds of CUPs. Loads of users. Our technology should help. That's where concurrency comes in. 

## What 

In computer science, concurrency is the ability of **different** parts or units of a program, algorithm, or problem to be **executed** out-of-order or in partial order, **without affecting** the **final** outcome.

This allows for **parallel execution** of the **concurrent** units, which can significantly improve overall **speed** of the execution in multi-processor and multi-core systems.


## FQAs

#### Q: concurrency vs parallelism?

A: Concurrency is when two or more tasks can start, run, and complete in **overlapping time periods**. It **doesn't** necessarily mean they'll ever both be running at the **same** instant. For example, multitasking on a **single-core** machine. 

Parallelism is when tasks **literally** run at the **same** time, e.g., on a multicore processor.

#### Q: Could you show me Concurrency and Parallelism Combinations?

A: Here are 4 from [Concurrency vs. Parallelism](http://tutorials.jenkov.com/java-concurrency/concurrency-vs-parallelism.html)

* **Concurrent, Not Parallel**: This means that it makes progress on more than one task seemingly at the same time (concurrently), but the application switches between making progress on each of the tasks - until the tasks are completed. There is **no true parallel execution** of tasks going in parallel threads / CPUs.
* **Parallel, Not Concurrent**: This means that the application only works on one task at a time, and this task is broken down into subtasks which can be processed in parallel. However, each task (+ subtask) is **completed before** the next task is split up and executed in parallel.
* **Neither Concurrent Nor Parallel**: This means that it works on only one task at a time, and the task is never broken down into subtasks for parallel execution. This could be the case for **small command line applications** where it only has a single job which is too small to make sense to parallelize.
* **Concurrent and Parallel**: in two ways, parallel concurrent execution & concurrent parallel model.
	
### Q: Could you give an analogy about Concurrent and Parallel?
	* A: Concurrent: Two queues to one coffee machine
	* Parallel: Two queues to two coffee machines

 

## How 

* [Go Concurrency Example - Let's Build a Concurrent Download Manager - zero dependency
](https://www.youtube.com/watch?v=vdhSk8vCx-k&list=WL&index=1&t=5s)




## More 

* [Summary: Concurrency is not Parallelism](https://medium.com/@k.wahome/concurrency-is-not-parallelism-a5451d1cde8d)
* [译 | Concurrency is not Parallelism](https://www.cyningsun.com/12-09-2019/concurrency-is-not-parallelism.html)
