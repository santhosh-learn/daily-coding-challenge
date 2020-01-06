"""
Given an array of integers,
return a new array such that each element at index [i] of the new array is the product of all the numbers in the original array except the one at [i].

For example,
if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""
inputArray= [1, 2, 3, 4, 5]
inputArrayLength=len(inputArray)

topArray=list(range(inputArrayLength))
bottomArray=list(range(inputArrayLength))

outputArray=[]

p=1
q=1

for x in range(inputArrayLength):
   topArray.append(p)
   p*=inputArray[x]

for x in list(range(inputArrayLength))[::-1]:
   bottomArray[x]=q
   q*=inputArray[x]

for x in range(inputArrayLength):
    outputArray.append(topArray[x]*bottomArray[x])

print(outputArray)