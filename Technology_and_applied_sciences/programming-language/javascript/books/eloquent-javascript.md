# Eloquent JavaScript： Reading notes


## C1. Values, Types, and Operators 

![C1](https://i.imgur.com/zzmLvbX.png)

1. JavaScript uses a fixed number of bits, **64** of them, to store a single number value. 
2. The important thing is to be aware of it and treat **fractional** digital numbers as **approximations**, not as precise values. (e.g. π )
3. `Infinity - 1` is still Infinity, and so on. Don’t put too much trust in infinity-based computation, though. 
4. **`NaN`** stands for “not a number”, even though it is a value of the number type. You’ll get this result when you, for example, try to calculate 0 / 0 (zero divided by zero), **`Infinity - Infinity`**, or any number of other numeric operations that **don’t yield a meaningful result**.
5. If we have a number for every character, a string can be described by **a sequence of numbers**.
6. **Backtick-quoted strings**, usually called **template** literals, can do a few more tricks. 
7. `NaN` is supposed to denote the result of a **nonsensical computation**, and as such, it isn’t equal to the result of any other nonsensical computations.
8. The difference in meaning between `undefined` and `null` is an accident of JavaScript’s design, and it doesn’t matter most of the time. In cases where you actually have to concern yourself with these values, I recommend treating them as mostly **interchangeable**.
9. I mentioned that JavaScript goes out of its way to accept almost any program you give it, even programs that **do odd things**. e.g. `console.log(8 * null) // → 0`
10. I recommend using the **three-character comparison** operators defensively to prevent unexpected type conversions from tripping you up.

## C2. Program Structure

<img src="https://i.imgur.com/cxGuqDp.png
" alt="c2" height="300"/><img src="https://i.imgur.com/xR3hbSQ.png" alt="tentacles" width="200"/>

1. It could display something on the screen—that counts as changing the world—or it could **change the internal state of the machine** in a way that will affect **the statements that come after it**. These changes are called ***side effects***. 
2. You should imagine **bindings** as **tentacles**, rather than boxes. They do not contain values; they **grasp** them — two bindings can refer to the same value. A program can access only the values that it still has a reference to. When you need to remember something, you grow a tentacle to hold on to it or you reattach one of your existing tentacles to it.
3. The collection of bindings and their values that exist at a given time is called the ***environment***.
4. A ***function*** is a piece of program wrapped in a value.
5. Executing a function is called ***invoking***, ***calling***, or ***applying*** it.
6. Though binding names cannot contain period characters, console.log does have one. This is because ***console.log isn’t a simple binding***. It is actually an expression that retrieves the log property from the value held by the consolebinding.
7. Showing a dialog box or writing text to the screen is **a side effect**.
8. Showing a dialog box or writing text to the screen is a side effect. A lot of functions are useful because of the side effects they produce. Functions may also produce values, in which case they don’t need to have a side effect to be useful. #Q 
9. Bindings can be used to file pieces of data under a name, and they are useful for tracking state in your program. ***The environment is the set of bindings that are defined.*** JavaScript systems always put a number of useful **standard** bindings into your environment.
10. **Functions** are special values that **encapsulate** a piece of program.

## C7. Project: A Robot

![](https://i.imgur.com/TFQUNtL.gif)

1. Data structures that don’t change are called `immutable` or `persistent`. They behave a lot like strings and numbers in that they are **who they are and stay that way**, rather than containing different things at different times. 
2. This is about **complexity management** again. When the objects in my system are fixed, stable things, I can consider operations on them in **isolation**—moving to Alice’s house from a given start state always produces the same new state. When objects change over time, that adds a whole new dimension of complexity to this kind of reasoning.
3. Anything that makes your code **easier** to understand makes it **possible** to build a more **ambitious** system.
4. JavaScript functions can be called with extra arguments without ill effects.