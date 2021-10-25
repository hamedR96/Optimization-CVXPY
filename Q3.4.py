# Question 3.4 by Hamed Rahimi

#The factory RadioIn builds two types of radios A and B. 
#Every radio is produced by the work of three specialists Pierre, Paul and Jacques. 
#Pierre works at most 24 hours per week. Paul works at most 45 hours per week. 
#Jacques works at most 30 hours per week.
#The resources necessary to build each type of radio and their selling prices as well are given in the following table:
#Radio A Radio B
#Pierre 1h 2h
#Paul 2h 1h
#Jacques 1h 3h
#Selling prices 15 euros 10 euros

#We assume that the company has no problem to sell its production, whichever it is.
#a) Model the problem of finding a weekly production plan maximizing the revenue of RadioIn as a linear programme. 
#Write precisely what are the decision variables, the objective function and the constraints.
#b) Solve the linear programme using the geometric method and give the optimal production plan.

import cvxpy as cp
# Create two variables.
A = cp.Variable()
B = cp.Variable()

# Create three constraints.
constraints = [A+2*B<=24, 2*A+B<=45, A+3*B<=30]

# Form objective.
obj = cp.Maximize(15*A+10*B)

# Form and solve problem.
prob = cp.Problem(obj, constraints)

prob.solve() # Returns the optimal value.

print("The status of the problem is:", prob.status)
print("optimal value of maximization is:", prob.value)
print("optimal value of variable A is :", A.value)
print("optimal value of variable B is :", B.value)
