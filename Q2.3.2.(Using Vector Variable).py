#Q2.3.2 (Using Vector Variable)

import cvxpy as cp

# Create vector with two shape and one parameter.
x = cp.Variable(2)
t = cp.Parameter(nonneg=True, value=1)

# no constraints.
constraints = None 

sqr=cp.square(x[0]-2)
log=cp.log(-4+x[0]+x[1])
log=log/t

F= sqr  + (3*x[1])  - log

# Form objective
obj = cp.Minimize(cp.sum(F))
# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve() # Returns the optimal value.

new_v=prob.value
old_v=6


print("it takes few secs to find the best value of t")


while(new_v<old_v): # it tries to increase t to find the optimal t
  t.value=t.value+100
  sqr=cp.square(x[0]-2)
  log=cp.log(-4+x[0]+x[1])
  log=log/t
  F= sqr  + (3*x[1])  - log
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
