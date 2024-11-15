from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        
        output = [1] * n
        
        for i in range(1, n):
            
            # Check LH neighbor
            if ratings[i] > ratings[i-1]:
                output[i] = output[i-1] + 1
                
                
                
        for i in range(n - 2, -1, -1):
            # Check RH neighbor
            if ratings[i] > ratings[i+1] and output[i] <= output[i+1]:
                output[i] = output[i+1] + 1
            
        return sum(output)
                


    
        
        
# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.candy(ratings = [1,2,87,87,87,2,1]))    
    print(solution.candy(ratings = [1,3,2,2,1]))    
    print(solution.candy(ratings = [1,0,2]))    
    print(solution.candy(ratings = [1,2,2]))    

    
# Time Complexity: O(n)
# Space Complexity: O(n)