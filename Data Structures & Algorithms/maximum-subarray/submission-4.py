class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L = 0
        R = 1

        maximum = nums[0]
        result = nums[0]

        while L < len(nums):
                        
            if result > maximum:
                maximum = result

            if (result < 0) and (R < len(nums)): # RESULT IS NEGATIVE... CHUNK NEVER 
                L = R # SET L TO R (END POINT)
                R += 1
                result = nums[L] # RESET RESULT
            elif R < len(nums):
                result += nums[R]
                R += 1
            else:
                result -= nums[L]
                L += 1
        
        return maximum
            

