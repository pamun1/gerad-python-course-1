import pandas as pd
from greedy import greedy_solve

supply_df = pd.read_csv("data/supply_large.csv")
demand_df = pd.read_csv("data/demand_large.csv")
costs_df = pd.read_csv("data/costs_large.csv")

print("costs_df")
print(costs_df)

print("costs_df.head(10)")
print(costs_df.head(10))

print("costs_df.tail(7)")
print(costs_df.tail(7))

print("costs_df['supplier']")
print(costs_df['supplier'])

print("costs_df[['supplier']]")
print(costs_df[['supplier']])

print("costs_df[['supplier', 'customer']]")
print(costs_df[['supplier', 'customer']])

print("costs_df.loc[0]")
print(costs_df.loc[0])

print("costs_df.loc[0, 'cost']")
print(costs_df.loc[0, 'cost'])

print("costs_df.loc[[0, 3], ['supplier', 'cost']]")
print(costs_df.loc[[0, 3], ['supplier', 'cost']])

print("costs_df.describe()")
print(costs_df.describe())

print("costs_df['cost'].describe()")
print(costs_df['cost'].describe())

print(costs_df['cost'].mean())
print("costs_df.mean()")

print("costs_df[costs_df['cost'] < 12]")
print(costs_df[costs_df['cost'] < 12])

print("costs_df[(costs_df['cost'] < 12) & (costs_df['supplier'] == 'S2')]")
print(costs_df[(costs_df['cost'] < 12) & (costs_df['supplier'] == 'S2')])

costs_dict = costs_df.set_index(["supplier", "customer"]).to_dict()["cost"]
supply_dict = supply_df.set_index("supplier").to_dict()["supply"]
demand_dict = demand_df.set_index("customer").to_dict()["demand"]

greedy_solve(supply_dict, demand_dict, costs_dict, verbose=True)


print(supply_df["supply"].sum())
print(demand_df["demand"].sum())