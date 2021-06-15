<h1 align="center">
<br>
	<a href="https://www.wikiwand.com/en/Grep">
  <img src="https://i.imgur.com/II8yoVH.png" alt="grep example" width=42%">
  </a>
  <br><br>
Grep 
  <br><br>
</h1>

> grep is a command-line **utility** for **searching plain-text data sets** for lines that match a **regular expression**. [[wiki](https://www.wikiwand.com/en/Grep)]

## Why 

### Why do you care about Grep?

![](http://imgur.com/i87vM6b.png)

### Whye do we use Grep?

1. **Saves time** over finding the required configuration.
1. Solves the problem related to the **troubleshooting** more quickly.
1. Help for **debugging** the code more quickly.
1. Finding out the **blank files and folders** in Linux.

source: [fosslinux.com](https://www.fosslinux.com/18892/top-5-uses-of-grep-command.htm)

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

### use case 

1. How to exclude the parameter/search string?
2. Count the **occurrence** of a string
3. How to search in the tar(zip) file
4. How to get the line before and after the searched string?
5. BONUS and the Bumper One, How the search a string in all file in the directory

source: [Top 5 uses of GREP command in Linux](https://www.fosslinux.com/18892/top-5-uses-of-grep-command.htm)


### [Examples](https://ss64.com/osx/grep.html) 

Search the file example.txt, including binary data (-a) for the string 'hunting the snark':

```
$ sudo grep -a 'hunting the snark' example.txt
```

Search the whole partition (/disk0), including binary data (-a) for the string 'hunting the snark' return all the lines
starting 25 Before the text found and 50 lines After the matching text found, this can be a way to discover fragments of deleted files:

```
$ sudo grep -a -B 25 -A 50 'hunting the snark' /dev/disk0> results.txt
```

Search the file wordlist.txt for any lines that don't include at least one vowel:

```
$ grep -v [aeiou] wordlist.txt
```

Remove lines from invoices.txt if they appear in paid.txt:

```
$ grep -F -x -v -f paid.txt invoices.txt >paidinvoices.txt
```

List all the file links in the current folder - in the ouptut of ls each symbolic directory has l permission at the begining of the permission flags, so grep ^l will list only symbolic links:

```
$ ls -lR | grep ^l
A less cryptic method is to use find . -type l
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


#### Q: How to grep All Files in a Directory Recursively?

[A](https://elearning.wsldp.com/linuxcommands/grep-all-files-in-directory-recursively/#:~:text=To%20grep%20All%20Files%20in%20a%20Directory%20Recursively%2C,search%20the%20string%20inside%20the%20current%20working%20directory.): 

```
grep -R error /var/log/
```

* `-R`: Read all files under each directory, recursively This is equivalent to the -d recurse option.

#### Q: How to search plain-text data sets for lines that match a regular expression in a folder?

A:

```
grep -R "communication" ./
```
