<h1 align="center">
<br>
	<a href="https://www.wikiwand.com/en/Find_(Unix)">
  <img src="https://i.imgur.com/8qNj2bL.jpeg" alt="find" width=42%">
  </a>
  <br><br>
find (Unix)  
  <br><br>
</h1>


> In Unix-like and some other operating systems, find is a command-line utility that **locates** files based on some **user-specified criteria** and then applies some **requested action** on each matched object. [[wiki](https://www.wikiwand.com/en/Find_(Unix))]

## Why 

search from a desired starting location and then recursively traversing the nodes (directories) of a hierarchical structure (typically a tree).

## How

### Examples

#### From the [current](https://www.wikiwand.com/en/Find_(Unix)#/From_the_current_working_directory) working directory

``` bash
$ find . -name 'my*'
```

This searches the current working directory tree for **files whose names start with my**. The single quotes avoid the shell expansion—without them the shell would replace my* with the list of files whose names begin with my in the current working directory. In newer versions of the program, the directory may be omitted, and it will imply the current working directory.

#### Regular files only

``` bash
$ find . -name 'my*' -type f
```

This limits the results of the above search to **only regular files**, therefore excluding directories, special files, symbolic links, etc. my* is enclosed in single quotes (apostrophes) as otherwise the shell would replace it with the list of files in the current working directory starting with my…

#### Search all directories

``` bash
$ find / -name myfile -type f -print
``` 
This searches **every directory for a regular file whose name is myfile and prints it to the screen**. It is generally not a good idea to look for files this way. This can take a considerable amount of time, so it is best to specify the directory more precisely. Some operating systems may mount dynamic file systems that are not congenial to find. More complex filenames including characters special to the shell may need to be enclosed in single quotes.



## What 

### Overview

In Unix-like and some other operating systems, find is a command-line utility that **locates** files based on some **user-specified criteria** and then applies some **requested action** on each matched object.

It initiates a search from **a desired starting location** and then recursively traversing the **nodes** (directories) of a hierarchical structure (typically a **tree**). find can traverse and search through different file systems of partitions belonging to one or more storage devices mounted under the starting directory.

The possible search criteria include a pattern to match against the **filename** or a **time range** to match against the modification time or access time of the file. By default, find returns a list of all files below the current working directory, although users can limit the search to any desired maximum number of levels under the starting directory.

The related locate programs use a database of indexed files obtained through find (updated at regular intervals, typically by cron job) to provide a faster method of searching the entire file system for files by name.


### Others

* **History**
* Find syntax
* POSIX protection from infinite output
* Examples
* Related utilities

## FAQs

#### Q: find vs grep?

A: The main **difference** between the two is that grep is used to search for **a particular string in a file** whereas find is used to **locate files in a directory**, etc. also you might want to check out the two commands by typing 'man find' and 'man grep'. ... Find is for searching **files** and grep is for searching **string**.

source: [toolbox.com](https://www.toolbox.com/tech/operating-systems/question/difference-between-grep-and-find-command-100906/#:~:text=The%20main%20difference%20between%20the,'%20and%20'man%20grep'.&text=Find%20is%20for%20searching%20files%20and%20grep%20is%20for%20searching%20string.)

