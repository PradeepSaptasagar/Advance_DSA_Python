# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        count = 0
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next
        target = count - n
        slow = dummy
        for _ in range(target):
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr is not None:
            nodes.append(curr)
            curr = curr.next
        size = len(nodes)
        if n == size:
            return head.next
        target_prev = nodes[size - n - 1]
        target_prev.next = target_prev.next.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_map = {}
        curr = head
        count = 0
        while curr is not None:
            count += 1
            node_map[count] = curr
            curr = curr.next
        if n == count:
            return head.next
        target_prev = node_map[count - n]
        target_prev.next = target_prev.next.next
        return head