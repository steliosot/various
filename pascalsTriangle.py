def pt(n):
    res=[]
    for x in range(n):
        l=len(res)
        res=[1 if i==0 or i==len(res) else res[i-1]+res[i] for i in range(len(res)+1)]
        yield res

print(list(pt(10)))
