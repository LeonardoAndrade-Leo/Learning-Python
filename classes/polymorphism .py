# polymorphism is when the same method or function is used by other classes but having different behaviors

class Vehicle:
    def move(self):
        return('It is just the base for all others')

class Car:
    def move(self):
        return('The car is being driven by Natan')

class Plane:
    def move(self):
        return('The plane is being flown by Léo')

class Bike:
    def move(self):
        return('The bike is being riden by Leotan')

#testing
vehicles=[Car(), Plane(), Bike()]

for vehicle in vehicles:
    print(vehicle.move())




    
  



