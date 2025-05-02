class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        queue = deque([0])
        seen = set()



        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue
                if s[start:end] in word_set:
                    queue.append(end)
                    seen.add(end)

        return False

# Time Complexity: O(N^3) if you count substring slicing cost
# Space Complexity: O(N)
# Mnemonic: “Slice Dice and Think Twice”
# - "Slice" → Creating s[start:end] takes O(N) time
# - "Dice" → We're checking every possible slice of the string
# - "Think Twice" → For each of N start points, check up to N end points
#                   and slicing takes O(N) → O(N^3) total