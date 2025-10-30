'''
Ejercicio
'''

try:
    print(10/0)
    print([1,2,3,4][4])
except Exception as e: 
    print(f"Haocurrido un errror: {e} ({type(e).__name__})")
    
print()

'''
Extra
'''

class StrTypeError(Exception):
    pass 

def proccess_params(parameters: list):
    if len(parameters) < 3:
        raise IndexError
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer parámetro no puede ser una cadena de texto")

    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)
    
try:
    proccess_params([1,2,3,4])
except IndexError as e:
    print("El numero del elemento de la lista deber se mayor a dos.")
except ZeroDivisionError as e:
    print("El segundo numero de la lista no puede ser cero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido ningun error.")
finally:
    print("El programa ha finalizado sin detenerse.")