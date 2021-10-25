#Q2.3

import cvxpy as cp

# Create two variables and one parameter.
x = cp.Variable()
y = cp.Variable()
t = cp.Parameter(nonneg=True, value=1)

# no constraints.
constraints = None 

sqr=cp.square(x-2)
log=cp.log(-4+x+y)
log=log/t

F= sqr  + (3*y)  - log

# Form objective
obj = cp.Minimize(F)
# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve() # Returns the optimal value.

new_v=prob.value
old_v=6


print("it takes few sec to find best value of t")


while(new_v<old_v): # it tries to increase t to find the optimal t
  t.value=t.value+100
  sqr=cp.square(x-2)
  log=cp.log(-4+x+y)
  log=log/t
  F= sqr  + (3*y)  - log
# Form objective
  obj = cp.Minimize(F)
# Form and solve problem.
  prob = cp.Problem(obj, constraints)
  prob.solve() # Returns the optimal value.
  old_v=new_v
  new_v=prob.value

print("optimal value of t is:", t.value)
print("The status of the problem is:", prob.status)
print("optimal value of minimization is:", prob.value)
print("optimal value of variable x is :", x.value)
print("optimal value of variable y is :", y.value) 