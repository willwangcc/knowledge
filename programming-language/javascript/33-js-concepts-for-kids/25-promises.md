# Promise 

![promise](https://i.imgur.com/JIqQdt5.png)

> The **Promise** object represents the eventual completion (or failure) of an asynchronous operation, and its resulting value.


## Why do we use Promise?

Promises provide a **mechanism** to handle the **results** and **errors** from **asynchronous** operations. You can accomplish the same thing with callbacks, but promises provide improved **readability** via **method chaining and succinct error handling**.

``` javascript 
const isGreater = (a, b) => {
return new Promise ((resolve, reject) => {
  if(a > b) {
    resolve(true)
  } else {
    reject(false)
  }
  })
}
isGreater(1, 2)
.then(result => {
  console.log('greater')
})
.catch(result => {
  console.log('smaller')
})
```

### What are the pros and cons of using Promises instead of callbacks?

Pros:

* **Avoid callback hell** which can be **unreadable**.
* Makes it easy to write **sequential asynchronous code** that is readable with `.then()`.
* Makes it easy to write parallel asynchronous code with `Promise.all()`.

Cons:

* Slightly more complex code (debatable).
* In older browsers where ES2015 is not supported, you need to load a polyfill in order to use it. 

## 项目

- [原生es6封装一个Promise对象](https://juejin.im/post/5bfc9e4ee51d451dca4794af) : 实现一个Promise 