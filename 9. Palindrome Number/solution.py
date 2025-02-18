class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Eliminate negative numbers and multiples of 10 right off the bat
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        
        
        reversed_half = 0
        while x > reversed_half:    
            # Compare just one half of the digits
            # x % 10 gets the last digit        
            reversed_half = reversed_half * 10 + x % 10
            # x // 10 removes the last digit
            x //= 10 
            
            # continue on until reversed x half is larger
            
        # First part checks even DIGIT numbers and the second part checks odd DIGIT numbers (removes middle DIGIT)
        return x == reversed_half or x == reversed_half // 10
    
    
    # Time complexity is O(d) where d is the number of digits in x
    # Space complexity is O(1) because we only use one small variable to track the other half