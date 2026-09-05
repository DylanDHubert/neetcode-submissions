from collections import defaultdict
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # ITERATE OVER n IN NUMS...
        # TRACK CONSECTIVE COUNT, IF COUNT > len(nums) // 2, RETURN n
        # WHEN TRANSITION TO NEW n RESET
        # REQUIRES SORTED LIST

        nums = sorted(nums)

        counter, curr = 1, nums[0]
        required = math.ceil(len(nums) / 2)

        for n in nums[1:]:
            if n == curr:
                counter += 1
                if counter >= required: return curr
            else:
                counter = 1
                curr = n
        
        return curr
                
            
