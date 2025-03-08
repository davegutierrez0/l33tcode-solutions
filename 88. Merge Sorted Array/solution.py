class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1_copy = nums1[0:m]
        pointer_1 = 0 
        pointer_2 = 0
        write_pointer = 0

        while write_pointer < len(nums1):
            if pointer_2 >= len(nums2) or (pointer_1 < m and nums1_copy[pointer_1] <= nums2[pointer_2]):
                nums1[write_pointer] = nums1_copy[pointer_1]
                pointer_1 += 1

            else:
                nums1[write_pointer] = nums2[pointer_2]
                pointer_2 += 1

            write_pointer += 1

# Time Complexity: (O(m + n))
# Space Complexity: O(m)