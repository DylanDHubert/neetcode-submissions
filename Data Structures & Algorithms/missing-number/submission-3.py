class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        p = n = nums[0]

        if p != 0: return 0

        for n in nums[1:]:
            if n - p != 1:
                return (n + p) // 2
            p = n
        
        return n + 1