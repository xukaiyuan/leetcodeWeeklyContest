def maximum69Number (num):
    """
    :type num: int
    :rtype: int
    """
    res = ""
    flag = False
    
    for ch in str(num):
        if (ch == "9"):
            res += ch
        else:
            if (flag):
                res += ch
            else:
                res += "9"
                flag = True
    
    return int(res)


def printVertically(s):
    """
    :type s: str
    :rtype: List[str]
    """
    words = s.split(" ")
    length = -1
    
    for word in words:
        length = max(length, len(word))
    
    res = [[" " for col in range(len(words))] for row in range(length)]

    
    for i in range(len(words)):
        for j in range(min(len(words[i]), length)):
            res[j][i] = words[i][j]
    
    for i in range(len(res)):
        res[i] = ''.join(res[i])
        res[i] = res[i].rstrip()
        
    return res

#s = "HOW ARE YOU"
s = "TO BE OR NOT TO BE"
print(printVertically(s))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        def isLeaf(node):
            return (node.left == None and node.right == None)
        
        if (root == None):
            return root
        
        if (isLeaf(root) and root.val == target):
            return None
        
        queue = [root]
        stack = []
        relation = {}
        
        while (len(queue) != 0):
            cur = queue.pop(0)
            if (cur.left != None):
                queue.append(cur.left)
                relation[cur.left] = ("l", cur)
            if (cur.right != None):
                queue.append(cur.right)
                relation[cur.right] = ("r", cur)
            
            stack.append(cur)

        while (len(stack) != 0):
            if (isLeaf(stack[-1]) and stack[-1].val == target):
                delete = stack.pop()
                if (delete not in relation):
                    return None
                else:
                    parent = relation[delete][1]
                    if (relation[delete][0] == "l"):
                        parent.left = None
                    else:
                        parent.right = None
            else:
                stack.pop()
        
        return root

'''
class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        maxRangeRight = [-1] * (n + 1)
        maxRight = -1
        maxRangeLeft = [-1] * (n + 1)
        maxLeft = n + 2
        
        curLeft = n + 2
        curRight = -1
        
        for i in range(len(ranges)):
            maxRight = max(maxRight, ranges[i] + i)
            maxRangeRight[i] = maxRight
        
        for i in range(len(ranges) - 1, -1, -1):
            maxLeft = min(maxLeft, i - ranges[i])
            maxRangeLeft[i] = maxLeft
        
        print(maxRangeRight)
        print(maxRangeLeft)
'''
