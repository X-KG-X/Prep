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

class User:
    def __init__(self, usernname, email):
        self.name= usernname
        self.email=email
        self.account_bal=0

    def make_deposit(self, amount):
        self.account_bal+=amount
        return self

    def make_withdrawal(self, amount):
        if self.account_bal>amount:
            self.account_bal-=amount
        else:
            print(f"Not enough money to withdraw {amount}")
        return self

    def display_balance(self):
        print(f"{self.name}'s account balance is {self.account_bal}'" )

    def transfer_money(self, toUser, amount):
        self.account_bal-=amount
        toUser.account_bal+=amount
        return self


GG=User("Georgina Lalnunfeli Thiak", "gg@gmail.com")
KG=User("King Wolf", "wolf@gmail.com")
XX=User("Owl", "xx@gmail.com")


GG.transfer_money(KG,100).display_balance()
KG.display_balance()