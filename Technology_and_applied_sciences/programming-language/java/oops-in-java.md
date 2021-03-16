# OOPS in Java

> **Object-oriented programming System(OOPs)** is a programming paradigm based on the concept of “objects” that contain data and methods. The primary purpose of object-oriented programming is to increase the flexibility and maintainability of programs. Object oriented programming brings together data and its behaviour(methods) in a single location(object) makes it easier to understand how a program works. 

Java is an object oriented language because it provides the features to implement an object oriented model. These features includes **Abstraction, encapsulation, inheritance and polymorphism**.


## 1. Abstraction

One of the most fundamental concept of OOPs is Abstraction. Abstraction is a process where you show **only “relevant” data** and **“hide” unnecessary details** of an object from the user. For example, when you login to your Amazon account online, you enter your user_id and password and press login, what happens when you press login, how the input data sent to amazon server, how it gets verified is all abstracted away from the you.

## 2. Encapsulation(e.g. create class)

Encapsulation simply means **binding object state(fields) and behaviour(methods) together**. If you are creating class, you are doing **encapsulation**. 

The whole idea behind encapsulation is to **hide the implementation details from users**. If a data member is private it means it can only be accessed within the same class. No outside class can access private data member (variable) of other class.

The idea of encapsulation is to keep classes separated and prevent them from having tightly coupled with each other.

A example of encapsulation is the class of java.util.Hashtable. User only knows that he can store data in the form of key/value pair in a Hashtable and that he can retrieve that data in the various ways. But the actual implementation like, how and where this data is actually stored, is hidden from the user. User can simply use Hashtable wherever he wants to store Key/Value pairs without bothering about its implementation.

Encapsulation is also known as “data Hiding“.


## 3. Inheritance(e.g. subclass)

- [ ] [Java example](https://beginnersbook.com/2015/07/java-swing-tutorial/)

* Inheritance is the mechanism by which an object **acquires the some/all properties** of another object.
* It supports the concept of hierarchical classification.

For example: Car is a four wheeler vehicle so assume that we have a class FourWheeler and a sub class of it named Car. Here Car acquires the properties of a class FourWheeler. Other classifications could be a jeep, tempo, van etc. FourWheeler defines a class of vehicles that have four wheels, and specific range of engine power, load carrying capacity etc. Car (termed as a sub-class) acquires these properties from FourWheeler, and has some specific properties, which are different from other classifications of FourWheeler, such as luxury, comfort, shape, size, usage etc.

A car can have further classification such as an open car, small car, big car etc, which will acquire the properties from both Four **Wheeler** and **Car**, but will still have some specific properties. This way the level of hierarchy can be extended to any level.


## 4. Polymorphism(e.g. sub method)

* Polymorphism means to process objects differently **based on their data type.**
* In other words it means, **one method with multiple implementation, for a certain class of action**. And which implementation to be used is decided **at runtime** depending upon the situation (i.e., data type of the object)
* This can be implemented by designing a generic interface, which provides generic methods for a certain class of action and there can be multiple classes, which provides the implementation of these generic methods.

Lets us look at same example of a car. A car have a gear transmission system. It has four front gears and one backward gear. When the engine is accelerated then depending upon which gear is engaged different amount power and movement is delivered to the car. The action is same applying gear but based on the type of gear the action behaves differently or you can say that it shows many forms (polymorphism means **many forms**)


Polymorphism could be static and dynamic both. Method **Overloading** is **static** polymorphism while, Method overriding is dynamic polymorphism.

* **Overloading** in simple words means **more than one method having the same method name that behaves differently** based on the arguments passed while calling the method. This called static because, which method to be invoked is decided at the time of **compilation**
* **Overriding** means a **derived** class is implementing a method of its super class. The call to overriden method is resolved **at runtime**, thus called runtime polymorphism


## Thanks 

- [OOPs in Java: Encapsulation, Inheritance, Polymorphism, Abstraction](https://beginnersbook.com/2013/03/oops-in-java-encapsulation-inheritance-polymorphism-abstraction/)
- [Encapsulation in Java with example](https://beginnersbook.com/2013/05/encapsulation-in-java/)