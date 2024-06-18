def main():

#list [1,4,6,7,78]
    scores = [1, 4, 6, 7, 78]
    student_names = ["Alice", "Bob", "Jerry", "Jane", "Bill"]
    for index in range (len(scores)):
        print(f"{student_names[index]}: {scores[index]}")

    #create a dictionary for names and scores
    student_names ={
        "Alice": 87,
        "Bob": 79,
        "Jerry": 94,
        "Sarah": 90
    }

    # print Bob and sarahs score
    print(student_names["Bob"])
    print(student_names["Sarah"])

    # Get all the keys and values from all the student score dictionary
    for student in student_names:   
        print(f" \n {student}: {student_names[student]} \n")


#Declare a car dictionary
    car = {"make": "Ferarri", "model":"F-50","year":2021,"value": 500000, "engine": 4.8}

#get all teh keys and values from the car dictionary
    print("\n\n")
    for key, value in car.items():
        print(f"{key}: {value}")

# How to use the split method
    car_info = "Ferrari, f-50, 2021,500000,4.8"
    car_data= car_info.split(",")
    print(car_data)

#get the individual item from the resulting list
    car_make = car_data[0]
    car_model = car_data[1]
    car_year = int(car_data[2])
    car_price = float(car_data[3])
    engine_size = float(car_data[4])

    print("Car Information \n")
    print(f" Make: {car_make} -- Model:{car_model}")
    print(f"Year: {car_year}-- Price{car_price}-- Engine: {engine_size}")

main()
# function to load menu items from the file and create a dictionary
# Input: none
#Output: dictionary of menu items

def get_menu_items():
#create a file handle that gives us acces to the file
#create an empty dictionary to store menu items and prices
#loop through data in the file and read file one line at a time
# split the line of data at the coma using .split()
#get items and price from the resulting list and create and store in the dictinary
#close the file
    data_file = open("menu.txt","r")
    menu_items = {}
    for line_of_data in data_file:

        keys_and_value = line_of_data.split("'")

        item = keys_and_value[0]
        price = float(keys_and_value[1])
        menu_items [item] =price
    data_file.close()
    return menu_items


def main():
   
    menu_items = get_menu_items()
    total = 0
    #PROMPT USER FOR AN ITEM 
    # declare a variable to keep track of the total
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
