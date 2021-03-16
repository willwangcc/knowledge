# Node.js

## 1. Background  

I am going to do a stock search web app using node.js as a backend, like [this](https://www.youtube.com/watch?v=_4dkPTeX0mo&feature=youtu.be).

## 2. Why do we choose node.js?


### 2.1 History of Backend language 

#### 第一代后端平台 （输入输出）

Web 后端语言的兴起是从静态网页向动态网页的发展所产生的，最早的动态页面技术就是 **CGI** 技术，将客户端的输入交给 CGI 程序，然后将 CGI 程序的输出返回给客户端。早期的 CGI 程序只要是任何有标准输入输出的语言都可以编写，这也就是第一代后端平台。

#### 第二代后端平台 （简化CGI）

后来为了**简化 CGI 程序的修改编译发布的流程**，就有了脚本语言实现 CGI 应用。也就是 **Perl** 这样的语言。也就是第二代后端平台。

#### 第三代后端平台 (HTML和Code混合)



虽然 Perl 作为脚本语言**解决了开发效率**的问题，但是它同样需要在程序代码中掺杂 HTML 语言，为了解决这个问题，就有了 **PHP 这样的将 HTML 和 程序代码混杂**，并且能**快速开发**的语言。同时，**Java EE** 的标准也提出了 JSP 这样的解决方案，也就是第三代后端平台，从此，现代的后端开发基本就形成了。

#### 第四代后端平台 （事件循环&常驻内存）

再往后来，也就是 Node.js Go Swoole 这种以**事件循环、常驻内存**为特点的后端平台，姑且能算是第四代后端平台。而目前来说，第三代和第四代开发平台是并存的。

Python: 人生苦短，我用Python.


### 2.2 Pros and Cons 

![different backend language](https://cdn-images-1.medium.com/max/603/1*hYXCmiNjk5fqN3k4buT5Kg.jpeg)

There are several choices of Back-end language that we can choose. 

Like [*Choosing the Right Programming Language for Your Startup*](https://medium.com/aws-activate-startup-blog/choosing-the-right-programming-language-for-your-startup-b454be3ed5e2) said, We can consider three apsects related to your programming stacks: 

-  **the Characteristics of the Language**: Cloud? Security?  If you are developing for the cloud, stick with interpretative, dynamic, open source languages for rapid and more cost-effective development. For enterprise applications that have critical security requirements or must integrate with legacy environments, compiled languages may be better.
-  **your Local Ecosystem**: Research your local community to understand if you have a ready supply of skilled workers that can be tapped for affordable talent.
-  **the Problem Domain you are solving** : Somebody might have already solved 80% of your problem and have a general license available for you to build on.


> AWS developers often tell us they use the three points above to come up with a short list, and then make their final selection by identifying which language will allow them to **iterate the quickest**. They feel that this is the most important aspect because the nature of start-ups is to fail fast and fail forward. Fast iterations enable you test ideas, determine your problem space and provide you with solutions as you propel towards MVP.


### 2.3 PHP vs Node.js

#### Where PHP wins

1. Mixing code with content
2. Deep code base
3. Simplicity (sort of)
4. New code is helping it catch up
5. No client app needed
6. SQL
7. Speed of coding
8. Competition

#### Where Node.js wins

1. Separating concerns
2. Newer code means more modern features
3. Complexity of closures and more?
4. Dozens of language options
5. Service calls are thinner than HTML-fat PHP calls
6. **JSON**
7. Raw speed
8. Solidarity

From [*PHP vs. Node.js: An epic battle for developer mind share*](https://www.infoworld.com/article/3166109/application-development/php-vs-nodejs-an-epic-battle-for-developer-mind-share.html) 

## 3. What is Node.js?

### Node.js 

![Node.js](https://uploads.toptal.io/blog/image/50/toptal-blog-1_B.png)

> Node.js® is a JavaScript **runtime** built on Chrome's V8 JavaScript engine. Node.js uses an **event-driven**, **non-blocking I/O model** that makes it lightweight and efficient. Node.js' package ecosystem, npm, is the largest ecosystem of open source libraries in the world.

Maybe you are confused by what is said above. So instead of talking about what is Node.js, we try to figure it out that what is not Node.js.

> “Node.js**不是一种独立的语言**，与PHP、Python、Perl、Ruby的“既是语言也是平台”不同。Node.js也**不是一个JavaScript框架**，不同于CakePHP、Django、Rails。Node.js更**不是浏览器端的库**，不能与jQuery、ExtJS相提并论。Node.js是一个让JavaScript运行在服务端的开发平台，它让JavaScript成为脚本语言世界的一等公民，在服务端堪与PHP、Python、Perl、Ruby平起平坐。”   
> “Node.js是一个划时代的技术，它在原有的Web前端和后端技术的基础上总结并提炼出了许多新的概念和方法，**堪称是十多年来Web开发经验的集大成者。**Node.js可以作为服务器向用户提供服务，与PHP、Python、Ruby on Rails相比，它跳过了Apache、Nginx等HTTP服务器，直接面向前端开发。Node.js的许多设计理念与经典架构（如LAMP）有着很大的不同，可提供强大的伸缩能力，以适应21世纪10年代以后规模越来越庞大的互联网环境。”

>  —— Excerpt From: 郭家宝(BYVoid). “Node.js开发指南.” 

It is not a language, framwork or library. 

### Intuition 
> 在这个故事里，茶叶铺就是**网络服务器**。我们自己就是浏览器。

> 我们要是不想浏览器事必躬亲，**那就把活扔给服务器干**；当服务器一下子服务很多浏览器时就**不能认死理非要串行操作**，要灵活统筹，同时开始几件事，**哪件完事关闭哪件**。 

> 这三个特征用江湖切口说就叫：

> - 服务器端JavaScript处理：**server-side JavaScript execution**

> - 非阻断/异步I/O：**non-blocking or asynchronous I/O**

> - 事件驱动：**Event-driven**

> —— [Node.js是用来做什么的？ - 张戎的回答 - 知乎
](https://www.zhihu.com/question/33578075/answer/252611915)


![Non-blocking](https://i.imgur.com/97c0ggR.jpg)

![Event loop](https://i.imgur.com/f7e1pWp.jpg)

### Exmaple

![example](https://i.imgur.com/cKUU2jh.jpg)
> —— [ Youtube: Node.js Tutorial - Intro to Node.js (Level 1)
](https://www.youtube.com/watch?v=GJmFG4ffJZU)
 

## 4. How to learn Node.js?

![backend](https://camo.githubusercontent.com/989b5d78efe42fefa78f26443f146d027dcfb9b0/68747470733a2f2f692e696d6775722e636f6d2f6a7a3478726c512e706e67)

## 5. Reference 
1. [Choosing the Right Programming Language for Your Startup](https://medium.com/aws-activate-startup-blog/choosing-the-right-programming-language-for-your-startup-b454be3ed5e2)
2. [聊聊初创公司的后端语言选型 (小众语言)](https://ipfans.github.io/2016/01/startup-architecture-language/)
3. [后端语言选型浅谈](https://segmentfault.com/a/1190000006163263)
4. [我为什么向后端工程师推荐Node.js
.2011](http://www.infoq.com/cn/articles/why-recommend-nodejs)
5. [我为什么反对用Node
](http://www.infoq.com/cn/articles/why-oppose-Node)
6. [PHP vs. Node.js: An epic battle for developer mind share](https://www.infoworld.com/article/3166109/application-development/php-vs-nodejs-an-epic-battle-for-developer-mind-share.html)
7. [Node.js是用来做什么的？ - 张戎的回答 - 知乎
](https://www.zhihu.com/question/33578075/answer/252611915)
8. [ Youtube: Node.js Tutorial - Intro to Node.js (Level 1)
](https://www.youtube.com/watch?v=GJmFG4ffJZU)