#Question 3.2 by Hamed Rahimi

import cvxpy as cp

# Create two scalar optimization variables.
b1 = cp.Variable()
b2 = cp.Variable()
b3 = cp.Variable()
b4 = cp.Variable()

# Create two constraints.
constraints = [((0.35*b1)+(0.6*b2)+(0.35*b3)+(0.4*b4)) <= 0.5,
               ((0.15*b1)+(0.05*b2)+(0.2*b3)+(0.1*b4)) >= 0.08,
               ((0.15*b1)+(0.05*b2)+(0.2*b3)+(0.1*b4)) <= 0.13,
               ((0.3*b1)+(0.2*b2)+(0.4*b3)+(0.2*b4)) <= 0.35,
               ((0.2*b1)+(0.15*b2)+(0.05*b3)+(0.3*b4)) >= 0.19,
               b1 >= 0.1, b1 <= 0.25, b2 >= 0.05, b2 <= 0.2, b3 >= 0.3,
               b1+b2+b3+b4 == 1]

# Form objective.
obj = cp.Minimize((55*b1) + (65*b2) + (35*b3) + (85*b4)) # Declare objective function

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()


print("The status of the problem is:", prob.status)
print("optimal value of minimization is:", prob.value)
print("optimal value of variable b1 is :", b1.value)
print("optimal value of variable b2 is :", b2.value)
print("optimal value of variable b3 is :", b3.value)
print("optimal value of variable b4 is :", b4.value)