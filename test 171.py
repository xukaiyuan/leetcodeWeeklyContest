def getNoZeroIntegers(n):
    """
    :type n: int
    :rtype: List[int]
    """
    def zeroInt(x):
        for ch in str(x):
            if(ch == "0"):
                return True
        
        return False
    
    res1 = 1
    
    while(res1 < n):
        if(zeroInt(res1) or zeroInt(n - res1)):
            res1 += 1
            continue
        else:
            break
    
    return [res1, n - res1]
'''       
res = []
res = getNoZeroIntegers(1010)
print(res)
'''
def minFlips(a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: int
    """
    aORb = a | b
    aXORb = a ^ b
    aORbXORc = aORb ^ c
    
    res = 0
    
    while (aORbXORc != 0):
        tmp = aORbXORc & 1
        record = aORb & 1
        ref = aXORb & 1
        if (tmp == 1):
            if(record == 1 and ref == 1):
                res += 1
            elif (record == 1 and ref == 0):
                res += 2
            else:
                res += 1
        
        aORbXORc = aORbXORc >> 1
        aORb = aORb >> 1
        aXORb = aXORb >> 1
        
    return res
'''
print(minFlips(8, 3, 5))
'''

class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        G = {}
        ids = [-1] * n
        self.cnt_iso = 0
        numOfCircles = 0
        self.paths = []
        
        def allCircles(G, n):
            cnt = 0
            
            for i in range(3, n + 1):
                cnt += circlesWithLength(G, n, i)
            
            return cnt
        
        def circlesWithLength(G, n, length):
            cnt = 0
            
            for i in range(0, n - length + 1):
                cnt += circlesWithPath(G, length, [i])
            
            return cnt
        
        def circlesWithPath(G, length, path):
            l = len(path)
            last = path[-1]
            cnt = 0
            
            if (l == length - 1):
                for i in G[last]:
                    if (i > path[1] and i not in path and path[0] in G[i]):
                        cnt += 1
                        self.paths.append((path + [i]))
            else:
                for i in G[last]:
                    if (i > path[0] and i not in path):
                        cnt += circlesWithPath(G, length, path + [i])
            
            return cnt
        
        def graphInit(n, connections):
            for i in range(n):
                ids[i] = i
                self.cnt_iso += 1
                G[i] = set()
                
            for connection in connections:
                G[connection[0]].add(connection[1])
                G[connection[1]].add(connection[0])
                
                #union(connection[0], connection[1])
        
        def find(p):
            if (p == ids[p]):
                return p
            
            tmp = find(ids[p])
            ids[p] = tmp
            
            return tmp
        
        def connected(p, q):
            return (find(p) == find(q))
        
        def union(p, q):
            if(not connected(p, q)):
                self.cnt_iso -= 1
                index_p = find(p)
                index_q = find(q)
                
                ids[index_p] = index_q
        
        graphInit(n, connections)
        numOfCircles = allCircles(G, n)
        
        # print(self.cnt_iso)
        # print(numOfCircles)
        tmp = set()
        
        for path in self.paths:
            tmp.add(path[0])

        if (len(tmp) > numOfCircles + 1):
            return -1
        else:
            return len(tmp) - 1
        
