class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        middle = len(nums) // 2

        left, right = nums[:middle], nums[middle:]

        left, right = self.sortArray(left), self.sortArray(right)

        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]

        if left: result.extend(left)
        if right: result.extend(right)

        return result

