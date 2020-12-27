# Mutex and semaphore 


<img src="https://i.imgur.com/wzWbIXj.jpg" alt="mutex & semaphore" width="200"/> 

from [semaphore](http://www.ruanyifeng.com/blog/2013/04/processes_and_threads.html)


## Why?

* race condition -> mutex
* [producer consumer problem](https://www.wikiwand.com/en/Producer%E2%80%93consumer_problem) -> semaphore 
* [Barrier](https://www.wikiwand.com/en/Barrier_(computer_science))

## What? 

### Mutex vs Semaphore 

* A binary semaphore works the same way as a mutex 
* Mutex manages **one** units of shared resources while semaphore manages **N** unit of shared resources 
* For a locked mutex it must be unlocked by the **same** thread, but a semaphore can be incremented by a **different** thread 

## Q&A


### ?

Semaphore has two operations, P and V can be implemented with a mutex and a conditional variable. Its logic can be easily expressed with a guarded command.

## Thanks 

- @davidxk
- [Python中的生产者消费者问题](http://blog.jobbole.com/52412/)
- [Producer Consumer Problem using Semaphores | Set 1](https://www.geeksforgeeks.org/producer-consumer-problem-using-semaphores-set-1/)