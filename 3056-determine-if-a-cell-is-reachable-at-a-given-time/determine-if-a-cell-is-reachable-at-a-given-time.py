class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        if sx == fx and fy == sy : 
            if t==0 : 
                return True
            return t >1
        distance = max([abs(fx-sx),abs(fy-sy)])
        return distance <=t
        