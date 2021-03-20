# Design patterns with illustrations

## Features

- before and after 
- get the intuition by pictures

## Design pattern

### Creational
Creational design patterns are concerned with **how objects are created.** Normally we create objects by calling their constructor (i.e., **calling their class object with arguments**), but sometimes we need more **flexibility** in how objects are created — which is why the creational design patterns are useful.

For Python programmers, some of these patterns are fairly similar to each other — and some of them, as we will note, aren’t really needed at all. This is because the original design patterns were primarily created for the **C++ language** and needed to work around some of that language’s limitations. **Python doesn’t have those limitations.**


1. [x] **Simple Factory🏠**: Simple factory simply **generates an instance for client without exposing any instantiation logic** to the client e.g. door 
2. [ ] Factory Method🏭: Factory Method is a creational design pattern that provides an interface for creating objects in a **superclass**, but allows **subclasses** to alter the type of objects that will be created.
- [ ] Abstract Factory🔨: A factory of factories e.g. door & experts
- [ ] Builder👷: Builder is a creational design pattern that lets you construct complex objects **step by step**. The pattern allows you to produce **different** types and representations of an object using the **same** construction code. 
- [ ] Prototype🐑: Prototype is a creational design pattern that lets you copy existing objects **without** making your code dependent on their classes.
- [ ] Singleton💍: Singleton is a creational design pattern that lets you ensure that a class has only **one instance**, while providing a global access point to this instance.


### Structural 
The primary concern of structural design patterns is **how objects are composed together to form new, larger objects.**

Three themes stand out in structural design patterns: adapting interfaces, adding functionality, and handling collections of objects.

- **Adapter**: Adapter pattern lets you wrap an otherwise **incompatible** object in an adapter to make it **compatible** with another class. e.g. card reader, power adapter.
- **Bridge**: Consider you have a website with different pages and you are supposed to allow the user to change the theme. What would you do? Create multiple copies of each of the pages for each of the themes or would you just create separate theme and load them based on the user's preferences? Bridge pattern allows you to do the second
- [Composite](https://www.wikiwand.com/en/Composite_pattern): Composite is a structural design pattern that lets you **compose** objects into tree structures and then work with these structures as if they were **individual** objects.
- **Decorator**: Decorator pattern lets you dynamically change the behavior of an object at run time by wrapping them in an object of a decorator class.
- Facade
- **Flyweight**: Flyweight is a structural design pattern that lets you fit more objects into the available amount of RAM by **sharing** common parts of state between multiple objects instead of **keeping** all of the data in each object. 




### Behavioral                 
The behavioral patterns are concerned with **how things get done**; that is, with algorithms and object interactions. They provide powerful ways of thinking about and organizing computations, and like a few of the patterns seen in the previous two chapters, some of them are supported directly by built-in Python syntax.

The Perl programming language’s well-known motto is, “there’s more than one way to do it”; whereas in Tim Peters’ Zen of Python, “there should be one—and preferably only one—obvious way to do it”. Yet, like any programming language, there are sometimes two or more ways to do things in Python, especially since the introduction of comprehensions (use a comprehension or a for loop) and generators (use a generator expression or a function with a yield statement). And as we will see in this chapter, Python’s support for coroutines adds a new way to do certain things.


1. [ ] Chain of Responsibility🔗: It helps building a chain of objects. Request enters from one end and keeps going from object to object till it finds the **suitable** handler.
- [ ] Command👮: Allows you to encapsulate actions in objects. The key idea behind this pattern is to provide the means to decouple **client** from **receiver**.
- [ ] Iterator➿: An iterator returns items from a collection one at a time until it has returned all items from the collection.
- [ ] Mediator👽: A general example would be when you talk to someone on your mobile phone, there is a network provider sitting between you and them and your conversation goes through it instead of being directly sent. In this case **network provider** is mediator.
- [ ] Memento💾: The memento pattern is a software design pattern that provides the ability to restore an object to its previous state (undo via rollback).
- [ ] Observer😎: A good example would be the job seekers where they **subscribe** to some job posting site and they are notified whenever there is a matching job opportunity.
- [ ] Visitor🏃: Visitor is a behavioral design pattern that lets you separate **algorithms** from the **objects** on which they operate.
- [ ] Strategy💡: Strategy pattern allows you to switch the algorithm or strategy based upon the situation.
- [ ] State💢: Imagine you are using some **drawing** application, you choose the paint brush to draw. Now the brush changes its behavior based on the selected color i.e. if you have chosen red color it will draw in red, if blue then it will be in blue etc. State is a behavioral design pattern that lets an object **alter its behavior** when its internal **state** changes. It appears as if the object changed its class.
- [ ] Template Method📒：Template method defines the **skeleton** of how a certain algorithm could be performed, but defers the implementation of those steps to the children classes.



## Reference

- [Python in Practice](https://github.com/lovexiaov/python-in-practice): Create Better Programs Using Concurrency, Libraries, and Patterns. (Dr Dobbs JOLT best book award 2014. )
- [design patterns for humans](https://github.com/kamranahmedse/design-patterns-for-humans): 5 mins read each
- [Design Patterns Game](http://designpatternsgame.com/): “Gang of Four” patterns in JavaScript
- [dive into design patterns](https://sourcemaking.com/design_patterns)
- [Design Patterns Illustrated](https://www.slideshare.net/HermanPeeren/design-patterns-illustrated/37-Iterator_Enable_sequential_access_to)
- [Object-Oriented Design Patterns in Life](https://www.sihui.io/design-patterns/)
- [Refactoring](https://refactoring.guru/design-patterns/catalog)
- [Python Patterns](https://python-patterns.guide)
- [Useful posters of the GoF patterns](http://www.celinio.net/techblog/?p=65)


## More 

- [Understanding The Visitor Design Pattern](https://www.youtube.com/watch?v=TeZqKnC2gvA)
