class Node:
    def __init__(self,val):
        self.val=val
        self.next=next
        self.prev=prev

def append(self,val):
    new_node=Node(val)
    if not self.head:
        self.head=new_node
    else:
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
        new_node.prev=current

# Time complexity=O(N), Space complexity=O(1)

