from typing import List


def solution(arr: List[int]) -> List[int]:
    i = len(arr) - 1
    temp_max = arr[i]
    arr[i] = -1
    i -= 1
    while i >= 0:
        temp = arr[i]
        arr[i] = temp_max
        temp_max = max(temp, temp_max)
        i -= 1
    return (arr)
    

print(solution(arr=[400]))
