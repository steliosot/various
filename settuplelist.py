# Lists

l = [1,2,3,4,5]

l.append(6)
l.insert(0,0)
l.extend([7,8,9])

l.remove(1)
l.pop()
l.pop(5) # at index

l.reverse()
l.sort()
k=sorted(l)
l.sort(reverse=True)

for i in l:
    print(i)

for i,v in enumerate(l):
    print(i, v)

for i in enumerate(l):
    print(i)

l=[[i,v] for i,v in enumerate(l)]

l = [1,2,3,4,5]
print("-".join([str(x) for x in l]))
print(l)
str = "test test test"

print("%20".join(str.split()))


l= [1,2,3,4,4,5,6,7]
print(tuple(l))

s=set(l)
print(s)
ns=set()
for i,v in enumerate(l):
    ns.add(v)

print("ns:",ns)
nl=[]
l= [1,2,3,4,4,5,6,7]
[nl.append(x) for x in l if not x in nl]
print(nl)

from collections import OrderedDict
print(list(OrderedDict.fromkeys('abracadabra')))

from iteration_utilities import unique_everseen
lst = [1,1,1,2,3,2,2,2,1,3,4]
list(unique_everseen(lst))
