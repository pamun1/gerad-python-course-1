from data import read_from_csv

import matplotlib.pyplot as plt

# Reading the data
supply_file = "data/supply_medium.csv"
demand_file = "data/demand_medium.csv"
costs_file = "data/costs_medium.csv"

supply = read_from_csv(supply_file, "supplier", "supply")
demand = read_from_csv(demand_file, "customer", "demand")
costs = read_from_csv(costs_file, ["supplier", "customer"], "cost")

# Line plot
plt.plot(supply.keys(), supply.values(), marker="o", 
			         color="orange", label="Supply")
plt.xlabel("Supplier")
plt.ylabel("Units")
plt.title("Supply")
plt.legend()
plt.savefig("plots/supply_plot.png")
plt.show()

# Bar plot
plt.bar(demand.keys(), demand.values(), color="blue", 
			        label="Demand")
plt.xlabel("Customer")
plt.ylabel("Units")
plt.title("Demand")
plt.legend()
plt.savefig("plots/demand_plot.png")
plt.show()