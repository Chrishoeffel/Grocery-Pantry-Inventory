pantry_inventory = {}

print("""
Pantry Inventory Options
-----------------------
1: Add item
2: Remove item
3: View basket
4: Exit Program

""")

option = int(input('Enter an option: '))

while option !=0:
    if option == 1:
        item = input('Enter an item: ')
        
        if item in pantry_inventory:
            print("Item already in pantry")
            qnty = int(input("Enter the quantity: "))
            pantry_inventory[item] += qnty
        else:

            qnty = int(input("Enter the quantity: "))
            pantry_inventory[item] = qnty    

    elif option ==2:
        item = input('Enter an item: ')
        del(pantry_inventory[item])

    elif option ==3:
        for item in pantry_inventory:
            print(item,":",pantry_inventory[item])
    
    elif option !=0:
        print("You didn't enter a valid number.")
    option = int(input("\n\nEnter an option: "))

else:
    print('Pantry inventory program closed.')