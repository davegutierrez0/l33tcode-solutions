class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False

        if not s or s == t:
            return True

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j+=1

        return i == len(s)

# Time Complexity: O(N), where N = len(t)
# Space Complexity: O(1)

# 🧠 Easy Way to Remember:
# # Two fingers, one goal — move on match, skip on noise.
# # s = melody you're listening for
# # t = the crowd of sounds
# # Advance only when you hear the right note