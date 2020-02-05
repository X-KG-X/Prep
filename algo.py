# class Solution:
#     def twoSum(self, nums, target):
#         hashMap={}
#         for i, n in enumerate(nums):
#             if target-n in hashMap:
#                 return [i, hashMap[target-n]]
#             else:
#                 hashMap[n]=i
#         return []

# x=Solution().twoSum([2,7,11,15],9)
# print(x)

# def rreverse(s):
#     if s == "":
#         return s
#     else:
#         return rreverse(s[1:]) + s[0]

# print(rreverse("Hello"))

# def selectionSort(listGiven):
#     holder=0
#     for i in range(0,len(listGiven)-1):
#         for j in range(i+1,len(listGiven)):
#             if listGiven[i]>listGiven[j] and listGiven[holder]>listGiven[j]:
#                 holder=j
#         listGiven[i], listGiven[holder]=listGiven[holder],listGiven[i]
#     return listGiven
    
# x=[5,3,2,6,0,7,2]

# print(selectionSort(x))
#O(n^2)


    
# x=[5,3,2,6,0,7,2]
# def insertionSort(x):
#     for i in range(1,len(x)):
#         k=i
#         for j in range(i-1,-1,-1):
#             if x[k]<x[j]:
#                 print(k,j)
#                 x[k],x[j]=x[j],x[k]
#                 k=j
#                 print(x)

# print(insertionSort(x))


#OOP-------------------------------

# class User:
#     def __init__(self, usernname, email):
#         self.name= usernname
#         self.email=email
#         self.account_bal=0

#     def make_deposit(self, amount):
#         self.account_bal+=amount
#         return self

#     def make_withdrawal(self, amount):
#         if self.account_bal>amount:
#             self.account_bal-=amount
#         else:
#             print(f"Not enough money to withdraw {amount}")
#         return self

#     def display_balance(self):
#         print(f"{self.name}'s account balance is {self.account_bal}'" )

#     def transfer_money(self, toUser, amount):
#         self.account_bal-=amount
#         toUser.account_bal+=amount
#         return self


# GG=User("Georgina Lalnunfeli Thiak", "gg@gmail.com")
# KG=User("King Wolf", "wolf@gmail.com")
# XX=User("Owl", "xx@gmail.com")


# GG.transfer_money(KG,100).display_balance()
# KG.display_balance()


#Circular Q

# class MyCircularQueue:

#     def __init__(self, k: int):
#         """
#         Initialize your data structure here. Set the size of the queue to be k.
#         """
#         self.myQ=[None]*k
#         self.head=-1
#         self.tail=-1
#         self.size=k

#     def enQueue(self, value: int) -> bool:
#         """
#         Insert an element into the circular queue. Return true if the operation is successful.
#         """
#         if self.isFull():
#             return False
#         if self.isEmpty():
#             self.head=0
#         self.tail=(self.tail+1)%self.size
#         self.myQ[self.tail]=value
#         return True

            
#     def deQueue(self) -> bool:
#         """
#         Delete an element from the circular queue. Return true if the operation is successful.
#         """
#         if self.isEmpty():
#             return False
#         if self.head==self.tail:
#             self.head=-1
#             self.tail=-1
#             return True
#         self.head=(self.head+1)%self.size
#         return True

#     def Front(self) -> int:
#         """
#         Get the front item from the queue.
#         """
#         if self.isEmpty():
#             return self.head
#         return self.myQ[self.head]

#     def Rear(self) -> int:
#         """
#         Get the last item from the queue.
#         """
#         if self.isEmpty():
#             return self.tail
#         return self.myQ[self.tail]

#     def isEmpty(self) -> bool:
#         """
#         Checks whether the circular queue is empty or not.
#         """
#         if self.head==-1:
#             return True
#         else:
#             return False

#     def isFull(self) -> bool:
#         """
#         Checks whether the circular queue is full or not.
#         """
#         if ((self.tail+1)%self.size)==self.head:
#             return True
#         else:
#             return False
        


# # Your MyCircularQueue object will be instantiated and called as such:

# obj = MyCircularQueue(6)
# # print(len(obj))
# print(obj.enQueue(6))
# print(obj.Rear())
# print(obj.Rear())
# print(obj.deQueue())
# # print(len(obj.myQ))
# print(obj.enQueue(5))
# print(obj.Rear())
# print(obj.deQueue())
# print(obj.Front())
# print(obj.deQueue())
# print(obj.deQueue())
# print(obj.deQueue())


# from queue import *

# class MovingAverage:

#     def __init__(self, size: int):
#         """
#         Initialize your data structure here.
#         """
#         self.myQ=Queue(maxsize=size)
#         self.sum=0
#         self.maxSize=size
#         self.curSize=0

#     def next(self, val: int) -> float:
#         if self.myQ.full():
#             self.sum-=self.myQ.get()
#             self.sum+=val
#             self.curSize=self.maxSize
#             self.myQ.put(val)
#             return self.sum/self.curSize
#         self.sum+=val
#         self.curSize+=1
#         self.myQ.put(val)
#         return self.sum/self.curSize
# x= MovingAverage(3)
# z=Queue(maxsize=2)
# print(x.next(1))
# print(x.next(10))
# print(x.next(3))
# print(x.next(5))

# ************* Data Structure *******


# Singly Linked list

# class Node:
#     def __init__(self, value):
#         self.value= value
#         self.next= None

# class SLL:
#     def __init__(self):
#         self.head=None

#     def printValues(self):
#         runner=self.head
#         while (runner !=None):
#             print(runner.value)
#             runner=runner.next
#         return self

#     def addBack(self, value):
#         newNode=Node(value)
#         if self.head == None:
#             self.head=newNode
#             return self
#         runner= self.head
#         while (runner.next != None):
#             runner=runner.next
#         runner.next=newNode
#         return self
    
#     def addFront(self, value):
#         newNode=Node(value)
#         curHead=self.head
#         newNode.next=curHead
#         self.head=newNode
#         return self
    
#     def removeBack(self):
#         if self.head==None:
#             return self
#         runner=self.head
#         while (runner.next.next != None):
#             runner=runner.next
#         runner.next=None
#         return self
    
#     def removeFront(self):
#         if self.head == None:
#             return self
#         self.head=self.head.next
#         return self

#     def removeVal(self, val):
#         if self.head==None:
#             return self
#         if self.head.value==val:
#             self.head=self.head.next
#             return self
#         runner=self.head
#         while (runner.next !=None):
#             if runner.next.value==val:
#                 runner.next=runner.next.next
#                 return self
#             runner=runner.next
#         return self

#     def insertVal(self, val, n):
#         if self.head ==None:
#             return self
#         newNode= Node(val)
#         runner=self.head
#         counter=0
#         if n==0:
#             newNode.next=runner
#             self.head=newNode
#             return self
#         while (runner.next!=None):
#             counter+=1
#             if counter==n:
#                 newNode.next=runner.next
#                 runner.next=newNode
#                 return self
#             elif counter+1==n:
#                 self.addBack(val)
#                 return self
#             runner=runner.next
#         return self

        

# my_list = SLL()	# create a new instance of a list
# # my_list.printValues().removeBack().printValues()
# my_list.addBack(0).addBack(1).addBack(2).addBack(3).printValues().insertVal(100,4).printValues()
# # chaining, yeah!
# # output should be:
# # Linked lists
# # are
# # fun!

#----------------------Leet
class Node:
    def __init__(self, val):
        self.value=val
        self.next=None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.head==None:
            return
        if index==0:
            return self.head.value
        if index<0:
            return -1
        counter=0
        runner=self.head
        while (runner!=None):
            if counter==index:
                return runner.value
            if counter> index:
                return -1
            counter+=1
            runner=runner.next
        return -1
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode=Node(val)
        curHead=self.head
        newNode.next=curHead
        self.head=newNode
        return self

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode=Node(val)
        if self.head == None:
            self.head=newNode
            return self
        runner= self.head
        while (runner.next != None):
            runner=runner.next
        runner.next=newNode
        return self
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # if self.head ==None:
        #     return self
        newNode= Node(val)
        runner=self.head
        counter=0
        if index==0:
            newNode.next=runner
            self.head=newNode
            return self
        while (runner.next!=None):
            counter+=1
            if counter==index:
                newNode.next=runner.next
                runner.next=newNode
                return self
            # elif counter+1==index:
            #     self.addAtTail(val)
            #     return self
            # elif index>counter+1:
            #     return self
            runner=runner.next
        counter+=1
        if counter==index:
            runner.next=newNode
        return self

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head==None:
            return self
        if index==0:
            self.head=self.head.next
            return self
        if index<0:
            return -1
        counter=0
        runner= self.head
        while (runner.next!=None):
            counter+=1
            if counter==index:
                runner.next=runner.next.next
                return self
            runner=runner.next
        if index>counter:
            return -1
        
    def printValues(self):
        runner=self.head
        while (runner !=None):
            print(runner.value)
            runner=runner.next
        return self



# Your MyLinkedList object will be instantiated and called as such:
# ["MyLinkedList","addAtHead","get","addAtHead","addAtHead","deleteAtIndex","addAtHead","get","get","get","addAtHead","deleteAtIndex"]
# [[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]


x=MyLinkedList()
x.addAtHead(4).printValues()
print("--------")
print(x.get(1))
print("--------")
x.addAtHead(1).printValues()
print("--------")
x.addAtHead(5).printValues()
print("--------")
x.deleteAtIndex(3)
print("--------")
x.addAtHead(7).printValues()
print("--------")
print(x.get(3))
print("--------")
print(x.get(3))
print("--------")
print(x.get(3))
print("--------")
x.addAtHead(1).printValues()
print("--------")
x.deleteAtIndex(4)
print("--------")



