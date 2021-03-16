# value types and reference types 

![reference vs value](https://i.imgur.com/d6N0JXg.gif)

> Understand the **difference** between value types and reference types, and assigning **values** vs assigning **pointers**.

check [the best answer: take notes example](https://stackoverflow.com/a/13268731/6011182)

## What 

* Variables that are assigned a non-primitive value are given a reference to that value. That reference points to the object’s location in memory. The variables don’t actually contain the value. 
* Value types are immutable.
* Value types are compared by value.
* Value types are copied by value.


![1](https://i.imgur.com/qpKIBVy.png)

![2](https://i.imgur.com/dRAfw65.png)

--- [JavaScript Primitive vs. Reference Values](http://www.javascripttutorial.net/javascript-primitive-vs-reference-values/)


## Q & A 

### [1](https://stackoverflow.com/questions/639514/how-can-i-get-the-memory-address-of-a-javascript-variable). How can I get the memory address of a JavaScript variable?

> If it would be possible at all, it would be very dependent on the javascript engine. The more modern javascript engine compile their code using a just in time compiler and messing with their internal variables would be either bad for performance, or bad for stability.
>
> If the engine allows it, why not make a function call interface to some native code to exchange the variable's values?


### 2. Why do we need a reference type?

Suppose every time you wanted to refer to the book `The Hobbit`, you had to instead make a copy of the entire text. That is, instead of saying "When I was reading `The Hobbit` the other day...", you'd have to say "When I was reading `In a hole in the ground there lived a hobbit... [all the text] ... Well thank goodness for that, said Bilbo, handing him the tobacco jar.` the other day..."

Now suppose every time you used a database in a program, instead of referring to the database, y*ou simply made a full copy of the entire database, every single time you used any of it in any way.* How fast do you think such a program would be?

References allow you to write sentences that talk about books by use of their titles instead of their contents. Reference types allow you to write programs that **manipulate objects by using small references rather that enormous quantities of data**.

from [Eric](https://stackoverflow.com/questions/9232186/why-do-we-need-reference-types-in-net)

