class node:
    def __init__(self,val):
        self.val=val
        self.next=next
        self.prev=prev

    def traverse_forward(self):
        current=self.head
        while current:
            print(current.val,end="")
            current=current.next
        print()

    def traverse_backward(self):
        current=self.head
        while current.next:
            current=current.next
        while current:
            print(current.val,end="")
            current=current.prev
        print()

    