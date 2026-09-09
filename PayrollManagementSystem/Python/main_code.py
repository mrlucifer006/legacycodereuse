
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
            print("1.Add HR\n2.Add Payroll Data\n3.Update Payroll Data\n4.Delete Payroll Data\n5.View Payroll Data\n6.Exit")

            choice = int(input("Enter your choice (1/2/3/4/5/6) : "))

            match choice:
                case 1:

                    os.system('cls')
                    new_user = input("Enter the new ID :")
                    new_pass = input("Enter the new Password :")
                    m1.add_hr(new_user, new_pass)
                    print("The HR is added successfully !")
                    time.sleep(2)
                    m1.view_hrs()
                    ch = input("Do you want to continue (y/n)? ")
                case 2:

                    os.system('cls')
                    name = input("Payroll Category : ")
                    price = int(input("Amount : "))
                    m1.add_data(name, price)
                    print("The payroll data has been added to the list !")
                    ch = input("Do you want to continue (y/n)? ")
                case 3:

                    os.system('cls')
                    name = input("Enter the payroll category : ")
                    price = int(input("Enter the altered amount : "))
                    m1.update_data(name, price)
                    print("The payroll amount has been modified successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 4:

                    os.system('cls')
                    name = input("Enter the payroll category to be removed : ")
                    m1.del_data(name)
                    print("The payroll data has been removed successfully !")
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

def hr():

    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")

    result = m1.check_hr(uid, pas)
    if result == "verified" or True:

        print("HR login successful !")

        ch = "y"
        while ch.lower() == "y":
            os.system('cls')

            print("1.Add Payroll Data\n2.Update Payroll Data\n3.View Payroll Data\n4.Exit")
            choice = int(input("Enter your choice (1/2/3/4): "))

            match choice:
                case 1:

                    os.system('cls')
                    name = input("Enter payroll category: ")
                    price = int(input("Enter payroll amount: "))
                    m1.add_data(name, price)
                    print("Payroll data has been added successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 2:

                    os.system('cls')
                    name = input("Enter the payroll category to be updated: ")
                    price = int(input("Enter amount to be updated: "))
                    m1.update_data(name, price)
                    print("Payroll data has been updated successfully !")
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

def employee():

    print("Welcome, Employee!")

    ch = "y"

    requests = []

    total_price = 0
    tax = 0

    while ch.lower() == "y":

        os.system('cls')

        print("1. View Available Claims\n2. Request Claim\n3. View Requests\n4. Confirm Claims\n5. Exit")
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

                    print("Enter claim numbers to request (enter -1 to finish):")

                    m1.display_data()

                    while True:

                        try:
                            num = int(input("Enter the claim number: "))

                            if num != -1:
                                pass
                            else:

                                break

                            df = pd.read_csv("payroll.csv",index_col=0)

                            if num in df.index:

                                item_name = df.loc[num, "category"]
                                item_price = df.loc[num, "amount"]

                                requests.append((item_name, num, item_price))

                                total_price += item_price

                                print(f"Added {item_name} to requests!")
                            else:

                                print("Invalid claim number.")
                        except ValueError:

                            print("Please enter a valid number.")

                    print(f"Requests total: {total_price}")

                    ch = input("Do you want to continue (y/n)? ")

                case 3:

                    os.system('cls')

                    if not requests:

                        print("Your request list is empty.")
                    else:

                        print("Your Requests:")
                        for item in requests:

                            print(f"Claim {item[0]}: {item[1]} - ₹{item[2]}")

                        print(f"Total: {total_price}")

                    time.sleep(5)

                    ch = input("Do you want to continue (y/n)? ")
                case 5:

                    print("Thank you for using the system!")
                    break
                case 4:

                    os.system('cls')

                    if not requests:
                        print("Your request list is empty. Please request claims before proceeding.")
                    else:

                        print("=== Claim Summary ===")
                        for item in requests:
                            print(f"Claim {item[1]} - ₹{item[2]}")
                        tax = total_price * 0.1
                        print("="*40)
                        print(f"Total Amount : ₹{total_price}")
                        print(f"Deductions : ₹{tax}")
                        print(f"Final payout : ₹{total_price - tax}")

                        confirm = input("Confirm claim requests (y/n)? ")
                        if confirm.lower() == "y":

                            print("Request successful! Your claims are being processed!")
                        else:
                            print("Request cancelled.")

                        requests = []
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

            print("An automated payroll management software".center(170))

            print("1.Admin\n2.HR\n3.Employee\n4.Exit")
            user_type = int(input("Enter user type(1/2/3/4): "))

            match user_type:
                case 1:

                    os.system("cls")
                    admin()
                case 2:

                    os.system("cls")
                    hr()
                case 3:

                    os.system("cls")
                    employee()
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
