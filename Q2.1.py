# Q2.1 
# We want to formulize  Min (x1-4)^2+7*(x2-4)^2+4*x2 in CVPXY and solve it

import cvxpy as cp

# we reate two variables for x1 and x2.
x1 =cp.Variable()
x2 =cp.Variable()

# There is no constrain so:
constraints = None

# we formulate our problem.
F=(x1 - 4)**2+ 7*((x2 - 4)**2) + 4*x2

#we define our objectvie funtion
obj = cp.Minimize(F)

# insert Cons and Obj in cvxpy to solve the problem.
prob = cp.Problem(obj, constraints)
prob.solve() # Returns the optimal value.

print("The status of the problem is:", prob.status)
print("optimal value of minimization is:", prob.value)
print("optimal value of variable x1 is :", x1.value)
print("optimal value of variable x2 is :", x2.value)