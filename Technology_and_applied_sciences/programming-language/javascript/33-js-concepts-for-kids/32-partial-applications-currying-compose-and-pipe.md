# 32. Partial Applications, Currying, Compose and Pipe

## Currying

![currying](https://i.imgur.com/jK1N81y.gif)

### Why currying?

A programmer’s pipe-dream is to write code, and be able to use it repeatedly with little effort. It’s expressive because you write in a way that expresses what is needed, and it’s reuse because.. well, you’re reusing. What more could you want?

[curry can help](https://hughfdjackson.com/javascript/why-curry-helps/).

**Pros**: 

* **Little pieces** can be **configured** and **reused** with ease, without clutter;
* Functions are used **throughout**.

Before:

``` javascript 
var add = function(a, b){ return a + b }
add(1, 2) //= 3
```

``` javascript 
add(1, 2, 'IGNORE ME') //= 3
add(1) //= NaN
```

After:

``` javascript 
var sum3 = curry(function(a, b, c){ return a + b + c })
sum3(1, 2, 3) //= 6
sum3(1)(2, 3) //= 6
sum3(1, 2)(3) //= 6
```


### What is currying?

> There is a way to reduce functions of more than one argument to functions of one argument, a way called currying after Haskell B. Curry. [1]
> 

**Currying** is a process to reduce functions of more than one argument to functions of one argument with the help of lambda calculus.

只传递给函数一部分参数来调用它，让它返回一个函数去处理剩下的参数。

``` javascript 
multiply = (n, m) => (n * m)
multiply(3, 4) === 12 // true

curryedMultiply = (n) => ( (m) => multiply(n, m) )
triple = curryedMultiply(3)
triple(4) === 12 // true
```


## Reference 

- [Why Curry Helps](https://hughfdjackson.com/javascript/why-curry-helps/): 生动形象