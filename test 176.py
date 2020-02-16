class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        res = 0
        
        for i in range(m):
            left = 0
            right = n - 1
            
            if (grid[i][left] < 0):
                res += n
                continue
            elif (grid[i][right] >= 0):
                continue
            
            while(left <= right):
                mid = int((right - left) / 2 + left)

                if (grid[i][mid] >= 0):
                    left = mid + 1
                else:
                    if (grid[i][mid - 1] >= 0):
                        res += (n - mid)
                        left = right + 1
                    else:
                        right = mid - 1
        
        return res

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))

class ProductOfNumbers(object):

    def __init__(self):
        self.product = []
        self.zero = set()
        self.curr = 1

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """ 
        if (num == 0):
            self.zero.add(len(self.product))
            self.product.append(self.curr)
        else:
            self.curr *= num
            if (len(self.product) == 0):
                self.product.append(num)
            else:
                self.product.append(self.curr)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        for i in range(len(self.product) - 1, len(self.product) - k - 1, -1):
            if (i in self.zero):
                return 0

        if (k == len(self.product)):
            return self.curr
        else:
            return self.curr / self.product[len(self.product) -k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)