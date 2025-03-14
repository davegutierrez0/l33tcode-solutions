class Solution:
    def myPow(self, x: float, n: int) -> float:

        def binaryExp(x:float,n:int) -> float:

            if n == 0:
                return 1.0

            if n < 0:
                return 1.0 / binaryExp(x, -n)

            if n % 2 != 0:
                return x * binaryExp(x * x, (n-1) / 2)
            else:
                return binaryExp(x * x, n / 2)


        return binaryExp(x,n)



# Time Complexity: O(log |n|)
# Space Complexity: O(log |n|)  # due to recursive call stack