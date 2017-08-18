
# list -> general purpose, grow and shrink as you go, sortable, sequence type
# Tuple -> Immutable, good for fixed data, faster than lists, sequence type
# Set -> No dups, very fast comparing to lists, math operations( union, intersect, difference), Unordered
# Dict -> key value pair, unordered


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

# lists are mutable, tuples are immutable
#
# mytuple = ('a','b','c')
# # no append, remove, pop etc.
#
# print(mytuple)
#
# myset = {'a','b','c','a'}
#
# print('a' in myset) # more optimized
#
# set1 = {1,2,3,4,5}
# set2 = {1,3,5,100}
#
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.union(set2))
#
# # Create an empty list
# s=[], s=list()
# t=(), t=tuple()
# s=set()

dict={1:'a',2:'b'}
fot k,v in dict:
    print(k,v)
dict.values()
dict.keys()
dict.items()


