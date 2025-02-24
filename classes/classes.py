# to create a class in python we use the word 'class' and the name of the class. The recommendation is writing the first letters in uppercase 
# To create an attribute, you have to write 'def __init__(self)' 

class Computer:
    def __init__(self, brand, ram_memory, graphics_card ): # init initialize the objects attributes. and self is used to acess the attributes. The atrributes are named in the parentheses. Self is use to reference the object we created from the class.
        self.brand = brand
        self.ram_memory= ram_memory
        self.graphics_card=graphics_card
    

     

# To create an object from the class:
computer_1= Computer ('Samsung', '16GB', 'lEOS')
print(computer_1.brand, computer_1.ram_memory, computer_1.graphics_card )
computer_2= Computer('MAC', '64gb', 'omg')
print(computer_2.brand, computer_2.ram_memory, computer_2.graphics_card)
