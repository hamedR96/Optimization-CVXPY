# Q2.1.2 (Using Vector Variable)
# We want to formulize  Min (x1-4)^2+7*(x2-4)^2+4*x2 in CVPXY and solve it

import cvxpy as cp

# we reate two Vectors with shape 2.
x =cp.Variable(2)

# There is no constrain so:
constraints = None

# we formulate our problem.
F=(x[0] - 4)**2+ 7*((x[1] - 4)**2) + 4*x[1]

#we define our objectvie funtion
#wrap up the vectors we use cp.sum
obj = cp.Minimize(cp.sum(F))

# insert Cons and Obj in cvxpy to solve the problem.
prob = cp.Problem(obj, constraints)
prob.solve() # Returns the optimal value.
print("The status of the problem is:", prob.status)
print("optimal value of minimization is:", prob.value)
print("optimal value of variable x is :", x.value)
