class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange=997
        self.bucketArray=[Bucket() for i in range(self.keyRange)]
        
    def _hash(self, key):
        return key% self.keyRange

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucketIndex=self._hash(key)
        self.bucketArray[bucketIndex].put(key,value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucketIndex=self._hash(key)
        self.bucketArray[bucketIndex].delete(key)
        
class Node:
    def __init__(self,key,val,next=None):
        self.key=key
        self.val=val
        self.next=next

class Bucket:
    def __init__(self):
        self.head=Node(0,0)
        
    def put(self, key, val):
        if not self.isPresent(key):
            newNode=Node(key,val, self.head.next)
            self.head.next=newNode
        else:
            cur=self.head
            while cur is not None:
                if cur.key==key:
                    cur.val=val
                    return
                cur=cur.next
        
    def get(self, key):
        if not self.isPresent(key):
            return -1
        else:
            cur=self.head
            while cur is not None:
                if cur.key==key:
                    return cur.val
                cur=cur.next
        
    def delete(self, key):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        
    def isPresent(self,key):
        cur=self.head
        while cur is not None:
            if cur.key==key:
                return True
            cur=cur.next
        return False

hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print(hashMap.get(1))
print(hashMap.get(3))
hashMap.put(2, 1)
print(hashMap.get(2))
hashMap.remove(2)
print(hashMap.get(2))