class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        length = len(startTime)
        res = 0
        
        for i in range(length):
            if (startTime[i] <= queryTime and queryTime <= endTime[i]):
                res += 1
        
        return res

from Queue import PriorityQueue as PQ
class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        words = text.split(" ")
        res = ""
        pq = PQ()
        
        for i in range(len(words)):
            word = words[i]
            pq.put((len(word), i, word.lower()))
        
        tmp = pq.get()[2]
        res = tmp[0].upper() + tmp[1:]
        
        while (pq.qsize() != 0):
            #print(pq.get())
            res += " "
            res += pq.get()[2]
        
        return res

from Queue import PriorityQueue as PQ
class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        pq = PQ()
        tmp = []
        res = []
        maxLength = -1
        
        for i in range(len(favoriteCompanies)):
            campanies = set(favoriteCompanies[i])
            pq.put((-len(campanies), i, campanies))
            maxLength = max(maxLength, len(campanies))
        
        while (pq.qsize() != 0):
            cur = pq.get()
            
            if (cur[0] + maxLength == 0):
                res.append(cur[1])
            else:
                flag = True
                for s in tmp:
                    if (cur[2].issubset(s)):
                        flag = False
                        break
                
                if (flag):
                    res.append(cur[1])
            
            tmp.append(cur[2])
        
        return sorted(res)

from Queue import PriorityQueue as PQ
class Solution(object):
    def numPoints(self, points, r):
        """
        :type points: List[List[int]]
        :type r: int
        :rtype: int
        """
        def euclidean(p1, p2):
            return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        
        length = len(points)
        res = length
        record = {}
        pq = PQ()
        blockLength = -1
        blockIndex = -1
        #dist = [[0] * length for _ in range(length)]
        
        for i in range(length):
            for j in range(i + 1, length):
                dist = euclidean(points[i], points[j])
                if (dist > 2 * r):
                    #print((i, j))
                    if (i not in record):
                        record[i] = set()
                    record[i].add(j)

        '''
        delete node from that has the lagest blocked points recursionly
        '''

        return res
        
        