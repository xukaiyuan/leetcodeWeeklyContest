class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res = 0
        cur = start
        
        for i in range(n):
            cur = start + 2 * i
            res ^= cur
        
        return res

class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        record = {}
        res = []
        
        for name in names:
            if (name not in record):
                record[name] = 1
                res.append(name)
            else:
                currentK = record[name]
                tmp = name + "(" + str(currentK) + ")"
                
                while (tmp in record):
                    currentK += 1
                    tmp = name + "(" + str(currentK) + ")"
                    
                record[name] = currentK
                record[tmp] = 1
                res.append(tmp)
        
        return res

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        res = []
        
        currentDry = [] # queue to store the days to dry
        currentFull = {}
        
        for i, rain in enumerate(rains):
            if (rain != 0):
                res.append(-1)
                if (rain in currentFull):
                    if (len(currentDry) == 0):
                        return []
                    else:
                        if (currentDry[-1] < currentFull[rain]):
                            return []
                        
                        tmp = []
                        while (currentDry[0] < currentFull[rain]):
                            tmp.append(currentDry.pop(0))
                        
                        res[currentDry.pop(0)] = rain
                        currentDry = tmp + currentDry
                        #index = currentDry.pop(0)
                        #res[index] = rain
                        currentFull[rain] = i
                else:   
                    currentFull[rain] = i
            else:
                currentDry.append(i)
                res.append("x")
                
        for i in range(len(res)):
            if (res[i] == "x"):
                res[i] = 1
                
        return res