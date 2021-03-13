from typing import List


# **************First Solution******************
# def solution(arr: List[int]) -> bool:
#     is_mountain = False
#     if len(arr) < 3:
#         return is_mountain
#     elif arr[1] <= arr[0]:
#         return is_mountain
#     else:
#         for i in range(2, len(arr)):
#             if arr[i] > arr[i - 1]:
#                 continue
#             elif arr[i] == arr[i - 1]:
#                 break
#             else:
#                 for j in range(i + 1, len(arr)):
#                     if arr[j] >= arr[j - 1]:
#                         inner_break = True
#                         break
#                 else:
#                     is_mountain = True
#             if is_mountain or inner_break:
#                 break
#     return is_mountain

# ************** This is Faster*******************
def solution(arr: List[int]) -> bool:
    is_mountain = False
    i = 1
    while i < len(arr):
        if arr[i] > arr[i - 1]:
            i = i + 1
        else:
            break
    if i == 1 or i == len(arr):
        return is_mountain
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            i += 1
        else:
            break
    if i == len(arr):
        is_mountain = True
    return is_mountain
    



print(solution(arr=[0, 3, 2, 1]))
