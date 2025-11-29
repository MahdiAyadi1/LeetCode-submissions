class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        prefix=strs[0]
        for word in strs[1:]:
            if len(prefix)> len(word):
                prefix = prefix[:len(word)]
            for index in range(len(prefix)):
                if prefix[index]!=word[index]:
                    prefix = prefix[0:index]
                    break
            if len(prefix) == 0:
                return ""
        return prefix
        
       