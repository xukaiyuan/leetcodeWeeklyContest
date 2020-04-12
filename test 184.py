class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = set()
        
        for word in words:
            for i in range(len(words)):
                if (word == words[i]):
                    continue
                else:
                    if (word in words[i]):
                        res.add(word)
        
        return list(res)

class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        res = ""
        tmp = ""
        #special = ""
        pStart = -1
        #pEnd = -1
        record = {"quot": "\"", "apos": "\'", "amp": "&", "gt": ">", "lt": "<", "frasl": "/"}
        
        for i in range(len(text)):
            if (text[i] == "&"):
                res += tmp
                tmp = ""
                pStart = i + 1
            elif (text[i] == ";"):
                #print(text[pStart: i])
                if (i - pStart > 5):
                    #print(text[pStart: i])
                    res += text[pStart - 1: i + 1]
                    pStart = -1
                else:
                    if (text[pStart: i] in record):
                        res += record[text[pStart: i]]
                        pStart = -1
                    else:
                        res += text[pStart - 1: i + 1]
                        pStart = -1
            else:
                if (pStart == -1):
                    tmp += text[i]
                    
        res += tmp
        
        return res

class dllNode:
    def __init__(self, value):
        self.value = value
        self.index = -1
        self.prev = None
        self.next = None

class doubleLinkedList:
    def __init__(self, m):
        self.head = dllNode(-1)
        self.head.index = -1
        self.tail = dllNode(-1)
        self.tail.index = m
        self.head.next = self.tail
        self.tail.prev = self.head
        self.record = {}
    
    def insert(self, node):
        next = self.head.next 
        node.next = next
        self.head.next = node
        next.prev = node
        node.prev = self.head
        
        #node.index = prev.index + 1
        #self.tail.index += 1
        
    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail
        node.index = node.prev.index + 1
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def put(self, value):
        node = dllNode(value)
        self.add(node)
        self.record[value] = node
    
    def get(self, value):
        node = self.record[value]
        curIndex = node.index
        tmp = node.prev
        while (tmp.value != -1):
            tmp.index += 1
            tmp = tmp.prev
        node.index = 0
        self.remove(node)
        self.insert(node)
        
        return curIndex
        

class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        res = []
        
        dll = doubleLinkedList(m)
        
        for i in range(1, m + 1):
            dll.put(i)
        
        for query in queries:
            cur = dll.get(query)
            res.append(cur)
            
        return res
        