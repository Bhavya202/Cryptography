print('Welcome')

message=input ('Enter Message You Want To Encrypt: ')
alphabet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
key = input("Enter Encryption key(Int): ")
encrypt =''

for i in message:
  position=alphabet.find(i)
  newposition=(position+ int(key) )%94
  encrypt+=alphabet [newposition]
output = (encrypt)

print ('Encrypted Message: '+ (output) )
print ('Encryption Key: '+ (key) )