class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        letter = []
        digit = []
        n = len(s)
        
        for i in range(n):
            if (s[i].isdigit()):
                digit.append(s[i])
            else:
                letter.append(s[i])
        
        if (abs(len(digit) - len(letter)) > 1):
            return res
        
        if (len(digit) > len(letter)):
            res = digit[0]
            digit.pop(0)
        else:
            res = letter[0]
            letter.pop(0)
        
        for i in range(n - 1):
            if (res[-1].isalpha()):
                res += digit[0]
                digit.pop(0)
            else:
                res += letter[0]
                letter.pop(0)
        
        return res

class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        items = set()
        tables = {}
        res = [["Table"]]
        
        for order in orders:
            if (int(order[1]) not in tables):
                tables[int(order[1])] = {}
            if (order[2] not in items):
                items.add(order[2])
            tables[int(order[1])][order[2]] = tables[int(order[1])].get(order[2], 0) + 1
        
        items = sorted(items)
        
        for item in items:
            res[0].append(item)
        
        for table in sorted(tables.keys()):
            newRow = [str(table)]
            
            for i in range(1, len(res[0])):
                newRow.append(str(tables[table].get(res[0][i], 0)))
            
            res.append(newRow)
        
        return res

class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        if (croakOfFrogs[0] != "c"):
            return -1
        
        def findPrev(target, stack, tmp):
            if (len(stack) == 0):
                return False
            else:     
                while (len(stack) != 0):
                    if (stack[-1] != target):
                        c = stack.pop()
                        tmp.append(c)
                    else:
                        stack.pop()
                        break
                
                while (len(tmp) != 0):
                    self.flag = True
                    c = tmp.pop()
                    stack.append(c)
                
                return True
        
        res = 0
        s = [croakOfFrogs[0]]
        tmp = []
        self.flag = False
        free = 0
        
        for i in range(1, len(croakOfFrogs)):
            if (croakOfFrogs[i] != "k"):
                s.append(croakOfFrogs[i])
            else:
                self.flag = False
                if (findPrev("a", s, tmp)):
                    if (findPrev("o", s, tmp)):
                        if (findPrev("r", s, tmp)):
                            if (findPrev("c", s, tmp)):
                                if (self.flag or len(s) != 0 or free == 0):
                                    res += 1
                                else:
                                    free -= 1
                                free += 1
                            else:
                                return -1
                        else:
                            return -1
                    else:
                        return -1
                else:
                    return -1
        
        return res if (len(s) == 0) else -1
                
            