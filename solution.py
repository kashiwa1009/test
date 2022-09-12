import random

def gussword():
     a=random.randint(1,99)         
     while True:
         b=int(input("please enter the first integer:"))
         if a==b:
             print("right answer")
             break
         elif b>a:
             print("smaller")
         else :
             print("bigger")

gussword()