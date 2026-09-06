class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, [], 0)
    
    def helper(self, nums, subset, IDX):
        if IDX == len(nums):
            return [subset]

        result = []
        
        result.extend(self.helper(nums, subset + [nums[IDX]], IDX+1))
        result.extend(self.helper(nums, subset, IDX+1))

        return result