<h1 align="center">
<br>
	<a href="https://www.wikiwand.com/en/Python_syntax_and_semantics#/Decorators">
    <img src="http://qxf2.com/blog/wp-content/uploads/2014/09/qxf2-gun-decorator1.jpg" alt="Understanding Python decorators" width=42%">
  </a>
  <br><br>
Python Decorators 
  <br><br>
</h1>

> A Python decorator is a **specific change to the Python syntax** that allows us to more conveniently **alter** functions and methods (and possibly classes in a future version). [[wiki.python.org](https://wiki.python.org/moin/PythonDecorators#What_is_a_Decorator)]





## Why 

* More readable


## How 

[Decorators](https://repl.it/@WillWang42/decorator)

``` python
# https://www.programiz.com/python-programming/decorator

def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

print(divide(2,5))

# Output
# I am going to divide 2 and 5
# 0.4

```

## What 

### Overview

A decorator is any callable Python object that is used to modify a function, method or class definition. A decorator is passed the original object being defined and returns a modified object, which is then bound to the name in the definition. Python decorators were inspired in part by Java annotations, and have a similar syntax; the decorator syntax is pure syntactic sugar, using @ as the keyword:

``` python 
@viking_chorus
def menu_item():
    print("spam")
```
is equivalent to

``` python
def menu_item():
    print("spam")
menu_item = viking_chorus(menu_item) 
``` 
 
..

## FAQs

#### Q: Good resource about python decorator?

A: 

* [PythonDecorators](https://wiki.python.org/moin/PythonDecorators#What_is_a_Decorator)
* [Understanding Python decorators](https://qxf2.com/blog/python-decorators/)
