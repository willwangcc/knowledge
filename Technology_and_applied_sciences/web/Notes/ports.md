# Ports

## Background Story 
In Apache Configuration, we set the listen port from 8080 to 80. So I just need to visit **http://localhost** instead of http://localhost:8080.

**Why?**

It is becuase **HTTP uses port 80** by default. So it is the same between http://localhost and http://localhost:80.

While entering a URL in a browser, if you do not enter the port no., then the request by default goes to port 80 (HTTP). Here is an exercise for you. Open these two URLs in your browser:

www.google.com

www.google.com:80

But if the server is listening at port 8080, you will always have to specify 8080. Why? Cause 8080 is not famous. 



## What is Port? 

![Port](https://i.imgur.com/AORJ9TW.jpg)
Ports are like rooms in a big buidling. When you want to send something, say a package, you need to tell the 
courier "which building you want to send" and "the room number", thus **port**.

In any building, we think there cannot be more than 65536(2^16) rooms.

As we know, there are always some room numbers better famous than other room numbers, just like some phone numbers are more fammous. (like 911)

In the computer world, there are 0 - 1023 port numbers.

By default, **HTTP uses port 80** and HTTPS uses port 443.

![Famous Port ](https://i.ytimg.com/vi/zCAyinelie0/maxresdefault.jpg)

## Why do we need port? 

### 1. Mutitasking
Ports were unnecessary on direct **point-to-point** links when the computers at each end could only run one program at a time. Ports became necessary after computers became **capable of executing more than one program** at a time and were connected to modern networks.

### 2. Filter Network Traffic 
When we know which port means which, we can make some port numbers have higher priority based on our demand. It is just like we always give way to important people, like the president.

![](https://i.imgur.com/ZDCn7B2.jpg)
![](https://i.imgur.com/m5kaFTL.png)


## How to use it? 

Port numbers are sometimes seen in web or other uniform resource locators (URLs). **By default, HTTP uses port 80 and HTTPS uses port 443**, but a URL like http://www.example.com:8080/path/ specifies that the web browser connects instead to port 8080 of the HTTP server.



![Ports in Action](https://i.imgur.com/TvkqoWB.png)
![Ports in Web](https://i.imgur.com/Mv1YXlk.jpg)


### Reference:
- https://www.wikiwand.com/en/- Port_(computer_networking)
- https://www.youtube.com/watch?v=zCAyinelie0
- [Youtube: Ports & IP Addressing](https://www.youtube.com/watch?v=zCAyinelie0)
- https://www.quora.com/Are-port-80-and-8080-the-same