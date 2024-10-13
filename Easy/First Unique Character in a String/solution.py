class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # Single character case
        if len(s) == 1:
            return 0
        
        UPPER_BOUND = 10**5 + 1
        
        minimum_index = UPPER_BOUND
        
               
        found = set(s)

        for char in found:
            if s.count(char) == 1:
                minimum_index = min(minimum_index,s.index(char))
                

        return minimum_index if minimum_index < UPPER_BOUND else -1
            
            
            
        
        

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.firstUniqChar(s = "leetcode"))
    print(solution.firstUniqChar(s = "loveleetcode"))
    print(solution.firstUniqChar(s = "aabb"))
    print(solution.firstUniqChar(s = "aabbc"))

    
# Time Complexity O(n^2)
# Space Complexity O(1)