<h1 align="center">
<br>
	<a href="https://www.wikiwand.com/en/Commit_(version_control)">
  <img src="https://i.imgur.com/WSVBK99.png" alt="git commits" width=42%">
  </a>
  <br><br>
Commit (version control) 
  <br><br>
</h1>

> In version control systems, a commit is an **operation** which sends the latest **changes** to the **source code** to the **repository**, making these changes part of the **head** revision of the repository. [[wiki](https://www.wikiwand.com/en/Commit_(version_control))]

## Why 

Good commit messages serve at least three important purposes:

* To speed up the **reviewing** process.
* To help us write a good **release note**.
* To help the future **maintainers** of Erlang/OTP (it could be you!), say five years into the future, to find out why a particular change was made to the code or why a specific feature was added.

## How

* [Commit message guidelines](https://www.mediawiki.org/wiki/Gerrit/Commit_message_guidelines)
* [Commit messages](https://wiki.koha-community.org/wiki/Commit_messages)
* [Writing good commit messages](https://github.com/erlang/otp/wiki/writing-good-commit-messages)
* [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary): A specification for adding human and machine readable **meaning** to **commit messages**
* [The whys and hows of a good commit message](https://www.slideshare.net/henriquemoody/commit-to-good-commit-messages)



## What 

### Overview

In version control systems, a commit is an **operation** which sends the latest **changes** to the **source code** to the **repository**, making these changes part of the **head** revision of the repository. Unlike commits in data management, commits in version control systems are kept in the repository indefinitely. Thus, when other users do an update or a checkout from the repository, they will receive the latest committed version, unless they specify they wish to retrieve a previous version of the source code in the repository. Version control systems allow rolling back to previous versions easily. In this context, a commit within a version control system is protected as it is easily rolled back, even after the commit has been applied.


### Usage

To **commit** a change in git on the command line, assuming git is installed, the following command is run:

``` bash 
git commit -m 'commit message'
```

This is also assuming that the files within the current directory have been **staged** as such:

``` bash 
git add .
```

The above command adds all of the files in the working directory to be staged for the git commit. After the commit has been applied, the last step is to push the commit to the given software repository, in the case below named origin, to the branch master:

``` bash
git push origin master
```

Also, a shortcut to add all the unstaged files and make a commit at the same time is:[2]

``` bash 
git commit -a -m 'commit message'
```

## FAQs

#### Q: keywords vs ?

A: 


