import math

def is_prime(n):
  if  n < 2:
    return False 
  
  for i in range(2,int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True
    
# Time Complexity: O(√N)
# Space Complexity: O(1)
# Mnemonic: "Only test up to root, or you'll overshoot."