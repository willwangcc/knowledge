# Screenshot: 如何快速记笔记？


## Why

* 为了快速记记录，便于当日回顾。
* screenshot最快记录笔记的方式。

为了便于管理screenshot，需要：

* 明确的**截图标准**，减少重复思考，形成习惯
* 统一的**存储地点**，减少重复操作，便于处理
* 可测的**处理标准**，减少模糊，提供效率

## How

* iPhone和Macbook在「知识点」和「结束点」截图
* 将截图**统一**存储在文件夹「Review」
* 在Review中统一处理

## What

* **统一存储**: 配合dropbox利用「shortcuts」的[shortcut](https://i.imgur.com/ac30rCf.jpeg)和[automation](https://i.imgur.com/BoIyroH.png)，同时修改Macbook默认截图存储路径，可以使得iPhone和Macbook的截图在一处，而不用任何额外操作。

## Q&A

1. screenshot的类型？
	* 知识点 
	* 一个小目标的完成
* 如何处理screenshot？
* screenshot存储在哪里？
* screenshot是否具有存储的价值，便于日后回顾？ 
* 如何节省截图空间？
	* for i in *.png; do sips -s format jpeg -s formatOptions 5 "${i}" --out "${i%png}jpg"; done
* How to change default mac screenshot location?
	* defaults write com.apple.screencapture location **~/Desktop**
	* killall SystemUIServer 
