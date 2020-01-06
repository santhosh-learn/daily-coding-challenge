## Product Of All Numbers Except One - Hard
### Question
```
Given an array of integers, 
return a new array such that each element at index [i] of the new array is the product of all the numbers in the original array except the one at [i].

For example,
If our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
```

### Solution
```
Simple solution:

Input : [1, 2, 3, 4, 5]
Output: [(2*3*4*5), (1*3*4*5), (1*2*4*5), (1*2*3*5), (1*2*3*4)]
```
```
For O(N) solution:

Input : [1, 2, 3, 4]

topArray    =   [              1,         a[0],    a[0]*a[1],    a[0]*a[1]*a[2]  ]
BottomArray =   [ a[1]*a[2]*a[3],    a[2]*a[3],         a[3],                 1  ]

Multiplying the two arrays element by element gives the required result
```
### Sources
>[stackoverflow.com](https://stackoverflow.com/questions/2680548/given-an-array-of-numbers-return-array-of-products-of-all-other-numbers-no-div)
