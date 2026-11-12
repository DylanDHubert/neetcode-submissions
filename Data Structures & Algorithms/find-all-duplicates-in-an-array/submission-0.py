class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # O(n) TIME WITH O(n) SPACE
        seen = {}
        duplicates = []
        for n in nums:
            if seen.get(n) is not None: duplicates.append(n)
            else: seen[n] = True
        return duplicates