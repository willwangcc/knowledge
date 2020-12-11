# Shell: a type of user interface

<center>
<img src="https://i.imgur.com/M5P2i7e.jpg" alt="Shell in Linux" width="250"/>
</center>

source: 《Advanced Programming in Unix Environment》

## Why?

In general, operating system shells use either **a command-line interface (CLI)** or **graphical user interface (GUI)**, depending on a computer's role and particular operation. It is named a shell because it is the **outermost layer** around the operating system.

## What?

> In computing, **a shell** is a **user interface** for access to an operating system's services.
> 
> source: [wiki](https://www.wikiwand.com/en/Shell_(computing))

库函数面向开发者，Shell面向用户。

Linux将高频「系统调用」(system call)组合封装成「库函数」，类比的话，「库函数」就像是汉字的**偏旁部首**(高频)，而「系统调用」如同汉字的**笔画**(基础)。

举个例子，一个简单的给变量分配内存空间的操作，需要动用多个系统调用。所以，分配内存这样的高频操作，就被定义成了一个库函数，如malloc()。将开发者从细节中解放出来。

而**Shell**则面向用户。一个shell对应一个终端 (terminal)。在计算机的上古时期，在GUI(图形用户界面)没有出现前，用户是在terminal上(实实在在的硬件)上与操作系统交互的，而shell就是为用户提供与硬件交流的界面。

现在，我们使用的应用，它可以

1. 直接调用系统函数
2. 调用库函数 (系统调用的模块化)
3. 运行shell脚本 （整合程序）
  

