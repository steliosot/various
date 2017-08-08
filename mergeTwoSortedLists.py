
def merge1(mylist1,mylist2):
    i,j,len1,len2=0,0,len(mylist1),len(mylist2)
    while(i<len1 and j<len2):
        if(mylist1[i]<mylist2[j]):
            yield mylist1[i]
            i+=1
        else:
            yield mylist2[j]
            j+=1
        if(i==len1):
            while(j<len2):
                yield mylist2[j]
                j+=1
        elif(j==len2):
            while(i<len1):
                yield mylist1[i]
                i+=1
l1=[1,3,6,8,9]
l2=[0,4,5,8]
m=(i for i in merge1(l1,l2))
print(*m)
