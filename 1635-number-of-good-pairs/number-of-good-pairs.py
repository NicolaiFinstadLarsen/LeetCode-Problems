class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] == nums[j] and i < j:
                    counter += 1
        return counter
        