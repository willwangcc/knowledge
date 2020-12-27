# MongoDB 

![mongoDB](https://i.imgur.com/qnnGr3P.png)

from [MongoDb 快速入门教程](https://www.cnblogs.com/chanshuyi/p/quick_start_of_mongodb.html)

## Why 起源？

在[如何用 60 行代码爬取知乎神回复？](https://yq.aliyun.com/articles/665228?utm_content=m_1000022544) 遇到 pymongo, 而 pymongo 即 Python 操作 **MongoDB** 的一个库。 

那为什么使用 MongoDB呢？ 

从原始存储信息开始聊起，

* 存储空间不连续使用，需要 **doubly-linked list** 对`文档`建立连接，便于遍历。 
	* <img src="https://i.imgur.com/95pkAfx.png" alt="pointer" height="200"/>
* 每条`文档`中的数据和属性可能日后变动，则需要增加**padding**, 便于之后修改，非删除然后添加新`文档`。
	* <img src="https://i.imgur.com/qIxgMuO.pngg" alt="padding" height="200"/>
* 真正的硬盘往往已经不连续了，存在着大大小小的磁盘碎片，我们只能插空写。为了仅可能连续写，避免跳来跳去，我申请空间策略就是**double上升**。我们从16M开始，不够就申请32M，再不够申请64M…直到2G为止（不再double，不够再申请还是2G） ![double](https://i.imgur.com/GfGQbhk.png)
* 写的问题解决了，为了解决读的问题，我们就可以对ID建**索引**，比如BST，每个节点都指向对应的文档。 ![B-Tree](https://i.imgur.com/ZxcdYCT.png)

这就是MongoDB?

* MongoDB saves documents whose **attributes** can be updated freely
* MongoDB adds **paddings** into documents to reduce fragments
* MongoDB uses pre/next **points** to increase lookup speed
* MongoDB saves the documents into a sequence of **16M**, 32M, ... 2GB files
* MongoDB uses **BTree**(a better version of BST) to build **index**

> MongoDB is a **document-oriented** DBMS. Think of MySQL but with **JSON-like objects** comprising the data model, rather than RDBMS tables. Significantly, MongoDB supports neither joins nor transactions. However, it features secondary indexes, an expressive query language, atomic writes on a per-document level, and fully-consistent reads.
Operationally, MongoDB features master-slave replication with automated failover and built-in horizontal scaling via automated range-based partitioning.

## How? 如何使用？

### 配置

prerequisite: brew, xcode 

下载：

```
brew update
brew install mongodb
```

设置：(数据存储位置和访问权限)

```
sudo mkdir -p /data/db
sudo chown -R $USER /data/db
sudo chmod go+w /data/db
```

* 在MAC上 `brew install mongodb` 前需要安装xcode, mongodb需要它用来compile。
* [How to install MongoDB on Mac](https://www.youtube.com/watch?v=d8Pft3pbAZU): 1分钟视频
* [Mongodb installation failed with homebrew and XCode 8.1.1](https://stackoverflow.com/questions/48251108/mongodb-installation-failed-with-homebrew-and-xcode-8-1-1): 可能的问题
* [MongoDB 在Mac OS中的开发环境](https://www.jianshu.com/p/620049a0be81) : 如果你想要「可视化」工具

## Run 

If you have installed mongodb through homebrew then you can simply start mongodb through

> brew services start mongodb

Then access the shell by

> mongo

You can shut down your db by

> brew services stop mongodb

You can restart your db by

> brew services restart mongodb

For more options

> brew info mongodb

## Q&A 

![sql vs mongoDB](https://i.imgur.com/yA4J1mc.png)
from [4. MongoDB教程 -- 入门](http://wanwu.tech/2017/03/28/MongoDB-intro/)

1. What makes MongoDB the best?

> MongoDB is considered to be best NoSQL database because of:
> 
> * Document-oriented (DO)
* High performance (HP)
* High **availability** (HA)
* Easy **scalability**
* Rich **query** language

## 参考


* [面试中如何胡侃知识点（以MongoDB为例）？](https://zhuanlan.zhihu.com/p/20786671)
* [Top Mongodb Interview Questions And Answers](https://intellipaat.com/interview-question/mongodb-interview-questions/)
* [30 Best MongoDB Interview Questions and Answers (2018 Update)](https://www.fullstack.cafe/blog/30-best-mongodb-interview-questions-and-answers)
* [mongodb知乎精华](https://www.zhihu.com/topic/19560787/top-answers)
**