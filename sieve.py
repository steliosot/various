def sieve(n):
    not_prime = []
    for i in range(2, n+1):
        if i not in not_prime:
            for j in range(i*i, n+1, i):
                print(j)
                not_prime.append(j)
                
sieve(5)
