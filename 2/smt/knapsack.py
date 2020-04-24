from z3 import *

s = Optimize()

price = [90, 760, 299, 190, 80, 1500, 150]
weight = [2000, 400, 470, 300, 150, 560, 1000]
capacity = 1500

knapsack = IntVector("k", len(price))
for x in knapsack:
  s.add(Or(x == 0, x == 1))

# TODO

print(s.check())
m = s.model()
for i in range(len(price)):
    if m.eval(knapsack[i]).as_long() == 1:
        print(price[i], weight[i])
