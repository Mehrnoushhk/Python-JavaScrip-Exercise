from typing import List

# ******************* First Solution******************
# def remove_duplicate(nums):
#     idx = 1
#     for i in range(1, len(nums)):
#         if nums[i] != nums[idx - 1]:
#             nums[idx] = nums[i]
#             idx = idx + 1
#     while len(nums) > idx:
#         nums.pop()
#     return(nums)



print(remove_duplicate(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
