from done_ex01 import cipher
from done_ex02 import decipher


def main():
    input_03 = {
            6 : 'Get me a vanilla ice cream, make it a double.',
            15 : "I don't much care for Leonard Cohen.",
            16 : "I like root beer floats.",
        }
    input_04 = {
            12 : "nduzs ftq buzq oazqe",
            3 : "fdhvdu qhhgv wr orvh zhljkw.",
            20 : "ufgihxm uly numnys.",
        }
#    text = input('cipher: ')
#    keyword = input('keyword: ')
    print()
    for (key, text) in input_03.items():
        print(key, ':', cipher(key, text))
    for (key, text) in input_04.items():
        print(key, ':', decipher(key, text))


if __name__ == '__main__':
    main()

