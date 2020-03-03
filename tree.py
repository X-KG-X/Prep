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
                    


exampleTree=Node(1)
exampleTree.left=Node(2)
exampleTree.right=Node(3)
exampleTree.left.left=Node(4)
exampleTree.right.right=Node(5)
print(Solution().buildTree([9,3,15,20,7],[9,15,7,20,3]))