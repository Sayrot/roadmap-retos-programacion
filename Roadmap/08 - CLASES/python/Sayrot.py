'''
Ejercicio
'''

class Programmer:
    
    surname = None
    
    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages
    
    def print(self):
        print(f"Nombre: {self.name} | Apellido: {self.surname} | Edad: {self.age} | Lenguajes: {self.languages} ")
        
my_programmer = Programmer("Andres", 26, ["Python", "Java", "Swift"])
my_programmer.print()
my_programmer.surname = ("Mejia")
my_programmer.print()
my_programmer.age = (27)
my_programmer.print()
print()


'''
Extra
'''

#LIFO

class Stack:
    
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        return self.stack.append(item)
    
    def pop(self):
        if self.count == 0:
            return None
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)
            
my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("c")
my_stack.push("D")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
my_stack.print()
print()

#FIFO

class Queue:
    
    def __init__(self):
        self.queue = []
        
    def equeue(self, item):
        return self.queue.append(item)
    
    def enqueue(self):
        if self.count == 0:
          return None
        return self.queue.pop(0)
    
    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in self.queue:
            print(item)

my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
my_queue.equeue("D")
print(my_queue.count())
my_queue.print()
my_queue.enqueue()
print()
print(my_queue.count())
my_queue.print()