class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs: return ''

        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for str in strs: 
                if str[i] != char:
                    return shortest[:i]


        return shortest

# Time complexity: O(n*m) where n is the number of words and m is the length of the shortest word
# Space complexity: O(1) since we are not using any extra space (previous version was actually (O(m*2) due to string concatenation)