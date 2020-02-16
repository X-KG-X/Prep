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
#     if len(s) == "":
#         return s
#     else:
#         return rreverse(s[1:])+(s[0])

# s=["H","e","l","l","o"]
# print(rreverse(s))

#   def reverse(self, string):
#     if len(string) == 0:
#       return string
#     else:
#       return self.reverse(string[1:]) + string[0]

#   def reverseIterative(self, string):
#     answer = ''
#     stack = [string]
#     while len(stack):
#       item = stack.pop()
#       answer += item[-1]

#       nextItem = item[:-1]
#       if len(nextItem):
#         stack.append(nextItem)
#     return answer

# a = 'hello'
# print(Solution().reverse(a))

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
# class Node:
#     def __init__(self, val):
#         self.value=val
#         self.next=None
        
# class MyLinkedList:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.head=None

#     def get(self, index: int) -> int:
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         if self.head==None:
#             return
#         if index==0:
#             return self.head.value
#         if index<0:
#             return -1
#         counter=0
#         runner=self.head
#         while (runner!=None):
#             if counter==index:
#                 return runner.value
#             if counter> index:
#                 return -1
#             counter+=1
#             runner=runner.next
#         return -1
            

#     def addAtHead(self, val: int) -> None:
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         """
#         newNode=Node(val)
#         curHead=self.head
#         newNode.next=curHead
#         self.head=newNode
#         return self

#     def addAtTail(self, val: int) -> None:
#         """
#         Append a node of value val to the last element of the linked list.
#         """
#         newNode=Node(val)
#         if self.head == None:
#             self.head=newNode
#             return self
#         runner= self.head
#         while (runner.next != None):
#             runner=runner.next
#         runner.next=newNode
#         return self
        

#     def addAtIndex(self, index: int, val: int) -> None:
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         """
#         # if self.head ==None:
#         #     return self
#         newNode= Node(val)
#         runner=self.head
#         counter=0
#         if index==0:
#             newNode.next=runner
#             self.head=newNode
#             return self
#         while (runner.next!=None):
#             counter+=1
#             if counter==index:
#                 newNode.next=runner.next
#                 runner.next=newNode
#                 return self
#             # elif counter+1==index:
#             #     self.addAtTail(val)
#             #     return self
#             # elif index>counter+1:
#             #     return self
#             runner=runner.next
#         counter+=1
#         if counter==index:
#             runner.next=newNode
#         return self

#     def deleteAtIndex(self, index: int) -> None:
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         if self.head==None:
#             return self
#         if index==0:
#             self.head=self.head.next
#             return self
#         if index<0:
#             return -1
#         counter=0
#         runner= self.head
#         while (runner.next!=None):
#             counter+=1
#             if counter==index:
#                 runner.next=runner.next.next
#                 return self
#             runner=runner.next
#         if index>counter:
#             return -1
        
#     def printValues(self):
#         runner=self.head
#         while (runner !=None):
#             print(runner.value)
#             runner=runner.next
#         return self



# # Your MyLinkedList object will be instantiated and called as such:
# # ["MyLinkedList","addAtHead","get","addAtHead","addAtHead","deleteAtIndex","addAtHead","get","get","get","addAtHead","deleteAtIndex"]
# # [[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]


# x=MyLinkedList()
# x.addAtHead(4).printValues()
# print("--------")
# print(x.get(1))
# print("--------")
# x.addAtHead(1).printValues()
# print("--------")
# x.addAtHead(5).printValues()
# print("--------")
# x.deleteAtIndex(3)
# print("--------")
# x.addAtHead(7).printValues()
# print("--------")
# print(x.get(3))
# print("--------")
# print(x.get(3))
# print("--------")
# print(x.get(3))
# print("--------")
# x.addAtHead(1).printValues()
# print("--------")
# x.deleteAtIndex(4)
# print("--------")
#====================REFACTOR ABOVE WITH SIZE ATTRIBUTE AND ALSO WITH DOUBELY LINKED LIST


class Solution:
#     def decompressRLElist(self, nums):
#         ans=[]
#         for i in range(0,len(nums),2):
#             temp=[nums[i+1]]*nums[i]
#             ans=ans+temp
#             temp=[]
#         return ans
            
# print(Solution().decompressRLElist([1,2,3,4]))


#
#     # def pivotIndex(self, nums: List[int]) -> int:
#     #     for i in range(0,len(nums)):
#     #         if sum(nums[:i])==sum(nums[i+1:]):
#     #             return i
#     #     return -1
    
#     def pivotIndexAlt(self, nums: List[int]) -> int:
#         total=sum(nums)
#         curSum=0
#         for i in range(0,len(nums)):
#             if total-curSum-nums[i]==curSum:
#                 return i
#             curSum+=nums[i]
#         return -1
            

#
#     def dominantIndex(self, nums):
#         max=nums[0]
#         if len(nums)==1:
#             return 0
#         if len(nums)==0:
#             return -1
#         for i in range(1, len(nums)):
#             if nums[i]>=nums[i-1]:
#                 max=nums[i]
#                 index=i
#         for j in range(0,len(nums)):
#             if nums[j]*2<max:
#                 return index
#             return -1

#
#     def plusOne(self, digits):
#         for i in range(len(digits)-1,-1,-1):
#             if digits[i]!=9:
#                 digits[i]+=1
#                 return digits
#             else:
#                 digits[i]=0
#         digits.insert(0,1)
#         return digits
            
#
#     def findDiagonalOrder(self, matrix):
#         if len(matrix)==0:
#             return matrix
#         m=len(matrix)
#         n=len(matrix[0])
#         i=0
#         j=0
#         result=[]
#         for k in range(0, m*n):
#             result.append(matrix[i][j])
#             if (i+j) %2==0:
#                 if j==n-1:
#                     i+=1
#                 elif i==0:
#                     j+=1
#                 else:
#                     i-=1
#                     j+=1
#             else:
#                 if i==m-1:
#                     j+=1
#                 elif j==0:
#                     i+=1
#                 else:
#                     i+=1
#                     j-=1
#         return result

# x=[[1,2,3],[4,5,6],[7,8,9]]
# print(Solution().findDiagonalOrder(x))

#
#     def spiralOrder(self, matrix):
#         if len(matrix)==0:
#             return matrix
#         #dir 0:left, 1:down, 2:right, 3:up
#         dir=0
#         m=len(matrix)
#         n=len(matrix[0])
        
#         # 4 pointers top, down, left, right
#         top=0
#         bottom=m-1
#         left=0
#         right=n-1
#         result=[]
#         while(top<=bottom and left<=right):
#             if dir==0:
#                 for i in range(left,right+1):
#                     result.append(matrix[top][i])
#                 top+=1
#             elif dir==1:
#                 for i in range(top,bottom+1):
#                     result.append(matrix[i][right])
#                 right-=1
#             elif dir==2:
#                 for i in range(right,left-1,-1):
#                     result.append(matrix[bottom][i])
#                 bottom-=1
#             elif dir==3:
#                 for i in range(bottom, top-1, -1):
#                     result.append(matrix[i][left])
#                 left+=1
#             dir=(dir+1) %4
#         return result

# x=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# print(Solution().spiralOrder(x))
# from queue import *
#
#     def generate(self, numRows):
#         result=[[1],[1,1]]
#         # Q=Queue(maxsize=2)
#         if numRows==0:
#             return
#         if numRows==1:
#             return result[0]
#         if numRows==2:
#             return result
#         for i in range(2,numRows):
#             for j in range(0,len(result)+1):
#                 if j==0:
#                     result.append([1])
#                     print(len(result))
#                 elif j<len(result)-1:
#                     print(result[i-1][j-1])
#                     print(result[i-1][j])
#                     result[i].append(result[i-1][j-1]+result[i-1][j])
#                 else:
#                     result[i].append(1)
#                     # Q.get()
#                     # Q.get()
#         return result
# print(Solution().generate(5))

    def addBinary(self, a: str, b: str) -> str:
        carry=0
        result=""
        aList=list(a)
        bList=list(b)
        while aList or bList or carry==1:
            if aList:
                carry+=int(aList.pop())
            if bList:
                carry+=int(bList.pop())
            result=str(carry%2)+result

            carry //=2
        return result  
    def altAddBinary(self, a: str, b: str) -> str:         
        a = int(a, 2)
        b = int(b, 2)
        return ("" + bin(a+b))[2:]


    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return haystack.find(needle)

    def longestCommonPrefix(self, strs):
        if strs==[]:
            return ""
        elif len(strs)==1:
            return strs[0]
        common=""
        minLen=len(min(strs))
        for i in range(minLen):
            for j in range(len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    return common
            common+=strs[j][i]
        return common

    def reverseString2point(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        print(s)
        return
    
    def arrayPairSum(self, nums) -> int:
        nums.sort()
        # i=0
        # j=1
        ans=0
        # small=0
        # while j<len(nums):
        #     small=min(nums[i], nums[j])
        #     ans+=small
        #     i+=2

        #     j+=2
        # return ans
        for i in range(0, len(nums),2):
            ans+=nums[i]
        return ans
    
    # def twoSum(self, numbers, target):
    #     for i in range(len(numbers)):
    #         for j in range(i+1, len(numbers)):
    #             if numbers[j]>target:
    #                 break
    #             if numbers[i]+numbers[j]==target:
    #                 return [i+1,j+1]
    #     return
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a={}
        y=enumerate(numbers)
        for index,i in y:
            print(index, i)
            if target-i in a:
                return a[target-i]+1,index+1
            a[i]=index
        
    def removeElement(self, nums, val):
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
        x=len(nums)
        return x
    def findMaxConsecutiveOnes(self, nums):
        sum1=0
        sum2=0
        for i in range(len(nums)):
            if nums[i]==1:
                sum1+=1
            else:
                if sum1>=sum2:
                    sum2=sum1
                sum1=0
        return max(sum1,sum2)
        
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        count=float("inf")
        j=0
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]  
            while summ>=s:
                count=min(count,i-j+1)
                summ-=nums[j]
                j+=1
        if count==float("inf"):
            count=0
        return count



# print(Solution().altAddBinary("11","1"))
# print(Solution().strStr("book","k"))
# print(Solution().longestCommonPrefix(["flower","flow", "flight"]))
# print(Solution().reverseString2point(["h","e","l","l","o"]))
# print(Solution().arrayPairSum([4,2,3,1]))
# print(Solution().twoSum([-1,0],-1))
# print(Solution().removeElement([3,2,2,3],3))
print(Solution().findMaxConsecutiveOnes([0,1]))