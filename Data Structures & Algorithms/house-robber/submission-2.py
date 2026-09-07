class Solution:
    def rob(self, nums: List[int]) -> int:
        # ITERATIVE DP
        one_ago = 0
        two_ago = 0

        curr = 0

        for INDEX in range(len(nums)):
            # BEST IS MAX OF ONE AGO (CAN'T ROB THIS), TWO AGO (ROB THIS!)
            curr = max(one_ago, two_ago+nums[INDEX])
            two_ago = one_ago # TWO AGO IS WHAT ONE AGO WAS
            one_ago = curr # AND ONE AGO, IS NOW CURRENT

        return curr






