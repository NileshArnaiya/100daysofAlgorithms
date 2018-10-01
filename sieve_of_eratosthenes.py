"""Sift the Two's and Sift the Three's,
The Sieve of Eratosthenes.
When the multiples sublime,
The numbers that remain are Prime."""

# Wrote a blog on this algorithm - https://iq.opengenus.org/the-sieve-of-eratosthenes/

def get_primes(n):

    if n<=0:
        raise ValueError("Please enter a positive integer")
    
    sieve_size = n//2-1 if n%2==0 else n//2

    sieve = [True for _ in range(sieve_size)]
    
    primes = []

    if n>=2:
        primes.append(2)

    for i in range(sieve_size):
        if sieve[i]:
            value_at_i = i*2 + 3
            primes.append(value_at_i)
            for j in range(i,sieve_size,value_at_i):
                sieve[j] = False

    return primes
    
print(get_primes(30))
