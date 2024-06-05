from typing import List


# class Solution:
#     def getconcatenation(self, nums: List[int]):
#         ans = []
#         for _ in range(2):
#             for i in nums:
#                 ans.append(i)
#         return ans


# class Solution:
#     def getconcatenation(self, nums : List[int]):
#         return nums + nums


class Solution:
    def getconcatenation(self, nums: List[int]):
        ans = []
        for i in range(len(nums)):
            nums.append(nums[i])
            ans = nums
        return ans


nums = [1, 2, 1]
sol = Solution()
result = sol.getconcatenation(nums)
print(result)
