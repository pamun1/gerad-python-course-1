## ===============================
## Getting started
## ===============================

# Strings
print("Hello, World!")
print('Hello, World!')
print("That's fine")

# Arithmetic
print(2 + 3)
print(34 - 12)
print(3 * 4)
print(10 / 2)
print(3 ** 2)


## ===============================
## Variable assignment
## ===============================

# Suppliers
s1 = 10
s2 = 20

# Customers
c1 = 18
c2 = 12

# Cost matrix
s1_c1 = 5
s1_c2 = 7
s2_c1 = 4
s2_c2 = 6

# Print variables
print(s1)
print(c1, c2)
print(s1, c2, s1_c2)

# f-strings
print(f"s1: {s1}, s2: {s2}")

# The type function
print(type(23.54))
print(type("Customer"))
print(type(s1))


## ===============================
## Lists
## ===============================

mixed = [1, "hello", 3.14, [2, 3]]
			
print(mixed[0])    # First element
print(mixed[-1])   # Last element
print(mixed[1:3])  # Slice from index 1 up to 3

# Functions on lists
suppliers = [10, 20]
customers = [18, 12]

print(len(suppliers))
print(sorted(customers))
print(customers)
print(sum(suppliers))
print(min(customers))
print(max(customers))


## ===============================
## Methods
## ===============================

# String methods
my_string = "hello world"
print(my_string.upper())
print(my_string.replace("o", "0"))
print(my_string.split())

# List methods
lst = [10, 20, 30]
			
lst.append(40)
lst.insert(1, 15)
lst.pop()
lst.remove(15)
lst.extend([50, 60])
lst.sort()
lst.reverse()
lst[0] = 99

print(lst)


## ===============================
## Mutability
## ===============================

# Mutable example (list)
mixed = [1, "hello", 3.14, [2, 3]]
mixed[0] = 42
mixed.pop()
print(mixed)

# Immutable example (str)
s = "hello"
# s[0] = "H" # This would raise an error
s = "Hello" # A new string object is assigned to s

# Immutable example (int)
x = 10
x = x + 5 # A new int object is assigned to x


## ===============================
## Dictionaries
## ===============================

supply_by_sup = {"S1": 10, "S2": 20}
demand_by_cust = {"C1": 18, "C2": 12}

print(supply_by_sup["S2"])
print(demand_by_cust["C1"])
print(len(supply_by_sup))

cost_by_sup_cust = {
				("S1", "C1"): 5,
				("S1", "C2"): 7,
				("S2", "C1"): 4,
				("S2", "C2"): 6
			}
			
print(cost_by_sup_cust[("S1", "C2")])
print(cost_by_sup_cust[("S2", "C1")])
print(len(cost_by_sup_cust))

# Dictionary methods
print(supply_by_sup.keys())
print(demand_by_cust.values())
print(cost_by_sup_cust.items())

print(supply_by_sup.get("S3", 0))
print(demand_by_cust.pop("C2"))

# Dictionary views vs lists
print(list(supply_by_sup.keys()))
print(list(demand_by_cust.values()))
print(list(cost_by_sup_cust.items()))
