class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        totalOne = 0
        
        for i in range(len(s)):
            if (s[i] == "1"):
                totalOne += 1
        
        if (s[0] == "1"):
            res = totalOne - 1
        else:
            res = totalOne + 1
            
        tmp = res
        
        for i in range(1, len(s) - 1):
            if (s[i] == "1"):
                tmp -= 1
            else:
                tmp += 1
            
            res = max(res, tmp)
    
        return res

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        
        if (k == n):
            return sum(cardPoints)
        
        def recursion(cardPoints, start, end, k):
            if (k == 0):
                return 0
            if (k == 1):
                return max(cardPoints[start], cardPoints[end])
            else:
                return max(cardPoints[start] + recursion(cardPoints, start + 1, end, k - 1),
                           cardPoints[end] + recursion(cardPoints, start, end - 1, k - 1))
            
        
        res = max(cardPoints[0] + recursion(cardPoints, 1, n - 1, k - 1),
                  cardPoints[n - 1] + recursion(cardPoints, 0, n - 2, k - 1))

        return res

# Q3: Sort all triples (row + col, col, nums[row][col]) in ascending order, then output only thrid elements.
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        if (k == n):
            return sum(cardPoints)
        if (k == n - 1):
            return sum(cardPoints) - min(cardPoints)
        
        tmpSum = 0
        tatal = 0
        
        for i in range(n - k):
            tmpSum += cardPoints[i]
        
        minSum = tmpSum
        total = tmpSum
        #print(minSum)
        
        for i in range(n - k, n):
            tmpSum -= cardPoints[i - (n - k)]
            tmpSum += cardPoints[i]
            total += cardPoints[i]
            
            minSum = min(minSum, tmpSum)
            #print(minSum)
        
        return total - minSum

class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        res = []
        
        m = len(nums)
        n = len(nums[0])
        
        for i in range(m):
            n = max(n, len(nums[i]))
            start = [i, 0]
            try:
                res.append(nums[start[0]][start[1]])
            except:
                pass
            
            for j in range(i):
                start[0] -= 1
                start[1] += 1
                
                if (start[0] > -1 and start[1] < n):
                    try:
                        res.append(nums[start[0]][start[1]])
                    except:
                        pass
        
        for i in range(1, n):
            start = [m - 1, i]
            
            try:
                res.append(nums[start[0]][start[1]])
            except:
                pass
            
            for j in range(n - i - 1):
                start[0] -= 1
                start[1] += 1
                
                if (start[0] > -1 and start[1] < n):
                    try:
                        res.append(nums[start[0]][start[1]])
                    except:
                        pass
  
        return res