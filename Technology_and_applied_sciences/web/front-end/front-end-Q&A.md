# Front end Q&A

## 目录

1. 前端要解决的核心问题是什么？
2. Store, Flux, Redux 有什么区别？
3. Redux 是如何处理异步(asynchrony)的？
4. Redux 和 Mobx 有什么区别？

## 1. 前端要解决的核心问题是什么？

解决应用**状态管理**的问题。具体而言，统一维护**公共**的应用状态，以**统一**并且**可控**的方式更新状态，状态更新后，View跟着更新。

## 2. Store, Flux, Redux 有什么区别？

- `Store`： 把状态存到一个外部变量里面。缺点是无历史记录，无法rollback, 难以debug.
- `Flux`:  Action -> Dispatcher -> Store -> View
	- 多个数据源: Store一一各自View，每次更新都只通知对应的View。
	- State可以修改。
	- Flux 执行修改的不一定是纯函数(Pure function)
- `Redux`: View ♻️ Store
	- 单一数据源：Only one store 
	- State 是只读的
	-  使用纯函数来执行修改 

![Flux vs Redux](https://i.imgur.com/aE6U2hD.png)	
	
某个程度，三者可以看作设计的递进。设计思想是「隔离变化」。

因为Store没有记录Action, 如果有Bug，便不知道是谁干的，难以Debug，所以隔离`action`，规定 「组件必须通过 `action` 来改变 state」。

即，组件(component)里面应该执行 `action` 来 `dispatch` 事件通知 `store` 去改变, 从而更新 `View`。 这样，便得到简单的 `Flux` 架构。但是 `Flux` 有缺点， 比如一个应用可以拥有多个Store，多个Store之间可能有依赖关系，Store封装了数据还有处理数据的逻辑。

为了让其更彻底，隔离变化，我们使用 Pure Function 生成 New state 而不是 修改 State, 来获得更好的 Version control. 同时，只用一个 Store, 逻辑边更加清晰。这样我们就得到了简单的 `Redux` 架构。

在实际使用中，我们一般使用`Redux`。 

![Redux](https://i.imgur.com/CfS5raD.png)

## 3. Redux 是如何处理异步(asynchrony)的？

对于异步操作来说，有两个非常关键的时刻：**发起请求的时刻**，和**接收到响应的时刻**（可能成功，也可能失败或者超时），这两个时刻都可能会更改应用的 state。一般是这样一个过程：

* 请求开始时，dispatch  一个请求开始 Action，触发 State 更新为“正在请求”状态，View 重新渲染，比如展现个Loading。
* 请求结束后，如果成功，dispatch  一个请求成功 Action，隐藏掉  Loading，把新的数据更新到  State；如果失败，dispatch  一个请求失败 Action，隐藏掉  Loading，给个失败提示。


典型的有三个解决方案：

* Redux-Thunk
* Redux-Promise
* Redux-Sage 


前两者，Redux 引入了中间件 Middleware 的概念, 把异步请求部分放在了 action creator中。 而Redux-Sage则是所有的异步操作看成“线程”，可以通过普通的action去触发它。

Redux-Thunk和Redux-Promise区别，在于Thunk封装少，自由度高，代码复杂，而Promise则相反。

而redux-saga则是用一些学习的复杂度，换来了代码的高可维护性。

![Redux-Sage](https://i.imgur.com/CxQvoiH.png)

## 4. Redux 和 Mobx 有什么区别？

`Redux`主要就是**函数式编程**思想，而`Mobx`更接近于面向对象编程。它把 state 包装成可观察的对象，这个对象会驱动各种改变。其核心思想是 

> 状态只要一变，其他用到状态的地方就都跟着自动变。

Redux 比 Mobx 更多的样板代码，是因为特定的设计约束。如果项目比较小的话，使用 MobX 会比较灵活，但是大型项目，像 MobX 这样没有约束，没有最佳实践的方式，会造成代码很难维护，各有利弊。

一般来说，小项目建议 MobX 就够了，大项目还是用 Redux 比较合适。

![Mobx](https://i.imgur.com/bwH1F9n.png)

## Reference 

- [Vuex、Flux、Redux、Redux-saga、Dva、MobX](https://zhuanlan.zhihu.com/p/53599723): 一切前端概念，都是纸老虎。

