#實體屬性 
#封裝在實體物件中的變數

class File:
    def __init__(self,name):
        self.name=name
        self.file=None # 尚未開啟檔案:初期是 None
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()    
f1=File("data1.txt")
f1.open()
data=f1.read()
print(data)

