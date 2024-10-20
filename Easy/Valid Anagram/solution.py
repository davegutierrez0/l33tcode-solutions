
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        return Counter(s) == Counter(t)



# Time complexity O(n)
# Space complexity O(n)

# Slower easy solution

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return True if sorted(s) == sorted(t) else False         
    
# # Time Complexity O(n*log(n))
# # Space Complexity O(n)