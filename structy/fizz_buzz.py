def fizz_buzz(n):

  result = []
  for i in range(1,n+1):
    if i % 15 == 0:
      result.append("fizzbuzz")
    elif i % 3 == 0:
      result.append("fizz")
    elif i % 5 == 0:
      result.append("buzz")
    else:
      result.append(i)

  return result

# Time Complexity: O(N)
# Space Complexity: O(N)
# Mnemonic: "Fizz for three, buzz for five, both for fifteen keeps it alive."