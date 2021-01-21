# map, reduce and filter  

![map, filter and reduce explained with emoji](https://i.imgur.com/agooVag.png)

Both `map` and `reduce` have as input **the array** and **a function** you define. They are in some way complementary: `map` cannot return one single element for an array of multiple elements, while `reduce` will always return the accumulator you eventually changed.

# map 

The `map()` method creates a **new** array with the results of calling **a provided function** on every element in the calling array.

``` javascript
// A function which calculates the square
const square = x => x * x

// Use `map` to get the square of each number
console.log([1, 2, 3, 4, 5].map(square))
```

foreach vs map: 

* `foreach`: This iterates over a list and **applies** some operation with **side effects** to each list member (example: saving every list item to the database)
* `map`: This iterates over a list, **transforms** each member of that list, and returns **another list** of the same size with the transformed members (example: transforming list of strings to uppercase)


# reduce 

The `reduce()` method applies a function against an **accumulator** and each element in the array (from left to right) to reduce it to **a single value**.

Using an array as an input, you can get one single element (let's say an Object, or a Number, or another Array) based on the callback function (the first argument) which gets the `accumulator` and  `current_element` parameters:



``` javascript 
const numbers = [1, 2, 3, 4, 5]

// Calculate the sum
console.log(numbers.reduce(function (acc, current) {
  return acc + current
}, 0)) // < Start with 0

// Calculate the product
console.log(numbers.reduce(function (acc, current) {
  return acc * current
}, 1)) // < Start with 1
```

# filter 

The `filter()` method creates **a new array** with all elements that **pass the test** implemented by the provided function.

``` javascript 
const words = ["spray", "limit", "elite", "exuberant", "destruction", "present"];

const longWords = words.filter(word => word.length > 6);
// longWords is ["exuberant", "destruction", "present"]
```

## Thanks 

- https://stackoverflow.com/questions/49934992/main-difference-between-map-and-reduce
- [JavaScript’s Reduce Method Explained By Going On a Diet](https://blog.codeanalogies.com/2018/07/24/javascripts-reduce-method-explained-by-going-on-a-diet/) :  If you have ever read a nutrition label, then you can understand the reduce() method in JavaScript.

