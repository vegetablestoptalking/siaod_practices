from z3 import *

s = Solver()

sq = IntVector("x", 9)


for x in sq:
    s.add(x > -100)

n = Int("n")
s.add(n == 42)

n = 15

s.add(Sum([sq[0], sq[1], sq[2]])==n)
s.add(Sum([sq[3], sq[4], sq[5]])==n)
s.add(Sum([sq[6], sq[7], sq[8]])==n)
s.add(Sum([sq[0], sq[4], sq[8]])==n)
s.add(Sum([sq[2], sq[4], sq[6]])==n)
s.add(Sum([sq[0], sq[3], sq[6]])==n)
s.add(Sum([sq[1], sq[4], sq[7]])==n)
s.add(Sum([sq[2], sq[5], sq[8]])==n)
s.add(Distinct(sq))
s.add(sq[0]!=6)
# TODO

print(s.check())
m = s.model()

for i in range(9):
    if i % 3 == 0:
        print()
    print(m.eval(sq[i]).as_long(), end=" ")
