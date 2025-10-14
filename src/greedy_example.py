from greedy import greedy_solve


costs = {("S1", "C1"): 5, ("S1", "C2"): 7, 
        ("S2", "C1"): 4, ("S2", "C2"): 6}
sup = {"S1": 10, "S2": 20}
dem = {"C1": 18, "C2": 12}

sol, rem_sup, rem_dem = greedy_solve(sup, dem, costs, verbose=True)

print(f"Shipment plan: {sol}")
print(f"Remaining supply: {rem_sup}")
print(f"Remaining demand: {rem_dem}")
print(f"Initial supply: {sup}")
print(f"Initial demand: {dem}")
