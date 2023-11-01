class Solution(object):
    def maxArea(self, height):
        first = 0 
        last = len(height)-1
        container = 0
        while first < last : 
            volume = min([height[last],height[first]])*(last-first)
            if volume > container :
                container = volume 
            if height[last] > height[first] : 
                first +=1 
            else: 
                last-=1
        return container

        