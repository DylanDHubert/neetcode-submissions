class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers - target = NUMBER WE NEED
        diff = {target - n: index for index, n in enumerate(numbers, 1)}

        for index, n in enumerate(numbers, 1):
            if diff.get(n) is not None:
                return [index, diff[n]]
