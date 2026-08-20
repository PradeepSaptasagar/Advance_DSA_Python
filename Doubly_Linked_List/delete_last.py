def delete_last(head):
    if head is None:
        return None

    if head.next is None:
        return None

    curr=head
    while curr.next is not None:
        curr=curr.next
    curr.prev.next=None
    del curr
    return head

# Time complexity=O(N), Space complexity=O(1)