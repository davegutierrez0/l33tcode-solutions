# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next    # Save next
            curr.next = prev         # Reverse
            prev = curr              # Move prev
            curr = next_node         # Move curr
        return prev

# Time Complexity: O(N)
# Space Complexity: O(1)