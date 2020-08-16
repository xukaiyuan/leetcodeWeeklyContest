class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if (len(arr) < 3):
            return False
        
        cnt = 0
        
        for i in range(len(arr)):
            if (arr[i] % 2 == 0):
                cnt = 0
            else:
                cnt += 1
            
            if (cnt == 3):
                return True
        
        return cnt == 3
        
class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n % 2 == 0):
            return n ** 2 / 4
        else:
            return (n ** 2 - 1) / 4

# didn't consider the position is not full
from Queue import PriorityQueue as PQ
class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        
        if (m == 2):
            return position[-1] - position[0]
        
        m -= 2
        pq = PQ()
        pq.put((-position[-1] + position[0], position[0], position[-1]))
        res = float("inf")
        
        while (m != 0):
            cur = pq.get()
            print(cur)
            
            if (cur[0] % 2 == 0):
                pq.put((cur[0] / 2, cur[1], cur[1] - cur[0] / 2))
                pq.put((cur[0] / 2, cur[2] + cur[0] / 2, cur[2]))
                res = min(res, -cur[0] / 2)
            else:
                pq.put((floor(cur[0] / 2), cur[1], cur[1] - floor(cur[0] / 2)))
                pq.put((floor(cur[0] / 2) + 1, cur[2] + floor(cur[0] / 2) + 1, cur[2]))
                res = min(res, -floor(cur[0] / 2))
            
            m -= 1
        
        return int(res)