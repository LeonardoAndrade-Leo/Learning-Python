class Person:
    def __init__(self, age):
        self.__age=age
    
    def set_age(self, new_age):
        if new_age>=0:
            self.__age=new_age
            print('Age chnaged successfully!')
        else:
            print('invalid Age! Try it again.')

    def get_age(self):
        return(f'Your age is {self.__age}')

natan = Person(27)
natan.set_age(28)
print(f'Your changed age is {natan.get_age()}')

# Set - to change an information
# Get - to see an information