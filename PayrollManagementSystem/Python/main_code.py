from support import *

def admin_payroll():
    if not login("admin.csv"):
        print("Access denied")
        return
    while True:
        choice = input("Admin: 1 staff 2 add 3 update 4 delete 5 view 0 exit: ")
        if choice == "1": add_staff()
        elif choice == "2": add_employee()
        elif choice == "3": update_employee()
        elif choice == "4": delete_employee()
        elif choice == "5": view_employee()
        elif choice == "0": return

def staff_payroll():
    if not login("hr.csv"):
        print("Access denied")
        return
    while True:
        choice = input("Staff: 1 add 2 update 3 view 0 exit: ")
        if choice == "1": add_employee()
        elif choice == "2": update_employee()
        elif choice == "3": view_employee()
        elif choice == "0": return

def main():
    while True:
        choice = input("Employee orders: 1 admin 2 HR 3 customer 0 exit: ")
        if choice == "1": admin_payroll()
        elif choice == "2": staff_payroll()
        elif choice == "3": customer_order()
        elif choice == "0": break

if __name__ == "__main__":
    main()
