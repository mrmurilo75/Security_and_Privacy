ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def decipher_freq(ciphertext):
    # setup
    txt_len = 0
    count = {}
    for ch in ALPHABET:
        count |= { ch : 0 }

    # compute histogram
    for c in ciphertext:
        if c in ALPHABET:
            count[c] += 1
            txt_len += 1

    result = sorted(( (cc/txt_len, key) for (key, cc)  in count.items() ), reverse = True)
    return result


def main():
    text = input('text: ')
    print()
    for (cc, key) in decipher_freq(text):
        print(key, ':', cc)



if __name__ == '__main__':
    main()

