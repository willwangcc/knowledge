# Docker 

> Docker provides a way to run applications securely isolated in a container, packaged with all its **dependencies** and **libraries**.



## Why?

> 

Imagine you are working on an analysis in R and you send your code to a friend. Your friend runs exactly this code on exactly the same data set but gets a slightly different result. This can have various reasons such as a different operating system, a different version of an R package, et cetera. **Docker is trying to solve problems like that.**

**A Docker container can be seen as a computer inside your computer.** The cool thing about this virtual computer is that you can send it to your friends; And when they start this computer and run your code they will get exactly the same results as you did.

In short, you should use Docker because

* it allows you to **wrangle dependencies** starting from the operating system up to details such as R and Latex package versions
* it makes sure that your analyses are **reproducible**.

There are a couple of other points what Docker helps with:

* **Portability**: Since a Docker container can easily be sent to another machine, you can set up everything on your own computer and then run the analyses on e.g. a more powerful machine.
* **Sharability**: You can send the Docker container to anyone (who knows how to work with Docker).

### Pros

* **Reproducibility**: Similar to a Java application, which will run exactly the same on any device capable of running a Java Virtual Machine, a Docker container is guaranteed to be identical on any system that can run Docker. 
* **Isolation**: Dependencies or settings within a container will not affect any installations or configurations on your computer, or on any other containers that may be running.
* **Security**: With important caveats, separating the different components of a large application into different containers can have security benefits: if one container is compromised the others remain unaffected.
* **DockerHub**:  For common or simple use cases, such as a LAMP stack, the ability to save images and push them to Docker Hub means that there are already many well-maintained images available. Being able to quickly pull a premade image or build from an officially-maintained Dockerfile can make this kind of setup process extremely fast and simple.
* **Environment Management**: Docker makes it easy to maintain different versions of, for example, a website using nginx. You can have a separate container for testing, development, and production on the same Linode and easily deploy to each one.
* **Continuous Integration**: Docker works well as part of continuous integration pipelines with tools like Travis, Jenkins, and Wercker. Every time your source code is updated, these tools can save the new version as a Docker image, tag it with a version number and push to Docker Hub, then deploy it to production.



## What?

### Philosophy

- 集装箱/Container 
- 标准化/Standardization： ①运输方式 ② 存储方式 ③ API接口
- 隔离/

### Parts

- Image
- Container 
- Repository

The relationship between Image and Container is like class and instance in OOD. An instance of an image is called container. 

### Docker vs VM

- **Docker**: an abstract of **application layer** 
- **Virtual Machine**: an abstract of **physical hardware layer**


## How?
 
### example  
 
- [My Simple Approach to using Docker and PHP](https://bitpress.io/simple-approach-using-docker-with-php/) : A good **introductory** article to start using Docker

### configuration 

- install: https://docs.docker.com/install/
- usage: https://docs.docker.com/

### usage

* [**Dockerfile**](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) : Docker builds images automatically by reading the instructions from a `Dockerfile` -- a text file that contains all commands, in order, needed to build a given image. 
* [**Docker-compose.yml**](https://docs.docker.com/compose/compose-file/) : The Compose file is a YAML file defining services, networks and volumes. The default path for a Compose file is `./docker-compose.yml`.
* **Docker-compose**: Define and run multi-container applications with Docker.
	* `docker-compose build`： Build or rebuild services
	* `docker-compose up`：Create and start containers

## When?

### When to use Docker 

- Learning new technologies
- Basic use cases
- App isolation
- Developer teams

### When Not to Use Docker

- Your app is complicated and you are not/do not have a sysadmin.
- Performance is critical to your application. 
- You don’t want upgrade hassles.
- Security is critical to your application.
- Multiple operating systems.
- Clusters.

## More
 
- [可能是把Docker的概念讲的最清楚的一篇文章](https://juejin.im/post/5b260ec26fb9a00e8e4b031a)
- [What is Docker and Why should I use it?](https://ropenscilabs.github.io/r-docker-tutorial/01-what-and-why.html)
- [When and Why to Use Docker](https://www.linode.com/docs/applications/containers/when-and-why-to-use-docker/) 
- [Docker 101: What it is and why it’s important](https://www.networkworld.com/article/2361465/docker-101-what-it-is-and-why-it-s-important.html)