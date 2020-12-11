# AJAX

## 1. Background

I don't want the whole page in my web app to refresh when I interact with servers in order to **update parts of a web page**. So I am looking a solution, which is AJAX.


## 2. What is AJAX?

>  AJAX stands for “**A**synchronous **Ja**vaScript and **X**ML”, and was coined by Jesse James Garrett, founder of Adaptive Path.

AJAX is not a programming language. 

AJAX just uses a combination of:

- A browser built-in **XMLHttpRequest object** (to **request** data from a web server)
- **JavaScript and HTML DOM** (to **display** or use the data)

> AJAX is a **misleading** name. AJAX applications might use XML to transport data, but it is equally common to **transport data as plain text or JSON text.**

### Example 

![Twitter](https://i.imgur.com/bfNOnUQ.jpg)

## 3. Why do we need AJAX?

### 3.1 Before 

In a traditional web page, when a user sends a request (like clicking on a Submit button), the user waits until the page gets reloaded. During the normal wait period, which ranges from anywhere between a few seconds to “ages”, the user would be presented with a blank browser screen to stare at. 

### 3.2 After 

But, now we have a technique called AJAX.

In asynchronous mode, the client and the server will work independently and also communicate independently, allowing the user to continue interaction with the web page, independent of what is happening on the server.

AJAX relies on XMLHttpRequest, CSS, DOM, and other technologies. The main characteristic of AJAX is its “**asynchronous**” nature, which means it can send and receive data from the server without having to refresh the page. Yes, you heard me right...**without having to refresh the page.**


## 4. How to use AJAX?

There’s nothing really new about AJAX. Normally, we make a request, and receive a page as the response. This is how the web works already — the only difference is that now we can make these requests from JavaScript.

![How AJAX works](https://www.w3schools.com/js/pic_ajax.gif)

1. An event occurs in a web page (the page is loaded, a button is clicked)
2. An XMLHttpRequest object is created by JavaScript
3. The XMLHttpRequest object sends a request to a web server
4. The server processes the request
5. The server sends a response back to the web page
6. The response is read by JavaScript
7. Proper action (like page update) is performed by JavaScript

### Show me the code
``` html
<!DOCTYPE html>
<html>
<body>

<div id="demo">

<h2>The XMLHttpRequest Object</h2>

<button type="button"
onclick="loadDoc('ajax_info.txt', myFunction)">Change Content
</button>
</div>

<script>
function loadDoc(url, cFunction) {
  var xhttp;
  xhttp=new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      cFunction(this);
    }
  };
  xhttp.open("GET", url, true);
  xhttp.send();
}
function myFunction(xhttp) {
  document.getElementById("demo").innerHTML =
  xhttp.responseText;
}
</script>
</body>
</html>


```
> -- [AJAX Examples](https://www.w3schools.com/js/js_ajax_examples.asp)

### jQuery ajax() Method

![](https://i.imgur.com/qULdeze.png)


## Reference


1. [Youtube: What Is Ajax?](https://www.youtube.com/watch?v=3l13qGLTgNw)
2. [Documentation: Ajax](https://developer.mozilla.org/en-US/docs/AJAX)
3. [AJAX Explained](https://www.codeproject.com/Articles/14142/AJAX-Explained)
4. [25 Excellent Ajax Techniques and Examples](https://www.webpagefx.com/blog/web-design/ajax_techniques/)
5. [jQuery ajax() Method](https://www.w3schools.com/jquery/ajax_ajax.asp)