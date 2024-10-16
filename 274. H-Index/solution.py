from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        num_papers = len(citations)

        for h_index in range(max(citations),-1,-1):
            
            if h_index <= num_papers and h_index <= len([citation for citation in citations if citation >= h_index]):
                return h_index     
        
        
# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.hIndex(citations = [3,0,6,1,5]))    
    print(solution.hIndex(citations = [1,3,1]))
    
# Time Complexity: O(n^2)
# Space Complexity: O(1)