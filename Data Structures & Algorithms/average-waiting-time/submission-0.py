class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time, total = 0, 0

        for arrival_time, cook_time in customers:
            # IF THE CHEF IS BUSY...
            if time > arrival_time: 
                # CUSTOMERS WAIT TIME IS:
                wait_time = time - arrival_time 
                total += wait_time 
            # OTHERWISE, CHEF CAN START RIGHT AWAY
            else:
                time = arrival_time  # MOVE TIME UP,
            # ADD TO TIME & TOTAL, THE COOK TIME REQUIRED
            total += cook_time
            time += cook_time
        
        return total / len(customers)
            

        

        