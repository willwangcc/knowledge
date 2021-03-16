# programming paradigms 


## Todo list 
- [ ]  Read Papers [Programming Paradigms for Dummies: What Every Programmer Should Know
](https://www.info.ucl.ac.be/~pvr/VanRoyChapter.pdf)
- [ ] Read Book [Seven Languages in Seven Weeks](https://book.douban.com/subject/10555435/)
- [ ] Read book [冒号课堂](https://book.douban.com/subject/4031906/)
- [ ] [The Forgotten History of OOP](https://medium.com/javascript-scene/the-forgotten-history-of-oop-88d71b9b2d9f) : OOP往事

![programming paradigms](https://i.imgur.com/Eb7zJtc.png)


## Functional programming

### 起源于问题

> 学函数语言，基本都会遇到map, reduce, filter, zip这些经典的高阶函数 -- [问题起源](https://i.imgur.com/0KrExOG.png)
 
在研究 First-order function, 读到这样一句话，产生疑惑：map, reduce, filter, zip 和 函数式语言 有什么关系呢？

第一版回答： 因为它们具有`functional programming` 的特征， 强调**执行的结果而非执行的过程**, 避免**使用程序状态以及易变物件**, 没有**side effects**, 如同**lambda calculus**。
 
### 发展于思考，阅读，与交流 
 
> In computer science, **functional programming** is a programming paradigm—a style of building the structure and elements of computer programs—that treats **computation** as the **evaluation of mathematical functions** and avoids **changing-state and mutable data**. It is a declarative programming paradigm, which means programming is done with **expressions** or **declarations**[1] instead of statements.

> 函数式编程（英语：functional programming）或称函数程序设计，又称泛函编程，是一种编程典范，它将电脑运算视为数学上的函数计算，并且避免使用程序状态以及易变物件。函数程式语言最重要的基础是λ演算（**lambda calculus**）。而且λ演算的函数可以接受函数当作输入（引数）和输出（传出值）。

> 比起指令式编程，函数式编程更加强调程序**执行的结果而非执行的过程**，倡导利用若干简单的**执行单元**让计算结果不断**渐进**，逐层推导复杂的运算，而不是设计一个复杂的执行过程。


### Code styles 

**Functional programming** is very different from imperative programming. The most significant differences stem from the fact that functional programming **avoids side effects**, which are used in imperative programming to implement state and I/O. Pure functional programming completely prevents side-effects and provides referential transparency.

Imperative programs have the environment and a sequence of steps manipulating the environment. **Functional programs** have an expression that is **successively substituted** until it reaches normal form. An example illustrates this with different solutions to the same programming goal (calculating Fibonacci numbers).

Printing first 10 Fibonacci numbers, **iterative**

```python 
def fibonacci(n, first=0, second=1):
    for _ in range(n):
        print(first) # side-effect
        first, second = second, first + second # assignment
fibonacci(10)
```

Printing first 10 Fibonacci numbers, **functional expression style**

```python
fibonacci = (lambda n, first=0, second=1:
    "" if n == 0 else
    str(first) + "\n" + fibonacci(n - 1, second, first + second))
print(fibonacci(10), end="")
```

Printing a list with first 10 Fibonacci numbers, with **generators**

```python 
def fibonacci(n, first=0, second=1):
    for _ in range(n):
        yield first
        first, second = second, first + second # assignment
print(list(fibonacci(10)))
```

Printing a **list** with first 10 Fibonacci numbers, **functional expression style**

``` python 
fibonacci = (lambda n, first=0, second=1:
    [] if n == 0 else
    [first] + fibonacci(n - 1, second, first + second))
print(fibonacci(10))
```

Printing first 10 Fibonacci numbers, **recursive style**

``` python 
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

for n in range(10):
    print(fibonacci(n))
```


## Thanks 
- [wiki: functional programming](https://www.wikiwand.com/en/Functional_programming#/Coding_styles)


