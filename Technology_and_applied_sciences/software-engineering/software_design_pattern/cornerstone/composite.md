# Composite


> Composite is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects.  [[refactor](https://refactoring.guru/design-patterns/composite)]


## What 

- The Composite Pattern can bring symmetry not only to object hierarchies in Python, but even to hierarchies exposed by low-level system calls and high-level network applications. In Python, the Composite Pattern can often be implemented with less fuss than in tightly constrained object oriented languages. You won’t be forced to inherit your container objects and the objects inside of them from a common parent class. **Instead, you can build classes that share only a common interface rather than any implementation** — or that are simply duck typed to offer common behavior. - [Gang of Four book](https://python-patterns.guide/gang-of-four/)


> The Composite Pattern suggests that whenever you design “container” objects that collect and organize what we’ll call “content” objects, you will simplify many operations if you give container objects and content objects a shared set of methods and thereby support as many operations as possible without the caller having to care whether they have been passed an individual content object or an entire container. [[python-pattern](https://python-patterns.guide/gang-of-four/composite/)]

## Why 

## How 

- The art of using the Composite Pattern is determining where to break the symmetry. 


## Example 

- [the UNIX file system](https://python-patterns.guide/gang-of-four/composite/)
	- `ls` on both files and directories 
	- different commands `touch` for creating a new file and `mkdir` for creating a new directory 

## Reference

- [The Composite Pattern](https://python-patterns.guide/gang-of-four/composite/)