from typing import List

class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost = 0, 0
        current_balance, start = 0, 0
        
        num_stations = len(gas)
        
        for idx in range(num_stations):
            total_gas += gas[idx]
            total_cost += cost[idx]
            current_balance += gas[idx] - cost[idx]
            
            if current_balance < 0:
                start = idx + 1
                current_balance = 0
                
                
        return start if total_gas >= total_cost else -1



# O(n) Time Complexity
# O(1) Space Complexity


 
# Old O(n^2) solution that works but also times out from nested loop 
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


#         if sum(gas) < sum(cost):
#             return -1
                
#         num_stations = len(gas)

#         for i in range(num_stations):
#             gas_current = gas[i]
            
#             if (gas[i] == 0 and cost[i] == 0) or (gas_current < 0):
#                 continue 
            
#             j = i + 1

#             while i != j and gas_current >= 0:
#                 gas_current -= cost[(j-1) % num_stations]

#                 if gas_current < 0:
#                     break
                
#                 gas_current += gas[(j % num_stations)]
#                 j = (j+1) % num_stations


#             # print("gas_current: ",gas_current - cost[(j-1) % num_stations])
#             if (gas_current - cost[(j-1) % num_stations] ) >= 0:
#                 return i
                

#         return -1
    
    
    # Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))    
    print(solution.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
    
