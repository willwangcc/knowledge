# Interview question 

##  To do 


* [x] [面经:V. Debounce / Throttle](https://github.com/caomingkai/Front-End-Common-Problems/blob/master/Note-of-Eloquent-JavaScript-JS-and-Browser.md#v-debounce--throttle) : 会写会讲
* [x] [面经: How-to-Make-Animation-using-JS.md](https://github.com/caomingkai/Front-End-Common-Problems/blob/master/How-to-Make-Animation-using-JS.md) : 如何移动一个图片
* [setTimeout vs setInterval](https://github.com/caomingkai/Front-End-Common-Problems/blob/master/setTimeout-vs-setInterval.md) : 重点
* [Facebook Interview Preparation](https://caomingkai.github.io/2018/10/06/Facebook-Interview-Preparation/) : 最后看
* [Event Emitter](https://github.com/caomingkai/Front-End-Common-Problems/blob/master/Event-Emitter.md) : 面经题
* [Auto-complete Implementation](https://github.com/caomingkai/Front-End-Common-Problems) : 必知
* [算法题](https://github.com/caomingkai/Front-End-Common-Problems) : 必知
* [排序算法 in JavaScript](https://github.com/caomingkai/Front-End-Common-Problems/blob/master/Sorting-Algorithms-in-JS.md)
* [Stack & Queue in JavaScript](https://github.com/caomingkai/Front-End-Common-Problems) 面试题
* [Trie Tree in JavaScript](https://github.com/caomingkai/Front-End-Common-Problems)
* [Find 1st Bad Version](https://github.com/caomingkai/Front-End-Common-Problems/blob/master/Coding-Problem-find-the-1st-Bad-Version.md)
* [Flatten an Nested Array](https://github.com/caomingkai/Front-End-Common-Problems/blob/master/How-to-Flatten-an-Array.md) 常考题
* [Reposition Elements in an Array](https://github.com/caomingkai/Front-End-Common-Problems/blob/master/Reposition-an-Array.md)
* [Search for a Symmetric Node](https://github.com/caomingkai/Front-End-Common-Problems/blob/master/Search-for-a-Symmetric-Node.md)
* [26个精选的JavaScript面试问题](https://juejin.im/post/5bd95d22e51d45685f442f73)
* [Concurrency model and Event Loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop) : 理解异步执行的原理，stack vs heap 
* ES6 新特性

* [大部分人都会做错的经典闭包面试题](https://www.cnblogs.com/xxcanghai/p/4991870.html)


Some additional links our engineers found helpful

* **Helpful** Examples: http://www.sitepoint.com/5-typical-javascript-interview-exercises/
* Learn JavaScript | **MDN**: https://developer.mozilla.org/en-US/Learn/JavaScript
* **Video**: Douglas Crockford, "**Advanced JavaScript**:" https://www.youtube.com/watch?v=DwYPG6vreJg
* **Eloquent JavaScript**: http://eloquentjavascript.net/
* Learning **Advanced** JavaScript: http://ejohn.org/apps/learn/
* JavaScript **Garden**: http://bonsaiden.github.io/JavaScript-Garden/


## callback

![callback](https://i.imgur.com/DLnhczu.gif)

I am going to try to keep this dead simple. **A "callback" is any function that is called by another function which takes the first function as a parameter.** A lot of the time, **a "callback" is a function that is called when something happens.** That something can be called an "event" in programmer-speak.

Imagine this scenario: you are expecting a package in a couple of days. The package is a gift for your neighbor. Therefore, once you get the package, you want it brought over to the neighbors. You are out of town, and so you leave instructions for your spouse.

You could tell them to get the package and bring it to the neighbors. If your spouse was as stupid as a computer, they would sit at the door and wait for the package until it came (NOT DOING ANYTHING ELSE) and then once it came they would bring it over to the neighbors. But there's a better way. Tell your spouse that ONCE they receive the package, they should bring it over the neighbors. Then, they can go about life normally UNTIL they receive the package.

In our example, the receiving of the package is the "event" and the bringing it to the neighbors is the "callback". Your spouse "runs" your instructions to bring the package over only when the package arrives. Much better!

by 

```javascript 
// 异步
function fn(cb){
console.log(1); 
setTimeout(cb,1000); 
console.log(3);
}

function cb(){console.log(2)}

fn(cb)
// 1
// 3
// 
// 2
```

## Debounce & Throttle

**Debounce**: For events like keydown, scroll, we don't want to trigger event in the middle of it, but only want to trigger after user pause! (ie. we only care the **final** result)

**Throttling**: For events like mouseover, we don't want to trigger event every for every single move, but only want to trigger it every `200ms` if such event happens (ie. we only care **sample** results)

### Debounce 

Given a function and a **delay** period, we want return a **debouncified** function:

* whenever called, will only be executed after the specified delay.
* **Ignore** calls in the **middle** of the delay, and reschedule the starting time of delay
* must receive **variant number** of arguments

Logic:

* **Ignore**: setTimeout -> clearTimeout -> ... -> ... 
* share the same Timeout Handler -> closure (gives you access to an outer function's scope from an inner function.)

``` javascript 
function debouncify( func, delay ){
    let timeoutHandler   
    return function(){   // closure used to access to the same handler 
        clearTimeout(timeout_handler)
        timeoutHandler = setTimeout(() => {
            func(arguments)
        }, delay)
    }
}

// test
function printTime(){
    console.log(new Date().toLocaleTimeString());
}

let printTimeAfterFiveSecs = debouncify(printTime, 5000)

// need to call 
console.log(new Date().toLocaleTimeString()) // get the start time
printTimeAfterFiveSecs()
printTimeAfterFiveSecs()
printTimeAfterFiveSecs()
printTimeAfterFiveSecs()
printTimeAfterFiveSecs()
printTimeAfterFiveSecs()
printTimeAfterFiveSecs()   // should be 5sec after the start time
```

### Throttle

![before](https://i.imgur.com/ZUiDwSy.gif)

![after](https://i.imgur.com/6h0OLGr.gif)


|---|

``` javascript 
function throttle(fn, interval = 300) {
    let canRun = true;
    return function () {
        if (!canRun) return;  // stop here before 300
        canRun = false;
        setTimeout(() => {
            fn.apply(this, arguments);
            canRun = true;
        }, interval);
    };
}
```
[函数节流与函数防抖](https://juejin.im/entry/58c0379e44d9040068dc952f)


