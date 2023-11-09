class Solution(object):
    def countHomogenous(self, s):
        if s=="" : 
            return 0
        substrings = []
        word = s[0]
        for i in range(len(s)-1) : 
            if s[i]==s[i+1] : 
                word += s[i+1] 
            else : 
                substrings.append(word)
                word = s[i+1]
        substrings.append(word)
        output = 0
        for i in substrings : 
            output += ((len(i)+1)*len(i))/2
        return output % (10**9 +7 )



        