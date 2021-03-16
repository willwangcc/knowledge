# TypeScript

## 1. Background  


## 2. What is TypeScript ?



## 3. Why do we need TypeScript?

[Why We Chose Typescript](https://redditblog.com/2017/06/30/why-we-chose-typescript/)

## 4. How to use TypeScript?

If you have been familiar with any Object Oriented Language, just play TypeScript on [TypeScript Online](https://www.typescriptlang.org/play/) and google when you encounter problems.

``` TypeScript
class Greeter {
    greeting: string;
    constructor(message: string) {
        this.greeting = message;
    }
    greet() {
        return "Hello, " + this.greeting;
    }
    max(x: number, y: number): number {
        return x > y ? x : y;
    }
}

let greeter = new Greeter("world");

let button = document.createElement('button');
button.textContent = "Say Hello";
button.onclick = function() {
    alert(greeter.max(2, 4));
}

document.body.appendChild(button);
```

0. [TypeScript Online](https://www.typescriptlang.org/play/)
1. [Quick start](https://www.typescriptlang.org/docs/tutorial.html)
2. [TypeScript Deep Dive](https://basarat.gitbooks.io/typescript/)
3. [TypeScript at Slack](https://slack.engineering/typescript-at-slack-a81307fa288d)



## Reference

1. [TypeScript 入门教程](https://ts.xcatliu.com/)