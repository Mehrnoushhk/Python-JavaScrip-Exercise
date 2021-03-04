from typing import List

def twosum(nums: List[int], target: int) -> List[int]:
    def check(arr, idx, num):
        if arr[idx] > num:
            return 'gt'
        elif arr[idx] == num:
            return 'eq'
        else:
            return 'lt'

    nums.sort()
    n = len(nums)
    while True:
        start_idx = 0
        end_idx = n - 1
        idx = (end_idx - start_idx) // 2
        result = check(nums, idx, target)
        if result == 'eq':
            target_idx = idx
            break
        elif result == 'lt':
            start_idx = idx
            end_idx = n - 1
        else:
            start_idx = 0
            end_idx = idx
    return target_idx

nums = [2, 7, 11, 15]
target = 9
print(twosum(nums, target))