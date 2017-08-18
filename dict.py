mydict = {'a':1,'b':2,'c':[3,4]}
print(mydict)

mydict['a']=100
mydict.update({'a':1,'b':2,'c':[3,4,6]})

del mydict['a']
last=mydict.pop('b')
print(mydict.keys())
print(mydict.values())
print(mydict.items())

for k,v in mydict.items():
    print(k,v)

for i,v in enumerate(mydict):
    print(v,mydict.get(v))
