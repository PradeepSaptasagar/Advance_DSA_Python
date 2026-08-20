# The code can be used for inserting at any position

class Node:
    def __int__(self,val):
        self.val=val
        self.next=next
        self.prev=prev

    def insert_at(self,val,position):
        new_node=Node(val)
        if position==0:
            self.insert_at_head(val)  # use insert_at_head.py file here  
            return

        current=self.head
        count=0
        while current and count<position-1:
            current=current.next
            count+=1

        if current is None:
            print("Position out of bounds")
            return

        new_node.next=current.next
        new_node.prev=current
        if current.next:
            current.next.prev=new_node
        current.next=new_node

# Time complexity=O(N), Space complexity=O(1)