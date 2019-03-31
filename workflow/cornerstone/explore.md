# Explore： 如何快速解决一个新遇到的技术问题？ 


## Why?

- 在学习新知识和新技术时，有时会陷入问题漩涡，一个新问题接着一个新问题，迷失其中而忘记最初的问题是什么了。

想要得到的最佳实践是：

- **解决**：快速解决新问题
- **地图**：获得新技术的地图
- **积累**：获得当前问题解决方案的积累和推广

## How?

``` python
def solve():
	if solved:
		screenshot() # review
		return 
		
	while queue:
		record()
		define()
		if urgent:
			slove()
		else:
			screenshot()	
	return replay() # case study	
```

1. **记录**：出现新问题，一定先记录，再解决，避免陷入问题漩涡，忘记最初的问题是什么。
1. **定义**：定义问题是什么？
	- 定义清楚一个问题，就解决了一半的问题。
	- 明确**清晰**的结束条件，这是避免进入**问题漩涡**的一个重要步骤。
1. **选择**："要么不做，要做就做完"
	- 	**现在做**(对解决现有问题有用) or 
	-  **以后做**(对打基础有用 -> 截图)
1. **闭环**：
	1. 得到解决方案 → 截图交给「*review*」工作流
	1. 出现新的问题 → 循环到1


**复盘**：查询 `chrome://history/` ，理清解决目标过程遇到的

- **障碍**：思考下次如何优化？
- **收获**：连接到已有知识树。


Example: [本地运行一个开源工具](https://workflowy.com/s/explain-my-shell3/Y8ZlMSiGBKN3pKvI)

![本地运行一个开源工具](https://i.imgur.com/f5urBht.png)

## What?

- "要么不做，要做就做完": [Impatient Execution](https://briancasel.com/impatient-execution/) Fail Fast. 不做比做完更困难。

## More

- 费曼技巧