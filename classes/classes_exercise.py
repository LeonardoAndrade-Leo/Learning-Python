
# CREATE A CLASS NAMED CAR AND CREATE AT LEAST 3 ATTRIBUTES AND 3 METHODS FOR IT

class Car:
    def __init__(self, brand, color, size):
        self.brand=brand
        self.color=color
        self.size=size

    def Ligar(self):
        print('Para ligar, gire a chave')
    
    def Desligar(self):
        print('para desligar, gire a chave novamente')

    def Print_Information(self):
        print(self.brand, self.color, self.size)

car1= Car('Fiat', 'blue', 'big')
car1.Ligar()
car1.Desligar()
car1.Print_Information()



