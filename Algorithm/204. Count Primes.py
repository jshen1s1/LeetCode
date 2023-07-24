class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False

        # the smallest factor of a non-prime numer will not be > sqrt(n)
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for multiples in range(i*i, n, i):
                    # change indexes of all multiples of found prime 
                    primes[multiples] = False

        return sum(primes)