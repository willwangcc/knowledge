# Review system

## To do 
* [x] [morning routine](https://i.imgur.com/xZVfpTV.png): 把Alfred中的命令(m1, m2, m3)三合一: `screenshots to evernote`: 方案：连接，存疑？
* [ ] 如何提高 @review 整理的时间效率，让其**Focus**在最重要的事情上？

## tools

1. Shortcuts 
1. Alfred - review 
1. Evernote 
1. workflowy.com 


## workflow 

* **截图**： 包括电脑和手机，条件是值得复习和深入了解的知识点
* **归档**：Shortcuts & Alfred 
	* 每天早上使用App: 「Shortcuts」将手机截图传到特定目录。
	* 然后使用我自己的做的Alfred的「workflow - review」, 将所有传到Evernote, 并打开笔记。
* **记录**: 在evernote中浏览，在「workflowy」中记录所有知识点
* **分类**：对知识点分类
	* 值得系统化的，进一步阅读，归纳
	* To do list

## 操作操作度(13步)

1. 拿起iPhone
1. 右滑屏幕
1. 点击workflow1
1. 点击workflow2
1. 跳出窗口，点击“Delete”
1. Mac: 快捷键唤出Alfred
1. 输入m...
1. 选择 m1: convert png to jpeg
1. 选择 m2: convert file to evernote
1. 选择 m3: m3: delete jpeg3
1. Evernote: 快捷键进入“Present”模式
1. 鼠标点击图片，进入图片模式
1. 开始在workflowy中记录“知识点”

## show me 

![shortcuts](https://i.imgur.com/TdhUSIf.png)

![screenshots to evernote](https://i.imgur.com/0Cnx2EH.png)

![evernote](https://i.imgur.com/2OIL9Zf.jpg)

![workfowy](https://i.imgur.com/ADELdZ0.jpg)


## How 

### Alfred 

![morning routine: review](https://i.imgur.com/5nVzNlV.png)


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
	
tell application "Finder"
    set fl to files of folder POSIX file "/Users/wangzhixiang/Desktop/review" as alias list
end tell

set theDate to current date
set today to date string of theDate

tell application "Finder"
	set NoOfFiles to count of (files of folder POSIX file "/Users/wangzhixiang/Desktop/review" )
end tell

tell application id "com.evernote.evernote"
	set note1 to create note title today & " 🎟 " & NoOfFiles & " Cards" with text "知识卡片🎟-路标★&焦点❶-一生所学(术语&人名&反常识)" notebook "N1 - 浇水集1 - 正反卡片⚡️"
	tell note1 to append text " " 
	
	repeat with f in fl
		tell note1 to append attachment f
	end repeat
	
	open note window with note1

end tell 

end alfred_script
-- -----------------------
-- reference
-- https://dev.evernote.com/doc/articles/applescript.php
-- http://www.documentsnap.com/evernote-mac-import-folder/
-- http://macscripter.net/viewtopic.php?id=27926 (count the number of files)
```

Third Step:

* remove all files in `review`: cause we cannot run third script until step2 finished

``` bash 
cd /Users/wangzhixiang/Desktop/review
rm *.jpg
exit
```


## Wait to delete

* [m1](https://i.imgur.com/6811jYJ.png)
* [m2](https://i.imgur.com/APPTSMh.png)
* [m3](https://i.imgur.com/m1aaRb9.png)

