# jQuery 

## 1. Background

Sometimes it takes much time to write codes to finish a function, which I think that should have been written by some people. It is what we call "Wheel". I wonder if there are some wheels that have been invented in JavaScript. Therefore, I finished a function with less code and less time. jQuery comes into sight.

![JQuery](http://randomperspective.com/comic/javascript-vs-jquery.png)

## 2. What is jQuery? 

![](https://t37.net/files/resource/1455/commitstrip.jpg)

> jQuery is **the most popular library** on the web today.
It's a library of JavaScript functions that make it easy for webpage developers to do common tasks--
like **manipulating the webpage, responding to user events, getting data from their servers, building effects and animations**, and much more.

## 3. Why do we use jQuery? 
Problem
![Problem](https://i.imgur.com/x7WLSm5.jpg)
Solution 
![Solution](https://i.imgur.com/SLuU23E.png)

Besides, If you learn jQuery, you'll be able to use it in your own webpages, understood other developer's webpages, and have a better understanding generally about how to use libraries.


## 4. How to use jQuery?

The jQuery library contains the following features:

- **HTML/DOM** manipulation
- **CSS** manipulation
- **HTML event** methods
- **Effects and animations**
- **AJAX**
- **Utilities**

### Example 
 
```
$(document).ready(function(){
    $("p").click(function(){
        $(this).hide();
    });
});
```

The jQuery syntax is tailor-made for **selecting** HTML elements and performing some **action** on the element(s).

**jQuery Selectors** 

 **$("p"),$("#test"),$(".test"),$("p.intro"),$("p:first")** : jQuery selectors are used to "find" (or select) HTML elements based on their **name, id, classes, types, attributes, values of attributes** and much more. 

**jQuery Event** 

 ![jQuery Event](https://i.imgur.com/a9NmRIQ.png)

> The on() method attaches one or more event handlers for the selected elements.



```
$("p").on({
    mouseenter: function(){
        $(this).css("background-color", "lightgray");
    }, 
    mouseleave: function(){
        $(this).css("background-color", "lightblue");
    }, 
    click: function(){
        $(this).css("background-color", "yellow");
    } 
});
```

### 4.1 jQuery Effects

1. jQuery Hide/Show
2. jQuery Fade
3. jQuery Slide
4. jQuery Animate
5. jQuery stop()
6. jQuery Callback 
7. jQuery Chaining

> **Callback**:  $(selector).hide(speed,callback);

A callback function is executed after the current effect is 100% finished.



```
$("button").click(function(){
    $("p").hide("slow", function(){
        alert("The paragraph is now hidden");
    });
});
```

> **jQuery - Chaining:** $("#p1").css("color", "red").slideUp(2000).slideDown(2000);

there is a technique called chaining, that allows us to run multiple jQuery commands, one after the other, on the same element(s).

### 4.2 jQuery HTML 


1. jQuery Get
1. jQuery Set
1. jQuery Add
1. jQuery Remove
1. jQuery CSS Classes
1. jQuery css()
1. jQuery Dimensions

> Get: text(), html(), and val(), attr()

```
$("#btn1").click(function(){
    alert("Text: " + $("#test").text());
});
$("#btn2").click(function(){
    alert("HTML: " + $("#test").html());
});
```

> Set Content and Attributes and **Callback**

```
$("#btn1").click(function(){
    $("#test1").text("Hello world!");
});
$("#btn2").click(function(){
    $("#test2").html("<b>Hello world!</b>");
});
$("#btn3").click(function(){
    $("#test3").val("Dolly Duck");
});
```

> With jQuery, it is easy to **add** new elements/content.


```
$("p").append("Some appended text.");
Try it Yourself »

```

> With jQuery, it is easy to **remove** existing HTML elements.


```
$("#div1").remove();
```

> With jQuery, it is easy to **manipulate** the CSS of elements.

```
$("button").click(function(){
    $("h1, h2, p").addClass("blue");
    $("div").addClass("important");
});
```

> The css() method sets or returns one or more style properties for the selected elements.


```
$("p").css({"background-color": "yellow", "font-size": "200%"});
```
> With jQuery, it is easy to **work with the dimensions** of elements and browser window.

![](https://www.w3schools.com/jquery/img_jquerydim.gif)

```
$("button").click(function(){
    var txt = "";
    txt += "Width: " + $("#div1").width() + "</br>";
    txt += "Height: " + $("#div1").height();
    $("#div1").html(txt);
});
```

### 4.3 jQuery Traversing

1. jQuery Ancestors
1. jQuery Descendants
1. jQuery Siblings
1. jQuery Filtering

> jQuery traversing, which means "move through", are used to "find" (or select) HTML elements based on their relation to other elements. Start with one selection and move through that selection until you reach the elements you desire.

![div](https://www.w3schools.com/jquery/img_travtree.png)

> parent()
parents()
parentsUntil()

![parents](https://i.imgur.com/EOE7a2A.png)

> children()
find()

![find](https://i.imgur.com/sRIdLaQ.png)

> siblings()
next()
nextAll()
nextUntil()
prev()
prevAll()
prevUntil()

![siblings](https://i.imgur.com/3BUyGxL.png)

> The first(), last(), eq(), filter() and not() Methods

![](https://i.imgur.com/P3aEOV4.png)

### 4.4 jQuery AJAX

1. jQuery AJAX Intro
1. jQuery Load
1. jQuery Get/Post

> $(selector).load(URL,data,callback);

![jQuery Ajax](https://i.imgur.com/yFxHc3M.png)

> The jQuery **get() and post()** methods are used to request data from the server with an HTTP GET or POST request.

> $.get(URL,callback);

* **GET** - Requests data from a specified resource
* **POST** - Submits data to be processed to a specified resource

![$.get(URL,callback);
](https://i.imgur.com/WMJXUQc.png)


### 4.5 jQuery Misc

1. jQuery noConflict()
1. jQuery Filters

> What if other JavaScript frameworks also use the $ sign as a shortcut?

```
$.noConflict();
jQuery(document).ready(function(){
    jQuery("button").click(function(){
        jQuery("p").text("jQuery is still working!");
    });
});
```

> Use jQuery to filter/search for specific elements.

![](https://i.imgur.com/Jko2Wed.png)


## Reference

1. [maps of jQuery](https://learn-anything.xyz/web-development/javascript-libraries/jquery)
2. [jquery-tips-everyone-should-know](https://github.com/AllThingsSmitty/jquery-tips-everyone-should-know#checking-if-jquery-loaded)
3. [jQuery Introduction](https://www.w3schools.com/jquery/jquery_intro.asp)