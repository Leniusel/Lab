#Name: Doris Tran
#Filename: M02_IfElseWhile.py
#The App will accept inputs for student's name, their gpa, and will give different messages depending on their gpa. The user
#can exit the app by inputing 'ZZZ' as a student's lastname.

#Default variables
student = " "      #stores student's fullname
GPA = 0.0          #stores gpa score
process = True     #boolean value that checks if the app is processing student records

lname = ""         #stores student's lastname
fname = ""         #stores student's firstname

#Functions that returns a student's fullname and checks if the user wants to exit the app via entering "ZZZ" as a student's lastname.
def fullname(student, process):
    lname = input("\nEnter Student's Last Name (Enter 'ZZZ' to quit): ")
    if lname == "ZZZ":
        print("Quiting.....") 
        process = False
        return student, process
    else:
        fname = input("Enter Student's First Name: ")
        student = fname + " " + lname
        return student, process
   
 #Function that validates the GPA input. It checks if the input is a float. If the user inputs invalid data, ask user to try again.   
def gpa_score(GPA):
    try:
        GPA = float(input("\nEnter " + student + "'s GPA: "))
        assert 4.0 >= GPA >= 0.0
        return GPA;
    except:
        print("Please enter a valid GPA.")
        return gpa_score(GPA);

#Function that prints a message depending on the student's gpa. Python checks row by row, so looking for students that qualify
#for the Dean's list goes first. Honar Roll goes second.
def message():
    if GPA >= 3.50:
        print("The student " + student + " has made the Dean's List.")
    elif GPA >= 3.25:
        print("The student " + student + " has made the Honar Roll.")
    else:
        print("This student did not make it to the Dean's List or the Honar Roll.")

#A while loop that checks if the process variable is true. Once false, the app will terminate
while process == True:
    student, process = fullname(student, process)
    if process == False:
        print("program terminated")
    else:  
      GPA = gpa_score(GPA)
      message()
