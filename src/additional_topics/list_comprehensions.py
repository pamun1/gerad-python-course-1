from greedy import greedy_solve
from data import read_from_csv

## ===============================
## List comprehensions
## ===============================

# List comprehension without a condition
squares = [x * x for x in range(10)]

# List comprehension with a condition
even_squares = [x * x for x in range(10) if x % 2 == 0]

# Creating a flow matrix
supply_file = "data/supply_medium.csv"
demand_file = "data/demand_medium.csv"
costs_file = "data/costs_medium.csv"

supply = read_from_csv(supply_file, "supplier", "supply")
demand = read_from_csv(demand_file, "customer", "demand")
costs = read_from_csv(costs_file, ["supplier", "customer"], "cost")

# Solving with the greedy heuristic
flows, rem_sup, rem_dem  = greedy_solve(supply, demand, costs)

flows_matrix = [[flows[s, c] for c in demand.keys()] 
                for s in supply.keys()]

print(flows_matrix)