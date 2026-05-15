class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        i = len(nums)//2
        if nums[0] > nums[i-1]:
            return self.findMin(nums[0:i])
        return self.findMin(nums[i:])