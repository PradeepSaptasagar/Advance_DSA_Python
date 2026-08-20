def delete_at_position(head,position):
    if head is None or position<=0:
        return head

    if position==1:
        return delete_head(head)  # use delete_head.py here

    curr=head
    count=1
    while curr is not None and count<position:
        curr=curr.next
        count+=1

    if curr is None:
        return head

    if curr.next is None:
        return delete_last(head)   # use delete_last.py here

    return delete_node(head,curr)

# Time complexity=O(N), Space complexity=O(1)
