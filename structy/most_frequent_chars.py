
def most_frequent_char(s):

  if not s:
    return None

  
  char_set = set(s)
  count = 0
  most_common = s[0]
  
  for char in char_set:
    char_count = s.count(char)
    if char_count > count:
      most_common = char
      count = char_count

  return most_common

# time complexity: O(n^2)
# space complexity: O(n)


def most_frequent_char(s):

  if not s:
    return None

  
  frequency = {}

  for char in s:
    frequency[char] = frequency.get(char,0) + 1

  return max(frequency, key=frequency.get)

# time complexity: O(n)
# space complexity: O(n)
# The second implementation is more efficient than the first one.
# The first implementation has a time complexity of O(n^2) because it uses the count() method inside a loop, which iterates through the string for each character in the set.
# The second implementation has a time complexity of O(n) because it iterates through the string once to create the frequency dictionary and then uses the max() function to find the character with the highest frequency.
# The space complexity of both implementations is O(n) because they both use additional data structures (set and dictionary) to store the characters and their frequencies.