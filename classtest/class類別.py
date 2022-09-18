#  封裝變數或函式
#封裝的變數或函式，統稱類別的屬性


#定義(建立)類別，才能使用類別中封裝的屬性

class test:
    x=3
    def say():
         print("hello")

print(test.x)

test.say()

#沒有創造實例


class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
             print("not supported")
        print("read from",src)
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")





