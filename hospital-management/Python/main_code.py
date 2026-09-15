from support import *

def admin_patients():
    if not login("admin.csv"):
        print("Access denied")
        return
    while True:
        choice = input("Admin: 1 staff 2 add 3 update 4 delete 5 view 0 exit: ")
        if choice == "1": add_staff()
        elif choice == "2": add_patient()
        elif choice == "3": update_patient()
        elif choice == "4": delete_patient()
        elif choice == "5": view_patient()
        elif choice == "0": return

def staff_patients():
    if not login("doctor.csv"):
        print("Access denied")
        return
    while True:
        choice = input("Staff: 1 add 2 update 3 view 0 exit: ")
        if choice == "1": add_patient()
        elif choice == "2": update_patient()
        elif choice == "3": view_patient()
        elif choice == "0": return

def main():
    while True:
        choice = input("Patient orders: 1 admin 2 doctor 3 customer 0 exit: ")
        if choice == "1": admin_patients()
        elif choice == "2": staff_patients()
        elif choice == "3": customer_order()
        elif choice == "0": break

if __name__ == "__main__":
    main()
