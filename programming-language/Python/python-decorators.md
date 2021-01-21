# Python Decorators 

![Gun](http://qxf2.com/blog/wp-content/uploads/2014/09/qxf2-gun-decorator1.jpg)

source: [Understanding Python decorators](https://qxf2.com/blog/python-decorators/)


## Why 

* More readable

## What 


> In object-oriented programming, the decorator pattern is a design pattern that allows **behavior** to be added to **an individual object**, dynamically, without affecting the behavior of other objects from the same class.
> 
> The "decorators" we talk about with concern to Python are **not** exactly the same thing as the DecoratorPattern described above. A Python decorator is a **specific change to the Python syntax** that allows us to more conveniently **alter** functions and methods (and possibly classes in a future version). This supports more readable applications of the **DecoratorPattern** but also other uses as well.
> 
> source: [PythonDecorators](https://wiki.python.org/moin/PythonDecorators#What_is_a_Decorator)


## Code 

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