c1 = {34,17,50,82,88}
c2 = {34,67,82,19,63}
print(c1.isdisjoint(c2))

c1.discard(34)
c1.discard(82)

print(c1.isdisjoint(c2))
print()

c1 = {34,17,50,82,88}
c2 = {34,67,82,19,63}
print(c1.issubset(c2))

c1 = {34,82}
c2 = {34,67,82,19,63}
print(c1.issubset(c2))

print()

c1 = {34,82}
c2 = {34,67,82,19,63}
print(c2.issuperset(c1))



