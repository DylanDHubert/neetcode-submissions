class Solution:
    def rob(self, nums: List[int]) -> int:
        # NAIVE: return max(sum(nums[::2]), sum(nums[1::2]))

        # MAKE DP...
        DP = {}

        def recursivelyRob(IDX=0, curr=0):
            if IDX >= len(nums): return curr
            if DP.get((IDX, curr)) is not None: return DP.get((IDX, curr))

            to_rob = recursivelyRob(IDX + 2, curr + nums[IDX])

            not_to_rob = recursivelyRob(IDX + 1, curr)

            DP[(IDX, curr)] = max(to_rob, not_to_rob)
            return DP[(IDX, curr)]

        return recursivelyRob()