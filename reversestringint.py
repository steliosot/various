
k =['a','b','c']
l= [False for x in range(128)]

# for i,v in enumerate(k):
#     if l[v]:
#         print("double")
#     l[v]=True
#     print(i, v, l[i])

for i in k:
    val=ord(i)
    if l[val]:
        print("double")
    l[val]=True


x=2468
y=str(x)
z =int(y)

y[::-1] # reverse order of elements of string

int(str(x)[::-1]) # reverse an int

x=2442
x==int(str(x)[::-1]) # palindrome of a number

a =['a','b','c']
a[::-1]
a.reverse() # in place 
k=reversed(a)
