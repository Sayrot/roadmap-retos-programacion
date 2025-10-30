'''
Funciones definidas por el usuario
'''

#Funciones simples
def saludar():
    print("Hola, bienvenido a la programación en Python")
    
saludar()

def despedir():
    print("Adiós, hasta pronto")
    
despedir()

#Funciones con retorno
def sumar(a, b):
    return a + b
resultado = sumar(5, 3)
print("La suma es:", resultado) 


#Funcion con argumento 
def saludar_persona(nombre):
    print(f"Hola, {nombre}, bienvenido a la programación en Python")

saludar_persona("Sayrot")

#Funciones con argumentos
def saludar_persona_edad(nombre, edad):
    print(f"Hola, {nombre}, tienes {edad} años y bienvenido a la programación en Python")

saludar_persona_edad("Sayrot", 25)
saludar_persona_edad(edad=25, nombre="Sayrot")


#Funciones con valor por defecto
def saludar_persona_defecto(nombre="Invitado"):
    print(f"Hola, {nombre}, bienvenido a la programación en Python")

saludar_persona_defecto()
saludar_persona_defecto("Sayrot")

#Funcion con varios argumentos
def saludo_multiple(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}, bienvenido a la programación en Python")

saludo_multiple("Andres", "Manuel", "Sayrot", "Sonia") 


#Funcion con varios argumentos con clave-valor
def saludo_clave_valor(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")
        
saludo_clave_valor(nombre="Sayrot", edad=25, ciudad="Madrid")


'''
Funciones aniadas
'''
def funcion_externa():
    def funcion_interna():
        print("Hola desde la función interna")
    funcion_interna()
    
funcion_externa()


'''
Funciones del lenguaje
'''
print("Hola, bienvenido a la programación en Python")  #Función print
print(len("Hola"))  #Función len
print(type(123))  #Función type
print("Andres".upper())  #Función upper
print("ANDRES".lower())  #Función lower
print("Hola, bienvenido a la programación en Python".replace("Python", "Funciones"))  #Función replace
print("Hola, bienvenido a la programación en Python".split())  #Función split
print("Hola, bienvenido a la programación en Python".find("bienvenido"))  #Función find
print("Hola, bienvenido a la programación en Python".count("o"))  #Función count
print("Hola, bienvenido a la programación en Python".startswith("Hola"))  #Función startswith
print("Hola, bienvenido a la programación en Python".endswith("Python"))  #Función endswith
print("  Hola, bienvenido a la programación en Python  ".strip())  #Función strip
print("  Hola, bienvenido a la programación en Python  ".lstrip())  #Función lstrip
print("  Hola, bienvenido a la programación en Python  ".rstrip())  #Función rstrip
print("Hola, bienvenido a la programación en Python".capitalize())  #Función capitalize         
print("Hola, bienvenido a la programación en Python".title())  #Función title
print("Hola, bienvenido a la programación en Python".islower())  #Función islower
print("Hola, bienvenido a la programación en Python".isupper())  #Función isupper


'''
Variables globales y locales
'''

#Variable global
mensaje = "Hola, bienvenido a la programación en Python"
def mostrar_mensaje():
    print(mensaje)  #Accede a la variable global
mostrar_mensaje()
print(mensaje)  #Accede a la variable global
print()

#Variable local
def mostrar_mensaje_local():
    mensaje_local = "Hola desde la variable local"
    print(mensaje_local)  #Accede a la variable local
mostrar_mensaje_local()
#print(mensaje_local)  #Error, no puede acceder a la variable local
print()

'''
Extra
'''

def print_number(text_1, text_2)-> int:
    for numbr in range(1, 101):
        if numbr % 3 == 0 and numbr % 5 == 0:
            print(text_1 + text_2)
        elif numbr % 3 == 0:
            print(text_1)
        elif numbr % 5 == 0:
            print(text_2)
        else:
            print(numbr)

print_number("Fizz", "Buzz")