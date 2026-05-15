class Solution:
    def reverse(self, n):
        res = ""
        for i in str(n):
            res = i + res
        return int(res)
    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse(n))