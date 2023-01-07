Min Cost Climbing Stairs

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost1 = cost
        cost1.append(0)
        #print(len(cost))
        temp1 = 0
        temp2 = 0
        for i in range(len(cost1)-3,-1,-1):
            temp2 = cost[i] + cost[i+2] 
            temp1 = cost[i+1] + cost[i]
            cost[i] = min(temp1,temp2)
        return (min(cost[0],cost[1]))
            
