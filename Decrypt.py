print ('Welcome!!')

import random
for i in range(1):
  keygen = (random.randint(11111111111, 999999999999999))

print ("")

message=input ('Enter Message You Want To Decrypt: ')
alphabet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
key = input("Encryption Key: ")
decrypt=''

for i in message:
  position=alphabet.find(i)
  newposition=(position+ -int(key) )%94
  decrypt+=alphabet [newposition]
output = (decrypt)
keyout = (keygen)

print ('Decrypted message: '+ (output) )
