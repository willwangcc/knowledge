# Design patterns with illustrations

> My journey to make friends with design patterns

## Why

About design patterns, there are so many related [repositories](https://github.com/kamranahmedse/design-patterns-for-humans), [tutorials](https://refactoring.guru/design-patterns/catalog), [books](https://www.amazon.com/Design-Patterns-Object-Oriented-Addison-Wesley-Professional-ebook/dp/B000SEIBB8), even [game](https://designpatternsgame.com/). And use cases in different programming languages, e.g. [python](https://python-patterns.guide/).

Why do you create new one? Because they are not what I want. So what is your need?

* The **code** to show **difference** **before** and **after** using the pattern
* The **pciture** to show **intuition** behind the pattern
* The **prospect** of solving the problem by **myself**, which is the most important


## What

> working in progress

| key 🔑 | why | what  | how  | when | 
| :-------- | :---------: | :----------: | :---------: |  :---------: |
|**Simple Factory🏠**| create without the mess | <img src="https://i.imgur.com/cpS1wFc.png" alt="Builder" width="200"/><br> | `new`| |
|**Factory Method🏭**| generic & sub-class | <img src="https://i.imgur.com/kMY2Y84.png" alt="Builder" width="200"/><br>subclass| `extends`| |
|**Abstract Factory🔨**| stuff & steps | <a href="https://refactoring.guru/design-patterns/abstract-factory"><img src="https://i.imgur.com/jXCYg06.png" alt="Abstract Factory" width="200"/></a> |`implements`| dependencies |
|**Builder👷**| to avoid the constructor telescoping | <img src="https://i.imgur.com/0BPaW0q.png" alt="Builder" width="200"/>|`new`&   `function`  | |
|**Prototype🐑**| similar & save | <img src="https://i.imgur.com/jbcu18T.png" alt="Builder" width="200"/> | `clone` |  |
|**Singleton💍**|  unique| <img src="https://i.imgur.com/Ir8x2Cf.png" alt="Builder" width="200"/>| `getInstance()` | ⚠️|
|**Adapter🔌**| | <img src="https://i.imgur.com/Jm1rBhJ.jpg" alt="Adapter" width="200"/>| `WildDogAdapter`||
|Bridge🚡|composition over inheritance| <img src="https://i.imgur.com/HSIGiiZ.png" alt="Bridge" width="200"/>||
|Composite🌿| uniform |<img src="https://i.imgur.com/uhFRwSy.png" alt="Composite" width="200"/>|
|Decorator☕|dynamically change|<img src="http://qxf2.com/blog/wp-content/uploads/2014/09/qxf2-gun-decorator1.jpg" alt="Decorator" width="200"/>|[python](https://repl.it/@WillWang42/decorator)| **切面需求**<br>e.g.<br>插入日志<br>性能测试<br>事务处理<br>缓存<br>权限校验|
|Facade📦|simplified interface → complex subsystem |<img src="https://i.imgur.com/bYMfJAx.jpg" alt="Facade" width="200"/> <br>e.g. hit the button ||
|Flyweight🍃|sharing & frugality|<img src="https://i.imgur.com/vGbsoLh.png" alt="Flyweight" width="200"/>||
|Proxy🎱|extra functionality|<img src="https://i.imgur.com/tHIXbE8.png" alt="Proxy" width="200"/> <br>|`function`+||
|Chain of Responsibility🔗|request with multi handle|<img src="https://i.imgur.com/EyoYZbI.png" alt="Chain of Respnsibility" width="200"/> <br>|`setNext`| |
|Command|encapsulate actions in objects|<img src="https://i.imgur.com/lVFORZg.png" alt="Command" width="200"/> <br>|`Client` & `Invoker` & `Command` & `Receiver` ||
|Iterator➿|what's next|<img src="https://i.imgur.com/wecacEH.png" alt="Iterator" width="200"/> <br>|`next`|
| Mediator👽|encapsulate interact|<img src="https://i.imgur.com/DTjsQHf.png" alt="Mediator" width="200"/> <br>|meidator & user|
| Memento|redo|<img src="https://i.imgur.com/dGzcnqh.png" alt="Memento" width="200"/> <br>|`save`|
| Observer | subscribe & notice |<img src="https://i.imgur.com/iIpUCr3.png" alt="Observer" width="200"/> <br>|`attach`|
|[Visitor](https://www.wikiwand.com/en/Visitor_pattern)🚕|add more without modify|<img src="https://i.imgur.com/8RWeDoc.png" alt="Visitor" width="200"/> <br> | `interface`| |
|Strategy|choose x suitable|<img src="https://i.imgur.com/wX1y2jT.png" alt="Strategy" width="200"/> <br>|`if`||
|State|state → class|<img src="https://i.imgur.com/zh3pkxI.jpg" alt="state" width="200"/> <br>|`interface` & `class` & `function`||
|Template| skeleton → children classes|<img src="https://i.imgur.com/wSF69sB.png" alt="Template" width="200"/> <br>|`Builder`|

