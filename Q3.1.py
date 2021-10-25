#Question 3.1 by Hamed Rahimi

# s= stream r= reservoir

# Goal is to minimizae Cost which is equal to 100R+50S

# S+R <= 100
# S<= 100
# ((50S+250R)/(S+R)) <= 100 which is equal to 150R-50S<=0


import cvxpy as cp
# Create two scalar optimization variables.
r = cp.Variable()
s = cp.Variable()

# Create constraints.

constraints = [r + s == 500,
               150*s-50*r <= 100,
               s <= 100]
# Form objective.
obj = cp.Minimize(100*r + 50*s)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve() # Returns the optimal value.


print("The status of the problem is:", prob.status)
print("optimal value of minimization is:", prob.value)
print("optimal value of stream is :", r.value)
print("optimal value of reservoir is :", s.value)

#############################