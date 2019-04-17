def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number for GCD:"))
b=int(input("Enter second number for GCD:"))
GCD=gcd(a,b)
print("GCD is: ")
print(GCD)
