# 8.3 Collections

> This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple. [[docs.python.org/3](https://docs.python.org/3/library/collections.html)]

## Why 

This module implements specialized container datatypes providing **alternatives** to Python’s general purpose built-in containers, dict, list, set, and tuple.

## How

1. `namedtuple()`: factory function for creating **tuple subclasses** with named fields
1. [`deque`](https://docs.python.org/3/library/collections.html#deque-objects): list-like container with **fast appends and pops** on either end
1. `ChainMap`: dict-like class for creating **a single view of multiple mappings**
1. `Counter`: dict subclass for **counting hashable objects**
1. [`OrderedDict`](https://repl.it/@WillWang42/collections-orderedDict): dict subclass that **remembers the order entries** were added
1. `defaultdict`: dict subclass that calls a factory function to **supply missing values**
1. `UserDict`: wrapper around dictionary objects for **easier dict subclassing**
1. `UserList`: wrapper around list objects for **easier list subclassing**
1. `UserString`: wrapper around string objects for **easier string subclassing**

### [deque](https://gto76.github.io/python-cheatsheet/#deque)

A thread-safe list with efficient appends and pops from either side. Pronounced "deck". More on [pymotw.com](https://pymotw.com/3/collections/deque.html)


``` python
from collections import deque
<deque> = deque(<collection>, maxlen=None)
<deque>.appendleft(<el>)                       # Opposite element is dropped if full.
<deque>.extendleft(<collection>)               # Collection gets reversed.
<el> = <deque>.popleft()                       # Raises IndexError if empty.
<deque>.rotate(n=1)                            # Rotates elements to the right.
```

## What 

* factory function
* container
* class
* subclass
* **wrapper**: 
	* Wrapper pattern, where some computer programming code allows certain classes to work together that otherwise would not
	* Wrapper function, a function whose main purpose is to call a second function
 	