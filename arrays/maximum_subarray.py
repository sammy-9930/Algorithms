from typing import List

"""Approach 1: time complexity O(N3)"""
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = 0
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 current_sum = 0
#                 for k in range(i, j+1):
#                     current_sum += nums[k]
#                     if current_sum > max_sum:
#                         max_sum = current_sum
#         return max_sum

"""Approach 2: Time complexity O(N2)"""
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = 0
#         for i in range(len(nums)):
#             print("i: ", nums[i])
#             current_sum = 0
#             for j in range(i, len(nums)):
#                 print("j :", nums[j])
#                 current_sum += nums[j]
#                 print("current_sum : ", current_sum)
#                 if current_sum > max_sum:
#                     max_sum = current_sum
#                     print("max_sum : ", max_sum)
#         return max_sum

"""Approach 3: Kadane's algorithm
Time complexity: O(N)"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        # initialize max subarray to a default value
        max_sub = nums[0]
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
        return max_sub


solution = Solution()
# array_of_numbers = [5, 4, -1, 7, 8]
array_of_numbers = [-2, 1, -3, 4, -3, 15]
result = solution.maxSubArray(array_of_numbers)
print(result)
