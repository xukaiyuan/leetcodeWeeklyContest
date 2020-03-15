class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        tmp = set()
        res = []
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            minimum = matrix[i][0]
            col = 0
            for j in range(n):
                if (matrix[i][j] < minimum):
                    minimum = matrix[i][j]
                    col = j
            flag = True
            for k in range(m):
                if (matrix[k][col] > minimum):
                    flag = False
            
            if (flag):
                res.append(minimum)
            
        
        return res
                
class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.size = maxSize
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if (len(self.stack) != self.size):
            self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if (len(self.stack) == 0):
            return -1
        else:
            return self.stack.pop()

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

import math
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrder(self, root):
        if (root.left):
            self.inOrder(root.left)
            
        self.increment.append(root.val)
        
        if(root.right):
            self.inOrder(root.right)
    
    def construct(self, root, start, end, left):
        if (start <= end):
            mid = (end - start) / 2 + start
            #print((start, end))
            newNode = TreeNode(self.increment[mid])

            if (left):
                root.left = newNode
            else:
                root.right = newNode

            self.construct(newNode, start, mid - 1, True)
            self.construct(newNode, mid + 1, end, False)
        
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.increment = []
        
        self.inOrder(root)
        
        #level = int(math.log(len(self.increment), 2))
        rootIndex = len(self.increment) / 2
        res = TreeNode(self.increment[rootIndex])
        
        self.construct(res, 0, rootIndex - 1, True)
        self.construct(res, rootIndex + 1, len(self.increment) - 1, False)
        
        return res    