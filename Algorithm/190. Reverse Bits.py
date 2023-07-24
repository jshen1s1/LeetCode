class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x = bin(n)[2:] # to bin str
        x = x[::-1] + ('0'*(32-len(x))) # reverse + extra zeros
        return int(x, 2) # bin str to int