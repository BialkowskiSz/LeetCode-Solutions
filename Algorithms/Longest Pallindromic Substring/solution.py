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
                indexMap[value].append(index + 1)
            else:
                indexMap[value] = [index + 1]
        
        for index, value in enumerate(s):
            indexMapPop = indexMap[value][::-1]
            for indexMapPopValue in indexMapPop:
                #   If length of potential pallindrome is less then don't check it
                if ((indexMapPopValue + 1) - index) > longest:
                    potentialPallindrome = s[index : indexMapPopValue :]
                    lenPallindrome = self.isPallindrome(potentialPallindrome)
                    if lenPallindrome is not None:
                        if lenPallindrome > longest:
                            longest = lenPallindrome
                            longestString = potentialPallindrome
        
        return longestString
            
        
    
    def isPallindrome(self, s):
        length = len(s)
        if length <= 1:
            return length
        
        check = (s == s[::-1])
        if check:
            return length
        return None
