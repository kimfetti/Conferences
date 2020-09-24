# Scaled It!
# Largest Prime Factor Solution
# Author: JJ


def is_prime(n):
    """
    Checks if input value is prime.
    Loops over all values smaller than input;
        returns False as soon as factor is found.
    """
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def largest_prime_factor(n):
    """
    Checks for largest prime factor of input number, n.
    Loops over all values smaller than n
    """
    for i in range(n,1,-1):
        if n%i==0:           #Check to see if i is a factor of n
            if is_prime(i):   #Check to see if i is prime
                return i

print(largest_prime_factor(15857333))