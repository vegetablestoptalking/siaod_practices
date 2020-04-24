from z3 import *

s = Solver()

names = "WA NT SA Q NSW V T".split()
WA, NT, SA, Q, NSW, V, T = range(7)
land = IntVector("land", 7)

for x in land:
    s.add(x >= 0, x <= 2)

# TODO

print(s.check())
m = s.model()
for i in range(7):
    print(names[i], m.eval(land[i]).as_long())

