def isPrime(num):
    for i in range(2,num):
        #print(i)
        if num%i==0:
            return False
    return True

def listprimes(num):
    for i in range(2,num):
        if isPrime(i):
            print(i)

listprimes(200)
