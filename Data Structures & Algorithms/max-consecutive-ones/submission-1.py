class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        this_max = 0
        nums.append(0) # IN THE CASE THAT MAX 1S ENDS AT -1
        for v in nums:
            if v:
                this_max += 1
            else:
                if this_max > maximum:
                    maximum = this_max
                this_max = 0
        return maximum