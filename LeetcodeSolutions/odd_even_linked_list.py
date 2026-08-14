# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = head
        count = 1
        while tail.next is not None:
            tail = tail.next
            count += 1
        curr = head
        for _ in range(count // 2):
            even_node = curr.next
            next_odd = even_node.next   # 1. Save the next odd node before breaking links

            if even_node == tail:
                break
            curr.next = next_odd        # 2. Skip the even node
            tail.next = even_node       # 3. Move even node to the tail
            tail = even_node            # 4. Update tail pointer
            tail.next = None            # 5. Safely isolate the new tail
            
            curr = next_odd             # 6. Move curr directly to the saved odd node
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd_nodes=[]
        even_nodes=[]
        i=1
        curr=head
        while curr is not None:
            if i%2!=0:
                odd_nodes.append(curr)
            else:
                even_nodes.append(curr)
            i+=1
            curr = curr.next
        for j in range(len(odd_nodes)-1):
            odd_nodes[j].next=odd_nodes[j+1]
        for j in range(len(even_nodes)-1):
            even_nodes[j].next=even_nodes[j+1]
        if odd_nodes and even_nodes:
            odd_nodes[-1].next=even_nodes[0]
        if even_nodes:
            even_nodes[-1].next=None
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_dummy = ListNode(0)
        even_dummy = ListNode(0)
        odd_curr = odd_dummy
        even_curr = even_dummy
        curr = head
        i = 1
        while curr is not None:
            if i % 2 != 0:
                odd_curr.next = curr
                odd_curr = odd_curr.next
            else:
                even_curr.next = curr
                even_curr = even_curr.next
            curr = curr.next
            i += 1
        even_curr.next = None
        odd_curr.next = even_dummy.next
        return odd_dummy.next