class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:        
        k = 0
        for IDX in range(len(nums)):
            if nums[IDX] != val:
                nums[k] = nums[IDX]
                k += 1
        return k
        