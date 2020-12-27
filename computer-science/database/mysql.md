# SQL 


## 基础概念

* **冗余**: 用来表示存储两倍的数据, 但会使数据访问更快. 相当于redis
* **主键**: 用来执行每个表的关键性数据, 并且,每个表中只有一个主键.
* **外键**: 这应该是mysql的关键, 使用外键来关联不同表.
* **复合键**: 将多个键组合一起来作为索引值. 一般用于复合索引
* **索引**:借用一组值, 来对表进行排序. 可以比作书的目录.
* **参照完整性**: 参照的完整性要求关系中不允许引用不存在的实体


## 使用指南

* install:  `brew install sql`
* start: `mysql.server start`
* stop: `mysql.server stop`
* interact: `mysql `

If there is any error:

* [Completely Remove MySQL on Mac OS X](http://soatechlab.blogspot.com/2011/01/completely-remove-mysql-on-mac-os-x.html)
* `brew install sql`
* **reboot**
* `brew services start mysql`  from [Install MySQL on macOS Sierra](https://gist.github.com/nrollr/3f57fc15ded7dddddcc4e82fe137b58e)
* **reboot**  - [why](https://errorcodespro.com/error-server-quit-without-updating-pid-file-mac/) 
* `mysql.server status` 
