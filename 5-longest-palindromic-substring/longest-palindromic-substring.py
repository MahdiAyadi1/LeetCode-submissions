class Solution(object):
    def longestPalindrome(self, s):
        n=len(s)
        for i in range(n):
            for j in range(i+1):
                test = s[j:n-i+j]
                if test == test[::-1]:
                    return test
        