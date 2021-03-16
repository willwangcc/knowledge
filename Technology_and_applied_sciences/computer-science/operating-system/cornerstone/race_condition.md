# Race condition 

<img src="https://i.imgur.com/xJBC94R.jpg" alt="Inside the Linux Kernel" width="200" height = ""/>

by  [x race conditions](https://hacks.mozilla.org/2017/06/avoiding-race-conditions-in-sharedarraybuffers-with-atomics/)


## Background
	
在早期的UNIX版本中，存在一个叫UNIX login的攻击方式。当一个新用户登陆到系统后，需要从root权限切换到user权限，假如在切换过程中一直按ESC键，则会导致权限切换不成功，使得登陆的用户一直具有root权限，从而控制整个计算机。
	
## What? 
	
A race condition occurs when two or more threads can access **shared data** and they try to change it at the **same time**. 

Because the thread scheduling algorithm can swap between threads at any time, you don't know the order in which the threads will attempt to access the shared data. Therefore, the result of the change in data is dependent on the thread scheduling algorithm, i.e. both threads are "racing" to access/change the data.
	
## Examples
	
### the example in life: Money
	
* ![withdraw](https://i.imgur.com/kNuNnFc.jpg)
* ![transfer](https://i.imgur.com/IyEId68.jpg)
* ![final](https://i.imgur.com/j4tpEMb.png)
	
### the example in in the logic circuit 
	
Race condition is not only related with software but also related with hardware too. Actually the term initially was coined by the hardware industry.
	
> The term originates with the idea of two signals racing each other to influence the output first.
	
Race condition in a logic circuit:
	
![logic circuit](https://i.imgur.com/dCBkb43.png)
	
You need to do some replacement to map it to the software world:
	
"two signals" => "two threads"/"two processes"
	
"influence the output" => "influence some shared state"
	
## Code

Problems often occur when one thread does a "**check-then-act**" (e.g. "check" if the value is X, then "act" to do something that depends on the value being X) and another thread does something to the value in between the "check" and the "act". E.g:
	
``` c
if (x == 5) // The "Check"
{
// If another thread changed x in between "if (x == 5)" and "y = x * 2" above,
y = x * 2; // The "Act"
// y will not be equal to 10.
}
```
	
The point being, y could be 10, or it could be anything, depending on whether another thread changed x in between the check and act. You have no real way of knowing.
	
In order to prevent race conditions from occurring, you would typically put a lock around the shared data to ensure only one thread can access the data at a time. This would mean something like this:
	
```c 
// Obtain lock for x
if (x == 5)
{
y = x * 2; // Now, nothing can change x until the lock is released.
// Therefore y = 10
}
// release lock for x
```
	
## Reference
	
- [Secure Programming HOWTO: Chapter 7. Design Your Program for Security](https://www.dwheeler.com/secure-programs/Secure-Programs-HOWTO/avoid-race.html)
- [What is a race condition?](https://stackoverflow.com/questions/34510/what-is-a-race-condition)