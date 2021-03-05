def solution(nums, target):
    nums_dict = {}
    for idx, num in enumerate(nums):
        if (target - num) in nums_dict:
            return [nums_dict[target - num], idx]
        else:
            nums_dict[num] = idx




nums = [14, 13, 6, 7, 8, 10, 1, 2]
target = 9

print(solution(nums, target))
