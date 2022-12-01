class node:
    def __init__(self,data):
        self.data = data
        self.prev=None
        self.next = None
def printd11(head):
    cur = head
    while cur!=None:
        print(cur.data)
        cur = cur.next
    print()
head = node(10)
temp1 = node(20)
temp2= node(30)
temp3= node(40)
head.next=temp1
temp1.prev=head

temp1.next=temp3
temp3.next=temp2
printd11(head)

import time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)