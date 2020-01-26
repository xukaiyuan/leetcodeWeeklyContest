from Queue import PriorityQueue
class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        class CompareAble:
            def __init__(self, restaurant):
                self.rating = restaurant[1]
                self.id = restaurant[0]

            def __cmp__(self, other):
                if self.rating < other.rating:
                    return 1
                elif self.rating == other.rating:
                    if self.id < other.id:
                        return 1
                    else:
                        return -1
                else:
                    return -1
                
        pq = PriorityQueue()
        res = []
        
        for restaurant in restaurants:
            if (not veganFriendly):
                if (restaurant[3] <= maxPrice and restaurant[4] <= maxDistance):
                    pq.put(CompareAble(restaurant))
            else:
                if (restaurant[2] and restaurant[3] <= maxPrice and restaurant[4] <= maxDistance):
                    pq.put(CompareAble(restaurant))

        while pq.qsize()!= 0:
            res.append(pq.get().id)
        
        return res