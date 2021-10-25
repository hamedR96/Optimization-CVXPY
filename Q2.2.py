#Q2.2

#We want to formulize  F = Min (x1)**3 + (x2 - x3)**2 + (x3)**3 + 2 in CVPXY and solve it

import cvxpy as cp

# Create three variables.
x1 = cp.Variable()
x2 = cp.Variable()
x3 = cp.Variable()

# Create two constraints.
constraints =  [x1 >= 0, x3 >= 0]

# Form objective.
obj = cp.Minimize((x1)**3 + (x2 - x3)**2 + (x3)**3 + 2)

# Form and solve problem.
prob = cp.Problem(obj,constraints)
prob.solve() # Returns the optimal value.

print("The status of the problem is:", prob.status)
print("optimal value of minimization is:", prob.value)
print("optimal value of variable x1 is :", x1.value)
print("optimal value of variable x2 is :", x2.value)
print("optimal value of variable x3 is :", x3.value)


