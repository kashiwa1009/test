
# def hex_to_num():
#     a=reversed(input(" please enter the hex:"))
#     count=0
#     sum_num=[] 
#     for i in a:
#         if i.isdigit()==True:
#              answer=int(i)*(16**count)
#              count+=1
#              sum_num.append(answer)
#         else:
#              answer=(ord(i)-55)*(16**count)
#              count+=1 
#              sum_num.append(answer)
#     print(sum(sum_num))

# hex_to_num()

def hex_to_dec():
    hexnum=input("輸入十六進位數字:")
    decnum=0

    for power,digit in enumerate(reversed(hexnum)):
        if digit.isdigit():
            digit_num=int(digit)
        else:
            digit_num=ord(digit.upper())-ord("A")+10 
        decum+=digit_num*(16**power)
    print("十進位數字結果:",decnum)

hex_to_dec()


