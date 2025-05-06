def pair_sum(numbers, target_sum):
  
  previous = {}

  for i in range(len(numbers)):
    complement = target_sum - numbers[i]

    if complement in previous:
      return (previous[complement],i)
    else:
      previous[numbers[i]] = i
    
# Time complexity: O(n)
# Space complexity: O(n)
# Hashmap is used to store the indices of the numbers to 
# reduce the time complexity and use only a single pass