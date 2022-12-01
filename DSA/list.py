# # # l = [2,4,6,5,9,4,8,7,1,55]
# # # print(*l)
# # # print(l)
# # # print(l[2])
# # # print(l[-3])
# # # c= len(l)
# # # print(c)
# # # l.insert(10,10)
# # # print(l)
# # # print(l.count(1))
# # # print(l.index(55))
# # # print(l.index(4,2,8))
# # # # sum and average the list
# # # def average(l):
# # #     sum=0
# # #     for i in l:
# # #         sum = sum+i
# # #         n= len(l)
# # #     return sum/n
# # # print(average(l))
# # # def sort,average(l):
# # #     return sum(l)/len(l)
# # # print(sortaverage(l))
# # #
# # # # even and old
# # # def evenodd(sl):
# # #     even = []
# # #     odd = []
# # #     for i in l:
# # #         if i%2==0:
# # #             even.append(i)
# # #         else:
# # #             odd.append(i)
# # #     return even, odd
# # # sl = [2,4,6,5,9,4,8,7,1,55]
# # # even,odd = evenodd(l)
# # # print("even number =",even)
# # # print("odd niumber =",odd)
# # #
# #
# # #FIND THE SMALL VALUES
# # def smals(l,x):
# #     res = [ ]
# #     for i in l:
# #         if i<x:
# #             res.append(i)
# #     return res
# #
# # l = [5,3,2,4,7,8,9,6,17]
# # x=5
# # print(smals(l,x))
# #
# # #TO FIND THE LARGEST ELEMENT
# # def getmax(l):
# #     for i in l:
# #         for j in l:
# #             if j>i:
# #                 break
# #         else:
# #             return j
# #     return None
# # print(getmax(l))
# #
# # def seclar(l):
# #     if len(l)<=1:
# #         return None
# #     lar= getmax(l)
# #     sec = None
# #     for x in l:
# #         if x!=lar:
# #             if sec == None:
# #                 sec =x
# #             else:
# #                 sec = max(sec,x)
# #                 print(sec)
# #     return sec
# # print(seclar(l))
# #
# #
# #
#


# # to find the reverse
# def re(l):
#     print(*l)
# def reve(l):
#     re(l)
#     s=0
#     n = len(l)-1
#     while s<n:
#         l[s],l[n]=l[n],l[s]
#         s = s+1
#         n =n-1
#
# l=[20,30,40]
# reve(l)
# re(l)
# print(*l)


#self
# def arr(l):
#     n = len(l)
#     s= 2
#     for i in range(n-2):
#         l[i-2]=l[i]
#     l[]
#
#
# l = [1,2,3,4,5]
# arr(l)
# print(*l)
class node:
    def __init__(self,k):
        self.key=k
        self.next = None
def searches(head,x):
    pos =1
    cur =head
    while cur!=None:
        if cur.key==x:
            return pos
        pos=pos+1
        cur=cur.next
head = node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(50)
x=30
print(searches(head,x))

class node:
    def __init__(self,k):
        self.key=k
        self.next =None
def inserctbegin(head,key):
    temp=node(key)
    temp.next=head
    return temp
def prints(head):

    cur=head
    while cur!=None:
        print(cur.key)
        cur=cur.next

head =None
head =inserctbegin(head,10)
head =inserctbegin(head,20)
head =inserctbegin(head,30)
prints(head)