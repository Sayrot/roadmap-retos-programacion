'''
Ejercicio
'''
#Pila/Stack (LIFO)

#Push
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)

#Pop
stack_item = stack[len(stack) -1]
del stack[len(stack) -1]
print(stack_item)
print(stack)
print(stack.pop())
print(stack)

print()
print("Queue")

#Cola/Queue (FIFO)

# enqueue
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)

# dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)
print(queue)
print(queue.pop(0))
print(queue)

'''
Ejercicio
'''

def web_navigation():
    stack = []
    
    while True:
        
        action = input("Añade una nueva url o interactua con las palabras adelante/atrás/salir: ")
        
        if action == "salir":
            print("Saliendo del navegador web...")
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)
        
        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}. ")
        else:
            print("Estas en la pagina de inicio")
        
        
#web_navigation()


def shared_printed():
    
    queue = []
    
    while True:
        
        action = input("Añade un docmento o selecciona imprimir/salir: ")
        
        if action == "salir":
            print("Saliendo...")
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Impriendo documento: {queue.pop(0)}")
            else:
                len(queue) < 0
                print("Cola de impresion vacia, añada nuevos documentos..")
        else:
            queue.append(action)
            print(f"Documento añadido a la cola: {queue}")
            
        
    


shared_printed()