#Question 3.3 by Hamed Rahimi

# r= rural u= urban Bu= profit of urban Br= profit of rural

# Goal is to maximizae net profit which is equal to Bu+Br-r-u

# r+u = 200


import cvxpy as cp

# Create two variables.
r = cp.Variable()
u = cp.Variable()

Bu= 5000*cp.atoms.elementwise.log1p.log1p(u)
Br= 7000*cp.atoms.elementwise.log1p.log1p(r)

# Create constraints.
constraints = [r + u == 200]

# Form objective.
obj = cp.Maximize(Bu+Br-r-u)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve() # Returns the optimal value.

print("The status of the problem is:", prob.status)
print("optimal value of maximization is:", prob.value)
print("optimal value of variable rural is :", r.value)
print("optimal value of variable urban is :", u.value)

#############################