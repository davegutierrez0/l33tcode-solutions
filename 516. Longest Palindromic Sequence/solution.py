class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        memo = [[0]*n for _ in range(n)]

        def lps(s,i,j,memo):
            
            # Return memo if computed already
            if memo[i][j] != 0:
                return memo[i][j]
            
            # If i is greater than j no palindrome here
            elif i > j:
                return 0
            
            # Single character palindrome
            elif i == j:
                return 1
            
            # Characters match - add two and go deeper in
            elif s[i] == s[j]:
                memo[i][j] = lps(s,i+1,j-1,memo) + 2
            else:
                # Otherwise take the max of one skipped character on either end 
                memo[i][j] = max(lps(s, i + 1, j, memo),lps(s,i,j-1,memo))
            
            return memo[i][j]
        
     

        return lps(s,0,n-1,memo)

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)