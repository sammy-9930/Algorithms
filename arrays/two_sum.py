class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(len(nums)):
            expected_number = target - nums[i]
            if expected_number in hash_map:
                return [hash_map[expected_number], i]
            else:
                hash_map[nums[i]] = i


solution = Solution()
nums = [3, 2, 4]
target = 6
result = solution.twoSum(nums, target)
print(result)
