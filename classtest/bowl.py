#組合 composition



class Bowl:
    max_scoop=3
    def __init__(self):
        self.flavor=[]

    def add_scoop(self,*args):
        for arg in args:
            if len(self.flavor)<self.max_scoop:
                self.flavor.append(arg)
    def descript(self):
         for i in self.flavor:
             print(i)

    #人類別->職員類別->學生類別

class ExtraBowl(Bowl):
    max_scoop=5




bowl=Bowl()
bowl.add_scoop("a")
bowl.add_scoop("b","c","d","e")
bowl.descript()
bowl=ExtraBowl()
bowl.add_scoop("a","b","c","d","e","f")
bowl.descript()

#----------------------------------------------------------------------------

# scoops屬性(一個list)，用來收集Scoop的實例物件
#add_scoop() method,可傳入數量不定的Scoop物件，將之放進scoops內
#show_content() method，用字串傳回scoops中所有Scoop物件的flavor的屬性


# class Scoop:
#     def __init__(self,flavor):
#         self.flavor=flavor

# class  Bowl:
#     def __init__(self):
#         self.scoops=[]  #不用傳參數，直接定義一個屬性 list 
#     def add_scoop(self,*args):
#         for arg in args:
#              self.scoops.append(arg)
#     def flavors(self):
#         return "".join(scoop for scoop in self.scoops)


# bowl=Bowl()
# bowl.add_scoop("aaa")
# bowl.add_scoop("bbb","ccc")

# print(bowl.flavors())




#---------------------------------------------------------------------

# # class Scoop:
# #     def __inti__(self,flavor):
# #         self.flavor=flavor

# class Scoop_maker:
#     def create(slef,flavors):
#         return[a for a in flavors]
    
# scoop_maker=Scoop_maker()
# scoops=scoop_maker.create(['a','b','c'])

# for a in scoops:
#     print(a)
