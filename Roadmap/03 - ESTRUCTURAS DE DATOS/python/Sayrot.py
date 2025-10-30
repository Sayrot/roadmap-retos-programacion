#Listas
mi_lista = ["Andres", "Maria", "Juan"]
print(mi_lista)
mi_lista.append("Manuel") # Agregar un elemento al final
print(mi_lista)
mi_lista.remove("Maria") # Eliminar un elemento
print(mi_lista)
print(mi_lista[1]) # Acceder a un elemento por su índice
mi_lista[0] = "Ana" # Modificar un elemento
mi_lista.sort() # Ordenar la lista
print(mi_lista)
print()

#Tuplas
mi_tupla = ("Rojo", "Verde", "Azul")
print(mi_tupla)
print(mi_tupla[0])
#mi_tupla[1] = "Amarillo"  # Esto generará un error porque las tuplas son inmutables
mi_tupla = tuple(sorted(mi_tupla)) # Ordenar la tupla (crea una nueva tupla
print(mi_tupla)
print()

#Diccionarios
mi_diccionario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
print(mi_diccionario)
print(mi_diccionario["edad"]) # Acceder a un valor por su clave
mi_diccionario["edad"] = 26   # Modificar un valor
print(mi_diccionario)
mi_diccionario["profesion"] = "Ingeniera" # Agregar un nuevo par clave-valor
print(mi_diccionario)
del mi_diccionario["ciudad"] # Eliminar un par clave-valor
print(mi_diccionario)
mi_diccionario = dict(sorted(mi_diccionario.items())) # Ordenar el diccionario por claves
print(mi_diccionario)
print()

#Sets
mi_set = {"manzana", "banana", "naranja"}
print(mi_set)
mi_set.add("pera") # Agregar un elemento
print(mi_set)
mi_set.remove("banana") # Eliminar un elemento
print(mi_set)
print("manzana" in mi_set)   # Verificar si un elemento está en el set   
mi_set = set(sorted(mi_set)) # No se puede ordenar 
print(mi_set)
print()

'''
Extra
'''
def mi_agenda():
    
    agenda = {}
    
    while True:
        print("1. Buscar contacto")
        print("2. Agregar contacto")
        print("3. Eliminar contacto")
        print("4. Actualizar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")   
        
        match opcion:
            case "1":
                name = input("Ingrese el nombre del contacto a buscar: ")
                if name in agenda:
                       print(f"El nummero de {name} es {agenda[name]}")
                else:
                       print(f"Contacto {name} no encontrado.")
            case "2":
                name = input("Ingrese el nombre del contacto: ")
                phone = input("Ingrese el número de teléfono: ")
                if phone.isdigit() and len(phone) >0 and len(phone) <=11:
                    agenda[name] = phone 
                    print(f"Contacto {name} agregado con éxito.")
                else:
                    print("Número de teléfono inválido. Debe contener solo dígitos y tener entre 1 y 11 caracteres.")
            case "3":
                name = input("Ingrese el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print(f"Contacto {name} eliminado con éxito.")
                else:
                    print(f"Contacto {name} no encontrado.")
            case "4":
                name = input("Ingrese el nombre del contacto a actualizar: ")
                if name in agenda:
                    phone = input("Ingrese el nuevo número de teléfono: ")
                    if phone.isdigit() and len(phone) >0 and len(phone) <=11:
                        agenda[name] = phone
                        print(f"Contacto {name} actualizado con éxito.")
                    else:
                        print("Número de teléfono inválido. Debe contener solo dígitos y tener entre 1 y 11 caracteres.")
                else:
                    print(f"Contacto {name} no encontrado.")
            case "5":
                if agenda:
                    for name, phone in agenda.items():
                        print(f"{name}: {phone}")
                else:
                    print("-->>La agenda está vacía.<<--")
            case "6":
                print("Saliendo de la agenda...")
            case _:
                print("Opción no válida. Intente de nuevo.")

mi_agenda()