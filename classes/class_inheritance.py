#INHERITANCE is used to inherit the same attributes and method of another class

class Employee:    #ParentClass
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    
    def show_info(self):
        print(f'The Employee {self.name} has a salary of {self.salary}')

class Manager (Employee):  #ChildClass
    def __init__(self, name, departament, salary):
        super().__init__(name, salary)
        self.departament=departament
    def show_info(self):
        print(f'The Employee {self.name} of the {self.departament} departament has a salary of {self.salary} ')

# Testing 

employee=Employee('Leonardo', '$ 2200')
employee.show_info()

manager=Manager('Natan', 'MarketPlace', '$ 2500')
manager.show_info()


        




        


    


        

            

        