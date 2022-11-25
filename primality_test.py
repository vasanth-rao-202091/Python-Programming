#Program for Primality test using fermat method
#function to calculate Power 
def power(b,n):
    if n==0:
        return 1
    x=power(b,n//2)
    if n%2==0:
        return x*x
    if n%2==1:
        return b*x*x 
#func to check is_prime
def test_prime(n):
    m = n-1
    for b in range(2,n-1):
        e = power(b,m)
        if e%n!=1:
            return False
    return True
num = int(input("Enter a Number: "))
if test_prime(num):
    print(f"{num}is a prime number")
else:
    print(f"{num}is not a prime")
