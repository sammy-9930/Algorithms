from collections import Counter

"""Time complexity: O(1)"""
# class Solution:
#     def isanagram(self, s: str, t: str) -> bool:
#         if len(t) != len(s):
#             return False
#         s = sorted(s)
#         t = sorted(t)
#         return s == t

# using Counter in python
# class Solution:
#     def isanagram(self, s: str, t: str) -> bool:
#         return Counter[s] == Counter[t]

"""Time complexity: O(s + t)"""
class Solution:
    def isanagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hashmap, t_hashmap = {}, {}
        for i in range(len(s)):
            # if the key does not exist in the hashmap, the default value the function is going to return is 0
            s_hashmap[s[i]] = 1 + s_hashmap.get(s[i], 0)
            t_hashmap[t[i]] = 1 + t_hashmap.get(t[i], 0)
        for c in s_hashmap:
            # handle validation if key doesn't exist
            if s_hashmap[c] != t_hashmap.get(c, 0):
                return False
        return True


s = "anagram"
t = "nagaram"
solution = Solution()
result = solution.isanagram(s, t)
print(result)


