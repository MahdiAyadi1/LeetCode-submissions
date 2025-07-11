class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        c = 0
        if len(a) > len(b):
            b = "0"*(len(a)-len(b)) + b
        elif len(b) > len(a):
            a = "0"*(len(b)-len(a)) + a
        for i in range(len(a)):
            aux = int(a[-1-i]) + int(b[-1-i]) + c
            if aux == 2:
                c = 1
                res = "0" + res
            elif aux == 3:
                c = 1
                res = "1" + res 
            else:
                c = 0
                res = str(aux) + res                
        if c == 1:
            return "1" + res
        return res