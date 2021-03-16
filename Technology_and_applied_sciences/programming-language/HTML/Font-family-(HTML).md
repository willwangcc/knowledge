<h1 align="center">
<br>
	<a href="https://www.wikiwand.com/en/Font_family_(HTML)">
  <img src="https://i.imgur.com/9G4ZTiW.png" alt="a design geek's paradise" width=42%">
  </a>
  <br><br>
Font family (HTML) 
  <br><br>
</h1>

> In HTML and XHTML, a CSS font family property is used to specify **a list of prioritized fonts** and **generic family names**; in conjunction with **correlating font properties**, this list determines the particular font face used to **render** characters. A font family is a grouping of fonts defined by 9 shared design styles. [[wiki](https://www.wikiwand.com/en/Font_family_(HTML)#)]

## Why 

used to render characters

## How

* [playground](https://www.w3schools.com/css/tryit.asp?filename=trycss_font-family)

A font face attribute, combined with other font presentation attributes may be applied in the HTML using the deprecated font element.

``` css
.text { font-family: times, serif; font-size:14pt; font-style:italic; }
<p class="text">
Sample text formatted with CSS in a separate stylesheet.
</p>

<p style="font-family: times, serif; font-size:14pt; font-style:italic">
Sample text formatted with inline CSS.
</p>

<p><i><font face="times, serif" size="3">
Sample text formatted with the deprecated FONT tag.
</font></i></p>
```

A best practice for CSS font-family values is to separate values with **commas** and **whitespace**, putting multi-word values in **quotes**.


``` css
.text { font-family: "calibri", Garamond, 'Comic Sans MS'; }
```

In CSS, a font-family (or face attribute in HTML) is a preferentially ordered list of font families to use when rendering text. The list is separated by commas (as shown above). To avoid unexpected results, the last font family on the font list should be one of the **generic families** which are by default always available in HTML and CSS. In the absence of a font being found, the web browser will use its default font, which may be a user-defined one. Depending on the web browser, a user can in fact override the font defined by the code writer. This may be for personal taste reasons, but may also be because of some physical limitation of the user, such as the need for a larger font size or the avoidance of certain colors.

In addition to local fonts, modern web browsers support linking custom font files directly by using the @font-face declaration. Once included, such fonts can be listed in the font-family property, alongside all local and fallback fonts.


## What 

### Overview

In HTML and XHTML, a CSS font family property is used to specify **a list of prioritized fonts** and **generic family names**; in conjunction with **correlating font properties**, this list determines the particular font face used to **render** characters. A font family is a grouping of fonts defined by 9 shared design styles.

Fonts sharing a **common design style** are commonly grouped into **font families**; Font Families' members are differentiated by a character's **shape display** (stroke weight, slant, relative width, etc.); A **font face** is the unique combination of a specific font family, and some of its members properties (CSS font properties).


### Others

* Generic fonts

## FAQs

#### Q: keywords vs ?

A: 


