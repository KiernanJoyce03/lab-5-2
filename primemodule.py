def is_prime(N):
    for i in range (2,N):
        if N % i == 0:
            return False
    return True
def print_prime(N):
    for i in range (N):
        isPrime = True
        for j in range(2,i):
            if N % j == 0:
                isPrime = False
        
        if isPrime == True:
            print (i, end = " ")        

def get_primes(N):
    lst = []
    for i in range (N):
        isPrime = True
        
        for j in range (2,i):
            if N % j == 0:
                isPrime=False
        if isPrime == True:
            lst.append(i)
    
    return lst