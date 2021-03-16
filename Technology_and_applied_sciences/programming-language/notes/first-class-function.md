<h1 align="center">
<br>
	<a href="https://www.wikiwand.com/en/First-class_function">
  <img src="https://i.imgur.com/jvGarqI.png" alt="Example | Pass a function as an Argument" width=42%">
  </a>
  <br><br>
First-class function
  <br><br>
</h1>

> In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens. This means the language supports passing functions as arguments to other functions, returning them as the values from other functions, and assigning them to variables or storing them in data structures. [[wiki](https://www.wikiwand.com/en/First-class_function)]

## Why 

start with why, to connect it with what you already know

## How

source: [http://rosettacode.org/](http://rosettacode.org/wiki/First-class_functions#Python)

``` python
>>> # Some built in functions and their inverses
>>> from math import sin, cos, acos, asin
>>> # Add a user defined function and its inverse
>>> cube = lambda x: x * x * x
>>> croot = lambda x: x ** (1/3.0)
>>> # First class functions allow run-time creation of functions from functions
>>> # return function compose(f,g)(x) == f(g(x))
>>> compose = lambda f1, f2: ( lambda x: f1(f2(x)) )
>>> # first class functions should be able to be members of collection types
>>> funclist = [sin, cos, cube]
>>> funclisti = [asin, acos, croot]
>>> # Apply functions from lists as easily as integers
>>> [compose(inversef, f)(.5) for f, inversef in zip(funclist, funclisti)]
[0.5, 0.4999999999999999, 0.5]
>>>
```


## What 

### Overview

In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens. This means the language supports 

* **passing functions as arguments** to other functions, 
* returning them as the **values** from other functions, and 
* assigning them to **variables** or storing them in data structures. 

Some programming language theorists require support for anonymous functions (function literals) as well. In languages with first-class functions, the names of functions do not have any special status; they are treated like **ordinary variables** with a function type. 

### History

The term was coined by Christopher Strachey in the context of "functions as first-class citizens" in the mid-1960s.

### Example 

First-class functions are a necessity for the functional programming style, in which the use of higher-order functions is a standard practice. A simple example of a higher-ordered function is the map function, which takes, as its arguments, a function and a list, and returns the list formed by applying the function to each member of the list. For a language to support **map**, it must support passing a function as an argument.

``` python
# Double all numbers using map and lambda 
  
numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(list(result)) 
```

## FAQs

#### Q: keywords vs ?

A: 

#### Q: any real-world example?

A: 

