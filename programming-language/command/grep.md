<h1 align="center">
<br>
	<a href="https://www.wikiwand.com/en/Grep">
  <img src="https://i.imgur.com/II8yoVH.png" alt="grep example" width=42%">
  </a>
  <br><br>
grep 
  <br><br>
</h1>

> grep is a command-line **utility** for **searching plain-text data sets** for lines that match a **regular expression**. [[wiki](https://www.wikiwand.com/en/Grep)]

## Why 

* **Saves time** over finding the required configuration.
* Solves the problem related to the **troubleshooting** more quickly.
* Help for **debugging** the code more quickly.
* Finding out the **blank files and folders** in Linux.

source: [Top 5 uses of GREP command in Linux](https://www.fosslinux.com/18892/top-5-uses-of-grep-command.htm)

## How

``` bash
$ grep root /etc/passwd
root:x:0:0:root:/root:/bin/bash
operator:x:11:0:operator:/root:/sbin/nologin

$ grep -n root /etc/passwd
1:root:x:0:0:root:/root:/bin/bash
12:operator:x:11:0:operator:/root:/sbin/nologin

$ grep -c false /etc/passwd
7
```

## What 

### Overview

grep is a command-line **utility** for **searching plain-text data sets** for lines that match a **regular expression**. Its name comes from the ed command g/re/p (globally search for a regular expression and print matching lines), which has the same effect. grep was originally developed for the Unix operating system, but later available for all Unix-like systems and some others such as OS-9.


### Others

* History
* Sample usage
* Implementations
* agrep
* Usage as a verb


## FAQs

#### Q: keywords vs ?

A: 


