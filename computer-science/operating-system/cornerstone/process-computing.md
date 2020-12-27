<h1 align="center">
<br>
	<a href="https://www.wikiwand.com/en/Process_(computing)">
  <img src="https://i.imgur.com/cyQ3ElJ.png" alt="various process states" width=42%">
  </a>
  <br><br>
Process (computing) 
  <br><br>
</h1>

> In computing, a process is the **instance** of a computer program that is being **executed** by one or many threads. [[wiki](https://www.wikiwand.com/en/Process_(computing))]

## Why 

**Process** is part of elements in both prallel computing and operating system.

## How

[Process management (computing) ](https://www.wikiwand.com/en/Process_management_(computing))

## What 

### overview

In computing, a process is the **instance** of a **computer program** that is being **executed** by one or many **threads**. It contains the program **code** and its **activity**. Depending on the operating system (OS), a process may be made up of multiple threads of execution that execute instructions **concurrently**.

### representation 

In general, a computer system process consists of (or is said to own) the following resources:

* An image of the executable machine **code** associated with a program.
* **Memory** (typically some region of virtual memory); which includes the executable code, process-specific data (input and output), a call stack (to keep track of active subroutines and/or other events), and a heap to hold intermediate computation data generated during run time.
* Operating system **descriptors of resources** that are allocated to the process, such as file descriptors (Unix terminology) or handles (Windows), and data sources and sinks.
* Security **attributes**, such as the process owner and the process' set of permissions (allowable operations).
* Processor **state** (context), such as the content of registers and physical memory addressing. The state is typically stored in computer registers when the process is executing, and in memory otherwise.

### others

* history
* Multitasking and process management
* Inter-process communication

## FAQs

#### Q: process vs computer program?

A: While a computer **program** is a passive collection of instructions, a **process** is the **actual execution of those instructions**. Several processes may be associated with the same program; for example, opening up several **instances** of the same program often results in more than one process being executed.

#### Q: Process vs Thread?

A: 

* Process: an abstract of **address space**, passive.
* Thread: an abstract of **CPU run-time stack**, active.

source: [Processes and Threads](http://www.qnx.com/developers/docs/6.4.1/neutrino/getting_started/s1_procs.html):  A intuitive explanation 

