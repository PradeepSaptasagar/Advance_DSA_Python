# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # Fewer than k nodes remain: leave them unchanged.
            group_next = kth.next  # First node after this group.
            prev, cur = group_next, group_prev.next
            while cur is not group_next:
                nxt = cur.next       # Save next node before changing the link.
                cur.next = prev      # Reverse this node's pointer.
                prev = cur
                cur = nxt
            old_group_head = group_prev.next  # It is now the group's tail.
            group_prev.next = kth            # Connect previous part to reversed group.
            group_prev = old_group_head
            