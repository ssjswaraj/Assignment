#to check if given no is prime or not


def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:        
        return True
    
# n=int(input("enter the number to bechecked for prime"))

import sys 
print(sys.argv,type(sys.argv))
n=int(sys.argv[1])


if isprime(n)==True:
    print("prime no")
else:
    print("not a prime no")