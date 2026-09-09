# import necessary modules
import support as m1
import time, os
import pandas as pd

'''The admin() function allows adminstrators to manage the systems by performing various tasks that include adding new 
doctors, adding new patient data, updating existing patient data, deleting patient data and viewing all patient data'''

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
            print("1.Add Doctor\n2.Add Patient Data\n3.Update Patient Data\n4.Delete Patient Data\n5.View Patient Data\n6.Exit")
            # Gets admin's choice
            choice = int(input("Enter your choice (1/2/3/4/5/6) : "))
            # Handle admin's choice
            match choice:
                case 1:
                    # Add a new doctor
                    os.system('cls')
                    new_user = input("Enter the new ID :")
                    new_pass = input("Enter the new Password :")
                    m1.add_doctor(new_user, new_pass)
                    print("The doctor is added successfully !")
                    time.sleep(2)
                    m1.view_doctors()
                    ch = input("Do you want to continue (y/n)? ")
                case 2:
                    # Add a new patient
                    os.system('cls')
                    name = input("Patient Name/Treatment : ")
                    price = int(input("Fee : "))
                    m1.add_data(name, price)
                    print("The patient data has been added to the list !")
                    ch = input("Do you want to continue (y/n)? ")
                case 3:
                    # Update an existing patient
                    os.system('cls')
                    name = input("Enter the patient/treatment name : ")
                    price = int(input("Enter the altered fee : "))
                    m1.update_data(name, price)
                    print("The patient fee has been modified successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 4:
                    # Delete a patient
                    os.system('cls')
                    name = input("Enter the patient name to be removed : ")
                    m1.del_data(name)
                    print("The patient data has been removed successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 5:
                    # View all patients
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

'''The doctor() function allows doctors to manage patient data by performing tasks such as adding new patient data, updating 
existing patient data, viewing all patient data'''
def doctor():
    # Get doctor credentials
    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")
    # Verify doctor credentials
    result = m1.check_doctor(uid, pas)
    if result == "verified" or True:
        # Display success message
        print("Doctor login successful !")
        # Loop until doctor chooses to exit
        ch = "y"
        while ch.lower() == "y":
            os.system('cls')
            # Get doctor choice
            print("1.Add Patient Data\n2.Update Patient Data\n3.View Patient Data\n4.Exit")
            choice = int(input("Enter your choice (1/2/3/4): "))
            # Handle doctor's choice
            match choice:
                case 1:
                    # Add a new patient
                    os.system('cls')
                    name = input("Enter patient/treatment name: ")
                    price = int(input("Enter patient fee: "))
                    m1.add_data(name, price)
                    print("Patient data has been added successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 2:
                    # update an existing patient
                    os.system('cls')
                    name = input("Enter the patient name to be updated: ")
                    price = int(input("Enter fee to be updated: "))
                    m1.update_data(name, price)
                    print("Patient data has been updated successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 3:
                    # View all patients
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

'''The patient() function simulates a patient experience and allow patients to view available treatments,add treatments 
to their appointments,view their appointments and proceed to checkout'''

def patient():
    # Welcome message for patient
    print("Welcome, Patient!")
    # Intialize a variable to track user's choice to continue
    ch = "y"
    # Initialize an empty appointments
    appointments = []
    # Initialize total price and discount
    total_price = 0
    discount = 0
    # Loop until user chooses to exit
    while ch.lower() == "y":
        # clear the console
        os.system('cls')
        # Display menu options
        print("1. View Available Treatments\n2. Book Appointment\n3. View Appointments\n4. Pay Bill\n5. Exit")
        try:
            # Get users choice
            choice = int(input("Enter your choice (1/2/3/4/5): "))
            # Use match statement to handle different choices
            match choice:
                # Handle view treatments option
                case 1:
                    # Clear the console
                    os.system('cls')
                    # Display treatments
                    m1.display_data()
                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask user idf they want to continue
                    ch = input("Do you want to continue (y/n)? ")
                case 2:
                    # Clear the console
                    os.system('cls')
                    # Prompt user to enter item numbers to add to appointments
                    print("Enter treatment numbers to book (enter -1 to finish):")
                    # Display the treatments
                    m1.display_data()
                    # Loop until user finishes booking items
                    while True:
                        # Get item number from the user
                        try:
                            num = int(input("Enter the treatment number: "))
                            # Check if user wants to finish adding items
                            if num != -1:
                                pass
                            else:
                                # Break out of the loop
                                break
                            # Read patients.csv file
                            df = pd.read_csv("patients.csv",index_col=0)
                            # Check if the item number is valid
                            if num in df.index:
                                # Get item name and price
                                item_name = df.loc[num, "patient_name"]
                                item_price = df.loc[num, "fee"]
                                # Add item to appointments
                                appointments.append((item_name, num, item_price))
                                # Update total price
                                total_price += item_price
                                # Print conformation message
                                print(f"Added {item_name} to appointments!")
                            else:
                                # Print error message for invalid item number
                                print("Invalid treatment number.")
                        except ValueError:
                            # print error message for invalid input
                            print("Please enter a valid number.")
                    # print appointments total
                    print(f"Appointments total: {total_price}")
                    # Ask user if they want to continue
                    ch = input("Do you want to continue (y/n)? ")

                # Handle view appointments option
                case 3:
                    # clear the console
                    os.system('cls')
                    # Check if the appointments is empty
                    if not appointments:
                        # print message the appointments is empty
                        print("Your appointment list is empty.")
                    else:
                        # print appointments contents
                        print("Your Appointments:")
                        for item in appointments:
                            # Print each item in the appointments
                            print(f"Treatment {item[0]}: {item[1]} - ₹{item[2]}")
                        # Print total price
                        print(f"Total: {total_price}")
                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask user if they want to continue
                    ch = input("Do you want to continue (y/n)? ")
                case 5:
                    #Print thankyou message for the patient
                    print("Thank you for using the hospital services!")
                    break
                case 4:
                    #Clear the console
                    os.system('cls')
                    # Check if appointments is empty
                    if not appointments:
                        print("Your appointment list is empty. Please book before proceeding to payment.")
                    else:
                        # Print billing summary
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
                        # Ask user to confirm payment
                        confirm = input("Confirm payment (y/n)? ")
                        if confirm.lower() == "y":
                            # Print successful message
                            print("Payment successful! Wishing you a speedy recovery!")
                        else:
                            print("Payment cancelled.")
                        # Reset appointments and total price
                        appointments = []
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
            print("An automated hospital management software".center(170))
            # Get the user type from user
            print("1.Admin\n2.Doctor\n3.Patient\n4.Exit")
            user_type = int(input("Enter user type(1/2/3/4): "))
            # Use match statement to handle different user types
            match user_type:
                case 1:
                    # Clear console and call admin function
                    os.system("cls")
                    admin()
                case 2:
                    # Clear console and call doctor function
                    os.system("cls")
                    doctor()
                case 3:
                    # Clear the console and call patient function
                    os.system("cls")
                    patient()
                    print("Thank you for using our service. Get well soon!")
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
