# Diffie Hellman

q = int(input('Enter the value of q: '))
g = int(input('Enter the value of ∝: '))
A = int(input('Enter the key component of A: '))
B = int(input('Enter the key component of B: '))

# Ket generation 
A_Key = pow(g,A,q)
B_Key = pow(g,B,q)

print('Key for A: ',A_Key)
print('Key for B: ',B_Key)


# generation of secret key
A_SKey = pow(B_Key,A,q)
B_SKey = pow(A_Key,B,q)

print('Secret Key for A: ',A_SKey)
print('Secret Key for B: ',B_SKey)