class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(reverse = True)
        
        total = sum(nums)
        #print(total)
        
        res = []
        curSum = 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            res.append(nums[i])
            
            if (curSum > total / 2):              
                return res

class Solution(object):
    def plusOne(self, s):
        for i in range(len(s) - 1, -1, -1):
            if (s[i] == "0"):
                s = s[:i] + "1" +s[i + 1:]
                break
            else:
                s = s[:i] + "0" +s[i + 1:]
        
        if (s[0] == "0"):
            s = "1" + s
        
        return s
    
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        
        while (len(s) != 1):
            if (s[-1] == "1"):
                s = self.plusOne(s)
            else:
                s = s[:-1]
            
            res += 1
        
        return res

import Queue
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        q = Queue.PriorityQueue()
        res = ""
        
        if (a != 0):
            q.put((-a, "a"))
        
        if (b != 0):
            q.put((-b, "b"))
        
        if (c != 0):
            q.put((-c, "c"))
        
        while (q.qsize() != 0):
            #print((q.queue, res))
            cur1 = q.get()
            if (len(res) < 2):
                res += cur1[1]
                
                if (cur1[0] != -1):
                    q.put((cur1[0] + 1, cur1[1]))
            else:
                if (res[-1] != res[-2]):
                    res += cur1[1]

                    if (cur1[0] != -1):
                        q.put((cur1[0] + 1, cur1[1]))
                else:
                    if (cur1[1] == res[-1]):
                        if (q.qsize() == 0):
                            return res
                        else:
                            cur2 = q.get()
                            q.put((cur1[0], cur1[1]))
                            res += cur2[1]
                            if (cur2[0] != -1):
                                q.put((cur2[0] + 1, cur2[1]))
                    else:
                        res += cur1[1]

                        if (cur1[0] != -1):
                            q.put((cur1[0] + 1, cur1[1]))

        return res

class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        for size in range(1, n + 1):
            i = 0
            while (i + size <= n):
                j = i + size - 1    
                parity = (i + j + n) % 2
                
                if (parity):
                    dp[i + 1][j + 1] = -stoneValue[i] + dp[i + 2][j + 1]
                    if (i + 1 < n):
                        dp[i + 1][j + 1] = min(dp[i + 1][j + 1], -stoneValue[i] - stoneValue[i + 1] + dp[i + 3][j])
                    if (i + 2 < n):
                        dp[i + 1][j + 1] = min(dp[i + 1][j + 1], -stoneValue[i] - stoneValue[i + 1] - stoneValue[i + 2] + dp[i + 4][j + 1])
                else:
                    dp[i + 1][j + 1] = stoneValue[i] + dp[i + 2][j]
                    if (i + 1 < n):
                        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], stoneValue[i] + stoneValue[i + 1] + dp[i + 3][j])
                    if (i + 2 < n):
                        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] + dp[i + 4][j + 1])
                
                i += 1

        if (dp[1][n] > 0):
            return "Alice"
        elif (dp[1][n] == 0):
            return "Tie"
        else:
            return "Bob"
        