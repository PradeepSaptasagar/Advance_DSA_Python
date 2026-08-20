class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=head

    def insert_at_head(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

# Time complexity=O(1), Space complexity=O(1)