'''
Ejercicio
'''
#Superclase

class Animal:
    
    def __init__ (self, name: str):
        self.name = name
        
    def sound(self):
        pass 
        
#Subclases

class Dog(Animal):
    
    def sound(self):
        print("Guau!")        

class Cat(Animal):
    
    def sound(self):
        print("Miau!")
        
def print_sound(animal: Animal):
    animal.sound()
        
my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = Dog("Firulais")
print_sound(my_dog)
my_cat = Cat("Luna")
print_sound(my_cat)


'''
Extra
'''

class Employee:
    
    def __init__(self, id: int, name: str):
        self.id = id 
        self.name = name
        self.employees = []
        
    def add_employee(self, employee):
        self.employees.append(employee)
        
    def print_employees(self):
        for employee in self.employees:
            print(f"Empleado a cargo: {employee.name}")
        
class Manager(Employee):
    
    def coordinate_projects(self):
        print(f"{self.name} esta coordiando los proyectos.")

class ProjectManager(Employee):
    
     def __init__(self, id: int, name: str, project_name: str):
         super().__init__(id, name)
         self.project_name = project_name
         
     def coordinate_project(self, project_name: str):
        print(f"{self.name} esta coordinando el proyecto {project_name}.")

class Programmer(Employee):
    
     def __init__(self, id: int, name: str, language: str):
         super().__init__(id, name)
         self.language = language
    
     def write_code(self, id: int, name: str, language: str):
       print(f"{self.name} esta escribiendo codigo en {self.language}.")
        
     def add(self, employee: Employee):
         print(f"Los programadores no pueden tener empleados a su cargo. {employee.name} no se ha agregado.")
        

my_manager = Manager(1, "SayrotDev")
my_projectmanager  = ProjectManager(2, "Andres", "Backend API")
my_projectmanager2 = ProjectManager(3, "Manuel", "Frontend App")
my_projectmanager3 = ProjectManager(4, "Laura", "Mobile App")
my_programmer  = Programmer(5, "Carlos", "Python")
my_programmer2 = Programmer(6," Ana", "JavaScript")
my_programmer3 = Programmer(7," Sofia", "Java") 

my_manager.add_employee(my_projectmanager)
my_manager.add_employee(my_projectmanager2) 
my_manager.add_employee(my_projectmanager3)

my_projectmanager.add_employee(my_programmer)
my_projectmanager2.add_employee(my_programmer2)
my_projectmanager3.add_employee(my_programmer3)

my_programmer.add(my_programmer2)

my_manager.print_employees()
my_projectmanager.print_employees() 
my_projectmanager2.print_employees()
my_projectmanager3.print_employees()    