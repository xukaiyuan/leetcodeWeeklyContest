class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        record = set()
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        mapping = {"E": 0, "N": 1, "W": 2, "S": 3}
        start = [0, 0]
        record.add(tuple(start))
        
        for direction in path:
            start[0] += dx[mapping[direction]]
            start[1] += dy[mapping[direction]]
            
            if (tuple(start) in record):
                return True
            
            record.add(tuple(start))
        print(record)
        return False