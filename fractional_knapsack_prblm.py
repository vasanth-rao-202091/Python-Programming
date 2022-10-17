# Knapsack problem
# Fractional Knapsack Problem
def max_profit(capacity,weights,profits,objects):
    p_to_w = []
    for i in range(len(profits)):
        p_to_w.append(profits[i]/weights[i])
    
    items = []
    
    for i in range(len(profits)):
        items.append([weights[i],profits[i],p_to_w[i],objects[i]])
    
    items = sorted(items,key=lambda x:x[2],reverse = True)
    
    cur_capacity = 0
    profit = 0

    for item in items:
        if cur_capacity+item[0] < capacity:
            cur_capacity+= item[0]
            profit += item[1]
        else:
            r = capacity - cur_capacity
            cur_capacity += r
            profit += ((r/item[0])*item[1])
            break
    return profit
    
weights = [10,20,30]
profits = [60,100,120]
objects = [1,2,3]
capacity = 60
print("Max. profit", max_profit(capacity,weights,profits,objects))


