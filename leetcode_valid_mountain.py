from typing import List


def solution(arr: List[int]) -> bool:
    is_mountain = False
    if len(arr) < 3:
        return is_mountain
    elif arr[1] <= arr[0]:
        return is_mountain
    else:
        peak = 1
        for i in range(2, len(arr)):
            if arr[i] > arr[i - 1]:
                continue
            elif arr[i] == arr[i - 1]:
                break
            else:
                for j in range(i, len(arr)):
                    if arr[j] >= arr[i]:
                        inner_break = True
                        break
                else:
                    is_mountain = True
            if is_mountain or inner_break:
                break
    return is_mountain


print(solution(arr=[0, 3, 2, 1]))
