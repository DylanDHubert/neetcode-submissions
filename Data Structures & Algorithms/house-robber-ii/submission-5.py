class Solution:
    def rob(self, nums: List[int]) -> int:
        # TRICK IS TO EITHER RUN TWO PROBLEMS, ALLOWING FIRST VS LAST IE, [:-1] VS [1:]
        # OR. TRACK IF FIRST ROBBED ONLY INSTEAD OF str(hit)

        def recRob(numbers, IDX=0):
            if IDX >= len(numbers):
                return 0

            if memoize.get(IDX) is not None: return memoize.get(IDX)
            
            to_rob = numbers[IDX] + recRob(numbers, IDX + 2,)
            not_to_rob = recRob(numbers, IDX + 1)
        
            memoize[IDX] = max(to_rob, not_to_rob)
            return memoize.get(IDX)

        # CHECK FOR len(1)
        if len(nums) == 1: return nums[0]

        # TRICK: CAN ONLY ROB [0 XOR -1], RUN ALLOWING EACH AND NOT THE OTHER
        # (SINCE THEY NEVER OCCUR TOGETHER)
        memoize = {}
        rob_first = recRob(nums[:-1])
        memoize = {}
        pass_first = recRob(nums[1:])

        return max(rob_first, pass_first)