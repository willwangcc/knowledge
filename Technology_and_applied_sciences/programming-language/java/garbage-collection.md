# Java Garbage Collection  

## Why?

- When it comes to **troubleshooting** various memory overflow issues and you experience critical delays in your software caused by garbage collection, we need to implement the necessary monitoring and adjustment of these "automated" technologies. 
- You get a better knowledge of what is going on beneath the code you write. This can often help you write more efficient code, which will guarantee better **performance**.


## Points

- Garbage Collector
- JVM Heap Memory allocation strategy
- Dead 
- Reference
- Garbage Collection Algorithm  
- Garbage Collector


## What?

|key|feature(pros/cons)|what|how|when to use|
|:--|:--|:--:|:--|:--|
|No GC|😄no worry while running<br>😰fragment<br>😰memory|<img src="https://i.imgur.com/6nIQHGs.gif" alt = "NO GC" height="100" width="200"> by [KEN](https://spin.atomicobject.com/2014/09/03/visualizing-garbage-collection-algorithms/)|Cleanup At The End|e.g. Apache web server|
|Reference Counting Collector|😄 detected ASAP<br> 😄🥇easily integrates<br>😰cyclic structures- >leak memory<br>😰response times|<img src="https://i.imgur.com/ncOcGz9.gif" alt = "Reference Counting Collector" height="100" width="200"> |Dispose of it when the reference drops to zero|e.g. Apple Objective-C🙋‍♂️|
|Mark-Sweep Collector|😄cyclic structure<br>😰detected ASAP<br>😰 retrofit<-consistency<br>😰risky when obejct🙅‍♂️traversal<br>😰garbage⛰️|<img src="https://i.imgur.com/JXkBx0Y.gif" alt = "Mark-Sweep Collector" height="100" width="200">| mark -> sweep|e.g. Apple Objective-C🙅‍♂️|
|Mark-Compact Collector|😄no call stacks<br>😄better memory access patterns<br>😄low memory<br>😄no fragment<br>😰complex<br>|<img src="https://i.imgur.com/OCNe00r.gif" alt = "Mark-Compact Collector" height="100" width="200"> |mark -> dispose -> move|e.g.Oracle’s Hotspot JVM: The tenured object space|
|Copying Collector|😄simplicity<br>😄flexibility<br>😄only live objects<br>😄no fragment<br>😄foundation <- high-performance<br>😰 all copied 🤔-> tuning<br>|<img src="https://i.imgur.com/6CpFvM9.gif" alt = "Copying Collector" height="100" width="200"> |It uses **two** memory spaces and simply **copies** live objects **back and forth** between them|the foundation of most high-performance garbage collection systems|


## Questions 


- generational garbage collection
- like why reference counting is usually a bad idea, and why mark-and-sweep is better
- some alternate implementations




## Reference(clean)

* [Visualizing Garbage Collection Algorithms](https://spin.atomicobject.com/2014/09/03/visualizing-garbage-collection-algorithms/)
* [垃圾回收的算法与实现](https://book.douban.com/subject/26821357/)
* [An Overview of Garbage Collection in Java](https://dzone.com/articles/an-overview-of-garbage-collection-in-java): Here we examine the importance of proper garbage collection for Java apps, the components of GC, and the various patterns at your disposal.
* [Should java developers know about garbage collection algorithms? ](https://softwareengineering.stackexchange.com/questions/158869/should-java-developers-know-about-garbage-collection-algorithms)
* [搞定JVM垃圾回收就是这么简单](https://zhuanlan.zhihu.com/p/43211695)
* [Java Garbage Collection – An Overview](http://www.tothenew.com/blog/java-garbage-collection-an-overview/)
* [JVM垃圾回收器 思维导图](https://www.spldeolin.com/posts/jvm-gc/)
* [[JVM]Java内存区域与垃圾收集 - 思维导图](https://www.jianshu.com/p/088d71f20a47)
* [[计算机领域的思维导图系列整理][java] 虚拟机JVM](https://blog.csdn.net/titer1/article/details/53872942): 各类思维导图
* [JVM垃圾回收思维导图（巨图预警）](https://blog.csdn.net/qq_34218615/article/details/80295214)
