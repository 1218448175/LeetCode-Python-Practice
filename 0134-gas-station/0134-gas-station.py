class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        min_index = -1
        total_spare = 0
        for i in range(n):
            spare = gas[i] - cost[i]
            total_spare += spare
            if total_spare < 0:
                total_spare = 0
                min_index = i
        
        return (min_index + 1) % n
