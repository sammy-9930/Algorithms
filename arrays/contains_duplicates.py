from typing import List

"""Time complexity: O(N)"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for number in nums:
            if number in hashset:
                return True
            hashset.add(number)
        return False


nums = [1,- 2, 3, 1]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)
