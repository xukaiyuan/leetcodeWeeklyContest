class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """        
        arr.sort()
        diff = arr[0] - arr[1]
        
        for i in range(1, len(arr) - 1):
            tmp = arr[i] - arr[i + 1]
            
            if (tmp != diff):
                return False
        
        return True