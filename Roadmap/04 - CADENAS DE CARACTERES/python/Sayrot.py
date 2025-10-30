'''
Operaciones
'''

s1 = "Hola"
s2 = "Python"

# Concatenación
s3 = s1 + " " + s2
print("Concatenación:", s3)
print()

# Repetición
s4 = s1 * 3
print("Repetición:", s4)
print()

# Acceso por índice
print("Acceso por índice:", s1[1])  # 'o'
print() 

# Subcadenas (slicing)
print("Subcadena:", s2[1:4])  # 'yth'
print()     

# Longitud
print("Longitud de s1:", len(s1))
print("Longitud de s2:", len(s2))
print()

# Búsqueda de subcadena
index = s3.find("Python")
print("Búsqueda de subcadena 'Python' en s3:", index)
print()

# Reemplazo de subcadena
s5 = s3.replace("Python", "Mundo")
print("Reemplazo de subcadena:", s5)
print()

# División de cadena
parts = s3.split(" ")
print("División de cadena:", parts)
print()

# Unión de cadena
s6 = "-".join(parts)
print("Unión de cadena:", s6)       
print()

#Mayúsculas, minúsculas, title, capitalize
print("Mayúsculas:", s1.upper())    
print("Minúsculas:", s2.lower())
print("Title:", s3.title())
print("Capitalize:", s3.capitalize())
print()

#Eliminiar espacios en blanco
s7 = "   Hola Mundo   "
print("Antes de strip:", repr(s7))  
print("Después de strip:", repr(s7.strip()))
print()

#Busqueda princiopio y final
print("Empieza con 'Hola':", s7.strip().startswith("Hola"))
print("Termina con 'Mundo':", s7.strip().endswith("Mundo"))
print()

#Busqueda por posicion
print("Hola Mundo".find("Mundo"))
print()

#Busqueda por ocurrencias
print("Ocurrencias de 'o' en s3:", s3.count("o"))
print()

#Formateo
print("Saludo: {}", "Lenguaje: {}".format(s1,s2))
print()

#Comprobaciones
s8 = "1234556789"
print(s8.isalnum())
print(s8.isalpha())
print(s8.isdigit())
print()


'''
Extra
'''

def comprobacion(palabra1, palabra2: str):
     
     #Palindromo
     print(f"{palabra1} es un palindromo?: {palabra1 == palabra1[::-1]}")
     print(f"{palabra2} es un palindromo?: {palabra2 == palabra2[::-1]}")
     
     #Angrama
     print(f"{palabra1} es un anagrama de {palabra2}?: {sorted(palabra1) == sorted(palabra2)}")
     
def isograma(palabra: str) -> bool:
    
    palabra_dict = dict()
    for characters in palabra:
        palabra_dict[palabra] = palabra_dict.get(characters, 0) + 1
        
    isograma = True
    values = list(palabra_dict.values())
    isograma_len = values[0]
    for palabra_count in values:
        if palabra_count != isograma_len:
            isograma = False
            break
        return isograma
    
    print(f"{palabra} es un isograma? {isograma(palabra)}")

comprobacion("Pyhton", "radar")
comprobacion("amor", "roma")
isograma("PythonPython")
