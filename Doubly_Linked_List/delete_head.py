def delete_head(head):
    if head is None:
        return None
    temp=head
    head=head.next
    if head is not None:
        head.prev=None
    del temp
    return temp

# Time complexity=O(1), Space complexity=O(1)