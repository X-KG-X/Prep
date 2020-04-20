# Hashset implementation with Linkedlist for collision
class HashSet:
    def __init__(self):
        self.keyRange=997
        self.bucketArray=[Bucket() for i in range(self.keyRange)]
    
    def _hash(self,key):
        return key%self.keyRange

    def add(self,key):
        bucket=self._hash(key)
        self.bucketArray[bucket].add(key)

    def remove(self,key):
        bucket=self._hash(key)
        self.bucketArray[bucket].delete(key)

    def contains(self, key):
        bucket=self._hash(key)
        return self.bucketArray[bucket].isPresent(key)


class Node:
    def __init__(self, value, nextNode=None):
        self.value =value
        self.next=nextNode

class Bucket:
    def __init__(self):
        self.head= Node(0)

    def add(self, newValue):
        if  not self.isPresent(newValue):
            newNode=Node(newValue, self.head.next)
            self.head.next=newNode

    def delete(self, value):
        prev=self.head
        cur=self.head.next
        while cur is not None:
            if cur.value==value:
                prev.next=cur.next
                return
            prev=cur
            cur=cur.next

    def isPresent(self, value):
        cur =self.head.next
        while cur is not None:
            if cur.value ==value:
                return True
            cur=cur.next
        return False

myHashSet= HashSet()
print(myHashSet.add(10))
# print(myHashSet.add(10))
print(myHashSet.contains(10))
print(myHashSet.remove(10))
print(myHashSet.contains(10))