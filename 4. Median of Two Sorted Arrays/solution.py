class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total_size = m + n
        merged = []

        if total_size % 2 != 0:
            median_elements = [(m + n) // 2]
        else:
            median_elements = [(m+n) // 2 - 1, (m+n) // 2]

        p1 = p2 = 0

        for _ in range(total_size):
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    merged += [nums1[p1]]
                    p1 += 1 
                else:
                    merged += [nums2[p2]]
                    p2 += 1
            elif p1 < m:
                merged += [nums1[p1]]
                p1 += 1
            elif p2 < n:
                merged += [nums2[p2]]
                p2 += 1
                
        median = 0
        print(merged)
        for element in median_elements:
            median += merged[element]

        median /= len(median_elements)
        print(median)

        return median

# Time Complexity: O(m+n)
# Space Complexity: O(m+n)
# The time complexity is O(m+n) because we are merging two sorted arrays, which takes linear time.
# The space complexity is O(m+n) because we are storing the merged array, which can be as large as the sum of the two input arrays.
# The algorithm is efficient for finding the median of two sorted arrays, as it only requires a single pass through both arrays.
# The algorithm is not optimal for large arrays, as it uses O(m+n) space to store the merged array.
# An optimal solution would use O(log(min(m, n))) time and O(1) space by using binary search.
# However, this solution is simple and easy to understand, making it a good choice for small to medium-sized arrays.


# Improved version:

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total_size = m + n
        merged = []

        if total_size % 2 != 0:
            odd = True
        else:
            odd = False

        iteration_range = (m + n + 1) // 2 if odd else (m + n) // 2 + 1

        p1 = p2 = 0

        for _ in range(iteration_range):
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    merged += [nums1[p1]]
                    p1 += 1 
                else:
                    merged += [nums2[p2]]
                    p2 += 1
            elif p1 < m:
                merged += [nums1[p1]]
                p1 += 1
            elif p2 < n:
                merged += [nums2[p2]]
                p2 += 1
                
        median = merged[-1] if odd else (merged[-1] + merged[-2]) / 2
        print(merged)
        print(median)

        return median
            
# Time Complexity: O(log(m+n)) in the worst case
# Space Complexity: O(((m+n) // 2 + 1)
