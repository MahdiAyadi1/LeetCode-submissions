class Solution(object):
    def sortVowels(self, s):
        d={}
        for i in range(len(s)) : 
            if s[i].lower() in ['a','e','i','o','u'] :
                if ord(s[i]) in d.keys() : 
                    
                    d[ord(s[i])] += 1 
                else :
                    d[ord(s[i])] = 1
        l = sorted(d.keys())
        t=""
        for i in s : 
            if i.lower() in ['a','e','i','o','u'] :
                t= t + (chr(l[0])) 
                if d[l[0]] == 1 :
                    l=l[1:]
                else : 
                    d[l[0]] -= 1
            else : 
                t = t + i
        return t
            

        