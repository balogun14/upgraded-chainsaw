#Euclid's Algorithm



def gcd(a,b):
    """
    Find the greatest denominator using Euclid's algorithm
    """
    while (b != 0):
        t = a
        a = b
        b = t%b
        
    return a



print(gcd(60,96))
print(gcd(20,8))