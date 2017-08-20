def findRepeated(l):
    for i in range(len(l)):
        #print(i)
        index=l[i]%n
        l[index]+=n

    for i,v in enumerate(l):
        print(l[i]/n)
        if l[i]/n>2:
            yield i

print([x for x in findRepeated(l)])
