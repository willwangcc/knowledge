# a-growing-web-developer

> 极大的拓宽了读者的视角，另一方面是其中的一些问题非常具有启发性。 
> 
> from [Back-End-Developer-Interview-Questions](http://www.go2going.com/2017/11/14/Back-End-Developer-Interview-Questions/) 

## List 

1. [ ] 通用问题
1. 开放式问题
1. 设计模式相关问题
1. 代码设计相关问题
1. 语言相关问题
1. Web相关问题
1. 数据库相关问题
1. 非关系型数据库相关问题
1. 代码版本管理相关问题
1. 并发问题
1. 分布式系统相关问题
1. 软件生命周期和团队管理相关问题
1. 逻辑和算法相关问题
1. 软件架构相关问题
1. 面向服务架构(SOA)和微服务(Microservice)相关问题
1. 安全相关问题
1. 比尔盖茨式问题
1. 代码示例问题


## 通用问题

### 为什么函数式编程越来越流行？ 

没有**side effect** -> 不会造成**race condition** -> 更好的处理
**concurrency**问题

> **摩尔定律**的不适用，目前来说cpu的发展基本上就是**对核心**，但是**oo**在处理**并发问题时**很棘手，而**函数式编程**的好处之一就是**引用透明没有副作用**，所以不会造成**资源竞争**，能够更好的**处理并发**。 - [from](https://i.imgur.com/D5Ddw6s.jpg)