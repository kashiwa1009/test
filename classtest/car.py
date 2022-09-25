# class Car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#     def descriptive(self):
#         print(f"{self.make}{self.model}{self.year}")

# mazda=Car("audi","a4","2019")
# mazda.descriptive()

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0


    def descriptive(self):
        long_name=f"{self.make}{self.model}{self.year}"
        return long_name

    def update_odometer(self,mileage):
        if mileage>=self.odometer:
             self.odometer=mileage
        else:
             print("you can't roll back an odometer!")
    
    def increment_odometer(self,miles):
        self.odometer+=miles

     #好處為可對函式進行擴充。
     #ex:禁止他人把里程數往回調小



    def readOdometer(self):
        print(f"this car has {self.odometer} miles on it.")

new_car=Car('audi','a4',2034)
# new_car.odometer=13
new_car.update_odometer(-1)
new_car.readOdometer()
print(new_car.descriptive())