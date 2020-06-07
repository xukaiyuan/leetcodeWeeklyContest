class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = [-1] * 2 * n
        
        for i in range(n):
            res[2 * i] = nums[i]
        
        for i in range(n, 2 * n):
            res[2 * (i - n) + 1] = nums[i]
        
        return res

from Queue import PriorityQueue as PQ
class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        pq = PQ()
        length = len(arr)
        arr.sort()
        
        median = arr[int((length - 1) / 2)]
        
        for i in range(length):
            pq.put((-abs(arr[i] - median), -arr[i], i))
        
        for i in range(k):
            tmp = pq.get()
            res.append(arr[tmp[2]])
        
        return res

class node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

class dll:
    def __init__(self, value):
        self.cur = node(value)
        self.record = {value: self.cur}

    def insert(self, value):
        new = node(value)
        self.record[value] = new

        if (self.cur.next != None):
            tmp = self.cur.next

            while (tmp != None):
                del self.record[tmp.value]
                tmp = tmp.next

        self.cur.next = new
        new.prev = self.cur

        self.cur = new

    def searchBack(self, steps):
        count = 0

        while (count < steps):
            if (self.cur.prev == None):
                break
            self.cur = self.cur.prev
            count += 1

        return self.cur

    def forward(self, steps):
        count = 0

        while (count < steps):
            if (self.cur.next == None):
                break
            self.cur = self.cur.next
            count += 1

        return self.cur
    
class BrowserHistory(object):
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.dll = dll(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.dll.insert(url)

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        node = self.dll.searchBack(steps)
        
        return node.value

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        node = self.dll.forward(steps)
        
        return node.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        dp = [[[0] * m for _ in range(n)] for _ in range(m)]
        res = float("inf")
        
        if (houses[0] != 0):
            dp[0][i][0] = cost[0][houses[0]]
        else:
            for i in range(n):
                dp[0][i][0] = cost[0][i]
        
        for i in range(1, m):
            if (houses[i] != 0):
                for k in range(m):
                    prevMin = float("inf")
                    
                    for j in range(n):
                        if (houses[i] != j):
                            prevMin = min(prevMin, dp[i - 1][j][k - 1])      
                        elif (k != m - 1):
                            prevMin = min(prevMin, dp[i - 1][j][k])
                            
                    dp[i][house[i]][k] = prevMin + cost[i][house[i]]
            else:
                for j in range(n):
                    for k in range(m):
                        prevMin = float("inf")
                        
                        for x in range(n):
                            if (j != x):
                                prevMin = min(prevMin, dp[i - 1][x][k - 1])
                            elif (k != m - 1):
                                prevMin = min(prevMin, dp[i - 1][x][k])
                        
                        dp[i][j][k] = prevMin + cost[i][j]
        
        for j in range(n):
            if (dp[-1][j][target - 1] != 0):
                res = min(res, dp[-1][j][target - 1])
        
        if (res < float("inf")):
            return res
        else:
            return -1
