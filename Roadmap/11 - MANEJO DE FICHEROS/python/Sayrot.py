import os

'''
Ejercicio
'''

file_name = "Sayrot.txt"

#with open(file_name, "w") as file:
    #file.write("Sayrot Dev\n")
    #file.write("Desarrollador Python\n")
    #file.write("Manejo de ficheros\n")

#with open(file_name, "r") as file:
    #content = file.read()
    #print(content)

#os.remove(file_name)

'''
Extra
'''

file_name_shop = "Shop.txt"

open (file_name_shop, "a")

while True:
    print("1. Add item")
    print("2. Update item")
    print("3. Delete item")
    print("4. View item")
    print("5. Show all items")
    print("6. Calculate Total Sale")
    print("7. calculate sales by product")
    print("8. Exit")

    option = input("Select an option: ")

    if option == "1":
        name = input("Enter item name: ")
        quantity = input("Enter item quantity: ")
        price = input("Enter item price: ")
        with open(file_name_shop, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")
            print("Item added successfully!.\n")
    
    elif option == "2":
        name = input("Enter item name to update: ")
        quantity = input("Enter new quantity: ")
        price = input("Enter new price: ")      
        with open(file_name_shop, "r") as file:
            lines = file.readlines()
            with open(file_name_shop, "w") as file:
                for line in lines:
                    if line.split(", ")[0] == {name}:
                        file.write(f"{name}, {quantity}, {price}\n")
                        print("Item updated suscessfully!.\n")

    elif option == "3":
        name = input("Enter item name to delete: ")
        with open(file_name_shop, "r") as file:
            lines = file.readlines()
            with open(file_name_shop, "w") as file:
                for line in lines:
                    if line.split(", ")[0] != {name}:
                        file.write(line)
                        print("Item deleted successfully!.\n")

    elif option == "4":
        name = input("Enter item name to view: ")
        print("Item details:")
        with open(file_name_shop, "r") as file: 
            for line in file.readlines():
                if line.split(", ")[0] == {name}:
                    print(line)
                    break

    elif option == "5":
        print("All items:")
        with open(file_name_shop, "r") as file:
            content = file.read()
            print(content)

    elif option == "6":
        total_sale = 0
        with open(file_name_shop, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total_sale += quantity * price
        print(f"Total sale: {total_sale}\n")

    elif option == "7":
        name = input("Enter item name t calculate sales: ")
        total_sale = 0 
        with open(file_name_shop, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total_sale += quantity * price
        print(f"Total sales for {name}: {total_sale}\n")
        

    elif option == "8":
        os.remove(file_name_shop)
        break

    else:
        print("Invalid option. Please try again.")

