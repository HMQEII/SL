# digital signature

from itertools import count

p = int(input('Enter the value for p: '))
q = int(input('Enter the value for q: '))
n =p*q 
pyhn = (p-1) * (q-1)
e = int(input('Enter the value for e: '))
print('Public key: (',e,',',n,')')

for k in count(1):
    if (pyhn * k + 1) % e == 0:
        d = (pyhn * k + 1) // e
        print('Private key: (',d,',',n,')')
        break

# performing encryption
M = int(input('Enter the value for M: '))
S = pow(M,d,n)
# S= M % n
print('Digital Signature: ',S)

# performing decryption
DM = pow(S,e,n)

if DM == M:
    print('Message is decrypted')
    print('Signature was correct')
else:
    print('Incorrect Digital Signature')