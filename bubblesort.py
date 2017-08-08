import random

def bubble_sort(mylist):
    for i in range(len(mylist)):
        for j in range(len(mylist)-1-i):
            if mylist[i]>mylist[i+1]:
                mylist[i], mylist[i+1]=mylist[i+1],mylist[i]

alist = [3,2,5,6]
bubble_sort1(alist)
print(alist)
