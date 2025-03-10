from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        chars = Counter()
        max_length = 0

        if len(s) < 2:
            return len(s)

        n = len(s)
        left = right = 0

        while right < n:
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left +=1

            max_length = max(max_length, right - left + 1)

            right += 1

        return max_length



# Time Complexity: O(n) where worst case each character is visited twice
# Space Complexity: O(min(n,m)) where O(k) is the size of the set sliding window 