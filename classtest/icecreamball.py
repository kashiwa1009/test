# #資料型態

# #定義自己的資料型態

# #封裝的變數或函式，為類別的屬性




# class Scoop:
#     def __init__(self,flavor): 
#         self.flavor=flavor  #定義一個flavor的屬性
#         #宣告，動態建立屬性


# class Scoop_Maker:   # 封裝的函式      #實體方法  
#     def create(self,flavors):
#          return [Scoop(flavor) for flavor in flavors]   # Scoop(flavor)<- 直接去抓Scoop裡的屬性
#         # return [a for a in flavors] 




# scoop_maker=Scoop_Maker() # 產生scoop_maker物件
# #可呼叫()

# scoops=scoop_maker.create(['a','b','c'])
# for scoop in scoops:
#     # print(scoop,scoop.flavor)
#     print(scoop.flavor)

 
