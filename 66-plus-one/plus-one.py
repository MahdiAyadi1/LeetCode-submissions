class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = [0]
        a.extend(digits)
        index = len(a) -1
        while 1:
            if a[index] == 9:
                a[index] = 0
                index-=1
            else :
                a[index] += 1
                break
        if a[0]==0:
            return a[1:]
        return  a
  
        