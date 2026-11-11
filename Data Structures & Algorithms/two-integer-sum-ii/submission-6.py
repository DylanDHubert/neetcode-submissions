class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # TWO POINTERS SINCE ARRAY IS SORTED...
        L, R = 0, len(numbers) - 1

        while True:
            result = numbers[L] + numbers[R]
            if result > target: R -= 1
            elif result < target: L += 1
            else: return [L+1, R+1]
