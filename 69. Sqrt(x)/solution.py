class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        
        # Binary search time 
        left, right = 1, x // 2
        
        
        while left <= right: 
            
            # Square root is never larger than half the number for x>=4 
            mid = (left + right) // 2
            
            # Right in the middle case
            if mid * mid == x:
                return mid
            
            
            # Left inches up to middle if too small
            elif mid * mid < x:
                result = mid # New floor
                left = mid + 1
                
            # Otherwise if too large, right inches downward 
            else: 
                right = mid - 1
                
            return result # Largest whole integer square root value


# Time Complexity: O(log(n)) due to binary search
# Space Complexity: O(1) due to only a few integer variables used 