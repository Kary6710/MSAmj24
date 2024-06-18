
def main():

    menu_items = {"Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    
    
    #PROMPT USER FOR AN ITEM 
    # declare a variable to keep track of the total

    total = 0
    while(True):
    
        item = input("Enter a menu item:")

        if item.lower() == "end":
            break

        try:
            #ITEM PRINT TOTAL COST OF THE INPUTTED ITEM
            price = menu_items[item] 
        except:
            continue
            #ignore any input that is not in the list

        total += price
        print(f" Total: ${total}")


# end program when user types any form of end

main()
