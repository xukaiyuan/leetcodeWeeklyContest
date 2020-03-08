class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if (n % 2 == 1):
            return "a" * n
        else:
            return "a" * (n - 1) + "b"

class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        n = len(light)
        res = 0
        
        on = [0] * (n + 1)
        on[0] = 1
        mostRight = -1
        
        for oper in light:
            on[oper] = 1
            mostRight = max(mostRight, oper)
            #print(on)
            blue = 0
            
            for i in range(0, mostRight):
                #print((oper, i, on[i]))
                if (on[i] == 0):
                    blue = 0
                    break
                else:
                    blue = 1

            res += blue  

        return res
                


class Solution(object):
    def miniute(self, ID, manager, informTime):
        if (len(self.directory[ID]) == 0):
            return 0
        else:
            branch = 0
            for employee in self.directory[ID]:
                branch = max(branch, self.miniute(employee, manager, informTime))
            
            return branch + informTime[ID]
        
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        self.directory = {}
        queue = [headID]
        res = 0
        
        for i in range(n):
            self.directory[i] = set()
        
        for i in range(n):
            if (manager[i] == -1):
                res += informTime[i]
                continue
            else:
                self.directory[manager[i]].add(i)
        
        res = self.miniute(headID, manager, informTime)
    
        
        return res

n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]

numOfMinutes(n, headID, manager, informTime)