def insertionSort(mylist):
    for i in range(1,len(mylist)):
        current=mylist[i]
        position=i
        while i>0 and mylist[i-1]>mylist[i]:
            mylist[i],mylist[i-1] = mylist[i-1], mylist[i]
            i-=1

a = [1,6,3,8.3,100,0]
insertionSort(a)
print(a)
