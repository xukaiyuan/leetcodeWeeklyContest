class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        record = {}
        
        for num in arr:
            record[num] = record.get(num, 0) + 1
        
        res = -1
        
        for key in record:
            if (record[key] == key):
                res = max(res, key)
        
        return res


class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        if (len(rating) < 3):
            return 0
        res = 0
        
        for i in range(len(rating)):
            descend = False
            for j in range(i + 1, len(rating)):
                if (rating[j] < rating[i]):
                    descend = True
                elif (rating[j] > rating[i]):
                    descend = False
                else:
                    continue
                for k in range(j + 1, len(rating)):
                    if (descend and rating[k] < rating[j]):
                        res += 1
                        #print((rating[i], rating[j], rating[k]))
                    elif(not descend and rating[k] > rating[j]):
                        res += 1
                    else:
                        continue
                        #print((rating[i], rating[j], rating[k]))
        
        return res

class UndergroundSystem(object):

    def __init__(self):
        self.checkInRecord = {} # id: (station, t)
        self.average = {} # (start, end): (time, cnt)
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkInRecord[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        (start, t1) = self.checkInRecord[id]
        del self.checkInRecord[id]
        
        if ((start, stationName) not in self.average):
            self.average[(start, stationName)] = (float(t - t1), 1)
        else:
            prevT, cnt = self.average[(start, stationName)]
            newT = float((prevT * cnt + float(t - t1)) / (cnt + 1))
            self.average[(start, stationName)] = (newT, cnt + 1)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return self.average[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

class Solution(object):
    def plusOne(self, cur, n):
        for i in range(n - 1, -1, -1):
            if (cur[i] != "z"):
                cur = cur[:i] + chr(ord(cur[i]) + 1) + cur[i + 1:]
                break
            else:
                #print(cur)
                cur = cur[:i] + "a" + cur[i + 1:]
                #print(("new", new))
        #print((cur, new))
        return cur
        
    def findGoodStrings(self, n, s1, s2, evil):
        """
        :type n: int
        :type s1: str
        :type s2: str
        :type evil: str
        :rtype: int
        """
        if (s1 > s2):
            return 0
        
        cur = s1
        index = n
        res = 0
        modulo = 1e9 + 7
        
        while (cur <= s2):
            if (evil not in cur):
                res += 1
                res %= modulo
                
            new = self.plusOne(cur, n)
            
            cur = new
            #print((cur, res))
        
        return int(res)