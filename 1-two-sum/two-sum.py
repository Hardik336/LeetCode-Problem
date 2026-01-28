class Solution(object):
    def twoSum(self,nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


obj=Solution()
obj.twoSum([1,2,3,4,5,6],5)