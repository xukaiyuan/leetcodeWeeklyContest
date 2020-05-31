class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        return (nums[-1] - 1) * (nums[-2] - 1)

class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        res = 0
        modulo = 10e9 + 7
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        hmax = -1
        vmax = -1
        
        cur = 0
        for cut in horizontalCuts:
            hmax = max(hmax, cut - cur)
            cur = cut
        hmax = max(hmax, h - cur)
        
        cur = 0
        for cut in verticalCuts:
            vmax = max(vmax, cut - cur)
            cur = cut
        vmax = max(vmax, w - cur)
               
        res = (hmax * vmax) % modulo

        print(hmax)
        print(vmax)
        
        return int(res)

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        connected = set()
        res = 0
        relation = {}
        uniDirection = {}
        queue = [0]
        
        for connection in connections:
            a, b = connection[0], connection[1]
            
            if (a not in relation):
                relation[a] = {b}
            else:
                relation[a].add(b)
                
            if (a not in uniDirection):
                uniDirection[a] = {b}
            else:
                uniDirection[a].add(b)
            
            if (b not in relation):
                relation[b] = {a}
            else:
                relation[b].add(a)
        
        while (len(queue) != 0):
            cur = queue.pop(0)
            connected.add(cur)
            
            for adj in relation[cur]:
                if (adj in connected):
                    continue
                else:
                    queue.append(adj)
                    if (cur in uniDirection and adj in uniDirection[cur]):
                        #print((adj, cur))
                        res += 1
                        
        return res