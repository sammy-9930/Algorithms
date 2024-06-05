from typing import List

"""Bucket sort, hashing, """
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap_nums = {}
        freq = [[] for i in range(len(nums) + 1)]
        print("freq: ", freq)
        for number in nums:
            hashmap_nums[number] = 1 + hashmap_nums.get(number, 0)
            # if nums[i] in hashmap_nums:
            #     hashmap_nums[nums[i]] += 1
            # else:
            #     hashmap_nums[nums[i]] = 1
        print(hashmap_nums)
        for key, value in hashmap_nums.items():
            freq[value].append(key)

        final_list = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                final_list.append(n)
                print(final_list)
                if len(final_list) == k:
                    return final_list


solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
result = solution.topKFrequent(nums, k)
print(result)