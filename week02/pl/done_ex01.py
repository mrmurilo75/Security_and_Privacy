# 1 - Implement encryption/decryption functions that
# take a key (as an integer in 0, 1,2, . . . , 25)
# and a string to operate as a Caesar cipher. 
# The function should only operate on the characters ‘a’, ‘b’, . . . ‘z’ (both upper and lower case),
# and it should leave any other characters, unchanged.

ORD_a = ord('a')
ORD_A = ord('A')
ORD_z = ord('z')
ORD_Z = ord('Z')

key  = int(input('key : '))
text = input('text: ')
cipher = ''

for c in text:
#    print(c)
    oc = ord(c)
#    print(oc)
    if oc >= ORD_a and oc <= ORD_z:
        cipher += chr(oc + key + ( (-ORD_z +ORD_a-1) if (oc + key > ORD_z) else 0))
    elif oc >= ORD_A and oc <= ORD_Z:
        cipher += chr(oc + key + ( (-ORD_Z +ORD_A-1) if oc + key > ORD_Z else 0))
    else:
        cipher += c

print(cipher)

