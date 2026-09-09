# import necessary modules
import support as m1
import time, os
import pandas as pd

'''The admin() function allows adminstrators to manage the systems by performing various tasks that include adding new 
teachers, adding new student data, updating existing student data, deleting student data and viewing all student data'''

def admin():
    # Get admin credentials
    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")
    # Verify admin credentials
    result = m1.check_admin(uid, pas)
    if result == "verified":
        # Loop until admin chooses to exit
        ch = "y"
        while ch.lower() == "y":
            # Clear the screen and display admin menu
            os.system('cls')
            print("1.Add Teacher\n2.Add Student Data\n3.Update Student Data\n4.Delete Student Data\n5.View Student Data\n6.Exit")
            # Gets admin's choice
            choice = int(input("Enter your choice (1/2/3/4/5/6) : "))
            # Handle admin's choice
            match choice:
                case 1:
                    # Add a new teacher
                    os.system('cls')
                    new_user = input("Enter the new ID :")
                    new_pass = input("Enter the new Password :")
                    m1.add_teacher(new_user, new_pass)
                    print("The teacher is added successfully !")
                    time.sleep(2)
                    m1.view_teachers()
                    ch = input("Do you want to continue (y/n)? ")
                case 2:
                    # Add a new student
                    os.system('cls')
                    name = input("Student Name : ")
                    price = int(input("Marks : "))
                    m1.add_data(name, price)
                    print("The student data has been added to the list !")
                    ch = input("Do you want to continue (y/n)? ")
                case 3:
                    # Update an existing student
                    os.system('cls')
                    name = input("Enter the student name : ")
                    price = int(input("Enter the altered marks : "))
                    m1.update_data(name, price)
                    print("The student marks has been modified successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 4:
                    # Delete a student
                    os.system('cls')
                    name = input("Enter the student name to be removed : ")
                    m1.del_data(name)
                    print("The student data has been removed successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 5:
                    # View all students
                    os.system('cls')
                    m1.display_data()
                    time.sleep(5)
                    os.system('cls')
                    ch = input("Do you want to continue (y/n)? ")
                case 6:
                    # Exit admin menu
                    print("Exited successfully !")
                    break
                case _:
                    # Handle invalid input
                    print("Invalid input")
                    break
    else:
        # Display error message for invalid credentials
        print("Invalid username or password")
        time.sleep(2)

'''The teacher() function allows teachers to manage student data by performing tasks such as adding new student data, updating 
existing student data, viewing all student data'''
def teacher():
    # Get teacher credentials
    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")
    # Verify teacher credentials
    result = m1.check_teacher(uid, pas)
    if result == "verified" or True:
        # Display success message
        print("Teacher login successful !")
        # Loop until teacher chooses to exit
        ch = "y"
        while ch.lower() == "y":
            os.system('cls')
            # Get teacher choice
            print("1.Add Student Data\n2.Update Student Data\n3.View Student Data\n4.Exit")
            choice = int(input("Enter your choice (1/2/3/4): "))
            # Handle teacher's choice
            match choice:
                case 1:
                    # Add a new student
                    os.system('cls')
                    name = input("Enter student name: ")
                    price = int(input("Enter student marks: "))
                    m1.add_data(name, price)
                    print("Student data has been added successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 2:
                    # update an existing student
                    os.system('cls')
                    name = input("Enter the student name to be updated: ")
                    price = int(input("Enter marks to be updated: "))
                    m1.update_data(name, price)
                    print("Student data has been updated successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 3:
                    # View all students
                    os.system('cls')
                    m1.display_data()
                    time.sleep(5)
                    os.system('cls')
                    ch = input("Do you want to continue(y/n)? ")
                case 4:
                    #To exit the option
                    print("Exited successfully !")
                    break
                case _:
                    # Handle invalid input for user type
                    print("Invalid input")
                    # Break out of the loop
                    break
    else:
        # Print error messsage for invalid username or password
        print("Invalid username or password")
        # Pause execution for 2 seconds
        time.sleep(2)

'''The student() function simulates a student experience and allow students to view available courses/marks,add courses 
to their enrollments,view their enrollments and proceed to confirm enrollments'''

def student():
    # Welcome message for student
    print("Welcome, Student!")
    # Intialize a variable to track user's choice to continue
    ch = "y"
    # Initialize an empty enrollments
    enrollments = []
    # Initialize total price and fee
    total_price = 0
    fee = 0
    # Loop until user chooses to exit
    while ch.lower() == "y":
        # clear the console
        os.system('cls')
        # Display menu options
        print("1. View Student Data\n2. Enroll in Course\n3. View Enrollments\n4. Pay Fees\n5. Exit")
        try:
            # Get users choice
            choice = int(input("Enter your choice (1/2/3/4/5): "))
            # Use match statement to handle different choices
            match choice:
                # Handle view student option
                case 1:
                    # Clear the console
                    os.system('cls')
                    # Display students
                    m1.display_data()
                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask user idf they want to continue
                    ch = input("Do you want to continue (y/n)? ")
                case 2:
                    # Clear the console
                    os.system('cls')
                    # Prompt user to enter item numbers to add to enrollments
                    print("Enter course numbers to enroll (enter -1 to finish):")
                    # Display the students
                    m1.display_data()
                    # Loop until user finishes enrolling items
                    while True:
                        # Get item number from the user
                        try:
                            num = int(input("Enter the course number: "))
                            # Check if user wants to finish adding items
                            if num != -1:
                                pass
                            else:
                                # Break out of the loop
                                break
                            # Read students.csv file
                            df = pd.read_csv("students.csv",index_col=0)
                            # Check if the item number is valid
                            if num in df.index:
                                # Get item name and price
                                item_name = df.loc[num, "student_name"]
                                item_price = df.loc[num, "marks"]
                                # Add item to enrollments
                                enrollments.append((item_name, num, item_price))
                                # Update total price
                                total_price += item_price
                                # Print conformation message
                                print(f"Added {item_name} to enrollments!")
                            else:
                                # Print error message for invalid item number
                                print("Invalid course number.")
                        except ValueError:
                            # print error message for invalid input
                            print("Please enter a valid number.")
                    # print enrollments total
                    print(f"Enrollments total fees: {total_price}")
                    # Ask user if they want to continue
                    ch = input("Do you want to continue (y/n)? ")

                # Handle view enrollments option
                case 3:
                    # clear the console
                    os.system('cls')
                    # Check if the enrollments is empty
                    if not enrollments:
                        # print message the enrollments is empty
                        print("Your enrollment list is empty.")
                    else:
                        # print enrollments contents
                        print("Your Enrollments:")
                        for item in enrollments:
                            # Print each item in the enrollments
                            print(f"Course {item[0]}: {item[1]} - ₹{item[2]}")
                        # Print total price
                        print(f"Total Fees: {total_price}")
                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask user if they want to continue
                    ch = input("Do you want to continue (y/n)? ")
                case 5:
                    #Print thankyou message for the student
                    print("Thank you for using the system!")
                    break
                case 4:
                    #Clear the console
                    os.system('cls')
                    # Check if enrollments is empty
                    if not enrollments:
                        print("Your enrollment list is empty. Please enroll before proceeding.")
                    else:
                        # Print billing summary
                        print("=== Fee Summary ===")
                        for item in enrollments:
                            print(f"Course {item[1]} - ₹{item[2]}")
                        tax = total_price * 0.05
                        print("="*40)
                        print(f"Total Fees : ₹{total_price}")
                        print(f"Tax : ₹{tax}")
                        print(f"Final Amount : ₹{total_price + tax}")
                        # Ask user to confirm enrollment
                        confirm = input("Confirm fee payment (y/n)? ")
                        if confirm.lower() == "y":
                            # Print successful message
                            print("Payment successful! Your enrollments are confirmed!")
                        else:
                            print("Payment cancelled.")
                        # Reset enrollments and total price
                        enrollments = []
                        total_price = 0

                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask if the user want to continue
                    ch = input("Do you want to continue (y/n)? ")
                # Handle invalid input
                case _:
                    # Print eror message
                    print("Invalid input")
                    # Ask if they want to continue
                    ch = input("Do you want to continue (y/n)? ")
        except ValueError:
            # Printing the error message
            print("Please enter a valid number.")
            # Ask the user if they want to continue
            ch = input("Do you want to continue (y/n)? ")

'''The main() function serves as the entry point of the software and it displays a menu to select user
 type, calls the corresponding function based on user input, handles invalid inputs and exceptions and asks the user if they 
 want to continue using the software'''
def main():
    ch = 'y'
    # Loop until user chooses to exit
    while ch.lower() == "y":
        try:
            #Clear the console
            os.system('cls')
            # Display title and menu
            print("An automated student management software".center(170))
            # Get the user type from user
            print("1.Admin\n2.Teacher\n3.Student\n4.Exit")
            user_type = int(input("Enter user type(1/2/3/4): "))
            # Use match statement to handle different user types
            match user_type:
                case 1:
                    # Clear console and call admin function
                    os.system("cls")
                    admin()
                case 2:
                    # Clear console and call teacher function
                    os.system("cls")
                    teacher()
                case 3:
                    # Clear the console and call student function
                    os.system("cls")
                    student()
                    print("Thank you for using our service.")
                case 4:
                    # Clear the console and print exit message
                    os.system("cls")
                    print("Exited. Thank you for using our service".center(170))
                    break
                case _:
                    # Print the error message
                    print("Invalid input. Enter a valid choice.")
        # Handle value error exception
        except ValueError:
            print("Please enter a valid number.")
            # Ask the user if they want to continue
            ch = input("Do you want to continue (y/n)? ")

#Check if the script is being run directly
if __name__ == "__main__":
    main()
