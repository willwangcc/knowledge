# JS Interview practice question 


## To do 

* [x] 1. 移动图片
* [x] 2. debouce 
* [x] 3. throttle 
* [x] 4. event emitter 
* [ ] 5. auto-complete
* [ ] 6. promise 


## 1. 移动图片

``` javascript 
<!DOCTYPE html>
<html>
<head>
<style>
	#container{
    	width: 100px;
        height: 100px;
    	border: 1px solid red;
        position: relative;
    }
</style>
</head>
<body>
	<div id="container">
</div>

<script>


// Version 1
function moveToRight(ele, dis, time) {
  let interval = 10;
  let oneStep = interval * dis / time;
  let totalSteps = dis / oneStep;
  let step = 0;
  let curLeft = ele.offsetLeft;
 
  let interval_handler= setInterval(function(){
    curLeft += oneStep;
    ele.style.left = curLeft + 'px';
    step += 1;
    if( step === totalSteps ) clearInterval(interval_handler);
  }, interval)
}


// Test  
let ele = document.getElementById("container");
moveToRight(ele, 100, 500);

</script>

</body>
</html>
```

## 2. Debounce 

> **Debounce**: For events like keydown, scroll, we don't want to trigger event in the middle of it, but only want to trigger after user pause! (ie. we only care the **final** result)

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

## 3. Throttle

![before](https://i.imgur.com/ZUiDwSy.gif)

![after](https://i.imgur.com/6h0OLGr.gif)

> **Throttling**: For events like mouseover, we don't want to trigger event every for every single move, but only want to trigger it every `200ms` if such event happens (ie. we only care **sample** results)

|---|---|---|

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

## 4. [event emitter](https://repl.it/@WillWang42/eventEmitter)

``` javascript 
class EventEmitter {
  constructor() {
    this.events = {};
  }
  
  on(event, listener) {
      if (typeof this.events[event] !== 'object') {
          this.events[event] = [];
      }
      this.events[event].push(listener);
      return () => this.removeListener(event, listener);
  }
    
  removeListener(event, listener) {
    if (typeof this.events[event] === 'object') {
        const idx = this.events[event].indexOf(listener);
        if (idx > -1) {
          this.events[event].splice(idx, 1);
        }
    }
  }
  
  emit(event, ...args) {
    if (typeof this.events[event] === 'object') {
      this.events[event].forEach(
        listener => {if(typeof listener === 'function') listener.apply(null, args)}
      );
    }
  }
  
  // register a wrapper function containing the listener on this event,
  // when get executed, 
  //   - first remove it on this event;
  //   - then execute real listener
  once(event, listener) {
    const remove = this.on(event, (...args) => {
        remove();
        listener.apply(null, args);
    });
  }
};

// Test 4: subscribe other event & callbacks at the same time
let data = {digit: 1}
console.log("Test 4:  digit should be 11 & 14 ")
emitter.on("c", function(data){ data.digit+=1 });
emitter.on("c", function(data){ data.digit+=2 });
emitter.on("d", function(data){ data.digit+=3 });;
let off2 = emitter.on("d", function(data){ data.digit+=4 });

emitter.emit("c", data); 
emitter.emit("d", data);  
console.log(data.digit)
      
off2()
emitter.emit("d", data);  
console.log(data.digit)
console.log()
```