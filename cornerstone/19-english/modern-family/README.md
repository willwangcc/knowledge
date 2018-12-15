# 看美剧学英语 


## Todo 

1. [x] 完成[src2md](https://gist.github.com/01f63bfaca2bfa32eb5288053235a7de#file-src2md-py): 字幕格式生成markdown格式，便于清晰的网页浏览，配合chrome插件[Readlang Web Reader
	- [ ] 对markdown中的生词(知识点)进行高亮。 如 `知识点` 。
	- [ ] 将同一句话进行合并。便于之后整句调取。  
](https://chrome.google.com/webstore/detail/readlang-web-reader/odpdkefpnfejbfnmdilmfhephfffmfoh) 使用。 
2. [ ] 完成单词库的检查，即设计一个txt, 用来查找新的src中有没有生词。
	- 本质是设计一个可“持久化”的hashmap
	- 这个阶段只完成最最简单的单词, 格式如 `{magnate:2} `, 单词：遇到的次数。之后可以加入，词组，句型等。(知识点)
	- 在后者，需要使用一个**数据库**来完成这些事情。
	- 可能的要求：单词：出现此单词的句子
3. 1368个过滤器，便于加深对1368个单词的深化理解
	- e.g. push + push的说明 + 相关句子
	- e.g. push的习语，以push为核心周边词汇。
	- e.g. push的相关统计。push: 2, shove(push forcefully): 3; push about: 2; 
4. 导出到[quizlet](https://quizlet.com/zh-cn )， 自动化处理，加速复习的方便。
 