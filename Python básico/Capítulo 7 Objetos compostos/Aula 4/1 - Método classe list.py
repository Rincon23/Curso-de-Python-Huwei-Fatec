l = []

l.append(81)
l.append(17)
l.append(49)
l.append(53)
print('1º',l)

l.clear()

print('2º',l)

l = [81,17,49,53]
a = l
b = l.copy()

print(id(l))
print(id(a))
print(id(b))

print(l.count(81))

l = [81,17,49,53]
l2 = [1,2,3,4]

l.extend(l2)
print(l)

l = [81,17,49,53]

print(l.index(17))
#print(l.index(300)) ValueError: 300 is not in list
print(300 in l)
print(81 in l)

l = [81,17,49,53,17]
print(l.index(17))
print(l.index(17,2))
print(l.index(17,l.index(17)+1))

l = [81,17,49,53]
l.insert(1, 195)
l.insert(30,100)
print(l)

l = [81,17,49,53]
a = l.pop(0)
print(l)
print(a)

l = [81,17,49,53]
del l[0]
l.remove(53)
print(l)

l = [2,81,195,17,49,81,1,2,3,4,35]
l.reverse()
print(l)

l = [2,81,195,17,49,81,1,2,3,4,35]
l.sort()
print(l)

l = [2,81,195,17,49,81,1,2,3,4,35]
l.sort(reverse=True)
print(l)