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

exampleTree=Node(1)
exampleTree.left=Node(2)
exampleTree.right=Node(3)
exampleTree.left.left=Node(4)
exampleTree.right.right=Node(5)
print(Solution().isSymmetric(exampleTree))