from collections import Counter 

def anagrams(s1, s2):
  return True if Counter(s1) == Counter(s2) else False

# Time complexity: O(n)
# Space complexity: O(k) where k is distinct characters so at worse case O(n)
