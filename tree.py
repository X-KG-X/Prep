import collections
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: Node):
        result=[]
        if root:
            result+=[root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
        return result
    
    def preorderTraversalIterative(self, root: Node):
        result=[]
        stack=[root]
        while stack:
            cur=stack.pop()
            if cur:
                result.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return result

    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     result=[]
    #     if root:
    #         result+=self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
    #     return result
    def inorderTraversal(self, root):
        result,stack=[],[[root,False]]
        while stack:
            cur,visited=stack.pop()
            if cur:
                if visited:
                    result.append(cur)
                else:
                    stack.append([cur.right, False])
                    stack.append([cur.val, True])
                    stack.append([cur.left, False])
        return result

    def postorderTraversal(self, root):
        # result=[]
        # if root:
        #     result+=self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
        # return result
        result,stack=[],[[root,False]]
        while stack:
            cur,visited=stack.pop()
            if cur:
                if visited:
                    result.append(cur)
                else:
                    stack.append([cur.val, True])
                    stack.append([cur.right, False])
                    stack.append([cur.left, False])
        return result

    def levelOrder(self, root):
        if not root:
            return
        result =[[]]
        Q=[[root,0]]
        while Q:
            cur, level=Q.pop(0)
            if cur:
                Q.append([cur.left, level+1])
                Q.append([cur.right, level+1])
                if level>=len(result):
                    result.append([])
                result[level].append(cur.val)
        return result
    
    def maxDepth(self, root):
        if root==None:
            return 0
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)
        max_d= max(left_depth,right_depth)+1
        return max_d
    
    def maxDepthIterative(self, root):
        if root==None:
            return 0
        stack=[[root, 1]]
        ans=0
        while stack:
            cur, depth=stack.pop()
            if cur:
                ans=max(ans,depth)
                stack.append([cur.left,depth+1])
                stack.append([cur.right,depth+1])
        return ans
    
    def isSymmetric(self, root):
        if root==None or (root.left==None and root.right==None):
            return True
        lQ=[root.left]
        rQ=[root.right]
        while lQ and rQ:
            l=lQ.pop(0)
            r=rQ.pop(0)
            if bool(l) != bool(r):
                return False
            if l and r:
                if l.val !=r.val:
                    return False
                lQ.append(l.left)
                lQ.append(l.right)
                rQ.append(r.right)
                rQ.append(r.left)
        return True

    def hasPathSumItretive(self, root, sum):
        # total=0
        if root==None:
            return False
        stack=[[root, root.val]]
        while stack:
            cur, total=stack.pop()
            if not cur.left and not cur.right and total==sum:
                return True
            if cur.right:
                stack.append([cur.right, total+cur.right.val])
            if cur.left:
                stack.append([cur.left, total+cur.left.val]) 
        return False

    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum-=root.val
        if not root.left and not root.right:
            return sum==0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


    def countUnivalSubtrees(self, root):
        self.count=0
        self.isUniv(root,0)
        return self.count
    
    def isUniv(self, cur, val):
        if not cur:
            return True
        
        if not all([self.isUniv(cur.left, cur.val),self.isUniv(cur.right, cur.val)]):
            return False
        
        self.count+=1
        
        return cur.val==val

    def countUnivalSubtreesIterative(self, root):
        if not root:
            return 0
        count=0
        stack=[[root, False]]
        while stack:
            cur, visited=stack.pop()
            if cur:
                if visited:
                    if not cur.left and not cur.right:
                        count+=1
                    else:
                        count+=self.univHelper(cur)

                else:
                    stack.append([cur, True])
                    stack.append([cur.right, False])
                    stack.append([cur.left, False])
        return count
    
    def univHelper(self, root):
        isUni=True
        stack=[root]
        while stack and isUni:
            cur=stack.pop()
            if cur:
                stack.append(cur.right)
                stack.append(cur.left)
                if not cur.left and not cur.right:
                    pass
                elif not cur.left:
                    isUni=(cur.val==cur.right.val)
                elif not cur.right:
                    isUni=(cur.val==cur.left.val)
                else:
                    isUni=(cur.val==cur.left.val) and (cur.val==cur.right.val)
        return isUni

    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        cur=postorder.pop()
        root=Node(cur)
        mid=inorder.index(cur)
        root.right=self.buildTree(inorder[mid+1:], postorder)
        root.left=self.buildTree(inorder[:mid], postorder)
        return root

# Populating Next Right Pointers in Each Node
    def connect(self, root):
        if not root:
            return root
        
        leftiest=root
        while leftiest.left:
            head=leftiest
            while head:
                head.left.next=head.right
                
                if head.next:
                    head.right.next=head.next.left
                head=head.next
            leftiest=leftiest.left
        return root

    
# Populating Next Right Pointers in Each Node II
    def connect2(self, root):
        if not root:
            return root
        # Q=[]
        # Q.append(root)
        Q=collections.deque([root])
        while Q:
            size=len(Q)
            for i in range(size):
                node =Q.popleft()
                if i<size-1:
                    node.next=Q[0]
                
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root

#   Lowest Common Ancestor of a Binary Tree
    def lowestCommonAncestor(self, root, p, q):
        if not root or root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left or right

# Serialize and Deserialize Binary Tree
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result=[]
        if not root:
            return ''
        Q=collections.deque([root])
        while Q:
            cur=Q.popleft()
            if cur:
                result.append(str(cur.val))
                Q.append(cur.left)
                Q.append(cur.right)
            else:
                result.append("#")
            
        print(','.join(result))
        return ','.join(result)
                
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=='':
            return None
        decoded=data.split(',')
        root=Node(int(decoded[0]))
        Q=collections.deque([root])
        index=1
        while Q:
            cur=Q.popleft()
            if decoded[index] !="#":
                cur.left=Node(int(decoded[index]))
                Q.append(cur.left)
            index+=1
            if decoded[index]!='#':
                cur.right=Node(int(decoded[index]))
                Q.append(cur.right)
            index+=1
        return root
  
#   Validate Binary Search Tree
    def isValidBST(self, root):
        return self.isValid(root,float('-inf'), float('inf'))
    def isValid(self, node, minVal, maxVal):
        if not node:
            return True
        if node.val<=minVal or node.val>=maxVal:
            return False
        
        left=self.isValid(node.left, minVal, node.val)
        right=self.isValid(node.right, node.val, maxVal)
        
        return left and right



#   Inorder Successor in BST
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        result=[]
        stack=[[root,False]]
        while stack:
            cur, visited=stack.pop()
            if cur:
                if visited:
                    result.append(cur.val)
                    if len(result)>1 and result[-2]==p.val:
                        return cur
                else:
                    stack.append([cur.right,False])
                    stack.append([cur,True])
                    stack.append([cur.left,False])
        return None


    def insertIntoBST(self, root, val):
        if not root:
            return Node(val)
        stack=[[root,0]]
        while stack:
            cur, d=stack.pop()
            if cur:
                if val<cur.val:
                    stack.append([cur.left,1])
                else:
                    stack.append([cur.right,2])
                prev=cur
            else:
                if d==1:
                    prev.left=Node(val)
                    return root
                elif d==2:
                    prev.right=Node(val)
                    return root     
        return
        
#         def inorder( node):
#             result=[]
#             if node:
#                 result+=inorder(node.left)+[node.val]+inorder(node.right)
#             return result

#         a=inorder(root)
#         for i in range(1,len(a)):
#             if a[i-1]>=a[i]:
#                 return False
#         return True

# Delete Node in a BST
    def deleteNode(self, root, key):
        if not root:
            return
        if root.val==key and not root.left and not root.right:
            return 
        stack=[[root,0]]
        holder=Node(None)
        while stack:
            cur,d=stack.pop()
            if cur:    
                if key==cur.val:
                    holder=cur
                    if cur.right:
                        stack.append([cur.right,1])
                    elif cur.left:
                        stack.append([cur.left,2])
                elif key>cur.val:
                    if cur.right:
                        stack.append([cur.right,1])   
                    elif cur.left:
                        stack.append([cur.left,2])
                        holder.val=cur.val
                        holder=cur
                elif key<cur.val:
                    if cur.left:
                        stack.append([cur.left,2])
                    elif cur.right:
                        stack.append([cur.right,1])
                        holder.val=cur.val
                        holder=cur
                
                if not cur.left and not cur.right:
                    if holder.val == False or holder.val:
                        holder.val=cur.val
                        if d==1:
                            prev.right=None
                        elif d==2:
                            prev.left=None
                        return root

                prev=cur
        return root
                    
# Balanced Binary Tree
    def isBalanced(self, root, h=1):
        if not root:
            return h
        l=self.isBalanced(root.left,h+1)
        if not l:
            return 
        r=self.isBalanced(root.right,h+1)
        if not r:
            return 
        return abs(l-r)<2 and max(l,r)
#     def isBalanced(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         return abs(self.maxDepth(root.left)-self.maxDepth(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
#     def maxDepth(self,root: TreeNode)->int:
#         if not root:
#             return 0
#         stack=[[root, 0]]
#         ans=0
#         while stack:
#             cur, depth=stack.pop()
#             if cur:
#                 stack.append([cur.left,depth+1])
#                 stack.append([cur.right,depth+1])
#             else:
#                 ans=max(depth,ans) 
#         return ans
                
exampleTree=Node(1)
exampleTree.left=Node(2)
exampleTree.left.left=Node(3)
exampleTree.left.left.left=Node(4)
exampleTree.right=Node(2)
exampleTree.right.right=Node(3)
exampleTree.right.right.right=Node(4)       
print(Solution().isBalanced(exampleTree))
        


# Binary Search Tree Iterator
                   
class BSTIterator:

    def __init__(self, root):
        self.stack=[[root,False]]
        self.root=root

    def next(self):
        """
        @return the next smallest number
        """
        if not self.root:
            return 
        while self.stack:
            # print(self.stack)
            # print("------------------------------")
            cur, visited=self.stack.pop()
            if cur:
                if visited:
                    return cur.val
                else:
                    if cur.right:
                        self.stack.append([cur.right,False])
                    self.stack.append([cur,True])
                    if cur.left:
                        self.stack.append([cur.left,False])
        return
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        if not self.root:
            return False
        if len(self.stack)==0:
            return False
        else:
            return True
    


