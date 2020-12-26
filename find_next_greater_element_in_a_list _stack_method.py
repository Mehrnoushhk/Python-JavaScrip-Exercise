# Given an array of integers, find the next greater element for every element in the array. The next greater element of an element x is the first grater number to the right of x, if there is no such number consider it -1


# Using Stacks
# To spped up use collection deque
from collections import deque
def find_next_greater(arr):
    result = [-1] * len(arr)
    s = deque()
    for i in range(0, len(arr)):
        while s and arr[s[-1]] < arr[i]:
            result[s[-1]] = arr[i]
            s.pop()
        s.append(i)
    print(result)

if __name__ == '__main__':
    find_next_greater([2, 7, 3, 5, 4, 6, 8])
    find_next_greater([5, 4, 3, 2, 1])

