def main():

    #capitalize a string
    my_name = "karyna"
    print(my_name.capitalize())

    # makes a string uppercase
    print(my_name.upper())

    # MAKE A STRING LOWERCASE
    last_name = "KARYNA"
    print(f"{my_name.capitalize()} {last_name.lower()}")

    # determine if a string is with a set of characters
    print(my_name.startswith("K"))
    if (not my_name.startswith("K") and not my_name.startswith ("k")):
        print("You spelt my name wrong!")
    else:
        print("You spelt my name correctly!")
    #determine iof a string end with a specified swt of characters 

    print(my_name.endswith("yna"))

    #find a set of characters in a string

    print(my_name.find("a",1))

    #loop through a string

    for letter in  my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} letters")

    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index}: {my_name[letter_index]}")

    
    #write code that counts the number of occruences of the odg in senteces print(f"")
    # use a while loop 
    sentence = "I have a dog. My dog is cute. Do you want a dog?" 
    number_of_dogs = 0
    dog_index = 0
    while (True):
        dog_index = sentence.find("dog",dog_index)
        (dog_index)
        if dog_index == -1:
            break
        else:
            number_of_dogs += 1
            dog_index += 1
            continue
    print(f"\nNumber of dogs: {number_of_dogs}\n")

    
main()
