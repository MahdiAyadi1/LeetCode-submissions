class Solution(object):
    def isValid(self, s):
        bracket=""
        while s :
            test = True
            if "()" in s:
                index = s.find("()")
                s = s[:index]+ s[index+2:]
                test = False
            if "{}" in s:
                index = s.find("{}")
                s = s[:index]+ s[index+2:]
                test = False
            if "[]" in s:
                index = s.find("[]")
                s = s[:index]+ s[index+2:]
                test = False
            if test : 
                return False
        return True