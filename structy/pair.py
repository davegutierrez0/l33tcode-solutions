def pairs(elements):
  
  res = []
  
  for i in range(0,len(elements) - 1):
    for j in range(i + 1 ,len(elements)):
      res.append([elements[i],elements[j]])
  
  return res

# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# "One starts the race, the other chases the trace!"
# i picks the first, j looks ahead