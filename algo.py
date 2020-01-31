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

def selectionSort(listGiven):
    holder=0
    for i in range(0,len(listGiven)-1):
        for j in range(i+1,len(listGiven)):
            if listGiven[i]>listGiven[j] and listGiven[holder]>listGiven[j]:
                holder=j
        listGiven[i], listGiven[holder]=listGiven[holder],listGiven[i]
    return listGiven
    
x=[5,3,2,6,0,7,2]

print(selectionSort(x))
        