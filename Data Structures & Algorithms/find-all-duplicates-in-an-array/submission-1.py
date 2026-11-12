class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # O(n) TIME WITH O(1) SPACE (USING INPUT ARRAY AS MAP)

        duplicates = []

        for INDEX in range(len(nums)):
            v = abs(nums[INDEX])
            
            if nums[v-1] < 0:
                duplicates.append(v)
            
            else:
                nums[v-1] *= -1
        
        return duplicates