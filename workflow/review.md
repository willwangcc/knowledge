# Review system

## To do 
* [x] [morning routine](https://i.imgur.com/xZVfpTV.png): 把Alfred中的命令(m1, m2, m3)三合一: `screenshots to evernote`
* [ ] 如何提高 @review 整理的时间效率，让其**Focus**在最重要的事情上？

## tools

<img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/> <img src="https://i.imgur.com/5L0C5zD.png" alt="shortcuts" width="20"/>
<img src="https://i.imgur.com/xeFNz0B.png" alt="review" width="20"/>
<img src="https://i.imgur.com/wkAKmBc.png" alt="evernote" width="20"/>
<img src="https://i.imgur.com/8MyBvDP.png" alt="drawing" width="20"/>
<img src="https://i.imgur.com/kLLtRlc.png" alt="drawing" width="20"/>


1. Shortcuts 
1. Alfred - review  
1. Evernote 
1. workflowy.com 
1. Github with MacDown 


## How: 整体逻辑? 

> 起源于好奇，定义成问题，发展于阅读，交流与思考，下切到行动指南，回归到总结反思，增值于分享输出

整体的操作逻辑如下：

* **截图**： 包括电脑和手机，条件是**值得复习和深入了解的知识点**都记录保留**学习现场**
* **归档**： screenshots to evernote using 「shortcuts」 & 「alfred/review」
* **记录**: 在「evernote」用**沉浸模式**阅读，在「workflowy」中记录所有知识点, 这个环节**越快越好**
* **分类**：将知识点分类到不同的**「github」知识库**中，然后**排序**处理


## How: 具体细节(10步)

<img src="https://i.imgur.com/TdhUSIf.png" alt="shortcuts" width="150"/> <img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/>
<img src="https://i.imgur.com/9XqaseO.png" alt="alfred-review" width="150"/>
<img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/>
<img src="https://i.imgur.com/2OIL9Zf.jpg" alt="evernote" width="100"/>
<img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/>
<img src="https://i.imgur.com/ADELdZ0.jpg" alt="workflowy" width="150"/>
<img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/>
<img src="https://i.imgur.com/MwXB1il.png" alt="workflowy" width="150"/>


1. **拿**起iPhone
1. 右**滑**屏幕
1. **点击**workflow1
1. **点击**workflow2
1. 跳出Alert窗口，**点击**“Delete”
1. Mac: **快捷键**`option + command + space`唤出Alfred
1. 输入`m,`, 回车`return`: 得到`evernote` 
1. Evernote: 快捷键`shift + return`进入“Present”模式
1. 鼠标**点击**图片: 进入图片模式
1. 开始在workflowy中记录“知识点”
1. 排序完，整理分享到「github」or 其他 

## How: set up? 

### Alfred 

![morning routine: review](https://i.imgur.com/p4OCLn6.png)


First step:

* move files in iCloud to Desktop: combine iPhone screenshot and Mac screenshot 
* convert png to jpeg in low quality: to save space 

``` bash 
cd /Users/wangzhixiang/Library/Mobile\ Documents/iCloud~is~workflow~my~workflows/Documents/screenshots
mv *.png /Users/wangzhixiang/Desktop/review
cd /Users/wangzhixiang/Desktop/review
for i in *.png; do sips -s format jpeg -s formatOptions 5 "${i}" --out "${i%png}jpg"; done
rm *.png
exit
```

Second step:

* write `applescript` to send files in `review` to evernote

``` applescript   
on alfred_script(q)
  -- your script here

tell application "Finder"	set fl to files of folder POSIX file "/Users/wangzhixiang/Desktop/review" as alias listend tellset theDate to current dateset today to date string of theDateon theSplit(theString, theDelimiter)	-- save delimiters to restore old settings	set oldDelimiters to AppleScript's text item delimiters	-- set delimiters to delimiter to be used	set AppleScript's text item delimiters to theDelimiter	-- create the array	set theArray to every text item of theString	-- restore the old setting	set AppleScript's text item delimiters to oldDelimiters	-- return the result	return theArrayend theSplittell application "Finder"	set NoOfFiles to count of (files of folder POSIX file "/Users/wangzhixiang/Desktop/review")end telltell application id "com.evernote.evernote"	set note1 to create note title today & " 🎟 " & NoOfFiles & " Cards" with text "知识卡片🎟-路标★&焦点❶-一生所学(术语&人名&反常识)" notebook "N1 - 浇水集1 - 正反卡片⚡️"	tell note1 to append text " "			repeat with f in fl		tell note1 to append attachment f				-- get the time of screenshot		set temp to f as string		set myTestString to temp		set myArray to my theSplit(myTestString, " ")		set choice to item 6 of myArray		tell note1 to append text choice		tell note1 to append text "⬆️"			end repeat		open note window with note1	-- delay NoOfFiles: no need 	NoOfFiles		tell application "Terminal"		do script "trash -v /Users/wangzhixiang/Desktop/review/*"
		do script "exit"	end tell	end tell

end alfred_script
-- -----------------------
-- reference
-- https://dev.evernote.com/doc/articles/applescript.php
-- http://www.documentsnap.com/evernote-mac-import-folder/
-- http://macscripter.net/viewtopic.php?id=27926 (count the number of files)
```



## log 

- 2018.10.28: 
	- 把 rm 改成 `trash`, 以备意外，可以回复。
	- 完成一键操作：files to evernote. 过程试图用javascript 取代 applescript，但是这是低频事件，提前优化，是一个错误策略。
