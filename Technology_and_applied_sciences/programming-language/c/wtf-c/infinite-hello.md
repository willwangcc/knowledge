# Infinite Hello 


## Points 

- Memory layout
- Assembly instruction
- Compiler implementation
- Stack protector
- Big endian and little endian



## Why?

The result is related to the **compiler implementation**, gcc has a compile option (-**fno-stack-protector**) to turn off stack protection. By default, stack protection is enabled. Regardless of whether i is declared before or after, i will push the stack **after the array** and only cycle 4 times. If the stack protection function is **turned off**, an infinite **loop** will occur.

Why?

<img src="https://i.imgur.com/wTrbwzY.png" alt="why infinite hello" width="200"/>

The problem of infinite loops, I think that memory is allocated from the back to the front. For example, in Excel, four grids are pulled down from the top, and the variable `i` is first allocated to the fourth grid of memory. Then the variable arr is allocated three grids of memory above, but the data of arr is allocated from top to bottom. When accessing the third index, it happens to access the memory of the fourth grid, which is the adress of variable `i`.


## Read More 

[GCC 中的编译器堆栈保护技术](https://www.ibm.com/developerworks/cn/linux/l-cn-gccstack/index.html)
