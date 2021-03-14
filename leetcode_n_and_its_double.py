from typing import List


def solution(arr: List[int]) -> bool:
    has_double = False
    num_dict = {}
    for num in arr:
        if num * 2 in num_dict or num / 2 in num_dict:
            has_double = True
            break
        else:
            num_dict[num] = 0
    return has_double


print(solution(arr=[10, 2, 5, 3]))
    