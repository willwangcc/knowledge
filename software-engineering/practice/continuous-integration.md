# Continuous integration

![Control Flow Diagram of CI](https://i.imgur.com/CToD13w.png)

> the practice of **merging** all developer working copies to a shared mainline several times a day. 

## Why?

-  to develop **quickly** and **safely**
-  to make new features easier to deploy 

When developing software, we want to be able to verify that our new features or bug fixes are safe and work as expected. We do this by running tests against our code. Sometimes, developers will run tests locally to verify that their changes are safe, but developers may not have the time to test their code on every system their software runs in. Further, as more and more tests are added the amount of time required to run them, even only locally, becomes less viable. Because of this, continuous integration systems have been created.


## What?

- to test new code 
- to help engineers fix their bugs 
- to merge all developer working **copies** to a shared **mainline** 

Continuous Integration (CI) systems are dedicated systems used to test new code. Upon a commit to the code repository, it is the responsibility of the continuous integration system to verify that this commit will not break any tests. To do this, the system must be able to fetch the new changes, run the tests and report its results. Like any other system, it should also be failure resistant. This means if any part of the system fails, it should be able to recover and continue from that point.


## How?

- Jenkins
- Docker
- Bash 

## More 

- [Open Sourcing a Python Project the Right Way](https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/): **TravisCI** for continuous testing integration
- [Infrastructure as Code, Part One
](https://crate.io/a/infrastructure-as-code-part-one/): Infrastructure as Code (IaC) bridges the gap between system administrators and developers
- [Python Developers Survey 2018 Results](https://www.jetbrains.com/research/python-developers-survey-2018/): Which Continuous Integration (CI) system(s) do you regularly use? (multiple questions): Jenkins / Hudson
- [Node.js & JavaScript Testing Best Practices (2019)](https://medium.com/@me_37286/yoni-goldberg-javascript-nodejs-testing-best-practices-2b98924c9347): As an independent Node.js consultant I’m engaged and review 10+ projects every year and my customers justifiably ask to focus on testing. A few months ago, I started to document here the insights and repeating errors I observe at the field and suddenly it piled-up into 30 testing best practices.
- [Introducing HyperDev](https://www.joelonsoftware.com/2016/05/31/introducing-hyperdev/): Buy and configure a continuous integration solution
- [A Continuous Integration System](http://aosabook.org/en/500L/pages/a-continuous-integration-system.html): A simple project to help you understand what is CI.  This project will demonstrate a small, bare-bones distributed continuous integration system that is designed for extensibility.




