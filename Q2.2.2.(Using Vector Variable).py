#Q2.2.2 (Using Vector Variable)

#We want to formulize  F = Min (x1)**3 + (x2 - x3)**2 + (x3)**3 + 2 in CVPXY and solve it

import cvxpy as cp

# Create vector variable with shape 3.
x = cp.Variable(3)

# Create two constraints.
constraints =  [(x[1]) >= 0, (x[2]) >= 0]

# Form objective.
obj = cp.Minimize((x[0])**3 + (x[1] - x[2])**2 + (x[2])**3 + 2)

# Form and solve problem.
prob = cp.Problem(obj,constraints)
prob.solve() # Returns the optimal value.

print("The status of the problem is:", prob.status)
print("optimal value of minimization is:", prob.value)
print("optimal value of variable x1 is :", x.value)