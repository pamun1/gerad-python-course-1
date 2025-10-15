from pyomo.environ import *
from data import read_from_csv

# Reading the data
supply_file = "data/supply_medium.csv"
demand_file = "data/demand_medium.csv"
costs_file = "data/costs_medium.csv"

supply = read_from_csv(supply_file, "supplier", "supply")
demand = read_from_csv(demand_file, "customer", "demand")
costs = read_from_csv(costs_file, ["supplier", "customer"], "cost")

# Pyomo
# Defining the model
model = ConcreteModel()

# Defining the sets
model.S = Set(initialize=supply.keys())
model.C = Set(initialize=demand.keys())

# Defining the variables
model.x = Var(model.S, model.C, domain=NonNegativeReals)

# Defining the objective function
model.obj = Objective(expr=sum(costs[(i,j)] for i in model.S for j in model.C), sense=minimize)

# Defining the constraints
model.sup_const = Constraint(
    model.S, 
    rule=lambda m, i: sum(m.x[i, j] 
                          for j in m.C) <= supply[i])

model.dem_const = Constraint(
    model.C, 
    rule=lambda m, j: sum(m.x[i, j] 
                          for i in m.S) >= demand[j]
)

# Configuring the solver
solver = SolverFactory("cbc")

# Solving the model
results = solver.solve(model, tee=True)

# Extracting the results with a dictionary comprehension
flows_opt = {(i, j): value(model.x[i, j]) 
             for i in model.S for j in model.C}

opt_cost = value(model.obj)

print(flows_opt)    
print(opt_cost)