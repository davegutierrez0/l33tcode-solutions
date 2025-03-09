class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1: return strs[0]

        common_prefix = ''

        i = 0 
        
        # Iterate through letters of first word 
        while i < len(strs[0]):
            common_prefix += strs[0][i]
            for word in strs:
                if not word.startswith(common_prefix):
                    return common_prefix[:len(common_prefix)-1]

            i += 1
        return common_prefix

# Time complexity: O(n*m) where n is the number of words and m is the length of the shortest word
# Space complexity: O(m) where m is the length of the shortest word