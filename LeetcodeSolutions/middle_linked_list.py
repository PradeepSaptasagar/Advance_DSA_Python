# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes=[]
        curr=head
        while curr is not None:
            nodes.append(curr)
            curr=curr.next
        mid_index=len(nodes)//2
        return nodes[mid_index]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        curr=head
        while curr is not None:
            length+=1
            curr=curr.next
        steps_needed=length//2
        curr=head
        counter=0
        while counter<steps_needed:
            curr=curr.next
            counter+=1
        return curr