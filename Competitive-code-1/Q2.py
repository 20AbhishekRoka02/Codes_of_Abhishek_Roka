"""
Create function which will take size of an array, an array of numbers and target value, and returns array of pairs of numbers which sum is equal to target number.

Testcase 1:

Input:
[1,2,3,4,5]

target: 5

Output:
[1,4]
[2,3]

Testcase 2:

Input:
[-3,-2,3,2,4]

target: 0
Output:
[-3,3]
[-2,2]
"""

def sumPairs(size,array,target):
    result = []
    for i in range(size):
        for j in range(i+1,size):
            if array[i]+array[j] == target:
                result.append((array[i],array[j]))
    return result

number = [-3,-2,3,2,4]
target = 0

print(sumPairs(len(number),number,target))