# make list then make loop that itrate the list and chek attendance

classOne = ["Abdo", "Abdelmonam","Eslam","Mohammed", "Haway","Ali","Yousef"]

for student in classOne: 
    attending = input (f" Is the {student} attending? (yes or no): ").lower()
    
    if attending == "yes":
        print("Attendance Confirmed!")
    else:
        print("Attendance Not Confirmed !")
    
    print("*" * 20)