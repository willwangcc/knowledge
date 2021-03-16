# Message Queue and EVent Loop 

> Understand how the message queue and event loop work in JavaScript specifically, and how it affects timing, hang, async, etc.


## This 

* [ ] check MDN 

> The `this` keyword evaluates to the value of the **ThisBinding** of the current execution context

In most cases, the value of `this` is determined by how a function is called.

**ThisBinding** is something that the JavaScript interpreter maintains as it evaluates JavaScript code, like a special CPU register which holds a reference to an object. The interpreter updates the ThisBinding whenever establishing an execution context in one of only three different cases:



**gutcheck:**

1. 

``` javascript 
if (true) {
    // What is `this` here?
}
```
> **window** — The marked line is evaluated in the initial global execution context.



2.

``` javascript 
var obj = {
    someData: "a string"
};

function myFun() {
    return this // What is `this` here?
}

obj.staticFunction = myFun;

console.log("this is window:", obj.staticFunction() == window);
console.log("this is obj:", obj.staticFunction() == obj);
  
```

> **obj** — When calling a function on an object, ThisBinding is set to the object.

3.

``` javascript 
var obj = {
    myMethod: function () {
        return this; // What is `this` here?
    }
};
var myFun = obj.myMethod;
console.log("this is window:", myFun() == window);
console.log("this is obj:", myFun() == obj);
```

> **window**

In this example, the JavaScript interpreter enters function code, but because `myFun` `obj.myMethod` is **not called on an object**, ThisBinding is set to window.

This is different from Python, in which accessing a method (obj.myMethod) creates a bound method object.

4.

``` javascript 
function myFun() {
    return this; // What is `this` here?
}
var obj = {
    myMethod: function () {
        eval("myFun()");
    }
};

```

> **window**

This one was tricky. When evaluating the eval code, `this` is `obj`. However, in the **eval** code, `myFun` is not called on an object, so ThisBinding is set to `window` for the call.

5.

``` javascript 
function myFun() {
    return this; // What is `this` here?
}
var obj = {
    someData: "a string"
};
console.log("this is window:", myFun.call(obj) == window);
console.log("this is obj:", myFun.call(obj) == obj);
```

> **obj**

The line `myFun.call(obj)`; is invoking the special built-in function `Function.prototype.call()`, which accepts **thisArg** as the first argument.

from [How does the “this” keyword work?
](https://stackoverflow.com/questions/3127429/how-does-the-this-keyword-work)

## Call, Apply, Bind 

* **bind**: It binds the function with provided value and context but it does not executes the function. **To execute function you need to call the function**.
* **call**: It executes the function with provided context and **parameter**.
* **apply**: It executes the function with provided context and **parameter as array**.


### Call

> The `call()` method calls a function with a given `this` value and arguments provided individually.

### Apply 

> The `call()` method calls a function with a given this value and arguments provided individually.

### Bind 

> The `bind()` method creates a new function that, when called, has its this keyword set to the provided value, with a given sequence of arguments preceding any provided when the new function is called.


``` javascript 
var module = {
  x: 42,
  getX: function() {
    return this.x;
  }
}

var unboundGetX = module.getX;
console.log(unboundGetX()); // The function gets invoked at the global scope
// expected output: undefined

var boundGetX = unboundGetX.bind(module);
console.log(boundGetX());
// expected output: 42
```

from [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)