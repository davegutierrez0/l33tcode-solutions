# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2 or (not list1 and not list2):
            return list1

        if list2 and not list1:
            return list2

        list1_pointer = list1
        list2_pointer = list2
        if list1_pointer.val <= list2_pointer.val:
            merged_list_head = list1_pointer 
            list1_pointer = list1_pointer.next

        else:
            merged_list_head = list2_pointer
            list2_pointer = list2_pointer.next


        current = merged_list_head

        while list1_pointer or list2_pointer:

            # Both still have values
            while list1_pointer and list2_pointer:

                # Add to list whichever is smaller first 
                if list1_pointer.val <= list2_pointer.val:
                    current.next = list1_pointer
                    current = current.next
                    list1_pointer = list1_pointer.next

                else:
                    current.next = list2_pointer
                    current = current.next
                    list2_pointer = list2_pointer.next


            # Add to list
            while list1_pointer:
                current.next = list1_pointer
                current = current.next

                # Increment List1
                list1_pointer = list1_pointer.next


            while list2_pointer:
                # Add to list
                current.next = list2_pointer
                current = current.next

                # Increment List2
                list2_pointer = list2_pointer.next
            
        return merged_list_head


# Time Complexity: O(N + M)
# Space Complexity: O(1)
# 🧵 Stitch the lists with a pointer:
# 1. Pick the smaller head → that's your thread start 🪡
# 2. While both lists exist:
#    - Sew on the smaller node → current.next = smaller
#    - Advance both the thread and source
# 3. When one list runs out, stitch the rest wholesale