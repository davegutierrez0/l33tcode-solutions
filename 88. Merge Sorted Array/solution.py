class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i, x in enumerate(nums1):
            if i>m-1 and nums1[i] == 0:
                nums1[i] = nums2.pop()

        nums1.sort()