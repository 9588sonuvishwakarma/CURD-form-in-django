print("main code of the link list")
class node:
    def __init__(self,k):
        self.key=k
        self.next=None
# tem1 = node(10)
# temp2=node(20)
# tem3=node(30)
# tem1.next=temp2
# temp2.next=tem3
# head=tem1

head= node(10)
head.next=node(20)
head.next.next=node(30)

print(head.key)
print(head.next.next.key)

# next step to search the  link list
print("\n this is search the link list")
class node:
    def __init__(self,k):
        self.key=k
        self.next=None
def search(head,x):
    pos = 1
    cur=head
    while cur!=None:
        if cur.key ==x:
            return pos
        pos = pos+1
        cur=cur.next
    return None

head= node(10)
head.next=node(20)
head.next.next=node(30)
print(search(head,20))



# traversing the linklist
print("\n this is the traversing the linklist")
class node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printlist(head):
    cur = head
    while cur!=None:
        print(cur.key,end=" ")
        cur = cur.next


head= node(10)
head.next=node(20)
head.next.next=node(30)
printlist(head)

# insert the in link list
print("\n  insert the in link list")
class node:
    def __init__(self,k):
        self.key=k
        self.next=None
def insertbegin(head,key):
    temp = node(key)
    temp.next=head
    return temp
def printlist(head):
    curr = head
    while curr!=None:
        print(curr.key)
        curr = curr.next
head= None
head = insertbegin(head,10)
head = insertbegin(head,20)
head = insertbegin(head,30)
head = insertbegin(head,40)
head = insertbegin(head,50)

printlist(head)

# insert at end
print("ensert at end")
class node:
    def __init__(self,k):
        self.key=k
        self.next=None

def insert(head, key):
    if head ==None:
        return node(key)
    curr = head
    while curr.next!=None:
        curr = curr.next
    curr.next = node(key)
    return head

def printlist(head):
    cur = head
    while cur!=None:
        print(cur.key,end=" ")
        cur = cur.next


head= node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)
printlist(head)

#insert at any position
print("insert at any position")
class node:
    def __init__(self ,k):
        self.key=k
        self.next = None
def inser(head, pos,x):
    temp = node(x)
    if pos==1:
        temp.next = head
        return temp
    cur=head
    for i in range(pos-2):
        cur = cur.next
        if cur==None:
            return head
    temp.next=cur.next
    cur.next=temp
    return head
print("dlel")
def delr(head):
    if head == None:
        return None
    if head.next == None:
        return None
    cur= head
    while cur.next.next!=None:
        cur = cur.next
    cur.next = None
    return head



def printlist(head):
    cur = head
    while cur!=None:
        print(cur.key)
        cur = cur.next
head = node(10)
head.next = node(20)
head.next.next = node(30)

head.next.next.next = node(40)
head = delr(head)
printlist(head)
head = inser(head,4,42)
print("\n")


printlist(head)



# circular linklist

#
# print("circular linklist")
# class node:
#     def __init__(self,k):
#         self.key=k
#         self.next=None
# def printcircular(head):
#     if head == None:
#         return
#     print(head.key)
#     curr = head.next
#     while curr!=head:
#         print(curr.key)
#         curr=curr.next
# def printlist(head):
#     cur = head
#     while cur!=None:
#         print(cur.key,end=" ")
#         cur = cur.next
# head= node(10)
# head.next=node(20)
# head.next.next=node(30)
# head.next.next.next=node(40)
# head.next.next.next.next=head
# printcircular(head)
# printlist(head)


