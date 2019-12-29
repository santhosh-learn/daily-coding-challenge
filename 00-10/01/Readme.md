##Two sum problem
```
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
```

###solution
```
If the array is: [4, 5, 1, 8] and the sum is 6 the algorithm would proceed with the steps below:
```
```
1. The hash table is initially empty and the first element in the array is 4. We simply put 4 into the hash table.

2. The next element is 5. We check to see if the sum minus the current element exists in the hash table. 6 - 5 = 1 does not exist in the hash table. So add 5 to the hash table.

3. The next element is 1. We check to see if the sum minus the current element exists in the hash table. 6 - 1 = 5 does exist in the hash table so we found a pair!
```
###Sources
>[Coderbyte.com](https://coderbyte.com/algorithm/two-sum-problem)
