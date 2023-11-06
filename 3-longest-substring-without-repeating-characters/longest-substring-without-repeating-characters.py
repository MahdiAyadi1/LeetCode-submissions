class Solution(object):
    def lengthOfLongestSubstring(self, s):
        window = 1
        i = 0
        n = len(s)
        output = 0 
        while (i+window<=n) :  
            if len(set(s[i:window+i]))== window : 
                output = window 
                window+=1
            else :
                i+=1
        return output
            