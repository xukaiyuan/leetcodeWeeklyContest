class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        res = -1
        
        words = sentence.split(" ")
        
        for i in range(len(words)):
            if (words[i].startswith(searchWord)):
                res = i + 1
                break
        
        return res

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ["a", "e", "i", "o", "u"]
        res = 0
        start = 0
        
        for i in range(k):
            if (s[i] in vowels):
                res += 1
        
        tmp = res
        
        for i in range(k, len(s)):
            if (s[start] in vowels):
                tmp -= 1
            start += 1
            if (s[i] in vowels):
                #print(s[i])
                tmp += 1
            #print(tmp)
            res = max(res, tmp)
        #print(start)
        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        record = [0] * 10
        #record[root.val] = 1
        self.res = 0
        
        self.recursion(root, record)
        
        return self.res
        
    def recursion(self, root, curRecord):
        curRecord[root.val] ^= 1
        if (root.left == None and root.right == None):
            if (sum(curRecord) == 1 or sum(curRecord) == 0):
                self.res += 1
        else:
            newRecord = curRecord[:]
            if (root.left != None):
                self.recursion(root.left, newRecord)
            if (root.right != None):
                self.recursion(root.right, curRecord)

class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        rows = len(nums1)
        cols = len(nums2)
        
        oneD = [[0] * cols for _ in range(rows)]
        dp = [[0] * cols for _ in range(rows)]
        res = -float("inf")
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                oneD[i][j] = nums1[i] * nums2[j]
                res = max(res, oneD[i][j])
        
        #print(res)
        
        for i in range(1, rows):
            #curSum = sum(oneD[i])
            for j in range(1, cols):
                preLine = max(oneD[i - 1][0: j])
                oneD[i][j] = max(oneD[i][j], oneD[i][j] + preLine, preLine)
                res = max(res, oneD[i][j])
        
        return res
            
'''            
wrong case:
[7,2,2,-1,-1,1,-4,7,6]
[-7,-9,-1,2,2,5,-7,2,-7,5]
'''