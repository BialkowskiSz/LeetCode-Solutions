import collections

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <= 1:
            return s
        
        longest  = 1
        longestString = s[0]
        indexMap = {}
        
        for index, value in enumerate(s):
            if value in indexMap:
                indexMap[value].appendleft(index + 1)
            else:
                indexMap[value] = collections.deque([index + 1])
        
        for index, value in enumerate(s):
            indexMapPop = indexMap[value]
            for indexMapPopValue in indexMapPop:
                #   If length of potential pallindrome is less then don't check it
                if (indexMapPopValue - index) > longest:
                    potentialPallindrome = s[index : indexMapPopValue :]
                    lenPallindrome = self.isPallindrome(potentialPallindrome)
                    if lenPallindrome is not None:
                        longest = lenPallindrome
                        longestString = potentialPallindrome
        
        return longestString
            
        
    
    def isPallindrome(self, s):
        length = len(s)
        
        check = (s == s[::-1])
        if check or length <= 1:
            return length
        
        return None
