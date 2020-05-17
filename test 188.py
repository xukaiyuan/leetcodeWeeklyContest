class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        cur = 1
        index = 0
        res = []
        
        while (cur <= n and index < len(target)):
            res.append("Push")
            
            if (cur != target[index]):
                res.append("Pop")
            else:
                index += 1
            
            cur += 1
        
        return res


class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        relation = {}
        res = 0
        stack = [0]
        
        for edge in edges:
            if (edge[0] in relation):
                relation[edge[0]].add(edge[1])
            else:
                relation[edge[0]] = set([edge[1]])
        
        while (len(stack) != 0):
            
        
        