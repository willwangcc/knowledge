# Algorithm 

## List 

1. How to Flatten an Array
1. Search for a symmetric node
1. Stack & Queue 
1. Reposition an Array
2. sorting algorithm
1. verify a prime number
1. Find all prime factors of a number
1. Get nth Fibonacci number
1. Find the greatest common divisor of two numbers?
1. Remove duplicate members from an array?
1. Merge two sorted array?
1. Swap two numbers without using a temp variable?
1. Reverse a string in JavaScript?
1. Find the first non repeating char in a string?
1. Match substring of a string?
1. Create all permutation of a string?
1. [Exclude items](https://repl.it/@WillWang42/Exclude-items)


## 1. [How to Flatten an Array](https://repl.it/@WillWang42/How-to-Flatten-an-Array)

> Given an nested array, flatten it to 1-dimension array.

## 2. Search for a symmetric node

## Verify a prime number 

``` javascript 
// https://repl.it/@WillWang42/isPrime
function isPrime(num){
  if (num === 1) return false;
  if (num > 1){
    for (i = 2; i < Math.sqrt(num)+1; i++){
      if (num % i === 0) return false;
    }
  }
  return true; 
}

// Test 
console.log(isPrime(1))   // false
console.log(isPrime(2))   // true
console.log(isPrime(4))   // false
console.log(isPrime(7))   // true
console.log(isPrime(101)) // true
```

## Find all prime factors of a number

Find all prime factors
``` javascript

```