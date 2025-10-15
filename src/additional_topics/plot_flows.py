from data import read_from_csv
from greedy import greedy_solve

import matplotlib.pyplot as plt


supply_file = "data/supply_medium.csv"
demand_file = "data/demand_medium.csv"
costs_file = "data/costs_medium.csv"

supply = read_from_csv(supply_file, "supplier", "supply")
demand = read_from_csv(demand_file, "customer", "demand")
costs = read_from_csv(costs_file, ["supplier", "customer"], "cost")

flows, rem_sup, rem_dem  = greedy_solve(supply, demand, costs)

flows_matrix = [[flows[s, c] for c in demand.keys()] 
                for s in supply.keys()]

plt.imshow(flows_matrix)
plt.colorbar(label="Units shipped")
plt.title("Shipment Flows")
plt.xticks(ticks=range(len(demand)), labels=list(demand.keys()))
plt.yticks(ticks=range(len(supply)), labels=list(supply.keys()))
plt.show()