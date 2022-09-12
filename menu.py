a={"a":83,
   "b":93,
   "c":90
}

def menu():
     sum=0
     while True:
         m=input("please enter what you want:")
         if m=='':
             break
         elif m not in a:
             print("not in")
         else:
             sum+=a[m]
     return(sum)

print(menu())