# Closure 

> In programming languages, a closure, also lexical closure or function closure, is a **technique** for **implementing lexically scoped name binding** in a language with **first-class functions**. 
> 
> source: [wiki](https://www.wikiwand.com/en/Closure_(computer_programming))

## Why 

Closures can avoid **the use of global values** and provides some form of **data hiding**. It can also provide an object oriented solution to the problem.

When there are few methods (one method in most cases) to be implemented in a class, closures can provide **an alternate and more elegant solution**. But when the number of attributes and methods get larger, it's better to implement a class.

## What 

A Closure is **a function object** that remembers values in enclosing scopes even if they are not present in memory. 

* **Nested Function**: function defined inside another function. 
* **Name binding**:  name binding is the association of entities (data and/or code) with identifiers.
* **First-class function**: a programming language is said to have first-class functions if it treats functions as first-class citizens. This means the language supports **passing functions as arguments to other functions**, **returning** them as the **values** from other functions, and **assigning** them to variables or storing them in data structures.

## Code

[closure](https://repl.it/@WillWang42/python-closure)

Here is a simple example where a closure might be more preferable than defining a class and making objects. But the preference is all yours.



``` python
# https://www.programiz.com/python-programming/closure

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier
    
# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))    
```
