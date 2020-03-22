class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        
        for i in range(len(nums)):
            if (res[index[i]] != -1):
                for j in range(len(nums) - 1, index[i], -1):
                    res[j] = res[j - 1]
                
            res[index[i]] = nums[i]
        
        return res