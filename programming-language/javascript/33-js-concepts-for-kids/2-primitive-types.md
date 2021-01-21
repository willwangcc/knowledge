# Primitive Types 

> Understand how different primitive types are **stored** in memory, down to the **addresses**, space **allocated**, and binary **representation** (if you haven’t run into the word mantissa you’re not far enough).

![primitive types](https://i.imgur.com/VP7HrmP.png)

## Summary 
> A primitive (primitive value, primitive data type) is data that is not an object and has no methods. In JavaScript, there are **6** primitive data types: `string`, `number`, `boolean`, `null`, `undefined`, `symbol` (new in ECMAScript 2015).
>
> Most of the time, a primitive value is represented directly at the lowest level of the language implementation.
>
> All primitives are **immutable**, i.e., they cannot be altered. It is important not to confuse a primitive itself with a variable assigned a primitive value. The variable may be reassigned a new value, but the existing value can not be changed in the ways that objects, arrays, and functions can be altered.


``` javascript 
// Primitive types
'bar' instanceof Object; // false
0 instanceof Object; // false
true instanceof Object; // false

null instanceof Object; // false
undefined instanceof Object; // false

const symbol = Symbol(42);
Symbol instanceof Object; // false

// Non-primitive types
const foo = function () {}
foo instanceof Object; // true
```

## Q & A 

目录：

1. How numbers are encoded in JavaScript? 
2. Why Strings, booleans and numbers can be represented as a primitive type but also as an object?
3. What is the motivation for bringing Symbols to ES6?



### 1. How numbers are encoded in JavaScript? 

There are no integers in JavaScript.

`number` - double-precision 64-bit float.

``` javascript 
var biggestNum = Number.MAX_VALUE;

var biggestInt = 9007199254740991;
var smallestInt = -9007199254740991;

Number('12.3')    // 12.3
Number('123e-1')  // 12.3
Number('0x11')    // 17
Number('foo')     // NaN

```
-- [How numbers are encoded in JavaScript](http://2ality.com/2012/04/number-encoding.html)


### 2. Why Strings, booleans and numbers can be represented as a primitive type but also as an object?

> You can use constructor functions to create a new object.

Certain primitive types (strings, numbers, booleans) appear to behave like objects because of a JavaScript featured called **autoboxing**.

```  javascript 
const pet = new String("dog")
typeof pet; // "object"
pet == "dog"; // true 
pet === "dog"; // false
```

[Why do we need **autoboxing**?](https://stackoverflow.com/questions/27647407/why-do-we-use-autoboxing-and-unboxing-in-java)

1. 代码更加简洁
1. 基本数据类型可以使用泛型



### 3. What is the motivation for bringing Symbols to ES6?

Before & After. 

ES5 的对象属性名都是字符串，这容易造成属性名的冲突。如果有一种机制，**保证每个属性的名字都是独一无二**的就好了，这样就从根本上防止属性名的冲突。这就是 ES6 引入Symbol的原因。

Before: 

```javascript 
var race = {
  protoss: 'protoss', // 神族
  terran: 'terran', // 人族
  zerg: 'zerg' // 虫族
}

function createRole(type){
  if(type === race.protoss){创建神族角色}
  else if(type === race.terran){创建人族角色}
  else if(type === race.zerg){创建虫族角色}
}
```
 
``` javascript 
// 传入字符串
createRole('zerg') 
// 或者传入变量
createRole(race.zerg)
```

After:

``` javascript 
var race = {
  protoss: Symbol(),
  terran: Symbol(),
  zerg: Symbol()
}

race.protoss !== race.terran // true
race.protoss !== race.zerg // true
```

example from [「每日一题」JS 中的 Symbol 是什么？](https://zhuanlan.zhihu.com/p/22652486)