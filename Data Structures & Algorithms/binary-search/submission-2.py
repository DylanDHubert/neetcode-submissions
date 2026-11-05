class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            index = (lo + hi) // 2
            choice = nums[index]

            if choice == target: return index
            if choice > target: hi = index - 1
            if choice < target: lo = index + 1

        return -1