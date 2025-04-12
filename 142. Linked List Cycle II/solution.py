# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow = head
        fast = head

        # Determine whether loop exists first
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break

        else:
            return None
        
        # Second phase to determine where
        slow = head 
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
    
    
# Time Complexity: O(N)
# Space Complexity: O(1)
# N = number of nodes in the linked list
# Mnemonic: 🐢🐇 "Detect, then Reset and Race"  #️⃣ #TortoiseAndHare