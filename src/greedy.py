def get_cost(cost_tuple):

    cost = cost_tuple[1]

    return cost

def greedy_solve(supply_by_sup, demand_by_cust, cost_by_sup_cust, verbose=False):

    flow_by_sup_cust = {}

    # Copy the dictionaries to prevent their modification
    rem_supply_by_sup = supply_by_sup.copy()
    rem_demand_by_cust = demand_by_cust.copy()

    sorted_costs = sorted(cost_by_sup_cust.items(), key=get_cost)

    # A lambda expression could also be used:
    # sorted_costs = sorted(cost_by_sup_cust.items(), key=lambda x: x[1])

    for (s, c), cost in sorted_costs:

        supply = rem_supply_by_sup[s]
        demand = rem_demand_by_cust[c]

        if supply > demand:
            quantity = demand
        elif supply < demand:
            quantity = supply
        else:
            quantity = supply  # or demand

        flow_by_sup_cust[(s, c)] = quantity
        
        rem_supply_by_sup[s] -= quantity
        rem_demand_by_cust[c] -= quantity

    if verbose:
        print(f"Shipment plan: {flow_by_sup_cust}")
        print(f"Remaining supply: {rem_supply_by_sup}")
        print(f"Remaining demand: {rem_demand_by_cust}")

    return flow_by_sup_cust, rem_supply_by_sup,\
        rem_demand_by_cust