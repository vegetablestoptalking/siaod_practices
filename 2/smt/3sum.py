from z3 import *

s = Solver()

m = 3
nums = [-1, 6, 8, 9, 10, -100, 78, 0, 1]
n = len(nums)

xs = IntVector("x", n)
xl = IntVector("xx", n)
for x in xs:
    s.add(Or(x == 0, x == 1))

s.add(Sum(xs)==3)
for i in range(n):
    s.add(xs[i]*nums[i])

print(s.check())
m = s.model()
for i in range(n):
    if m.eval(xs[i]).as_long() != 0:
        print(nums[i])
