c = set()
c.add(85)
c.add(190)
c.add(260)
c.add(89)
c.add('olá')
print(c)

c.clear()

print(c)

c = set()
c2 = c.copy()
print(id(c))
print(id(c2))

c = set()
c2 = c
print(id(c))
print(id(c2))

c1 = {26,32,45,58,63}
c2 = {19,34,58,67,82}

c3 = c1.difference(c2)

print(c3)

c1 = {26,32,45,58,63}
c2 = {19,34,58,67,82}

c1.difference_update(c2)

print(c1)

c1 = {26,32,45,58,63}
c1.discard(63)
print(c1)

c1 = {26,32,45,58,63}
c2 = {19,34,58,67,82}
c3 = c1.intersection(c2)
print(c3)

c1 = {26,32,45,58,63}
c2 = {19,34,58,67,82}
c1.intersection_update(c2)
print(c1)

