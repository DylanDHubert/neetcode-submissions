import math

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = sum(range(len(nums)+1))
        actual = sum(nums)

        if expected == actual: return 0
        else: return expected - actual