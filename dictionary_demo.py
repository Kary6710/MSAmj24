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
main()
