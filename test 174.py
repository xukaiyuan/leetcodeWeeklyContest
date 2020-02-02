from queue import PriorityQueue
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        pq = PriorityQueue()
        res = []
        
        for i in range(len(mat)):
            pq.put((sum(mat[i]), i))
        
        for i in range(k):
            res.append(pq.get()[1])
        
        return res

from queue import PriorityQueue
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        
        record = {}
        pq = PriorityQueue()
        res = 0
        count = 0
        
        for num in arr:
            record[num] = record.get(num, 0) + 1
        
        for key in record:
            pq.put((-record[key], key))
        
        while (count < length / 2):
            tmp = pq.get()
            count -= tmp[0]
            res += 1
        
        return res
        