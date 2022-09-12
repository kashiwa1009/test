from re import A


def rot13():
    a=input("please enter the word:")
    word=[]
    for i in a.lower():
        if ord(i)+13>ord("z"):
            word.append(chr(ord(i)-13))
        word.append(chr(ord(i)+13))
    print(''.join(word))

rot13()
        