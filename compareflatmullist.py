from functools import reduce
import operator
import random
import time

l = [[x for x in range(1,random.randrange(800,1000))] for x in range(1,random.randrange(800,1000))]

methods = dict()
def addToDict(name, score):
    methods[name] = score

start = time.time()
reduce(lambda x,y: x+y,l)
addToDict("lambda",round(time.time()-start,4))

start = time.time()
sum(l, [])
addToDict("sum",round(time.time()-start,4))

start = time.time()
[item for sublist in l for item in sublist]
addToDict("compr",round(time.time()-start,4))

start = time.time()
reduce(operator.concat, l)
addToDict("operator.concat",round(time.time()-start,4))

print(methods)

# {'lambda': 3.9837, 'sum': 3.9457, 'compr': 0.0305, 'operator.concat': 3.9574}
