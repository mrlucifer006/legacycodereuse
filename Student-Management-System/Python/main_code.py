
import support as m1
import time, os
import pandas as pd

def admin():

    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")

    result = m1.check_admin(uid, pas)
    if result == "verified":

        ch = "y"
        while ch.lower() == "y":

            os.system('cls')
            print("1.Add Teacher\n2.Add Student Data\n3.Update Student Data\n4.Delete Student Data\n5.View Student Data\n6.Exit")

            choice = int(input("Enter your choice (1/2/3/4/5/6) : "))

            match choice:
                case 1:

                    os.system('cls')
                    new_user = input("Enter the new ID :")
                    new_pass = input("Enter the new Password :")
                    m1.add_teacher(new_user, new_pass)
                    print("The teacher is added successfully !")
                    time.sleep(2)
                    m1.view_teachers()
                    ch = input("Do you want to continue (y/n)? ")
                case 2:

                    os.system('cls')
                    name = input("Student Name : ")
                    price = int(input("Marks : "))
                    m1.add_data(name, price)
                    print("The student data has been added to the list !")
                    ch = input("Do you want to continue (y/n)? ")
                case 3:

                    os.system('cls')
                    name = input("Enter the student name : ")
                    price = int(input("Enter the altered marks : "))
                    m1.update_data(name, price)
                    print("The student marks has been modified successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 4:

                    os.system('cls')
                    name = input("Enter the student name to be removed : ")
                    m1.del_data(name)
                    print("The student data has been removed successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 5:

                    os.system('cls')
                    m1.display_data()
                    time.sleep(5)
                    os.system('cls')
                    ch = input("Do you want to continue (y/n)? ")
                case 6:

                    print("Exited successfully !")
                    break
                case _:

                    print("Invalid input")
                    break
    else:

        print("Invalid username or password")
        time.sleep(2)

def teacher():

    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")

    result = m1.check_teacher(uid, pas)
    if result == "verified" or True:

        print("Teacher login successful !")

        ch = "y"
        while ch.lower() == "y":
            os.system('cls')

            print("1.Add Student Data\n2.Update Student Data\n3.View Student Data\n4.Exit")
            choice = int(input("Enter your choice (1/2/3/4): "))

            match choice:
                case 1:

                    os.system('cls')
                    name = input("Enter student name: ")
                    price = int(input("Enter student marks: "))
                    m1.add_data(name, price)
                    print("Student data has been added successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 2:

                    os.system('cls')
                    name = input("Enter the student name to be updated: ")
                    price = int(input("Enter marks to be updated: "))
                    m1.update_data(name, price)
                    print("Student data has been updated successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 3:

                    os.system('cls')
                    m1.display_data()
                    time.sleep(5)
                    os.system('cls')
                    ch = input("Do you want to continue(y/n)? ")
                case 4:

                    print("Exited successfully !")
                    break
                case _:

                    print("Invalid input")

                    break
    else:

        print("Invalid username or password")

        time.sleep(2)

def student():

    print("Welcome, Student!")

    ch = "y"

    enrollments = []

    total_price = 0
    fee = 0

    while ch.lower() == "y":

        os.system('cls')

        print("1. View Student Data\n2. Enroll in Course\n3. View Enrollments\n4. Pay Fees\n5. Exit")
        try:

            choice = int(input("Enter your choice (1/2/3/4/5): "))

            match choice:

                case 1:

                    os.system('cls')

                    m1.display_data()

                    time.sleep(5)

                    ch = input("Do you want to continue (y/n)? ")
                case 2:

                    os.system('cls')

                    print("Enter course numbers to enroll (enter -1 to finish):")

                    m1.display_data()

                    while True:

                        try:
                            num = int(input("Enter the course number: "))

                            if num != -1:
                                pass
                            else:

                                break

                            df = pd.read_csv("students.csv",index_col=0)

                            if num in df.index:

                                item_name = df.loc[num, "student_name"]
                                item_price = df.loc[num, "marks"]

                                enrollments.append((item_name, num, item_price))

                                total_price += item_price

                                print(f"Added {item_name} to enrollments!")
                            else:

                                print("Invalid course number.")
                        except ValueError:

                            print("Please enter a valid number.")

                    print(f"Enrollments total fees: {total_price}")

                    ch = input("Do you want to continue (y/n)? ")

                case 3:

                    os.system('cls')

                    if not enrollments:

                        print("Your enrollment list is empty.")
                    else:

                        print("Your Enrollments:")
                        for item in enrollments:

                            print(f"Course {item[0]}: {item[1]} - ₹{item[2]}")

                        print(f"Total Fees: {total_price}")

                    time.sleep(5)

                    ch = input("Do you want to continue (y/n)? ")
                case 5:

                    print("Thank you for using the system!")
                    break
                case 4:

                    os.system('cls')

                    if not enrollments:
                        print("Your enrollment list is empty. Please enroll before proceeding.")
                    else:

                        print("=== Fee Summary ===")
                        for item in enrollments:
                            print(f"Course {item[1]} - ₹{item[2]}")
                        tax = total_price * 0.05
                        print("="*40)
                        print(f"Total Fees : ₹{total_price}")
                        print(f"Tax : ₹{tax}")
                        print(f"Final Amount : ₹{total_price + tax}")

                        confirm = input("Confirm fee payment (y/n)? ")
                        if confirm.lower() == "y":

                            print("Payment successful! Your enrollments are confirmed!")
                        else:
                            print("Payment cancelled.")

                        enrollments = []
                        total_price = 0

                    time.sleep(5)

                    ch = input("Do you want to continue (y/n)? ")

                case _:

                    print("Invalid input")

                    ch = input("Do you want to continue (y/n)? ")
        except ValueError:

            print("Please enter a valid number.")

            ch = input("Do you want to continue (y/n)? ")

def main():
    ch = 'y'

    while ch.lower() == "y":
        try:

            os.system('cls')

            print("An automated student management software".center(170))

            print("1.Admin\n2.Teacher\n3.Student\n4.Exit")
            user_type = int(input("Enter user type(1/2/3/4): "))

            match user_type:
                case 1:

                    os.system("cls")
                    admin()
                case 2:

                    os.system("cls")
                    teacher()
                case 3:

                    os.system("cls")
                    student()
                    print("Thank you for using our service.")
                case 4:

                    os.system("cls")
                    print("Exited. Thank you for using our service".center(170))
                    break
                case _:

                    print("Invalid input. Enter a valid choice.")

        except ValueError:
            print("Please enter a valid number.")

            ch = input("Do you want to continue (y/n)? ")

if __name__ == "__main__":
    main()
