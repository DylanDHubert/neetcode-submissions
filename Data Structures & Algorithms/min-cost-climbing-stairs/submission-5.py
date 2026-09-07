class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_ago = cost[1]
        two_ago = cost[0]

        for c in cost[2:]:
            one_ago, two_ago = c + min(one_ago, two_ago), one_ago
 
        return min(one_ago, two_ago)

# cost 1 0 0 1
# 1ago X 0 1 1
# 2ago 1 X 0 1