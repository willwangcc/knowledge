# Review: 如何将经验变成积累？

<br>

<img src="https://i.imgur.com/3xYCguw.png" alt="sceenshot" height ="60"/> 
<img src="https://i.imgur.com/lywdaP3.png" alt="right" height="20"/> 
<img src="https://i.imgur.com/h0VjH0Q.png" alt="review" height="60"/> 
<img src="https://i.imgur.com/lywdaP3.png" alt="right" height="20"/> 
<img src="https://i.imgur.com/MwXB1il.png" alt="workflowy" height="60"/>

> 不总结反思，为什么奢望成长？

## Why?

<center>
<img src="https://i.imgur.com/PNAowPi.png" alt="review" height="90"/>
</center>

* **集中**处理所有与世界的交互
* **有效**从过去汲取未来的养分

而我想到的最好方式是截图，问题细分为：

* 明确的**截图标准**，减少重复思考，形成习惯
* 统一的**收集地点**，减少重复操作，便于处理
* 可测的**处理标准**，减少模糊判断，提高效率

## How?

> **起源**于好奇，**定义**成问题，**发展**于阅读、交流与思考，**下切**到行动指南，**回归**到总结反思，**增值**于分享输出



1. **截图**：「知识点」和「结束点」，在手机和电脑上截图以保留**认知现场**
1. **收集**：将所有截图**合并**一处，以集中处理
1. **处理**：分类**处理**，提问，连接，视觉，组织
	* **知识**：在Anki记录 and/or 在Github中建立条目
	* **行动**：放入Omnifocus
	* **未知**：放入workflowy



## What？

<img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/> <img src="https://i.imgur.com/5L0C5zD.png" alt="shortcuts" width="20"/>
<img src="https://i.imgur.com/CZTaNRb.jpg" alt="anki" width="20"/>
<img src="https://i.imgur.com/kLLtRlc.png" alt="drawing" width="20"/>
<img src="https://i.imgur.com/8MyBvDP.png" alt="drawing" width="20"/>

* **知识点**：新的知识，行动指南，细节，流程。使用「提问-连接-视觉-组织」来决定是否截图。
* **结束点**：一件事情结束，截图便于事后回顾，是否可以做的更好。
* **认知现场**: 与你有关的知识是决定是否投入时间的第一步，反之，忘记了用途，知识就成了记忆的孤岛。
*  **重要**: 衡量标准时这个**知识点**对你未来的**行动力**的**Impact**, 必须知道 > 有帮助 > 可能有帮助。 系统优化 > 思维提升 > 实施细节。
*  **合并**：配合dropbox利用「shortcuts」的[shortcut](https://i.imgur.com/ac30rCf.jpeg)和[automation](https://i.imgur.com/BoIyroH.png)，同时修改Macbook默认截图存储路径，可以使得iPhone和Macbook的截图在一处，而不用任何额外操作。
* **提问**：这个「知识点」有什么用？我为什么截图？思维方式，还是实施细节？主线任务，还是支线任务？
2. **连接**：这个与我以前做的东西有什么联系？
3. **视觉**：想象实际的使用场景？想象它是如何生长到我的「知识树」上的？
4. **组织**：把这个「知识点」放到那个节点上呢？急迫且重要，则贴上**标签

## Q&A

* How to change default mac screenshot location?
	* defaults write com.apple.screencapture location **~/Desktop**
	* killall SystemUIServer 
* How to save space for screenshots if needed? 
	* for i in *.png; do sips -s format jpeg -s formatOptions 5 "${i}" --out "${i%png}jpg"; done
* Should I delete screenshot after review?


