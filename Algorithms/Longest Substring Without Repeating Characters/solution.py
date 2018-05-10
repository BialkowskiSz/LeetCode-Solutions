class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length  = len(s)
        if length < 2:
            return length
        
        longest = 1
        counter = 1
        halfLength = math.ceil(length / 2)
        
        for index, value in enumerate(s):
            repeating = set()
            repeating.add(value)
            counter = 1
            for innerValue in s[index+1::]:
                if innerValue in repeating:
                    if counter > longest:
                        longest = counter
                    break
                repeating.add(innerValue)
                counter += 1
            if counter > longest:
                longest = counter
            
                
        return longest
        
