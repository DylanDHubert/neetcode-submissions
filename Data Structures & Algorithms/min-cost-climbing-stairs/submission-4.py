class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_ago = cost[1]
        two_ago = cost[0]

        for INDEX in range(2, len(cost)):
            one_ago, two_ago = cost[INDEX] + min(one_ago, two_ago), one_ago
 
        return min(one_ago, two_ago)

# cost 1 0 0 1
# 1ago X 0 1 1
# 2ago 1 X 0 1