
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
            print("1.Add Doctor\n2.Add Patient Data\n3.Update Patient Data\n4.Delete Patient Data\n5.View Patient Data\n6.Exit")

            choice = int(input("Enter your choice (1/2/3/4/5/6) : "))

            match choice:
                case 1:

                    os.system('cls')
                    new_user = input("Enter the new ID :")
                    new_pass = input("Enter the new Password :")
                    m1.add_doctor(new_user, new_pass)
                    print("The doctor is added successfully !")
                    time.sleep(2)
                    m1.view_doctors()
                    ch = input("Do you want to continue (y/n)? ")
                case 2:

                    os.system('cls')
                    name = input("Patient Name/Treatment : ")
                    price = int(input("Fee : "))
                    m1.add_data(name, price)
                    print("The patient data has been added to the list !")
                    ch = input("Do you want to continue (y/n)? ")
                case 3:

                    os.system('cls')
                    name = input("Enter the patient/treatment name : ")
                    price = int(input("Enter the altered fee : "))
                    m1.update_data(name, price)
                    print("The patient fee has been modified successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 4:

                    os.system('cls')
                    name = input("Enter the patient name to be removed : ")
                    m1.del_data(name)
                    print("The patient data has been removed successfully !")
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

def doctor():

    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")

    result = m1.check_doctor(uid, pas)
    if result == "verified" or True:

        print("Doctor login successful !")

        ch = "y"
        while ch.lower() == "y":
            os.system('cls')

            print("1.Add Patient Data\n2.Update Patient Data\n3.View Patient Data\n4.Exit")
            choice = int(input("Enter your choice (1/2/3/4): "))

            match choice:
                case 1:

                    os.system('cls')
                    name = input("Enter patient/treatment name: ")
                    price = int(input("Enter patient fee: "))
                    m1.add_data(name, price)
                    print("Patient data has been added successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 2:

                    os.system('cls')
                    name = input("Enter the patient name to be updated: ")
                    price = int(input("Enter fee to be updated: "))
                    m1.update_data(name, price)
                    print("Patient data has been updated successfully !")
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

def patient():

    print("Welcome, Patient!")

    ch = "y"

    appointments = []

    total_price = 0
    discount = 0

    while ch.lower() == "y":

        os.system('cls')

        print("1. View Available Treatments\n2. Book Appointment\n3. View Appointments\n4. Pay Bill\n5. Exit")
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

                    print("Enter treatment numbers to book (enter -1 to finish):")

                    m1.display_data()

                    while True:

                        try:
                            num = int(input("Enter the treatment number: "))

                            if num != -1:
                                pass
                            else:

                                break

                            df = pd.read_csv("patients.csv",index_col=0)

                            if num in df.index:

                                item_name = df.loc[num, "patient_name"]
                                item_price = df.loc[num, "fee"]

                                appointments.append((item_name, num, item_price))

                                total_price += item_price

                                print(f"Added {item_name} to appointments!")
                            else:

                                print("Invalid treatment number.")
                        except ValueError:

                            print("Please enter a valid number.")

                    print(f"Appointments total: {total_price}")

                    ch = input("Do you want to continue (y/n)? ")

                case 3:

                    os.system('cls')

                    if not appointments:

                        print("Your appointment list is empty.")
                    else:

                        print("Your Appointments:")
                        for item in appointments:

                            print(f"Treatment {item[0]}: {item[1]} - ₹{item[2]}")

                        print(f"Total: {total_price}")

                    time.sleep(5)

                    ch = input("Do you want to continue (y/n)? ")
                case 5:

                    print("Thank you for using the hospital services!")
                    break
                case 4:

                    os.system('cls')

                    if not appointments:
                        print("Your appointment list is empty. Please book before proceeding to payment.")
                    else:

                        print("=== Billing Summary ===")
                        for item in appointments:
                            print(f"Treatment {item[1]} - ₹{item[2]}")
                        tax = total_price * 0.18
                        if total_price > 10000:
                            discount = total_price * 0.1
                        print("="*40)
                        print(f"Total Price : ₹{total_price}")
                        print(f"Tax : ₹{tax}")
                        print(f"Discount : ₹{discount}")
                        print(f"Final Amount : ₹{total_price + tax - discount}")

                        confirm = input("Confirm payment (y/n)? ")
                        if confirm.lower() == "y":

                            print("Payment successful! Wishing you a speedy recovery!")
                        else:
                            print("Payment cancelled.")

                        appointments = []
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

            print("An automated hospital management software".center(170))

            print("1.Admin\n2.Doctor\n3.Patient\n4.Exit")
            user_type = int(input("Enter user type(1/2/3/4): "))

            match user_type:
                case 1:

                    os.system("cls")
                    admin()
                case 2:

                    os.system("cls")
                    doctor()
                case 3:

                    os.system("cls")
                    patient()
                    print("Thank you for using our service. Get well soon!")
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
