# SVG: 如何高效做一张文字图片？

## Why?

写一遍文章太长，一句话即可记得当时所想。如何快速制作一个文字图片？来当壁纸。

## How?


- code 

``` xml
<?xml version="1.0"?>
<svg width="1920" height="1200" xmlns="http://www.w3.org/2000/svg" version="1.1">
	<rect width="100%" height="100%" fill="#781e1e"/>

	<text text-anchor="middle"
			x="50%" y="50%"
			style="font: 192px Yuanti TC;
				fill: #872a29">
		<tspan font-weight="lighter">
			少  用  聰  明
		</tspan>
	</text>
</svg> 

```

- Chrome 打开 `少用聪明.svg`
- [Save SVG to PNG](https://gist.github.com/mbostock/6466603)

![少用图片](https://i.imgur.com/iIoeTj1.png)

## What?

- [SVG](https://www.wikiwand.com/en/Scalable_Vector_Graphics): an XML-based vector image format for two-dimensional graphics with support for **interactivity** and **animation**. SVG images and their behaviors are defined in XML text files. This means that they can be **searched**, **indexed**, **scripted**, and **compressed**. As XML files, SVG images can be created and edited with any text editor, as well as with drawing software.

## Q&A

- [Does SVG support embedding of bitmap images?](https://stackoverflow.com/questions/6249664/does-svg-support-embedding-of-bitmap-images)
- How do we view SVG on MacOS? [Gapplin](http://gapplin.wolfrosch.com/)
- 有什么字体推荐？[字体和风格](https://www.zhihu.com/question/20727176)

## More

Credit to [davidxk](https://github.com/davidxk)