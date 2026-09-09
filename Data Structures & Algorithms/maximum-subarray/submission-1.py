class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            memo = {}

            def mSA(index):
                if memo.get(index): return memo[index]
                if index < 0: return 0

                result = max(nums[index], nums[index] + mSA(index-1))

                memo[index] = result
                return result
            
            return max([mSA(index) for index in range(len(nums))])

