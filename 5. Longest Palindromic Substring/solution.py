class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans = [0,0]
        ansLength = 0

        for i in range(len(s)):
            # odd

            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > ansLength:
                    ansLength = right - left + 1
                    ans = [left,right + 1]
                
                left -= 1
                right += 1




            # even

            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > ansLength:
                    ansLength = right - left + 1
                    ans = [left,right + 1]
                
                left -= 1
                right += 1

        
        return s[ans[0]:ans[1]]
    
    
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)