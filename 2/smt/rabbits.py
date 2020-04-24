from z3 import *

r = Int("r")
p = Int("p")

s = Solver()

s.add(r+p==9)
s.add(r*4+p*2==24)
# TODO

print(s.check())
print(s.model())
