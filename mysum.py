# def mysum(*args):
#     if mysum:
#          for i in args:
#              sum+=i
#          print(sum)
#     else :
#         print(mysum())

# mysum()
# -------------------------------

def mysum(*args):
    if not args:
        return args
    output=args[0]
    for args in args[1:]:
        output+=args
    return output

print(mysum())