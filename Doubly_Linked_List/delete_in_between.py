# Given the pointer reference to the target node

def delete_node(head,del_node):
    if head is None or del_node is None:
        return head

    if head==del_node:
        head=del_node.next

    if del_node.next is not None:
        del_node.next.prev=del_node.prev

    if del_node.prev is not None:
        del_node.prev.next=del_node.next

    del del_node
    return head

# Time complexity=O(1), Space complexity=O(1)