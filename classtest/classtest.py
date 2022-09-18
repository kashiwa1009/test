#自己定義資料型態
#資料型態:int,folat,boolen,string,list,touple....

#定義手機的話

class phone:  #模板
    def __init__(self,os,number,is_waterproof): #self object的本身
        self.os=os
        self.number=number   # 屬性number  值 number
        self.is_waterproof=is_waterproof
     
    def output():
        print("nice")


phone1=phone("ios",123,True) #存到變數phone1 <- 物件object 
#串建一個手機資料 

phone2=phone("aaa",3423,False)
phone2=phone.output()


print(phone1.number)   # . <-取得屬性








