def intersection(a, b):
  a_set = set(a)

  intersection = []

  for num in b:
    if num in a_set:
      intersection += [num]

  return intersection

# Time complexity: O(n+m)
# Space complexity: O(n)
# where n is the length of a and m is the length of b
# The time complexity is O(n+m) because we are iterating through both lists once.
# The space complexity is O(n) because we are using a set to store the elements of list a.
