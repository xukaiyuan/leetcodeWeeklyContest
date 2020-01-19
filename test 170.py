def watchedVideosByFriends(watchedVideos, friends, id, level):
    """
    :type watchedVideos: List[List[str]]
    :type friends: List[List[int]]
    :type id: int
    :type level: int
    :rtype: List[str]
    """
    levelRelation = {}
    i = 0
    friendQueue = [id]
    record = {}
    targetFriends = set()
    res = []
    
    while (i <= level):
        levelLen = len(friendQueue)
        while(levelLen != 0):
            levelLen -= 1
            curGuy = friendQueue.pop(0)
            if(curGuy not in levelRelation):
                levelRelation[curGuy] = i
                if (i == level):
                    targetFriends.add(curGuy)
            else:
                continue

            curFriends = friends[curGuy]
            for curFriend in curFriends:
                friendQueue.append(curFriend)
            
            
        
        i += 1
    
    for target in targetFriends:
        for video in watchedVideos[target]:
            record[video] = record.get(video, 0) + 1

    tmp = sorted(record.items(), key = lambda item:(item[1], item[0]))
    for item in tmp:
        res.append(item[0])

    print(res)        
    
'''
watchedVideos = [["bjwtssmu"],["aygr","mqls"],["vrtxa","zxqzeqy","nbpl","qnpl"],["r","otazhu","rsf"],["bvcca","ayyihidz","ljc","fiq","viu"]]
friends = [[3,2,1,4],[0,4],[4,0],[0,4],[2,3,1,0]]
id = 3
level = 1
'''
watchedVideos =[["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 2
#watchedVideosByFriends(watchedVideos, friends, id, level)


def xorQueries(arr, queries):
    """
    :type arr: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    memo = [0] * len(arr)
    memo[0] = arr[0]
    res = []
    
    for i in range(1, len(arr)):
        memo[i] = memo[i - 1] ^ arr[i]
    
    for query in queries:
        if (query[1] == query[0]):
            res.append(arr[query[0]])
        elif(query[0] == 0):
            res.append(memo[query[1]])
        else:
            res.append(memo[query[1]] ^ memo[query[0] - 1])

    print(memo)
    
    return res


print(xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]))
