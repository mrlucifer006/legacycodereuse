from support import admin_menu, teller_menu, customer_menu
def main():
    while True:
        choice = input("\nBank Service Billing System\n1. Admin\n2. Teller\n3. Customer\n4. Exit\nChoose: ")
        if choice == "1": admin_menu()
        elif choice == "2": teller_menu()
        elif choice == "3": customer_menu()
        elif choice == "4": break
if __name__ == "__main__": main()
