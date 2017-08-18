# lambda


d=lambda x:2*x
mx = lambda x,y: x if x>y else y

print(d(2))

print(list(map(lambda x:x**2,[1,2,3,4])))
[x**2 for x in [1,2,3,4]]

print(list(filter(lambda x:x%2==0, [1,2,3,4])))
print([x for x in [1,2,3,4] if x%2==0])

from functools import reduce
print(reduce(lambda x,y:x*y,[1,2,3,4]))

# Generators: better in performance

def square_nums(nums):
    for i in nums:
        yield i**2

m=[1,2,3,4]
nums = square_nums(m)

for i in nums:
    print(i)


m=(x**2 for x in [1,2,3,4,5]) # list comprehension as  a generator
print(next(m))
print(next(m))
