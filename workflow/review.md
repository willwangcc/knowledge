# Review system

## To do 
* [x] [morning routine](https://i.imgur.com/xZVfpTV.png): 把Alfred中的命令(m1, m2, m3)三合一: `screenshots to evernote`
* [ ] 如何提高 @review 整理的时间效率，让其**Focus**在最重要的事情上？
* [ ] 补充整个review system背后的科学原理，why?
* [ ] 补充为什么使用「Evernote」，以及之后的截图复习系统?

## Tools

<img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/> <img src="https://i.imgur.com/5L0C5zD.png" alt="shortcuts" width="20"/>
<img src="https://i.imgur.com/xeFNz0B.png" alt="review" width="20"/>
<img src="https://i.imgur.com/wkAKmBc.png" alt="evernote" width="20"/>
<img src="https://i.imgur.com/8MyBvDP.png" alt="drawing" width="20"/>
<img src="https://i.imgur.com/kLLtRlc.png" alt="drawing" width="20"/>


1. Shortcuts 
1. Alfred/workflow - [screenshots to evernote](https://github.com/willwang-x/screenshots-to-evernote)  
1. Evernote 
1. workflowy.com 
1. Github with MacDown 


## How: 整体逻辑? 

> **起源**于好奇，**定义**成问题，**发展**于阅读、交流与思考，**下切**到行动指南，**回归**到总结反思，**增值**于分享输出

整体的操作逻辑如下：

* **截图**： 包括电脑和手机，条件是**值得复习和深入了解的知识点**都记录保留**学习现场**
* **归档**： screenshots to evernote using 「shortcuts」 & 「alfred/workflow」
* **记录**： 在「evernote」用**沉浸模式**阅读，在「workflowy」中记录所有知识点, 这个环节**越快越好**
* **分类**： 将知识点分类到不同的「github」**知识库**中，然后**排序**处理


## How: 具体细节?

<img src="https://i.imgur.com/TdhUSIf.png" alt="shortcuts" width="150"/> <img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/>
<img src="https://i.imgur.com/9XqaseO.png" alt="alfred-review" width="150"/>
<img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/>
<img src="https://i.imgur.com/2OIL9Zf.jpg" alt="evernote" width="100"/>
<img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/>
<img src="https://i.imgur.com/ADELdZ0.jpg" alt="workflowy" width="150"/>
<img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/>
<img src="https://i.imgur.com/MwXB1il.png" alt="workflowy" width="150"/>


1. iPhone screenshots to Mac：
	* **拿**起iPhone
	* 右滑屏幕
	* 点击workflow1
	* 点击workflow2
	* 跳出Alert窗口，点击“Delete"
1. Mac screenshots to Evernote:
	* **快捷键** `option + command + space` 唤出Alfred
	* **输入** `m,`, `return`: to evernote
1. Evernote to workflowy: 
	* **快捷键** `shift + return` 进入“Present”沉浸模式
	* 鼠标**点击**图片, 进入图片模式
	* 开始在workflowy中记录“知识点”
1. Evernote to Github:
	* @maps 中**排序**知识点，以github名，将知识点**分类**，如 web knowledge to github/a-growing-web-developer 
	* 使用Terminal唤出目录
	* 使用MacDown打开编辑
	* writing...
	* 完成一个知识点`git add/commit/push` 

## Log 

- 2018.10.28: 
	- 把 `rm` 改成 `trash`, 以备意外，可以恢复。
	- 完成一键操作：files to evernote. 过程试图用javascript 取代 applescript，但是这是低频事件，提前优化，是一个错误策略。
