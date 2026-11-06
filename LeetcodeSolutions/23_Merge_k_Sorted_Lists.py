# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))  # Node value orders the heap; i breaks ties.
        dummy = ListNode(0)
        tail = dummy
        while heap:
            _, i, node = heapq.heappop(heap)  # Extract the smallest remaining node.
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))  # Add its successor.
        tail.next = None  # Terminate the resulting list.
        return dummy.next
            