<h1 align="center">
<br>
	<a href="https://www.wikiwand.com/en/Double-ended_queue">
  <img src="https://i.imgur.com/zmbcyd5.png" alt="Double-ended queue example" width=42%">
  </a>
  <br><br>
Double-ended queue
  <br><br>
</h1>

> In computer science, a double-ended queue (abbreviated to deque, pronounced deck[1]) is **an abstract data type** that generalizes a queue, for which elements can be **added to or removed** from either the front (head) or back (tail). [[wiki](https://www.wikiwand.com/en/Double-ended_queue)]

## Why 

Start with BFS, which needs deque, list-like container with fast appends and pops on either end.

## How

### [Operations](https://www.wikiwand.com/en/Double-ended_queue#/Operations)

The basic operations on a deque are **enqueue** and **dequeue** on either end. Also generally implemented are **peek** operations, which return the value at that end without dequeuing it.

* insert element at back
* insert element at front
* remove last element
* remove first element
* examine last element
* examine first element

### Complexity

* In a doubly-linked list implementation and assuming no allocation/deallocation overhead, the time complexity of all deque operations is O(1). Additionally, the time complexity of insertion or deletion in the middle, given an iterator, is O(1); however, the time complexity of random access by index is O(n).
* In a growing array, the amortized time complexity of all deque operations is O(1). Additionally, the time complexity of random access by index is O(1); but the time complexity of insertion or deletion in the middle is O(n).

## What 

### Overview

In computer science, a double-ended queue (abbreviated to deque, pronounced deck[1]) is **an abstract data type** that generalizes a queue, for which elements can be **added to or removed** from either the front (head) or back (tail).[2] It is also often called a head-tail linked list, though properly this refers to a specific data structure implementation of a deque (see below).

### Naming conventions

Deque is sometimes written dequeue, but this use is generally **deprecated** in technical literature or **technical writing** because dequeue is also a verb meaning "**to remove from a queue**". Nevertheless, several libraries and some writers, such as Aho, Hopcroft, and Ullman in their textbook Data Structures and Algorithms, spell it dequeue. John Mitchell, author of Concepts in Programming Languages, also uses this terminology.

### Distinctions and sub-types

This differs from the queue abstract data type or first in first out list (FIFO), where elements can only be added to one end and removed from the other. This general data class has some possible sub-types:

* An **input-restricted** deque is one where deletion can be made from both ends, but **insertion** can be made at one end only.
* An **output-restricted** deque is one where insertion can be made at both ends, but **deletion** can be made from one end only.

Both the basic and most common list types in computing, queues and stacks can be considered specializations of deques, and can be implemented using deques.

### Others

* Distinctions and sub-types
* Implementations
* Language support
* Applications


## FAQs

#### Q: keywords vs ?

A: 


