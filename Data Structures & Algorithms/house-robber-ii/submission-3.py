class Solution:
    def rob(self, nums: List[int]) -> int:
        # TRICK IS TO EITHER RUN TWO PROBLEMS, ALLOWING FIRST VS LAST IE, [:-1] VS [1:]
        # OR. TRACK IF FIRST ROBBED ONLY INSTEAD OF str(hit)

        def recRob(these_nums, IDX=0, curr=0, hit=[]):
            if IDX >= len(these_nums):
                return curr

            if memoize.get((IDX, curr)): return memoize.get((IDX, curr))
            
            to_rob = recRob(these_nums, IDX + 2, curr + these_nums[IDX], hit.copy() + [IDX])
            not_to_rob = recRob(these_nums, IDX + 1, curr, hit.copy())
        
            memoize[(IDX, curr)] = max(to_rob, not_to_rob)
            return memoize.get((IDX, curr))
        # CHECK FOR len(1)
        if len(nums) == 1: return nums[0]
        memoize = {}
        rob_first = recRob(nums[:-1])
        memoize = {}
        pass_first = recRob(these_nums=nums[1:])
        return max(rob_first, pass_first)