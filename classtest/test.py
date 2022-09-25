class Scoop:
    def __init__(self,flavor):
        self.flavor=flavor
    def create(self,flavors):
        return [self.flavor for self.flavor in flavors]

scoops=Scoop('aaaqaa')
scoops.create("cholate","blueburry","aaa")



for scoop in scoops:
    print(scoop)

print(scoops)
