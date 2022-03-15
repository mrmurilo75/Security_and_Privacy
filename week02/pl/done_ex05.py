from done_ex02 import decipher_all


def main():
    input_05 = {
            'gryy gurz gb tb gb nzoebfr puncry' : 'chapel',
            'wziv kyv jyfk nyve kyv tpdsrcj tirjy' : 'cymbal',
            'baeeq klwosjl osk s esf ozg cfwo lgg emuz.' : '',
        }
#    text = input('cipher: ')
#    keyword = input('keyword: ')
    print()
    for (text, keyword) in input_05.items():
        print()
        for (key, text) in decipher_all(text, keyword).items():
            print(key, ':', text)


if __name__ == '__main__':
    main()

