import random

def game():
    answer=0
    while True:
        right=random.randint(1,31)
        print(right)
        a=input("please enter five integer :")
        if a=='':
             break 
        try:
            answer=int(a[0])*16+int(a[1])*8+int(a[2])*4+int(a[3])*2+int(a[4])*1
        except Exception as e :
            print("error",e)
        if answer==right:
            print("right answer!!")
        else: 
            print("false!")

game()