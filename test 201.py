class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        if (len(s) <= 1):
            return s
        
        stack = [s[0]]
        res = ""
        
        for i in range(1, len(s)):
            if (len(stack) == 0):
                stack.append(s[i])
                continue
                
            if (stack[-1].lower() != s[i].lower()):
                stack.append(s[i])
            else:
                if ((stack[-1].islower() and s[i].isupper()) or (stack[-1].isupper() and s[i].islower())):                  
                    stack.pop()
                else:
                    stack.append(s[i])
        
        for i in stack:
            res += i
        
        return res

class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if (n == 1):
            return "0"
        if (k - 1 == 2 ** (n - 1) - 1):
            return "1"
        elif (k - 1 < 2 ** (n - 1) - 1):
            return self.findKthBit(n - 1, k)
        else:
            return str((int(self.findKthBit(n - 1, 2 ** n - k)) + 1) % 2)