#資料型態

#定義自己的資料型態



class scoop:
    def __init__(self,flavor):
        self.flavor=flavor  #定義一個flavor的屬性
        #宣告，動態建立屬性


class scoop_maker:
    def create(self,flavors):
        return [scoop(flavor) for flavor in flavors]
        


class aaa:
    def __init__(self,abc):
        self.abc=abc

a=aaa("good")
print(a.abc)






# scoop_maker=scoop_maker() # 產生scoop_maker物件
# #可呼叫()

# scoops=scoop_maker.create(['a','b','c'])

# print(scoops) 
# #[<__main__.scoop object at 0x0000026D28286EE0>, <__main__.scoop object at 0x0000026D28286DC0>, <__main__.scoop object at 0x0000026D28286A90>]




# # for scoop in scoops:
# #     print(scoop.flavor)








# #實例(instance)

