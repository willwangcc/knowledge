<h1 align="center">
<br>
	<a href="https://www.wikiwand.com/en/Permutation#">
  <img src="https://i.imgur.com/fHBpsuY.png" alt="Permutation" width=42%">
  </a>
  <br><br>
Permutation
  <br><br>
</h1>

> In **mathematics**, a **permutation** of a set is, loosely speaking, an **arrangement** of its members into a **sequence** or **linear order**, or if the set is already ordered, a rearrangement of its elements. The word "permutation" also refers to the act or process of changing the linear order of an ordered set. [[wiki](https://www.wikiwand.com/en/Permutation#)]

## Why 

Permutations are used in almost every branch of mathematics, and in many other fields of science. In computer science, they are used for analyzing sorting algorithms; in quantum physics, for describing states of particles; and in biology, for describing RNA sequences.


## How

Algorithms to generate permutations

### Random generation of permutations

[Fisher–Yates shuffle](https://www.wikiwand.com/en/Fisher%E2%80%93Yates_shuffle)

### Generation in lexicographic order

There are many ways to systematically generate all permutations of a given sequence. One classic, simple, and flexible algorithm is based upon finding the next permutation in lexicographic ordering, if it exists. It begins by sorting the sequence in (weakly) increasing order (which gives its lexicographically minimal permutation), and then repeats advancing to the next permutation as long as one is found.

The following algorithm generates the next permutation lexicographically after a given permutation. It changes the given permutation in-place.

1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
1. Find the largest index l greater than k such that a[k] < a[l].
1. Swap the value of a[k] with that of a[l].
1. Reverse the sequence from a[k + 1] up to and including the final element a[n].

For example, given the sequence [1, 2, 3, 4] (which is in increasing order), and given that the index is zero-based, the steps are as follows:

1. Index k = 2, because 3 is placed at an index that satisfies condition of being the largest index that is still less than a[k + 1] which is 4.
1. Index l = 3, because 4 is the only value in the sequence that is greater than 3 in order to satisfy the condition a[k] < a[l].
1. The values of a[2] and a[3] are swapped to form the new sequence [1,2,4,3].
1. The sequence after k-index a[2] to the final element is reversed. Because only one value lies after this index (the 3), the sequence remains unchanged in this instance. Thus the lexicographic successor of the initial state is permuted: [1,2,4,3].

Following this algorithm, the next lexicographic permutation will be [1,3,2,4], and the 24th permutation will be [4,3,2,1] at which point a[k] < a[k + 1] does not exist, indicating that this is the last permutation.

This method uses about 3 comparisons and 1.5 swaps per permutation, amortized over the whole sequence, not counting the initial sort.

### Generation with minimal changes

* [Steinhaus–Johnson–Trotter algorithm](https://www.wikiwand.com/en/Steinhaus%E2%80%93Johnson%E2%80%93Trotter_algorithm)
* [Heap's algorithm](https://www.wikiwand.com/en/Heap%27s_algorithm)

###  Meandric permutations

## What 

### Overview

In **mathematics**, a **permutation** of a set is, loosely speaking, an **arrangement** of its members into a **sequence** or **linear order**, or if the set is already ordered, a rearrangement of its elements. The word "permutation" also refers to the act or process of changing the linear order of an ordered set.

### Permutations in computing

* Numbering permutations


#### Applications

Permutations are used in the interleaver component of the error detection and correction algorithms, such as turbo codes, for example 3GPP Long Term Evolution mobile telecommunication standard uses these ideas (see 3GPP technical specification 36.212[56]). Such applications raise the question of fast generation of permutations satisfying certain desirable properties. One of the methods is based on the permutation polynomials. Also as a base for optimal hashing in Unique Permutation Hashing.


### Others

* History
* Definition
* Notations
* Other uses of the term permutation
* Properties
* Permutations of totally ordered sets
* Permutations in computing


## FAQs

#### Q: Permutations vs  combinations?

A: Permutations differ from combinations, which are selections of some members of a set regardless of order. For example, written as tuples, there are six permutations of the set {1,2,3}, namely: (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), and (3,2,1). These are all the possible orderings of this three-element set.


