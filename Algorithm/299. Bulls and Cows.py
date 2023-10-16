class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b = 0
        c = 0
        
        '''
        # old way
        hashMap = Counter(secret)

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                b += 1
                hashMap[secret[i]] -= 1

        for i in range(len(guess)):
            if guess[i] in hashMap and guess[i] != secret[i] and hashMap[guess[i]] > 0:
                c += 1
                hashMap[guess[i]] -= 1
        '''

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                b += 1

        s = set(list(secret))
        for i in s:
            c += min(secret.count(i), guess.count(i))
        c -= b  


        return f'{b}A{c}B'