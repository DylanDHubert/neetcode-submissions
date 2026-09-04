class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)

        for IDX, t in enumerate(temperatures): # 2, 1, 1, 3

            if IDX == 0:
                stack.append((IDX, t)) # 2... 2

            else:
                while (stack) and (stack[-1][1] < t):
                    (cooler_day_IDX, _) = stack.pop()
                    results[cooler_day_IDX] = IDX - cooler_day_IDX
                stack.append((IDX, t))

        return results


