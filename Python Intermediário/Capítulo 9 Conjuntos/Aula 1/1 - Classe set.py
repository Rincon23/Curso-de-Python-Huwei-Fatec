c1 = {16,8,21,30,41,28}
print(c1)

c1 = {16,8,21,30,41,28,8}
print(c1)

c1 = {16,8,21,30,41,28,'8'}
print(c1)

c1 = {16,8,21,30,41,28,8.00}
print(c1)

c1 = {16,8,21,30,41,28,8.00001}
print(c1)

c2 = {}
print(type(c2))
c2 = set()
print(type(c2))

try:
    c4 = set(4,9,14,21)
except:
    print('Não se pode fazer o conjunto set dessa forma!')

c4 = set([4,5,6,2])
print(c4)
c4 = set((4,5,6,2))
print(c4)