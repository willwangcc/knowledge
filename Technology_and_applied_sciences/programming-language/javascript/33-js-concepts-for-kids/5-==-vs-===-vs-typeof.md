# == vs === vs typeof


> **Always** use `===`, unless you have a good reason to use `==`.

JavaScript has both strict and type–converting comparisons:

* **Strict comparison** (e.g., `===`) checks for value equality without allowing coercion
* **Abstract comparison** (e.g. `==`) checks for value equality with coercion allowed


Using `==` will try and convert one side of the expression to be the same type as the other. e.g. `string`, `number`, `boolean`, `null`, `undefined`, `symbol` 

``` javascript 
let a = "42";
let b = 42;

a == b;            // true
a === b;        // false
```

Besides, `==` compares **object references**, it checks to see if the two operands point to the same object (not equivalent objects, the same object).


``` javascript 
let a = [1,2,3]
let b = [1,2,3]
console.log(typeof(a)) // object
console.log(a == b) // false 
console.log(a === b) // false 
```