c1 = {34,17,50,82,88}

v = c1.pop()

print(v)
print(c1)

c1 = {34,17,50,82,88}
c1.remove(50)

print(c1)

c1 = {34,17,50,82,88}

print(50 in c1)
print(999 in c1)

c1 = {34,17,50,82,88}
c2 = {34,67,82,19,63}

u = c1.union(c2)

print(u)

c1 = {34,17,50,82,88}
c2 = {34,67,82,19,63}

s = c1.symmetric_difference(c2)

print(s)

c1 = {34,17,50,82,88}
c2 = {34,67,82,19,63}

c1.symmetric_difference_update(c2)
print(c1)

c1 = {34,17,50,82,88}
c2 = {34,67,82,19,63}
c1.update(c2)

print(c1)