from done_ex06 import decipher_freq

def main():
    substitution_07 = { 
            'E' : 'e',
            'C' : 'a',
            'T' : 'o',
            'W' : 't',
            'S' : 'h',
            'J' : 'g',

            'V' : 'i',
            'F' : 'n',
            'B' : 'w',
            'A' : 'd',
            'N' : 'r',
            'X' : 'c',
            'Z' : 'f',
            'P' : 's',
            'R' : 'p',
            'Q' : 'v',
            'K' : 'y',
            'G' : 'l',
            'Y' : 'q',
            'M' : 'u',
            'L' : 'm',
            'O' : 'b',
        }
    alphabet = ''
    remaining = ''
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if not c in substitution_07.keys():
            alphabet += c
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if not c in substitution_07.values():
            remaining += c
    text = input('text: ').upper()
    print()
    print(remaining)
    print()

    for (old, new) in substitution_07.items():
        text = text.replace(old, new)
    print(text)
    print()


    for (cc, key) in decipher_freq(text, ALPHABET = alphabet):
        if not cc == 0.0:
            print(key, ':', cc)



if __name__ == '__main__':
    main()

