# Why Python3? Show me the code 

## 1. Unicode8

## 2. dict.iteritems() vs. dict.items()

> There should be one-- and preferably only one --obvious way to do it. —— *The Zen of Python*

In python2,
`dict.items()` returns a **copy** of list of 2-tuples ([(key, value), (key, value), ...]), whereas `dict.iteritems()` is a generator that yields 2-tuples. The former takes more space and time initially, but accessing each element is fast, whereas the second takes less space and time initially, but a bit more time in generating each element.

Generators were introduced to the language in general.

In python3,
One of Python 3’s changes is that  items() now return iterators, and a list is never fully built. 


source: 

- [What is the difference between dict.items() and dict.iteritems()?](https://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems)
- [PEP 3106 -- Revamping dict.keys(), .values() and .items()](https://www.python.org/dev/peps/pep-3106/#id3)
- [Doc: Views And Iterators Instead Of Lists¶](https://docs.python.org/3/whatsnew/3.0.html#views-and-iterators-instead-of-lists)

``` python 
python2 = {"a":1, "b":2}
print python2.items()
print type(python2.items())
for key,val in python2.iteritems():
  print key, val

output:
# [('a', 1), ('b', 2)]
# <type 'list'>
# a 1
# b 2

python3 = {"a":1, "b":2}
print(python3.items())
print(type(python3.items()))
for key,val in python3.items():
  print(key, val)
  
output: 
# dict_items([('a', 1), ('b', 2)])
# <class 'dict_items'>
# a 1
# b 2  

```
