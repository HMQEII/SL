text = input('Enter thy text: ')
key = int(input('Enter key value: '))

char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ntext = text.upper()
print(ntext)
enc=''
for c in ntext:
    if c == ' ':
        enc += ' '
    else:
        # print(c)
        textvalue = char.index(c)
        encvalue = (textvalue + key)%26
        enc = enc + char[encvalue]

print('\nEncrypted value : ')
print(enc, end='')

dec=''

for c in enc:
    if c == ' ':
        dec += ' '
    else:
        # print(c)
        textvalue = char.index(c)
        decvalue = (textvalue - key)%26
        dec = dec + char[decvalue]

print('\nDecrypted value : ')
print(dec, end='')