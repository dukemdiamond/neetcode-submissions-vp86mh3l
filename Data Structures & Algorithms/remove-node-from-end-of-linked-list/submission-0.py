# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # So we could find the total length of the list, say L
        # Then we would remove the (L - n)nth node. 
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        
        # We also need to create a dummy node. This will help handle deletion near or at the head.
        dummy = ListNode(0, head)

        # We go to the node before the one we want to remove.
        prev = dummy
        steps = l - n
        for x in range(steps):
            prev = prev.next
        if prev.next:
            prev.next = prev.next.next
        
        return dummy.next
        