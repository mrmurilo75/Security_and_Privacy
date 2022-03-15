
def decipher(key, text):
    ORD_a = ord('a')
    ORD_A = ord('A')
    ORD_z = ord('z')
    ORD_Z = ord('Z')

    decipher = ''

    for c in text:
        oc = ord(c)
        if oc >= ORD_a and oc <= ORD_z:
            decipher += chr(oc - key - ( (-ORD_z +ORD_a-1) if oc - key < ORD_a else 0))
        elif oc >= ORD_A and oc <= ORD_Z:
            decipher += chr(oc - key - ( (-ORD_Z +ORD_A-1) if oc - key < ORD_A else 0))
        else:
            decipher += c

    return decipher

def decipher_all(text, keyword=''):
    deciphered = {}
    result = {}

    for key in range(26):
        deciphered |= {key : decipher(key, text)}

    for (key, ciph) in deciphered.items():
        if keyword in ciph:
            result |= { key : ciph }
    return result

def main():
    text = input('cipher: ')
    keyword = input('keyword: ')
    print()
    for (key, text) in decipher_all(text, keyword).items():
        print(key, ':', text)


if __name__ == '__main__':
    main()

